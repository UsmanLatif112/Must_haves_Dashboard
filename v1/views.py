import traceback
from flask import render_template, request, jsonify, redirect, url_for
from flask_login import login_user, login_required, logout_user
from app import app, login_manager
from user_management import User
from import_csv import import_csv_to_db
from models import db
from helpers import delete_file_if_exists
from user_management import authenticate


@app.route("/", methods=["GET", "POST"])
def login():
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

        result_content = init_the_testing()
        csv_file_path = "API_result.csv"
        import_csv_to_db(db.session, csv_file_path)
        
        delete_file_if_exists(csv_file_path)

        return jsonify(result_content)
    except Exception as e:
        print(f"While initializing the testing error {e}")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))  # replace 'login' with your login route


@app.route("/export_data")
def export_the_data_to_db():
    try:
        csv_file_path = "API_result.csv"
        with db.session.begin():
            import_csv_to_db(db.session, csv_file_path)

        # remove the csv file

        delete_file_if_exists(csv_file_path)
        return jsonify({"message": "API report expored to databas"})

    except Exception as e:
        traceback.print_exc()
        return jsonify({"message": "Unable to export the API report to database"})
