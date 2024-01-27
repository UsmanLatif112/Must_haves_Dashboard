import traceback
from flask_login import current_user
from flask import render_template, request, jsonify, redirect, url_for
from flask_login import login_user, login_required, logout_user
from app import app, login_manager
from user_management import User
from import_csv import import_csv_to_db
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
    
    
# @app.route('/perform_operation', methods=['POST'])
# @login_required
# def perform_operation():
#     try:
#         # Perform some operation and get a response
#         # For example, calling an external API
#         response = call_external_api()  # This is just a placeholder function
        
#         # Now, create an ApiResponse object populated with actual response details
#         api_response = ApiResponse(
#             user_id=current_user.id,  # Set the user_id to the current user's ID
#             description="Description of the operation",
#             api="URL of the external API",
#             method="POST",  # Assuming it was a POST request
#             response_code=response.status_code,  # Assuming 'response' has a 'status_code' attribute
#             result_according_to_response=response.reason,  # The textual reason of the HTTP response
#             response_time=0.123,  # You would measure this in your actual operation
#             response_message=response.text,  # Assuming 'response' has a 'text' attribute with the response content
#             response_data=response.content,  # Assuming 'response' has a 'content' attribute with raw response data
#             response_data_result="Result based on the content",
#         )
        
#         # Add the ApiResponse object to the session and commit it to the database
#         db.session.add(api_response)
#         db.session.commit()
        
#         # Return a success message or any other appropriate response
#         return jsonify({"message": "Operation performed and response recorded"})
    
#     except Exception as e:
#         # Handle exceptions and errors appropriately
#         db.session.rollback()
#         return jsonify({"message": "An error occurred", "error": str(e)})
