import csv
from datetime import datetime
from models import ApiResponse, QuickAnalysisModel, stagingapiaResponse,mapboosterapiaResponse, team_usermoduleModel, umbrellaResponse, ClientmoduleModel, ce_traffic_Model, tiger_traffic_Model, torrential_traffic_Model, bs_traffic_Model, ldr_traffic_Model

def _clip(value, limit):
    if value is None:
        return None
    return str(value)[:limit]


def save_api_log(session, user_id, description, api, method, response_code, result_according_to_response, response_time, response_message, response_data, payload_data, response_data_result):
    entry = ApiResponse(
        user_id=user_id,
        description=_clip(description, 256),
        api=_clip(api, 512),
        method=_clip(method, 128),
        response_code=int(response_code) if response_code not in (None, "") else None,
        result_according_to_response=_clip(result_according_to_response, 256),
        response_time=float(response_time) if response_time not in (None, "") else None,
        response_message=_clip(response_message, 1024),
        response_data=_clip(response_data, 60000),
        payload_data=_clip(payload_data, 255),
        response_data_result=_clip(response_data_result, 256),
    )
    session.add(entry)
    session.commit()


def import_csv_to_db(session, csv_file_path, user_id):  # Added user_id as a parameter
    with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
        csv_reader = csv.DictReader(csvfile)

        # Iterate over CSV rows and create ORM objects
        for row in csv_reader:
            response_entry = ApiResponse(
                user_id=user_id,  # Set the user_id for the ApiResponse
                description=_clip(row["Description"], 256),
                api=_clip(row["API"], 512),
                method=_clip(row["Method"], 128),
                response_code=int(row["Response Code"]) if row["Response Code"] else None,
                result_according_to_response=_clip(row["Result (according to response code)"], 256),
                response_time=float(row["Response Time"]) if row["Response Time"] else None,
                response_message=_clip(row["Response Message"], 1024),
                response_data=_clip(row["Response Data"], 60000),
                payload_data=_clip(row.get("Payload Data"), 255),
                response_data_result=_clip(row["Response Data Result"], 256),
            )

            # Add each new object to the session
            session.add(response_entry)

        # Commit all at once
        session.commit()
        print("CSV data imported successfully")

def import_quick_csv_to_db(session, csv_file_path, user_id):  # Added user_id as a parameter
    with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
        csv_reader = csv.DictReader(csvfile)

        # Iterate over CSV rows and create ORM objects
        for row in csv_reader:
            response_entry = QuickAnalysisModel(
                user_id=user_id,  # Set the user_id for the ApiResponse
                test_case=row["Test Case"],
                use_case=row["Use Case / Scenario"],
                result=row["Result"],
            )

            # Add each new object to the session
            session.add(response_entry)

        # Commit all at once
        session.commit()
        print("CSV data imported successfully")
        print("CSV data imported successfully")

def import_client_csv_to_db(session, csv_file_path, user_id):  # Added user_id as a parameter
    with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
        csv_reader = csv.DictReader(csvfile)

        # Iterate over CSV rows and create ORM objects
        for row in csv_reader:
            response_entry = ClientmoduleModel(
                user_id=user_id,  # Set the user_id for the ApiResponse
                test_case=row["Test Case"],
                use_case=row["Use Case / Scenario"],
                result=row["Result"],
            )

            # Add each new object to the session
            session.add(response_entry)

        # Commit all at once
        session.commit()
        print("CSV data imported successfully")
        
        
def import_user_team_csv_to_db(session, csv_file_path, user_id):  # Added user_id as a parameter
    with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
        csv_reader = csv.DictReader(csvfile)

        # Iterate over CSV rows and create ORM objects
        for row in csv_reader:
            response_entry = team_usermoduleModel(
                user_id=user_id,  # Set the user_id for the ApiResponse
                test_case=row["Test Case"],
                use_case=row["Use Case / Scenario"],
                result=row["Result"],
            )

            # Add each new object to the session
            session.add(response_entry)

        # Commit all at once
        session.commit()
        print("CSV data imported successfully")
        
        
def import_ce_traffic_csv_to_db(session, csv_file_path, user_id, campaign_type):  # Added user_id as a parameter
    with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
        csv_reader = csv.DictReader(csvfile)

        # Iterate over CSV rows and create ORM objects
        for row in csv_reader:
            response_entry = ce_traffic_Model(
                user_id=user_id,  # Set the user_id for the ApiResponse
                test_case=row["Test Case"],
                use_case=row["Use Case / Scenario"],
                result=row["Result"],
                campaign_type=campaign_type
            )

            # Add each new object to the session
            session.add(response_entry)

        # Commit all at once
        session.commit()
        print("CSV data imported successfully")
        
        
def import_tiger_traffic_csv_to_db(session, csv_file_path, user_id, campaign_type):  # Added user_id as a parameter
    with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
        csv_reader = csv.DictReader(csvfile)

        # Iterate over CSV rows and create ORM objects
        for row in csv_reader:
            response_entry = tiger_traffic_Model(
                user_id=user_id,  # Set the user_id for the ApiResponse
                test_case=row["Test Case"],
                use_case=row["Use Case / Scenario"],
                result=row["Result"],
                campaign_type=campaign_type
            )

            # Add each new object to the session
            session.add(response_entry)

        # Commit all at once
        session.commit()
        print("CSV data imported successfully")
        
def import_torrential_traffic_csv_to_db(session, csv_file_path, user_id, campaign_type):  # Added user_id as a parameter
    with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
        csv_reader = csv.DictReader(csvfile)

        # Iterate over CSV rows and create ORM objects
        for row in csv_reader:
            response_entry = torrential_traffic_Model(
                user_id=user_id,  # Set the user_id for the ApiResponse
                test_case=row["Test Case"],
                use_case=row["Use Case / Scenario"],
                result=row["Result"],
                campaign_type=campaign_type
            )

            # Add each new object to the session
            session.add(response_entry)

        # Commit all at once
        session.commit()
        print("CSV data imported successfully")
        
def import_bs_traffic_csv_to_db(session, csv_file_path, user_id, campaign_type):
    with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        created_at = datetime.now()
        
        records_to_insert = []
        for row in csv_reader:
            response_entry = bs_traffic_Model(
                user_id=user_id,
                test_case=row.get("Test Case", "N/A"),
                use_case=row.get("Use Case / Scenario", "N/A"),
                result=row.get("Result", "N/A"),
                campaign_type=campaign_type,
                created_at=created_at
            )
            records_to_insert.append(response_entry)

        # Bulk add objects to the session
        if records_to_insert:
            session.add_all(records_to_insert)
            session.commit()
            print(f"✅ CSV data imported successfully! Inserted {len(records_to_insert)} rows.")

def import_ldr_traffic_csv_to_db(session, csv_file_path, user_id, campaign_type):  # Added user_id as a parameter
    with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
        csv_reader = csv.DictReader(csvfile)

        # Iterate over CSV rows and create ORM objects
        for row in csv_reader:
            response_entry = ldr_traffic_Model(
                user_id=user_id,  # Set the user_id for the ApiResponse
                test_case=row["Test Case"],
                use_case=row["Use Case / Scenario"],
                result=row["Result"],
                campaign_type=campaign_type
            )

            # Add each new object to the session
            session.add(response_entry)

        # Commit all at once
        session.commit()
        print("CSV data imported successfully")
        

def import_umbrella_csv_to_db(session, csv_file_path, user_id):  # Added user_id as a parameter
    with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
        csv_reader = csv.DictReader(csvfile)

        # Iterate over CSV rows and create ORM objects
        for row in csv_reader:
            response_entry = umbrellaResponse(
                user_id=user_id,  # Set the user_id for the ApiResponse
                description=row["Description"],
                api=row["API"],
                method=row["Method"],
                response_code=int(row["Response Code"]) if row["Response Code"] else None,
                result_according_to_response=row["Result (according to response code)"],
                response_time=float(row["Response Time"]) if row["Response Time"] else None,
                response_message=row["Response Message"],
                response_data=row["Response Data"],
                payload_data=row.get("Payload Data"),
                response_data_result=row["Response Data Result"],
            )

            # Add each new object to the session
            session.add(response_entry)

        # Commit all at once
        session.commit()
        print("CSV data imported successfully")
        
        
def import_staging_csv_to_db(session, csv_file_path, user_id):  # Added user_id as a parameter
    with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
        csv_reader = csv.DictReader(csvfile)

        # Iterate over CSV rows and create ORM objects
        for row in csv_reader:
            response_entry = stagingapiaResponse(
                user_id=user_id,  # Set the user_id for the ApiResponse
                description=row["Description"],
                api=row["API"],
                method=row["Method"],
                response_code=int(row["Response Code"]) if row["Response Code"] else None,
                result_according_to_response=row["Result (according to response code)"],
                response_time=float(row["Response Time"]) if row["Response Time"] else None,
                response_message=row["Response Message"],
                response_data=row["Response Data"],
                payload_data=row.get("Payload Data"),
                response_data_result=row["Response Data Result"],
            )

            # Add each new object to the session
            session.add(response_entry)

        # Commit all at once
        session.commit()
        print("CSV data imported successfully")
        
def import_mapbooster_csv_to_db(session, csv_file_path, user_id):  # Added user_id as a parameter
    with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
        csv_reader = csv.DictReader(csvfile)

        # Iterate over CSV rows and create ORM objects
        for row in csv_reader:
            response_entry = mapboosterapiaResponse(
                user_id=user_id,  # Set the user_id for the ApiResponse
                description=row["Description"],
                api=row["API"],
                method=row["Method"],
                response_code=int(row["Response Code"]) if row["Response Code"] else None,
                result_according_to_response=row["Result (according to response code)"],
                response_time=float(row["Response Time"]) if row["Response Time"] else None,
                response_message=row["Response Message"],
                response_data=row["Response Data"],
                payload_data=row.get("Payload Data"),
                response_data_result=row["Response Data Result"],
            )

            # Add each new object to the session
            session.add(response_entry)

        # Commit all at once
        session.commit()
        print("CSV data imported successfully")