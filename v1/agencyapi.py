import requests
import csv
from csv import reader
import time
from flask import  request
def init_the_testing(campaign_id, quick_analysis_campaign_id, business_id , keywordname_id):
    # Retrieve the campaign_id from the form data
    # campaign_idd = request.form.get("campaign_id")
    Piroty_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJBaW1hbFJhemFfMjIiLCJUT0tFTiI6ImV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUp6ZFdJaU9pSkJhVzFoYkZKaGVtRmZNaklpTENKelkyOXdaWE1pT2x0ZExDSnBaQ0k2TVRFd05Dd2laWGh3SWpveE56QTNNVE00TmprNGZRLnUydDl0ZWxWem1WUHRkWmllUWE2TkVPRTE3NGVmZlFSNExJamtQdW52N1kiLCJleHAiOjIwMjAzMzg2OTh9.-Vo3eyz3OQGViYypBo4Oe5emU3_fCQ2fsE-wvB4_U8k"
    Campaign_IDd = str(campaign_id)
    Quick_Camp_Id = str(quick_analysis_campaign_id)
    business_CID_Id = str(business_id)
    keywordname_Id = str(keywordname_id)
    # ======================================
    auth_token = Piroty_token
    # ======================================
    id = f'{Campaign_IDd}'
    
    idD = str(f'{Campaign_IDd}')
    # ================================================
    Quick_Camp_IDD = f'{Quick_Camp_Id}'
    # Campaign ID which is deleted firs
    # ================================================

    # Campaign ID which is deleted first in delete api and get single campaign data with campaign id.

    Campaign_ID = f"{id}"

    # Campaign IDd which is used for other apis in which we need campaign id to get data
    # (Dont Delete Cam1)

    Campaign_IDd = "19460" 

    # Campaign IDdd which is used to add 8th keyword in campaign already having 7 keywords
    # (Dont Delete Cam2)

    Campaign_IDdd = "19491"

    # Campaign IDdr which is used to delete last keyword of campaign
    # (Dont Delete Cam3)

    Campaign_IDdr = "19360"

    # Campaign IDdt which is used to deauthorize business.
    # (Business campaign Del 4)

    Campaign_IDdt = "19361"
    
    # Campaign IDdt which is used to deauthorize business.
    # (Business campaign Del 5)
    
    Campaign_IDde = "19553"

    # Client id is used to get client api

    Quick_Camp_ID = Quick_Camp_Id
    
    Client_id = "1954"

    # Keyword which is used to create keyword add keyword or delete keyword

    # Keyword_new = f"apimust{id}"
    Keyword_new = f"{keywordname_Id}"
    
    # Client name which is used to create new client

    Client_Name_New = f"apimust{id}"

    # ================================================

    user_idd = "1104",
    business_CID = f"{business_CID_Id}"
    cam_namee = f"QuickCam{id}"
    keywords_for_analysiss = f"{keywordname_Id}"
                        
                        
    user_name = f"Apimust{id}12"
    email = f"Apimust12{id}@gmail.com"
    password =  "Usman@112"
    
    # data which is used to create new campaign

    User_id = "1104"
    business_gmb_CID = f"{business_CID_Id}"
    Campaign_name = f"API must have {id}"
    Client_name = "APITEST0026"
    keywords_for_analysis = f"{keywordname_Id}"
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
    # Initialize the response codes dictionary
    response_codes_dict = {}
    
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
        #  ====//// == Agency API == ////=======
    
            # {
            #     "description": "Create User with correct data",
            #     "url": "http://69.167.136.19:8010/users/create_user/",
            #     "method": "POST",
            #     "params":
            #         {
            #             "user_name": user_name,
            #             "email": email,
            #             "password": password
            #         },
            # },
            
            # {
            #     "description": "Create User with same username",
            #     "url": "http://69.167.136.19:8010/users/create_user/",
            #     "method": "POST",
            #     "params":
            #         {
            #             "user_name": user_name,
            #             "email": email,
            #             "password": password
            #         },
            # },
            
            # {
            #     "description": "Create User with same email",
            #     "url": "http://69.167.136.19:8010/users/create_user/",
            #     "method": "POST",
            #     "params":
            #         {
            #             "user_name": "user_name",
            #             "email": email,
            #             "password": password
            #         },
            # },
            
            # {
            #     "description": "Create User with special charcter in Username",
            #     "url": "http://69.167.136.19:8010/users/create_user/",
            #     "method": "POST",
            #     "params":
            #         {
            #             "user_name": "user_name@@",
            #             "email": "apimusthavestest10987@gmail.com",
            #             "password": password
            #         },
            # },
            
            # {
            #     "description": "Create User with incorrect email format",
            #     "url": "http://69.167.136.19:8010/users/create_user/",
            #     "method": "POST",
            #     "params":
            #         {
            #             "user_name": "user_name120",
            #             "email": "api 10987@gmail.com",
            #             "password": password
            #         },
            # },
            
            # {
            #     "description": "Create User with incorect password",
            #     "url": "http://69.167.136.19:8010/users/create_user/",
            #     "method": "POST",
            #     "params":
            #         {
            #             "user_name": "user_name1201",
            #             "email": "api10987@gmail.com",
            #             "password": "Usman"
            #         },
            # },
            
            # {
            #     "description": "Get all User list",
            #     "url": f"http://69.167.136.19:8010/users/list/",
            #     "method": "GET",
            #     "params": None
            # },
            
            # {
            #     "description": "Get SS0 link of user with correct data",
            #     "url": f"http://69.167.136.19:8010/users/login_link/",
            #     "method": "POST",
            #     "params": 
            #             {
            #             "user_name": "Aimalraza_22",
            #             "password": "Aimal@11"
            #             }
            # },
            
            # {
            #     "description": "Get SSO link of user with incorrect username",
            #     "url": f"http://69.167.136.19:8010/users/login_link/",
            #     "method": "POST",
            #     "params": 
            #             {
            #             "user_name": "Aimalraza_",
            #             "password": "Aimal@11"
            #             }
            # },
            
            # {
            #     "description": "Get SOS link of user with incorrect password",
            #     "url": f"http://69.167.136.19:8010/users/login_link/",
            #     "method": "POST",
            #     "params": 
            #             {
            #             "user_name": "Aimalraza_22",
            #             "password": "Usman@1"
            #             }
            # },
            
            # # # # # =========================================
            
            # {
            #     "description": "Create campaign with correct data",
            #     "url": "http://69.167.136.19:8010/campaigns/create/",
            #     "method": "POST",
            #     "params":
            #         {
            #         "user_id": User_id,
            #         "business_gmb_cid": business_gmb_CID,
            #         "campaign_name": Campaign_name,
            #         "client_name": Client_name,
            #         "keywords_for_analysis": keywords_for_analysis
            #         }
            # },
            
            # {
            #     "description": "Create campaign with incorrect user id",
            #     "url": "http://69.167.136.19:8010/campaigns/create/",
            #     "method": "POST",
            #     "params":
            #         {
            #         "user_id": 143789,
            #         "business_gmb_cid": business_gmb_CID,
            #         "campaign_name": Campaign_name,
            #         "client_name": Client_name,
            #         "keywords_for_analysis": keywords_for_analysis
            #         }
            # },
            
            # {
            #     "description": "Create campaign with incorrect GMB CID",
            #     "url": "http://69.167.136.19:8010/campaigns/create/",
            #     "method": "POST",
            #     "params":
            #         {
            #         "user_id": User_id,
            #         "business_gmb_cid": "98649953187944340729864995318",
            #         "campaign_name": Campaign_name,
            #         "client_name": Client_name,
            #         "keywords_for_analysis": keywords_for_analysis
            #         }
            # },
            
            
            # # # # # # =============================================================
            
            # {
            #     "description": "Get campaign by providing campaign ID",
            #     "url": f"http://69.167.136.19:8010/campaigns/{Campaign_IDd}/",
            #     "method": "GET",
            #     "params": None
            # },
            # {
            #     "description": "Get campaign by providing incorrect campaign ID",
            #     "url": "http://69.167.136.19:8010/campaigns/177/",
            #     "method": "GET",
            #     "params": None
            # },
            
            
            # # # # # # # =============================================================
            
            # {
            #     "description": "Get list of all campaigns",
            #     "url": "http://69.167.136.19:8010/campaigns/list/all/",
            #     "method": "GET",
            #     "params": None
            # },
            
            # # # # =============================================================
            
            # {
            #     "description": "Delete campaign by providing campaign ID",
            #     "url": f"http://69.167.136.19:8010/campaigns/delete/{Campaign_ID}/",
            #     "method": "DELETE",
            #     "params": None
            # },
            
            # {
            #     "description": "Delete campaign by providing incorrect campaign ID",
            #     "url": f"http://69.167.136.19:8010/campaigns/delete/1289/",
            #     "method": "DELETE",
            #     "params": None
            # },
            
            # {
            #     "description": "Delete campaign by providing already deleted campaign ID",
            #     "url": f"http://69.167.136.19:8010/campaigns/delete/{Campaign_ID}/",
            #     "method": "DELETE",
            #     "params": None
            # },
            
            # # # =============================================================
            
            # {
            #     "description": "Create Client",
            #     "url": "http://69.167.136.19:8010/client/create/",
            #     "method": "POST",
            #     "params":
            #         {
            #             "client_name": Client_Name_New
            #             }
            # },
            # {
            #     "description": "Create client with already created client name",
            #     "url": "http://69.167.136.19:8010/client/create/",
            #     "method": "POST",
            #     "params":
            #         {
            #             "client_name": Client_Name_New
            #             }
            # },
            
            # # # # # ======================================
            
            # {
            #     "description": "Get client by providing client ID",
            #     "url": f"http://69.167.136.19:8010/client/{Client_id}/",
            #     "method": "GET",
            #     "params": None
            # },
            # {
            #     "description": "Get client by providing incorrect client ID",
            #     "url": f"http://69.167.136.19:8010/client/128/",
            #     "method": "GET",
            #     "params": None
            # },
            
            # # # ======================================
            
            # {
            #     "description": "Get list of all clients",
            #     "url": f"http://69.167.136.19:8010/client/clients/list/",
            #     "method": "GET",
            #     "params": None
            # },
            
            # # # # # ======================================
            
            # {
            #     "description": "Get list of all Geo Gifs URLs",
            #     "url": "http://69.167.136.19:8010/geo/gifs/urls/list/",
            #     "method": "GET",
            #     "params":
            #         {
            #         "Page": 1,
            #         "Size": 50
            #         }   
            # },
            
            # # # # # ======================================
            
            # {
            #     "description": "Get list of Geo Gifs URLs by providing campaign ID",
            #     "url": f"http://69.167.136.19:8010/geo/gifs/urls/campaign/{Campaign_IDd}",
            #     "method": "GET",
            #     "params": None
            # },
            # {
            #     "description": "Get list of Geo Gifs URLs by providing incorrect campaign ID",
            #     "url": f"http://69.167.136.19:8010/geo/gifs/urls/campaign/1205",
            #     "method": "GET",
            #     "params": None
            # },
            
            # # # # # ======================================
            
            # {
            #     "description": "Get list of all Geo Grids URLs",
            #     "url": "http://69.167.136.19:8010/geo/grid/urls/list/all/",
            #     "method": "GET",
            #     "params": None
            # },
            
            # # # # ======================================
            
            
            # {
            #     "description": "Get list of Geo Grids URLs by providing campaign ID",
            #     "url": f"http://69.167.136.19:8010/geo/grid/urls/{Campaign_IDd}/",
            #     "method": "GET",
            #     "params": None
            # },
            
            # {
            #     "description": "Get list of Geo Grids URLs by providing incorrect campaign ID",
            #     "url": f"http://69.167.136.19:8010/geo/grid/urls/1496/",
            #     "method": "GET",
            #     "params": None
            # },
            
            # # # # ======================================
            
            # {
            #     "description": "Get list of latest Grids URLs by providing campaign ID",
            #     "url": f"http://69.167.136.19:8010/geo/grid/urls/latest/{Campaign_IDd}",
            #     "method": "GET",
            #     "params": None
            # },
            
            # {
            #     "description": "Get list of latest Grids URLs by providing incorrect campaign ID",
            #     "url": f"http://69.167.136.19:8010/geo/grid/urls/latest/8573",
            #     "method": "GET",
            #     "params": None
            # },
            
            # # # # ======================================
            
            # {
            #     "description": "Add keyword in campaign by providing campaign id",
            #     "url": "http://69.167.136.19:8010/keyword/create/",
            #     "method": "POST",
            #     "params":
            #         {
            #         "campaign_id": Campaign_IDde,
            #         "keyword": Keyword_new
            #         }
            # },
            # {
            #     "description": "Add keyword which is already added in campaign by providing campaign id",
            #     "url": "http://69.167.136.19:8010/keyword/create/",
            #     "method": "POST",
            #     "params":
            #         {
            #         "campaign_id": Campaign_IDde,
            #         "keyword": Keyword_new
            #         }
            # },
            # {
            #     "description": "Add keyword in campaign already having 7 keywords by providing campaign id",
            #     "url": "http://69.167.136.19:8010/keyword/create/",
            #     "method": "POST",
            #     "params":
            #         {
            #         "campaign_id": Campaign_IDdd,
            #         "keyword": "Pathan12323"
            #         }
            # },
            
            # # # # ======================================
            
            # {
            #     "description": "Deauthroize business by providing campaign ID",
            #     "url": f"http://69.167.136.19:8010/campaigns/business/deauthorization/{Campaign_IDdt}",
            #     "method": "GET",
            #     "params": None
            # },
            # {
            #     "description": "Deauthroize business which is already deauthroize by providing campaign ID",
            #     "url": f"http://69.167.136.19:8010/campaigns/business/deauthorization/{Campaign_IDdt}",
            #     "method": "GET",
            #     "params": None
            # },
            # {
            #     "description": "Deauthroize business by providing incorrect campaign ID",
            #     "url": f"http://69.167.136.19:8010/campaigns/business/deauthorization/{Campaign_IDdr}",
            #     "method": "GET",
            #     "params": None
            # }, 
            
            
            # # ======================================
            
            # {
            #     "description": "Get Reporting PDF with correct Campaign ID",
            #     "url": f"http://69.167.136.19:8010/reporting/pdf/{Campaign_IDd}",
            #     "method": "GET",
            #     "params":None
            # },
            
            # {
            #     "description": "Get Reporting PDF with Incorrect Campaign ID",
            #     "url": f"http://69.167.136.19:8010/reporting/pdf/789456123",
            #     "method": "GET",
            #     "params":None
            # },
            
            # # ======================================
            # {
            #     "description": "Create Quick Analysis Campaign with correct data",
            #     "url": "http://69.167.136.19:8010/quick_analysis/campaigns/create/",
            #     "method": "POST",
            #     "params":
            #         {
            #         "user_id": User_id,
            #         "business_gmb_cid": business_gmb_CID,
            #         "campaign_name": Campaign_name,
            #         "keywords_for_analysis": keywords_for_analysis
            #         }
            # },
            # # # ======================================
            # {
            #     "description": "Create Quick Analysis Campaign with Inccorrect GMB_CID",
            #     "url": "http://69.167.136.19:8010/quick_analysis/campaigns/create/",
            #     "method": "POST",
            #     "params":
            #         {
            #         "user_id": User_id,
            #         "business_gmb_cid": 159753456978634159494945642368,
            #         "campaign_name": Campaign_name,
            #         "keywords_for_analysis": keywords_for_analysis
            #         }
            # },
            # # # ======================================
            # {
            #     "description": "Create Quick Analysis Campaign with Inccorrect User ID",
            #     "url": "http://69.167.136.19:8010/quick_analysis/campaigns/create/",
            #     "method": "POST",
            #     "params":
            #         {
            #         "user_id": 798456,
            #         "business_gmb_cid": business_gmb_CID,
            #         "campaign_name": Campaign_name,
            #         "keywords_for_analysis": keywords_for_analysis
            #         }
            # },
            
        #     # # ======================================
            
            # {
            #     "description": "Get list of Quick Analysis Campaign with correct campaign ID",
            #     "url": f"http://69.167.136.19:8010/quick_analysis/campaigns/{Quick_Camp_ID}/",
            #     "method": "GET",
            #     "params": None
            # },
            
            # {
            #     "description": "Get list of Quick Analysis Campaign with Incorrect campaign ID",
            #     "url": f"http://69.167.136.19:8010/quick_analysis/campaigns/741528/",
            #     "method": "GET",
            #     "params": None
            # },
            
            {
                "description": "Get list of all Quick Analysis Campaigns",
                "url": f"http://69.167.136.19:8010/quick_analysis/campaigns/list/all/",
                "method": "GET",
                "params": None
            },
            
            # {
            #     "description": "Delete Quick Analysis Campaigns with campaign id",
            #     "url": f"http://69.167.136.19:8010/quick_analysis/campaigns/delete/{Quick_Camp_Id}/",
            #     "method": "DELETE",
            #     "params": None
            # },
            
        #     {
        #         "description": "Delete Quick Analysis Campaigns with incorrect campaign id",
        #         "url": f"http://69.167.136.19:8010/quick_analysis/campaigns/delete/978456185/",
        #         "method": "DELETE",
        #         "params": None
        #     },
            
        #     # ======================================
            
        #     {
        #         "description": "Delete keyword from campaign by providing campaign ID",
        #         "url": f"http://69.167.136.19:8010/keyword/delete/{Keyword_new}/{Campaign_IDde}",
        #         "method": "DELETE",
        #         "params": None
        #     },
        #     {
        #         "description": "Delete keyword which is already deleted from campaign by providing campaign ID",
        #         "url": f"http://69.167.136.19:8010/keyword/delete/{Keyword_new}/{Campaign_IDde}",
        #         "method": "DELETE",
        #         "params": None
        #     },
        #     {
        #         "description": "Try to delete last keyword of campaign by providing campaign ID",
        #         "url": f"http://69.167.136.19:8010/keyword/delete/hello/{Campaign_IDdr}",
        #         "method": "DELETE",
        #         "params": None
        #     },
            
        #     # ======================================
        ] # Your API list

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
