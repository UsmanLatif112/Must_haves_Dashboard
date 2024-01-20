import requests
import csv
from csv import reader
import time
from flask import  request
def init_the_testing():
    # Retrieve the campaign_id from the form data
    campaign_idd = request.form.get("campaign_id")
    Piroty_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJBaW1hbFJhemFfMjIiLCJUT0tFTiI6ImV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUp6ZFdJaU9pSkJhVzFoYkZKaGVtRmZNaklpTENKelkyOXdaWE1pT2x0ZExDSnBaQ0k2TVRFd05Dd2laWGh3SWpveE56QTNNVE00TmprNGZRLnUydDl0ZWxWem1WUHRkWmllUWE2TkVPRTE3NGVmZlFSNExJamtQdW52N1kiLCJleHAiOjIwMjAzMzg2OTh9.-Vo3eyz3OQGViYypBo4Oe5emU3_fCQ2fsE-wvB4_U8k"
    # ======================================
    auth_token = Piroty_token
    # ======================================
    id = f"{campaign_idd}"
    # ================================================

    # Campaign ID which is deleted first in delete api and get single campaign data with campaign id.

    Campaign_ID = f"{id}"

    # Campaign IDd which is used for other apis in which we need campaign id to get data
    # (API must haves 1)

    Campaign_IDd = "19458"

    # Campaign IDdd which is used to add 8th keyword in campaign already having 7 keywords
    # (API must haves 2)

    Campaign_IDdd = "19359"

    # Campaign IDdr which is used to delete last keyword of campaign
    # (API must haves 3)

    Campaign_IDdr = "19360"

    # Campaign IDdt which is used to deauthorize business.
    # (Business campaign Del 4)

    Campaign_IDdt = "19361"

    # Client id is used to get client api

    Client_id = "1954"

    # User id is used to create Campaign api

    User_id = "1104"

    # Keyword which is used to create keyword add keyword or delete keyword

    Keyword_new = f"apimust{id}"
    # Keyword_new = "hello"

    # Client name which is used to create new client

    Client_Name_New = f"apimust{id}"

    # data which is used to create new campaign

    User_id = "1104"
    business_gmb_CID = "10469100432931003566"
    Campaign_name = f"Apimusthave{id}"
    Client_name = "APITEST0026"
    keywords_for_analysis = "Red Royal Electric,American restaurant"

    # data which is used to create new campaign

    user_name = f"Apimust{id}"
    email = f"Apimust{id}@gmail.com"
    password = "Usman@112"

    User_id = "2948"
    business_gmb_CID = "10469100432931003566"
    Campaign_name = f"New API Campaign{id}"
    Client_name = "APITEST0026"
    keywords_for_analysis = "Red Royal Electric,American restaurant"

    # ======================================
    api_list = []
    # ======================================
    # Add a dictionary to store custom error messages for specific response codes
    custom_error_messages = {
        500: "Internal Server Error",
        501: "Not Implemented",
        502: "Bad Gateway",
        503: "Service Unavailable",
        504: "Gateway Timeout",
        505: "HTTP Version Not Supported",
        506: "Variant Also Negotiates",
        507: "Insufficient Storage",
        508: "Loop Detected",
        510: "Not Extended",
        511: "Network Authentication Required",
        400: "Bad Request",
        401: "Unauthorized",
        402: "Payment Required",
        403: "Forbidden",
        404: "Not Found",
        405: "Method Not Allowed",
        406: "Not Acceptable",
        407: "Proxy Authentication Required",
        408: "Request Timeout",
        409: "Conflict",
        410: "Gone",
        411: "Length Required",
        412: "Precondition Failed",
        413: "Payload Too Large",
        414: "URI Too Long",
        415: "Unsupported Media Type",
        416: "Range Not Satisfiable",
        418: "iam",
        421: "Misdirected Request",
        422: "Unprocessable Entity",
        423: "Locked",
        424: "Failed Dependency",
        426: "Upgrade Required",
        428: "Precondition Required",
        431: "Request Header Fields Too Large",
        451: "Unavailable For Legal Reasons",
        429: "Too Many Requests",
    }
    # ======================================

    # Function to hit the APIs and save results in a CSV file
    def hit_apis_and_save_results(api_list, auth_token, csv_filename):
        # with open(csv_filename, 'w', newline='') as csvfile:
        with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
            # writer = csv.writer(csvfile)
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            writer.writerow(
                [
                    "Description",
                    "API",
                    "Method",
                    "Response Code",
                    "Result (according to response code)",
                    "Response Time",
                    "Response Message",
                    "Response Data",
                    "Response Data Result",
                ]
            )
            # writer.writerow(['\n'])

            # Iterate over each API in the list
            for api in api_list:
                description = api.get("description", "No description provided")
                url = api["url"]
                method = api["method"]
                params = api["params"]

                headers = {
                    "Authorization": f"Bearer {auth_token}",
                    "Content-Type": "application/json",
                }

                try:
                    # Print the API description
                    print("==============================================")
                    print("   ")
                    print(f"API Description: {description}")

                    # Make the API request
                    start_time = time.time()

                    response = requests.request(
                        method, url, json=params, headers=headers
                    )
                    response_code = response.status_code
                    response_time = time.time() - start_time

                    response_message = custom_error_messages.get(response_code, "")
                    response_data = (
                        response.json()
                        if response.headers.get("content-type") == "application/json"
                        else response.text
                    )

                    # Determine the result based on response data
                    if response_data == {
                        "items": [],
                        "total": 0,
                        "page": 1,
                        "size": 50,
                    }:
                        response_result = "Fail"
                    else:
                        response_result = "Pass"

                    result_according_to_response_code = (
                        "Pass" if response_code in [200, 201, 202] else "Fail"
                    )
                    # Write the results to the CSV file
                    response_data = str(response_data).replace('"', ";")

                    writer.writerow(
                        [
                            description,
                            url,
                            method,
                            response_code,
                            result_according_to_response_code,
                            response_time,
                            response_message,
                            f'"{response_data}"',
                            response_result,
                        ]
                    )

                    # Print the results in the terminal
                    print(
                        f"API: {url}, Method: {method}, Response Code: {response_code}, Result (according to response code): {result_according_to_response_code}, "
                        f"Response Time: {response_time:.2f}, Response Message: {response_message}, Response Data: {response_data}, Response Data Result: {response_result}"
                    )

                    # Wait for 1 second before the next API hit
                    time.sleep(1)

                except Exception as e:
                    print("==============================================")
                    print("   ")
                    print(
                        f"Error occurred while processing API: {url}, Method: {method}, Error: {e}"
                    )

            print("==============================================")
            print("   ")
            print("API hits completed.")

    # Call the function to hit the APIs and save the results
    hit_apis_and_save_results(api_list, auth_token, "API_result.csv")

    # =====================================================================================
    # For example, let's assume your script's function is `hit_apis_and_save_results`
    auth_token = Piroty_token
    api_list = [
         # ====//// == Agency API == ////=======
    
            {
                "description": "Create User with correct data",
                "url": "http://67.225.255.186:8010/users/create_user/",
                "method": "POST",
                "params":
                    {
                        "user_name": user_name,
                        "email": email,
                        "password": password
                    },
            },
            
            {
                "description": "Create User with same username",
                "url": "http://67.225.255.186:8010/users/create_user/",
                "method": "POST",
                "params":
                    {
                        "user_name": user_name,
                        "email": email,
                        "password": password
                    },
            },
            
            {
                "description": "Create User with same email",
                "url": "http://67.225.255.186:8010/users/create_user/",
                "method": "POST",
                "params":
                    {
                        "user_name": "user_name",
                        "email": email,
                        "password": password
                    },
            },
            
            
        ]  # Your API list

    # Call the function to hit the APIs and save the results
    result_file = "API_result.csv"
    hit_apis_and_save_results(api_list, auth_token, result_file)

    # Read the CSV file and convert its content into a list of lists
    with open(result_file, "r", encoding="utf-8") as file:
        result_content = list(reader(file))

    # Skip the header row (first row of the CSV)
    result_content = result_content[1:]
    return result_content
    # Return the data as JSON

    # return jsonify(result)
