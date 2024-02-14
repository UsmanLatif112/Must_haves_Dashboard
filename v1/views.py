import traceback
from flask_login import current_user
from flask import render_template, request, jsonify, redirect, url_for
from flask_login import login_user, login_required, logout_user
from app import app, login_manager
from user_management import User
from import_csv import import_client_csv_to_db, import_csv_to_db, import_quick_csv_to_db, import_staging_csv_to_db, import_umbrella_csv_to_db
from models import ApiResponse, db
from helpers import delete_file_if_exists
from user_management import authenticate
from flask_login import login_required, current_user
from flask import jsonify
from models import ApiResponse, db


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
    return render_template("dashboard.html")


@app.route("/script")
@login_required
def script():
    return render_template("script.html")

@app.route("/umbrella_script")
@login_required
def umbrella_script():
    return render_template("umbrella_script.html")



@app.route("/Agency_api")
@login_required
def Agency_api():
    return render_template("Agency API dashboard.html")

@app.route("/staging_agency_script")
@login_required
def staging_agency_script():
    return render_template("staging_agency_script.html")


@app.route("/BSWA-must-haves")
@login_required
def BSWA():
    return render_template("BSWA.html")


@app.route("/Quick-analysis")
@login_required
def Quick():
    return render_template("Quick_analysis.html")

@app.route("/Quick-analysis-script", methods=["POST"])
@login_required
def Quick_script():
    try:
        from Quick_Analysis import init_the_testing

        # Call a function that initializes testing and returns data
        GMB_cid = request.form.get("C_id")
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
    


@app.route("/client_module")
@login_required
def client():
    return render_template("client_module.html")

@app.route("/client-module-script", methods=["POST"])
@login_required
def client_script():
    try:
        from client_module import init_the_testing

        # Call a function that initializes testing and returns data
        GMB_cid = request.form.get("C_id")
        print(f'{GMB_cid}')
        User_name = request.form.get("U_id")
        print(f'{User_name}')
        Pass_word = request.form.get("P_id")
        print(f'{Pass_word}')
        result_content = init_the_testing(GMB_cid, User_name, Pass_word)
        
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
        # Pass these IDs to the init_the_testing function
        result_content = init_the_testing(campaign_id, quick_analysis_campaign_id,business_id,keywordname_id)
        
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