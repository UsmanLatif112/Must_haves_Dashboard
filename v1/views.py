import traceback,csv,os
from traffic import *
from lib.page import *
from sqlalchemy import func
from datetime import datetime
from flask_login import current_user
from flask import render_template, request, jsonify, redirect, url_for,Blueprint
from flask_login import login_user, login_required, logout_user
from models import team_usermoduleModel,stagingapiaResponse, QuickAnalysisModel, ce_traffic_Model, tiger_traffic_Model, torrential_traffic_Model, bs_traffic_Model,umbrellaResponse
from app import app, login_manager,db
from user_management import User
from import_csv import import_client_csv_to_db, import_csv_to_db, import_quick_csv_to_db, import_staging_csv_to_db, import_umbrella_csv_to_db, import_user_team_csv_to_db, import_ce_traffic_csv_to_db, import_tiger_traffic_csv_to_db, import_torrential_traffic_csv_to_db, import_bs_traffic_csv_to_db
from models import ApiResponse, db
from helpers import delete_file_if_exists
from user_management import authenticate
from flask_login import login_required, current_user
from flask import jsonify,current_app
from models import ApiResponse, db
from sqlalchemy import text

main = Blueprint('main', __name__)

@app.route("/", methods=["GET", "POST"])
def login():
    # import pdb;pdb.set_trace()
    if request.method == "GET":
        return render_template("index.html")
    
     
    elif request.method == "POST":
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        print(
            f"Received email: {email}, password: {password}"
        )  # For debugging purposes

        if email and password:
           
            user = authenticate(email, password)
            if user:
                # import pdb;pdb.set_trace()
                login_user(user)
                return jsonify({"status": "ok"})
            else:
                print("Invalid credentials.")  # For debugging purposes
                return jsonify({"status": "error", "message": "Invalid credentials"})
        else:
            print("Email or password not provided")  # For debugging purposes
            return jsonify(
                {"status": "error", "message": "Email or password not provided"}
            )


@app.route("/dashboard")
@login_required
def dashboard():
    user_email = current_user.email  # Access the logged-in user's email directly
    return render_template("dashboard.html", user_email=user_email)


"""========================Agency API Views=========================="""

@app.route("/Agency_api")
@login_required
def Agency_api():
    user_email = current_user.email
    return render_template("Agency API dashboard.html", user_email=user_email)


@app.route("/script")
@login_required
def script():
    current_date_ = datetime.today().date()
    user_email = current_user.email
    user_id = current_user.id

    # If user ID is 100, display results for all users
    if user_id == 100:
        # Retrieve data for the current date for all users
        api_responses_list = ApiResponse.query.filter(
            func.date(ApiResponse.created_at) == current_date_
        ).order_by(ApiResponse.created_at.desc()).all()[:54]
        
        # If no data for the current date, retrieve the most recent data for all users
        if not api_responses_list:
            api_responses_list = ApiResponse.query.order_by(
                ApiResponse.created_at.desc()
            ).all()[:54]
    else:
        # Retrieve data for the current date filtered by the logged-in user
        api_responses_list = ApiResponse.query.filter(
            func.date(ApiResponse.created_at) == current_date_,
            ApiResponse.user_id == user_id
        ).order_by(ApiResponse.created_at.desc()).all()[:54]
        
        # If no data for the current date, retrieve the most recent data for the logged-in user
        if not api_responses_list:
            api_responses_list = ApiResponse.query.filter_by(
                user_id=user_id
            ).order_by(ApiResponse.created_at.desc()).all()[:54]

    return render_template("script.html", api_responses=api_responses_list, user_email=user_email)


@app.route("/run_script", methods=["POST"])
@login_required
def run_script():
    try:
        from agencyapi import init_the_testing

        # Call a function that initializes testing and returns data
        campaign_id = request.form.get("C_id")
        print(f'{campaign_id}')
        quick_analysis_campaign_id = request.form.get("Q_id")
        print(f'{quick_analysis_campaign_id}')
        keywordname_id = request.form.get("K_id")
        print(f'{keywordname_id}')
        business_id = request.form.get("B_id")
        print(f'{business_id}')
        Campaign_Status = request.form.get("C_St")
        print(f'{Campaign_Status}')
        # Pass these IDs to the init_the_testing function
        result_content = init_the_testing(campaign_id, quick_analysis_campaign_id,business_id,keywordname_id,Campaign_Status)
        
        # Commit the API responses to the database
        db.session.commit()
        
        # Import the CSV file data into the database, now passing the user_id
        csv_file_path = "API_result.csv"
        import_csv_to_db(db.session, csv_file_path, current_user.id)
        
        # Delete the CSV file after import
        delete_file_if_exists(csv_file_path)

        # Return the results as JSON
        return jsonify(result_content)
    except Exception as e:
        # Print the full traceback to help diagnose the issue
        traceback.print_exc()
        # Rollback the session in case of an error
        db.session.rollback()
        # Return a JSON response indicating an error
        return jsonify({"error": str(e), "message": "Failed to run the script"})
    
    
    
@app.route("/umbrella_script")
@login_required
def umbrella_script(): 
    current_date_ = datetime.today().date()
    user_email = current_user.email
    user_id = current_user.id

    # If user ID is 100, display results for all users
    if user_id == 100:
        # Retrieve data for the current date for all users
        umbrellaResponse_list = umbrellaResponse.query.filter(
            func.date(umbrellaResponse.created_at) == current_date_
        ).order_by(umbrellaResponse.created_at.desc()).all()[:54]
        
        # If no data for the current date, retrieve the most recent data for all users
        if not umbrellaResponse_list:
            umbrellaResponse_list = umbrellaResponse.query.order_by(
                umbrellaResponse.created_at.desc()
            ).all()[:54]
    else:
        # Retrieve data for the current date filtered by the logged-in user
        umbrellaResponse_list = umbrellaResponse.query.filter(
            func.date(umbrellaResponse.created_at) == current_date_,
            umbrellaResponse.user_id == user_id
        ).order_by(umbrellaResponse.created_at.desc()).all()[:54]
        
        # If no data for the current date, retrieve the most recent data for the logged-in user
        if not umbrellaResponse_list:
            umbrellaResponse_list = umbrellaResponse.query.filter_by(
                user_id=user_id
            ).order_by(umbrellaResponse.created_at.desc()).all()[:54]

    return render_template("umbrella_script.html", umbrellaResponses=umbrellaResponse_list, user_email=user_email)
    
@app.route("/run_umbrella_script", methods=["POST"])
@login_required
def run_umbrella_script():
    try:
        from umbrella_agency import init_the_testing

        # Call a function that initializes testing and returns data
        campaign_id = request.form.get("C_id")
        print(f'{campaign_id}')
        quick_analysis_campaign_id = request.form.get("Q_id")
        print(f'{quick_analysis_campaign_id}')
        keywordname_id = request.form.get("K_id")
        print(f'{keywordname_id}')
        business_id = request.form.get("B_id")
        print(f'{business_id}')
        # Pass these IDs to the init_the_testing function
        result_content = init_the_testing(campaign_id, quick_analysis_campaign_id,business_id,keywordname_id)
        
        # Commit the API responses to the database
        db.session.commit()
        
        # Import the CSV file data into the database, now passing the user_id
        csv_file_path = "umbrella_API_result.csv"
        import_umbrella_csv_to_db(db.session, csv_file_path, current_user.id)
        
        # Delete the CSV file after import
        delete_file_if_exists(csv_file_path)

        # Return the results as JSON
        return jsonify(result_content)
    except Exception as e:
        # Print the full traceback to help diagnose the issue
        traceback.print_exc()
        # Rollback the session in case of an error
        db.session.rollback()
        # Return a JSON response indicating an error
        return jsonify({"error": str(e), "message": "Failed to run the script"})
    

@app.route("/staging_agency_script")
@login_required
def staging_agency_script():
    current_date_ = datetime.today().date()
    user_email = current_user.email
    user_id = current_user.id

    # If user ID is 100, display results for all users
    if user_id == 100:
        # Retrieve data for the current date for all users
        stagingapiaResponse_list = stagingapiaResponse.query.filter(
            func.date(stagingapiaResponse.created_at) == current_date_
        ).order_by(stagingapiaResponse.created_at.desc()).all()[:54]
        
        # If no data for the current date, retrieve the most recent data for all users
        if not stagingapiaResponse_list:
            stagingapiaResponse_list = stagingapiaResponse.query.order_by(
                stagingapiaResponse.created_at.desc()
            ).all()[:54]
    else:
        # Retrieve data for the current date filtered by the logged-in user
        stagingapiaResponse_list = stagingapiaResponse.query.filter(
            func.date(stagingapiaResponse.created_at) == current_date_,
            stagingapiaResponse.user_id == user_id
        ).order_by(stagingapiaResponse.created_at.desc()).all()[:54]
        
        # If no data for the current date, retrieve the most recent data for the logged-in user
        if not stagingapiaResponse_list:
            stagingapiaResponse_list = stagingapiaResponse.query.filter_by(
                user_id=user_id
            ).order_by(stagingapiaResponse.created_at.desc()).all()[:54]

    return render_template("staging_agency_script.html", stagingapiaResponses=stagingapiaResponse_list, user_email=user_email)

@app.route("/Staging_agencyapi_script", methods=["POST"])
@login_required
def Staging_agencyapi_script():
    try:
        from Staging_agencyapi import init_the_testing

        # Call a function that initializes testing and returns data
        campaign_id = request.form.get("C_id")
        print(f'{campaign_id}')
        quick_analysis_campaign_id = request.form.get("Q_id")
        print(f'{quick_analysis_campaign_id}')
        keywordname_id = request.form.get("K_id")
        print(f'{keywordname_id}')
        business_id = request.form.get("B_id")
        print(f'{business_id}')
        # Pass these IDs to the init_the_testing function
        result_content = init_the_testing(campaign_id, quick_analysis_campaign_id,business_id,keywordname_id)
        
        # Commit the API responses to the database
        db.session.commit()
        
        # Import the CSV file data into the database, now passing the user_id
        csv_file_path = "Staging_API_result.csv"
        import_staging_csv_to_db(db.session, csv_file_path, current_user.id)
        
        # Delete the CSV file after import
        delete_file_if_exists(csv_file_path)

        # Return the results as JSON
        return jsonify(result_content)
    except Exception as e:
        # Print the full traceback to help diagnose the issue
        traceback.print_exc()
        # Rollback the session in case of an error
        db.session.rollback()
        # Return a JSON response indicating an error
        return jsonify({"error": str(e), "message": "Failed to run the script"})    


"""========================BSWA Views=========================="""

@app.route("/BSWA-must-haves")
@login_required
def BSWA():
    user_email = current_user.email
    return render_template("BSWA.html", user_email=user_email)

@app.route("/Quick-analysis")
@login_required
def Quick():
    from lib.page import read_row_limit, write_row_limit
    from models import stagingapiaResponse
    from datetime import datetime
    import csv

    current_date_ = datetime.today().date()
    user_email = current_user.email
    user_id = current_user.id

    # Initialize row limit to 8 by default
    row_limit = read_row_limit()
    csv_file_path = "BSWA Quick Analysis Report.csv"
    search_text = "Test quick analysis campaign create/edit/delete"

    try:
        # Check if the search_text is in the second column of the CSV file
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row_num, row in enumerate(reader, start=1):
                # Debugging: Print each row and the second column content
                print(f"Row {row_num}: {row}")  # Print the entire row
                if len(row) > 1:
                    print(f"Second column: {row[1]}")  # Print the second column value
                    if row[1].strip() == search_text:
                        row_limit = row_num
                        write_row_limit(row_limit)  # Use the row number as the limit
                        print(f"Match found on row {row_num}. Setting row_limit to {row_limit}.")
                        break
    except Exception as e:
        # Log the error or handle it accordingly
        print(f"Error reading CSV: {e}")
        write_row_limit("8")

    # Retrieve data for the current date, conditionally filtering by user_id
    query = QuickAnalysisModel.query.filter(func.date(QuickAnalysisModel.created_at) == current_date_)
    if user_id != 100:
        query = query.filter(QuickAnalysisModel.user_id == user_id)

    QuickAnalysisModels_list = query.order_by(QuickAnalysisModel.created_at.desc()).all()[:row_limit]

    # If no data for the current date, retrieve the most recent data
    if not QuickAnalysisModels_list:
        query = QuickAnalysisModel.query
        if user_id != 100:
            query = query.filter_by(user_id=user_id)
        QuickAnalysisModels_list = query.order_by(QuickAnalysisModel.created_at.desc()).all()[:row_limit]

    delete_file_if_exists(csv_file_path)
    return render_template("Quick_analysis.html", QuickAnalysisModels=QuickAnalysisModels_list, user_email=user_email)

@app.route("/Quick-analysis-script", methods=["POST"])
@login_required
def Quick_script():
    try:
        from Quick_Analysis import init_the_testing

        # Call a function that initializes testing and returns data
        GMB_cid = request.form.get("U_name")
        print(f'{GMB_cid}')
        User_name = request.form.get("U_id")
        print(f'{User_name}')
        Pass_word = request.form.get("P_id")
        print(f'{Pass_word}')
        result_content = init_the_testing(GMB_cid, User_name, Pass_word)
        
        # Commit the API responses to the database
        db.session.commit()
        
        # Import the CSV file data into the database, now passing the user_id
        csv_file_path = "BSWA Quick Analysis Report.csv"
        import_quick_csv_to_db(db.session, csv_file_path, current_user.id)
        
        # Delete the CSV file after import
        # Return the results as JSON
        return jsonify(result_content)
    except Exception as e:
        # Print the full traceback to help diagnose the issue
        traceback.print_exc()
        # Rollback the session in case of an error
        db.session.rollback()
        # Return a JSON response indicating an error
        return jsonify({"error": str(e), "message": "Failed to run the script"})
    


@app.route("/client_module")
@login_required
def client():
    from models import ApiResponse
    from datetime import datetime
    user_email = current_user.email
    current_date_ = datetime.today().date()
    api_responses_list = ApiResponse.query.filter(func.date(ApiResponse.created_at) == current_date_).all()[:54]
    if not api_responses_list:
        api_responses_list = ApiResponse.query.order_by(ApiResponse.created_at.desc()).limit(54).all()[:54]
    return render_template("script.html",api_responses=api_responses_list, user_email=user_email)

@app.route("/client-module-script", methods=["POST"])
@login_required
def client_script():
    try:
        from client_module import init_the_testing

        # Call a function that initializes testing and returns data
        Client_name= request.form.get("C_name")
        print(f'{Client_name}')
        User_name = request.form.get("U_id")
        print(f'{User_name}')
        Pass_word = request.form.get("P_id")
        print(f'{Pass_word}')
        result_content = init_the_testing(Client_name, User_name, Pass_word)
        
        # Commit the API responses to the database
        db.session.commit()
        
        # Import the CSV file data into the database, now passing the user_id
        csv_file_path = "BSWA Client Module Report.csv"
        import_client_csv_to_db(db.session, csv_file_path, current_user.id)
        
        # Delete the CSV file after import
        delete_file_if_exists(csv_file_path)

        # Return the results as JSON
        return jsonify(result_content)
    except Exception as e:
        # Print the full traceback to help diagnose the issue
        traceback.print_exc()
        # Rollback the session in case of an error
        db.session.rollback()
        # Return a JSON response indicating an error
        return jsonify({"error": str(e), "message": "Failed to run the script"})
    
   
@app.route("/user_&_team_module")
@login_required
def user_team_module():
    from models import team_usermoduleModel
    from datetime import datetime
    user_email = current_user.email
    current_date_ = datetime.today().date()
    team_usermoduleModels_list = team_usermoduleModel.query.filter(func.date(team_usermoduleModel.created_at) == current_date_).order_by(team_usermoduleModel.created_at.desc()).all()[:54]
    # if not team_usermoduleModel_list:
    #     team_usermoduleModel_list = ApiResponse.query.order_by(ApiResponse.created_at.desc()).limit(54).all()[:54]
    return render_template("user & team_module.html",team_usermoduleModel=team_usermoduleModels_list, user_email=user_email)

@app.route("/user_&_team_module_script", methods=["POST"])
@login_required
def User_script():
    try:
        from user_team_module import init_the_testing

        # Call a function that initializes testing and returns data
        team_user_name = request.form.get("U_name")
        print(f'{team_user_name}')
        User_name = request.form.get("U_id")
        print(f'{User_name}')
        Pass_word = request.form.get("P_id")
        print(f'{Pass_word}')
        USer_Role = request.form.get("UR_id")
        print(f'{USer_Role}')
        result_content = init_the_testing(USer_Role,team_user_name, User_name, Pass_word)
        
        # Commit the API responses to the database
        db.session.commit()
        
        # Import the CSV file data into the database, now passing the user_id
        csv_file_path = "BSWA user & team Module Report.csv"
        import_user_team_csv_to_db(db.session, csv_file_path, current_user.id)
        
        # Delete the CSV file after import
        delete_file_if_exists(csv_file_path)

        # Return the results as JSON
        return jsonify(result_content)
    except Exception as e:
        # Print the full traceback to help diagnose the issue
        traceback.print_exc()
        # Rollback the session in case of an error
        db.session.rollback()
        # Return a JSON response indicating an error
        return jsonify({"error": str(e), "message": "Failed to run the script"})
    

"""========================Traffic Views=========================="""
# TRAFFIC MUST HAVE VIEWS

@app.route("/Traffic-must-haves")
@login_required
def traffic_must_haves():
    user_email = current_user.email
    current_date_ = datetime.today().date()
    team_usermoduleModels_list = team_usermoduleModel.query.filter(func.date(team_usermoduleModel.created_at) == current_date_).order_by(team_usermoduleModel.created_at.desc()).all()[:54]
    return render_template("traffic.html", team_usermoduleModel=team_usermoduleModels_list, user_email=user_email)



"""
    CE TRAFFIC MUST HAVE
"""
@app.route("/CE-traffic-must-haves")
@login_required
def CE_traffic_must_haves():
    user_email = current_user.email
    user_id = current_user.id

    # Get the earliest timestamp based on the user ID
    earliest_timestamp_query = db.session.query(ce_traffic_Model.created_at)
    if user_id != 100:
        earliest_timestamp_query = earliest_timestamp_query.filter(ce_traffic_Model.user_id == user_id)
    earliest_timestamp = earliest_timestamp_query.order_by(ce_traffic_Model.created_at.desc()).limit(1).scalar()

    # Retrieve traffic models
    ce_traffic_Models_query = ce_traffic_Model.query.filter(ce_traffic_Model.created_at == earliest_timestamp)
    if user_id != 100:
        ce_traffic_Models_query = ce_traffic_Models_query.filter(ce_traffic_Model.user_id == user_id)

    ce_traffic_Models_list = ce_traffic_Models_query.order_by(ce_traffic_Model.created_at.desc()).all()

    return render_template("CE_traffic.html", ce_traffic_Model=ce_traffic_Models_list, user_email=user_email)

@app.route("/CE-traffic-must-haves-run-script", methods=["POST"])
@login_required
def CE_traffic_must_haves_run_script():
    try:

        test_cases = CE_Traffic_TestCases()
        result_content = test_cases.full_dashboard_must_haves()
        db.session.commit()
        csv_file_path = "CE_traffic_must_haves.csv"
        import_ce_traffic_csv_to_db(db.session, csv_file_path, current_user.id)

        delete_file_if_exists(csv_file_path)
        return jsonify(result_content)
    
    except Exception as e:
        traceback.print_exc()
        db.session.rollback()
        return jsonify({"error": str(e), "message": "Failed to run the script"})



"""
    Tiger TRAFFIC MUST HAVE
"""
@app.route("/Tiger-traffic-must-haves")
@login_required
def Tiger_traffic_must_haves():
    user_email = current_user.email
    user_id = current_user.id

    # Get the earliest timestamp based on the user ID
    earliest_timestamp_query = db.session.query(tiger_traffic_Model.created_at)
    if user_id != 100:
        earliest_timestamp_query = earliest_timestamp_query.filter(tiger_traffic_Model.user_id == user_id)
    earliest_timestamp = earliest_timestamp_query.order_by(tiger_traffic_Model.created_at.desc()).limit(1).scalar()

    # Retrieve traffic models
    tiger_traffic_Models_query = tiger_traffic_Model.query.filter(tiger_traffic_Model.created_at == earliest_timestamp)
    if user_id != 100:
        tiger_traffic_Models_query = tiger_traffic_Models_query.filter(tiger_traffic_Model.user_id == user_id)

    tiger_traffic_Models_list = tiger_traffic_Models_query.order_by(tiger_traffic_Model.created_at.desc()).all()

    return render_template("Tiger_traffic.html", tiger_traffic_Model=tiger_traffic_Models_list, user_email=user_email)
@app.route("/Tiger-traffic-must-haves-run-script", methods=["POST"])
@login_required
def Tiger_traffic_must_haves_run_script():
    try:

        test_cases = Tiger_Traffic_TestCases()
        result_content = test_cases.full_dashboard_must_haves()
        db.session.commit()
        csv_file_path = "Tiger_traffic_must_haves.csv"
        import_tiger_traffic_csv_to_db(db.session, csv_file_path, current_user.id)

        delete_file_if_exists(csv_file_path)
        return jsonify(result_content)
    
    except Exception as e:
        traceback.print_exc()
        db.session.rollback()
        return jsonify({"error": str(e), "message": "Failed to run the script"})



"""
    Torrential TRAFFIC MUST HAVE
"""
@app.route("/Torrential-traffic-must-haves")
@login_required
def Torrential_traffic_must_haves():
    user_email = current_user.email
    user_id = current_user.id

    # Get the earliest timestamp based on the user ID
    earliest_timestamp_query = db.session.query(torrential_traffic_Model.created_at)
    if user_id != 100:
        earliest_timestamp_query = earliest_timestamp_query.filter(torrential_traffic_Model.user_id == user_id)
    earliest_timestamp = earliest_timestamp_query.order_by(torrential_traffic_Model.created_at.desc()).limit(1).scalar()

    # Retrieve traffic models
    torrential_traffic_Models_query = torrential_traffic_Model.query.filter(torrential_traffic_Model.created_at == earliest_timestamp)
    if user_id != 100:
        torrential_traffic_Models_query = torrential_traffic_Models_query.filter(torrential_traffic_Model.user_id == user_id)

    torrential_traffic_Models_list = torrential_traffic_Models_query.order_by(torrential_traffic_Model.created_at.desc()).all()

    return render_template("Torrential_traffic.html", torrential_traffic_Model=torrential_traffic_Models_list, user_email=user_email)

@app.route("/Torrential-traffic-must-haves-run-script", methods=["POST"])
@login_required
def Torrential_traffic_must_haves_run_script():
    try:

        test_cases = Torrential_Traffic_TestCases()
        result_content = test_cases.full_dashboard_must_haves()
        db.session.commit()
        csv_file_path = "Torrential_traffic_must_haves.csv"
        import_torrential_traffic_csv_to_db(db.session, csv_file_path, current_user.id)

        delete_file_if_exists(csv_file_path)
        return jsonify(result_content)
    
    except Exception as e:
        traceback.print_exc()
        db.session.rollback()
        return jsonify({"error": str(e), "message": "Failed to run the script"})



"""
    BS TRAFFIC MUST HAVE
"""
@app.route("/BS-traffic-must-haves")
@login_required
def BS_traffic_must_haves():
    user_email = current_user.email
    user_id = current_user.id

    # Get the earliest timestamp based on the user ID
    earliest_timestamp_query = db.session.query(bs_traffic_Model.created_at)
    if user_id != 100:
        earliest_timestamp_query = earliest_timestamp_query.filter(bs_traffic_Model.user_id == user_id)
    earliest_timestamp = earliest_timestamp_query.order_by(bs_traffic_Model.created_at.desc()).limit(1).scalar()

    # Retrieve traffic models
    bs_traffic_Models_query = bs_traffic_Model.query.filter(bs_traffic_Model.created_at == earliest_timestamp)
    if user_id != 100:
        bs_traffic_Models_query = bs_traffic_Models_query.filter(bs_traffic_Model.user_id == user_id)

    bs_traffic_Models_list = bs_traffic_Models_query.order_by(bs_traffic_Model.created_at.desc()).all()

    return render_template("BS_traffic.html", bs_traffic_Model=bs_traffic_Models_list, user_email=user_email)

@app.route("/BS-traffic-must-haves-run-script", methods=["POST"])
@login_required
def BS_traffic_must_haves_run_script():
    try:

        test_cases = BS_Traffic_TestCases()
        result_content = test_cases.full_dashboard_must_haves()
        db.session.commit()
        csv_file_path = "BS_traffic_must_haves.csv"
        import_bs_traffic_csv_to_db(db.session, csv_file_path, current_user.id)

        delete_file_if_exists(csv_file_path)
        return jsonify(result_content)
    
    except Exception as e:
        traceback.print_exc()
        db.session.rollback()
        return jsonify({"error": str(e), "message": "Failed to run the script"})
    
    
    
    
    
    


""""=============================dashboard related=================================="""

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))  # replace 'login' with your login route


@app.route("/export_data")
@login_required  # Ensure only authenticated users can access this route
def export_the_data_to_db():
    try:
        csv_file_path = "API_result.csv"
        with db.session.begin():
            # Pass the current user's ID to associate records with the user
            import_csv_to_db(db.session, csv_file_path, current_user.id)

        # Remove the CSV file
        delete_file_if_exists(csv_file_path)
        return jsonify({"message": "API report exported to database"})  # Fix typo in message

    except Exception as e:
        traceback.print_exc()
        return jsonify({"message": "Unable to export the API report to database", "error": str(e)})