import csv
from models import ApiResponse

def import_csv_to_db(session, csv_file_path, user_id):  # Added user_id as a parameter
    with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
        csv_reader = csv.DictReader(csvfile)

        # Iterate over CSV rows and create ORM objects
        for row in csv_reader:
            response_entry = ApiResponse(
                user_id=user_id,  # Set the user_id for the ApiResponse
                description=row["Description"],
                api=row["API"],
                method=row["Method"],
                response_code=int(row["Response Code"]) if row["Response Code"] else None,
                result_according_to_response=row["Result (according to response code)"],
                response_time=float(row["Response Time"]) if row["Response Time"] else None,
                response_message=row["Response Message"],
                response_data=row["Response Data"],
                response_data_result=row["Response Data Result"],
            )

            # Add each new object to the session
            session.add(response_entry)

        # Commit all at once
        session.commit()
        print("CSV data imported successfully")