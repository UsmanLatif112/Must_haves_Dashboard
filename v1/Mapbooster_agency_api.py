import requests
import csv
from csv import reader
import time
from flask import  request
campaign_id_placeholder = None
campaign_id_placeholderr = None
campaign_id_placeholdertt = None
campaign_id_placeholdcd = None
def init_the_testing(campaign_id, business_id , keywordname_id, Campaign_Status):
    Piroty_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJVc21hbi1MYXRpZi1TUUEtQWRtaW4iLCJUT0tFTiI6ImV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUp6ZFdJaU9pSlZjMjFoYmkxTVlYUnBaaTFUVVVFdFFXUnRhVzRpTENKelkyOXdaWE1pT2x0ZExDSnBaQ0k2TlRrME1Td2laWGh3SWpveE56Y3pORGMxTWpZNGZRLjJPWWUyUVJRd1p3RExxYmRXeTAwVVR5WFViLU5mNXNTd0NYajBfcnJtLUkiLCJleHAiOjIwODY2NzUyNjh9.DyZo1jIKQziWcJOdbbMAE-2rVMOPPbdzajB61DG8Xqw"
    Campaign_IDd = str(campaign_id)
    business_CID_Id = str(business_id)
    keywordname_Id = str(keywordname_id).lower()
    Campaign_StatuSs = str(Campaign_Status)
    # ======================================
    auth_token = Piroty_token
    # ======================================
    Campaign_StatuS = f'{Campaign_StatuSs}'
    # (API must have for 8 key)
    Campaign_ITd = "46380" #use able43187
    # (API must have for last key)
    Campaign_IFrf = "46378" #use able
    # (API must have Business Auth)
    Campaign_IHrt = "46587" #use able
    Client_id = "6165"
    Keyword_neww = f"{keywordname_Id}new"
    # Client name which is used to create new client
    Client_Name_New = f"-AI-TEST-apimust{Campaign_IDd}"
    # ================================================                    
    user_name = f"-AI-TEST-AApimust23{Campaign_IDd}"
    email = f"Apimust12{Campaign_IDd}@gmail.com"   
    password =  "Usman@112"
    # data which is used to create new campaign
    # data which is used to create new campaign
    User_id = "5941"
    business_gmb_CID = f"{business_CID_Id}"
    Campaign_name = f"-AI-TEST-API must haves 23{Campaign_IDd}25"
    Client_name = "-AI-TEST-APITEST0026"
    keywords_for_analysis = f"{keywordname_Id}"
    
    project_name = f"-AI-TEST-API must haves project{Campaign_IDd}"
    Grid_Campaign_name = f"-AI-TEST-API must haves{Campaign_IDd}Grid"
    Grid_Campaign_name_Edit = f"-AI-TEST-API must haves{Campaign_IDd}Grid_Edit"
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
    response_storage = {} 
    
    # Function to hit the APIs and save results in a CSV file
    # Function to hit the APIs and save results in a CSV file
    def hit_apis_and_save_results(api_list, auth_token, csv_filename):
        global campaign_id_placeholder 
        global campaign_id_placeholderr
        global campaign_id_placeholdertt
        global campaign_id_placeholdcd
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
                    "Payload Data",
                    "Response Data Result",
                ]
            )

            for api in api_list:
                description = api.get("description", "No description provided")
                url = api["url"]
                method = api["method"]
                params = api["params"]
                if params and ("campaign_id" in params):
                    
                    params['campaign_id'] = campaign_id_placeholder

                headers = {
                    "Authorization": f"Bearer {auth_token}",
                    "Content-Type": "application/json",
                }

                try:
                    print(f"\nAPI Description: {description}\n")
                    start_time = time.time()

                    response = requests.request(method, url, json=params, headers=headers)
                    response_code = response.status_code
                    response_time = time.time() - start_time
                    response_message = custom_error_messages.get(response_code, "")

                    # Handle different response types
                    if response_code == 204:
                        response_data = f"This API does not return a response body for status code {response_code}."
                    else:
                        response_data = response.json() if "application/json" in response.headers.get("content-type", "") else response.text

                    # Store API response for future use
                    response_storage[description] = response_data

                    # Extract campaign ID dynamically
                    if description == "Create campaign with correct data" and response_code == 201:
                        created_campaign_id = response_data.get("campaign_id") 
                        
                        campaign_id_placeholder = created_campaign_id

                        if created_campaign_id:
                            print(f"Extracted campaign_id: {created_campaign_id}")
                            for next_api in api_list:
                                if "campaign_id_placeholder" in next_api["url"]:
                                    next_api["url"] = next_api["url"].replace("campaign_id_placeholder", str(created_campaign_id))
                   
                   
                   # Extract campaign ID dynamically
                    if description == "Create Quick Analysis Campaign with correct data" and response_code == 201:
                        created_campaignn_id = response_data.get("campaign_id") 
                        
                        campaign_id_placeholded = created_campaignn_id

                        if created_campaignn_id:
                            print(f"Extracted campaign_id: {created_campaignn_id}")
                            for next_api in api_list:
                                if "campaign_id_placeholded" in next_api["url"]:
                                    next_api["url"] = next_api["url"].replace("campaign_id_placeholded", str(created_campaignn_id))

                    response_result = "Pass" if response_code in [200, 201, 202] else "Fail"
                    
                    
                    # Extract campaign ID dynamically
                    if description == "Create New Grid tracking Campaign" and response_code == 201:
                        created_campaignn_id = response_data.get("campaign_id") 
                        
                        campaign_id_placeholdcd = created_campaignn_id

                        if created_campaignn_id:
                            print(f"Extracted campaign_id: {created_campaignn_id}")
                            for next_api in api_list:
                                if "campaign_id_placeholdcd" in next_api["url"]:
                                    next_api["url"] = next_api["url"].replace("campaign_id_placeholdcd", str(created_campaignn_id))

                    response_result = "Pass" if response_code in [200, 201, 202] else "Fail"
                    
                    # Extract project ID dynamically from Create New Grid tracking project
                    if description == "Create New Grid tracking project" and response_code == 201:
                        created_project_id = response_data.get("id")
                        campaign_id_placeholdertt = created_project_id

                        if created_project_id:
                            print(f"✅ Extracted project_id: {created_project_id}")
                            
                            # Update the next API params dynamically
                            for next_api in api_list:
                                if next_api["description"] in [
                                    "Create New Grid tracking Campaign",
                                    "Create New Grid tracking Campaign with incorrect user id",
                                    "Create New Grid tracking Campaign with incorrect GMB CID"
                                ]:
                                    next_api["params"]["project_id"] = created_project_id
                                    print(f"🔗 Injected project_id {created_project_id} into {next_api['description']} params")
                                                        
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
                                f'"{params}"',
                                response_result,
                            ]
                        )
                    # Print the results in the terminal
                    # print(
                    #     f"API: {url}, Method: {method}, Response Code: {response_code}, Result (according to response code): {result_according_to_response_code}, "
                    #     f"Response Time: {response_time:.2f}, Response Message: {response_message}, Response Data: {response_data},Payload Data: {params}, Response Data Result: {response_result}"
                    # )
                    print("===================================")    
                    print("         ")
                    print(f"API: {url}, Response Code: {response_code}, Response Data: {response_data}")
                    print("===================================") 
                    print("        ")
                    time.sleep(20)

                except Exception as e:
                    print(f"Error while processing API: {url}, Error: {e}")
        print("===================================")    
        print("         ")
        print("API execution completed.")
        print("         ")
        print("===================================")    
        return response_storage  
    api_list = [
        #  ====//// == Agency API == ////=======
    
            {
                "description": "Create User with correct data",
                "url": "https://maps-agency.locafy.com/users/create_user/",
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
                "url": "https://maps-agency.locafy.com/users/create_user/",
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
                "url": "https://maps-agency.locafy.com/users/create_user/",
                "method": "POST",
                "params":
                    {
                        "user_name": user_name,
                        "email": email,
                        "password": password
                    },
            },
            
            {
                "description": "Create User with special charcter in Username",
                "url": "https://maps-agency.locafy.com/users/create_user/",
                "method": "POST",
                "params":
                    {
                        "user_name": "-AI-TEST-user_name@@",
                        "email": "apimusthavestest10987@gmail.com",
                        "password": password
                    },
            },
            
            {
                "description": "Create User with incorrect email format",
                "url": "https://maps-agency.locafy.com/users/create_user/",
                "method": "POST",
                "params":
                    {
                        "user_name": "-AI-TEST-user_name120",
                        "email": "api 10987@gmail.com",
                        "password": password
                    },
            },
            
            {
                "description": "Create User with incorect password",
                "url": "https://maps-agency.locafy.com/users/create_user/",
                "method": "POST",
                "params":
                    {
                        "user_name": "-AI-TEST-user_name1201",
                        "email": "api10987@gmail.com",
                        "password": "Usman"
                    },
            },
            
            {
                "description": "Get all User list",
                "url": f"https://maps-agency.locafy.com/users/list/",
                "method": "GET",
                "params": None
            },
            
            {
                "description": "Get SS0 link of user with correct data",
                "url": f"https://maps-agency.locafy.com/users/login_link/",
                "method": "POST",
                "params": 
                        {
                        "user_name": "Usman-Latif-SQA-Admin",
                        "password": "Usman@112"
                        }
            },
            
            {
                "description": "Get SSO link of user with incorrect username",
                "url": f"https://maps-agency.locafy.com/users/login_link/",
                "method": "POST",
                "params": 
                        {
                        "user_name": "Aimalraza_",
                        "password": "Aimal@11"
                        }
            },
            
            {
                "description": "Get SOS link of user with incorrect password",
                "url": f"https://maps-agency.locafy.com/users/login_link/",
                "method": "POST",
                "params": 
                        {
                        "user_name": "Usman-Latif-SQA-Admin",
                        "password": "Usman@1"
                        }
            },
            
            # # =============================================================
            
            {
                "description": "Create Client",
                "url": "https://maps-agency.locafy.com/client/create/",
                "method": "POST",
                "params":
                    {
                        "client_name": Client_Name_New
                        }
            },
            {
                "description": "Create client with already created client name",
                "url": "https://maps-agency.locafy.com/client/create/",
                "method": "POST",
                "params":
                    {
                        "client_name": Client_Name_New
                        }
            },
            
            # # # # ======================================
            
            {
                "description": "Get client by providing client ID",
                "url": f"https://maps-agency.locafy.com/client/{Client_id}/",
                "method": "GET",
                "params": None
            },
            {
                "description": "Get client by providing incorrect client ID",
                "url": f"https://maps-agency.locafy.com/client/128/",
                "method": "GET",
                "params": None
            },
            
            # # ======================================
            
            {
                "description": "Get list of all clients",
                "url": f"https://maps-agency.locafy.com/client/clients/list/",
                "method": "GET",
                "params": None
            },
            
            # # # # # =========================================
            
            {
                "description": "Create campaign with correct data",
                "url": "https://maps-agency.locafy.com/campaigns/create/",
                "method": "POST",
                "params":
                    {
                    "user_id": User_id,
                    "business_gmb_cid": business_gmb_CID,
                    "campaign_name": Campaign_name,
                    "client_name": Client_name,
                    "keywords_for_analysis": keywords_for_analysis,
                    "grid_type": 7,
                    "grid_distance": 1
                    }
            },
            {
                "description": "Create campaign with incorrect user id",
                "url": "https://maps-agency.locafy.com/campaigns/create/",
                "method": "POST",
                "params":
                    {
                    "user_id": 143789,
                    "business_gmb_cid": business_gmb_CID,
                    "campaign_name": Campaign_name,
                    "client_name": Client_name,
                    "keywords_for_analysis": keywords_for_analysis,
                    "grid_type": 7,
                    "grid_distance": 1
                    }
            },
            
            {
                "description": "Create campaign with incorrect GMB CID",
                "url": "https://maps-agency.locafy.com/campaigns/create/",
                "method": "POST",
                "params":
                    {
                    "user_id": User_id,
                    "business_gmb_cid": "98649953187944340729864995318",
                    "campaign_name": Campaign_name,
                    "client_name": Client_name,
                    "keywords_for_analysis": keywords_for_analysis,
                    "grid_type": 7,
                    "grid_distance": 1
                    }
            },
            #================================
            # # ======================================
            
            {
                "description": "Deauthroize business by providing campaign ID",
                "url": f"https://maps-agency.locafy.com/campaigns/business/deauthorization/{Campaign_IHrt}",
                "method": "GET",
                "params": None
            },
            {
                "description": "Deauthroize business which is already deauthroize by providing campaign ID",
                "url": f"https://maps-agency.locafy.com/campaigns/business/deauthorization/{Campaign_IHrt}",
                "method": "GET",
                "params": None
            },
            {
                "description": "Deauthroize business by providing incorrect campaign ID",
                "url": f"https://maps-agency.locafy.com/campaigns/business/deauthorization/{Campaign_IFrf}",
                "method": "GET",
                "params": None
            }, 
            # # # # # =============================================================
            
            {
                "description": "Get list of all campaigns by campaign status",
                "url": f"https://maps-agency.locafy.com/campaigns/list/by/campaign_status/?campaign_status={Campaign_StatuS}&page=1&size=100",
                "method": "GET",
                "params": None
            },
            # # # # # # =============================================================
            
            {
                "description": "Get list of all campaigns",
                "url": "https://maps-agency.locafy.com/campaigns/list/all/",
                "method": "GET",
                "params": None
            },
            
            {
                "description": "Get list of all Geo Gifs URLs",
                "url": "https://maps-agency.locafy.com/geo/gifs/urls/list/",
                "method": "GET",
                "params":
                    {
                    "Page": 1,
                    "Size": 50
                    }   
            },
            # # # # ======================================
            
            {
                "description": "Get list of all Geo Grids URLs",
                "url": "https://maps-agency.locafy.com/geo/grid/urls/list/all/",
                "method": "GET",
                "params": None
            },
            # # # # ======================================
            
            {
                "description": "Get campaign by providing campaign ID",
                "url": f"https://maps-agency.locafy.com/campaigns/campaign_id_placeholder/",
                "method": "GET",
                "params": None
            },
            {
                "description": "Get campaign by providing incorrect campaign ID",
                "url": "https://maps-agency.locafy.com/campaigns/177/",
                "method": "GET",
                "params": None
            },
            
            {
                "description": "Get list of Geo Gifs URLs by providing campaign ID",
                "url": f"https://maps-agency.locafy.com/geo/gifs/urls/campaign/campaign_id_placeholder",
                "method": "GET",
                "params": None
            },
            {
                "description": "Get list of Geo Gifs URLs by providing incorrect campaign ID",
                "url": f"https://maps-agency.locafy.com/geo/gifs/urls/campaign/1205",
                "method": "GET",
                "params": None
            },
            # # # ======================================
            {
                "description": "Get list of Geo Grids URLs by providing campaign ID",
                "url": f"https://maps-agency.locafy.com/geo/grid/urls/campaign_id_placeholder/",
                "method": "GET",
                "params": None
            },
            
            {
                "description": "Get list of Geo Grids URLs by providing incorrect campaign ID",
                "url": f"https://maps-agency.locafy.com/geo/grid/urls/1496/",
                "method": "GET",
                "params": None
            },
            
            # # # ======================================
            
            {
                "description": "Get list of latest Grids URLs by providing campaign ID",
                "url": f"https://maps-agency.locafy.com/geo/grid/urls/latest/campaign_id_placeholder",
                "method": "GET",
                "params": None
            },
            
            {
                "description": "Get list of latest Grids URLs by providing incorrect campaign ID",
                "url": f"https://maps-agency.locafy.com/geo/grid/urls/latest/8573",
                "method": "GET",
                "params": None
            },
            {
                "description": "Get list of keywords suggestions for a business by providing CID",
                "url": f"https://maps-agency.locafy.com/keyword/suggestions/{business_gmb_CID}/",
                "method": "GET",
                "params":None
            },
            
            
            {
                "description": "Start campaign by provide Campaign Id",
                "url": f"https://maps-agency.locafy.com/campaigns/live/campaign_id_placeholder/",
                "method": "PATCH",
                "params": None
            },
            
            # ======================================
            
            {
                "description": "Get Reporting PDF with correct Campaign ID",
                "url": f"https://maps-agency.locafy.com/reporting/pdf/campaign_id_placeholder",
                "method": "GET",
                "params":None
            },
            
            {
                "description": "Get Reporting PDF with Incorrect Campaign ID",
                "url": f"https://maps-agency.locafy.com/reporting/pdf/789456123",
                "method": "GET",
                "params":None
            },
            # # ======================================
            {
                "description": "Get Campaign Map Rank Score by providing Campaign id",
                "url": f"https://maps-agency.locafy.com/graphs/campaign-map-rank-score/46587/",
                "method": "GET",
                "params":None
            },
            {
                "description": "Get Keyword Map Rank Score by providing Campaign id and keyword name",
                "url": f"https://maps-agency.locafy.com/graphs/keyword-map-rank-score/46587/software company",
                "method": "GET",
                "params":None
            },
            {
                "description": "Get Competitor Map Rank Score by providing Campaign id and keyword name",
                "url": f"https://maps-agency.locafy.com/graphs/competitor-map-rank-score/46587/software company",
                "method": "GET",
                "params":None
            }, 
            #======================================
            {
                "description": "Add keyword in campaign by providing campaign id",
                "url": "https://maps-agency.locafy.com/keyword/create/",
                "method": "POST",
                "params":
                    {
                    "campaign_id": campaign_id_placeholder,
                    "keyword": Keyword_neww
                    }
            },
            
            {
                "description": "Add keyword which is already added in campaign by providing campaign id",
                "url": "https://maps-agency.locafy.com/keyword/create/",
                "method": "POST",
                "params":
                    {
                    "campaign_id": campaign_id_placeholder,
                    "keyword": Keyword_neww
                    }
            },
            {
                "description": "Add keyword in campaign already having 7 keywords by providing campaign id",
                "url": "https://maps-agency.locafy.com/keyword/create/",
                "method": "POST",
                "params":
                    {
                    "campaign_id": Campaign_ITd,
                    "keyword": Keyword_neww
                    }
            },
            # ======================================
            
            {
                "description": "Delete keyword from campaign by providing campaign ID",
                "url": f"https://maps-agency.locafy.com/keyword/delete/'{Keyword_neww}'/campaign_id_placeholder",
                "method": "DELETE",
                "params": None
            },
            {
                "description": "Delete keyword which is already deleted from campaign by providing campaign ID",
                "url": f"https://maps-agency.locafy.com/keyword/delete/{Keyword_neww}/campaign_id_placeholder",
                "method": "DELETE",
                "params": None
            },
            {
                "description": "Try to delete last keyword of campaign by providing campaign ID",
                "url": f"https://maps-agency.locafy.com/keyword/delete/hello1/{Campaign_IFrf}",
                "method": "DELETE",
                "params": None
            },
            
            # # # =============================================================
            
            {
                "description": "Delete campaign by providing campaign ID",
                "url": f"https://maps-agency.locafy.com/campaigns/delete/campaign_id_placeholder/",
                "method": "DELETE",
                "params": None
            },
            
            {
                "description": "Delete campaign by providing incorrect campaign ID",
                "url": f"https://maps-agency.locafy.com/campaigns/delete/1289/",
                "method": "DELETE",
                "params": None
            },
            
            {
                "description": "Delete campaign by providing already deleted campaign ID",
                "url": f"https://maps-agency.locafy.com/campaigns/delete/campaign_id_placeholder/",
                "method": "DELETE",
                "params": None
            },
            
            # ======================================
            {
                "description": "Create Quick Analysis Campaign with correct data",
                "url": "https://maps-agency.locafy.com/quick_analysis/campaigns/create/",
                "method": "POST",
                "params":
                    {
                    "user_id": User_id,
                    "business_gmb_cid": business_gmb_CID,
                    "campaign_name": Campaign_name,
                    "keywords_for_analysis": keywords_for_analysis,
                    "grid_type": 7,
                    "grid_distance": 1
                    }
            },
            # # ======================================
            {
                "description": "Create Quick Analysis Campaign with Inccorrect GMB_CID",
                "url": "https://maps-agency.locafy.com/quick_analysis/campaigns/create/",
                "method": "POST",
                "params":
                    {
                    "user_id": User_id,
                    "business_gmb_cid": 159753456978634159494945642368,
                    "campaign_name": Campaign_name,
                    "keywords_for_analysis": keywords_for_analysis,
                    "grid_type": 7,
                    "grid_distance": 1
                    }
            },
            # # ======================================
            {
                "description": "Create Quick Analysis Campaign with Inccorrect User ID",
                "url": "https://maps-agency.locafy.com/quick_analysis/campaigns/create/",
                "method": "POST",
                "params":
                    {
                    "user_id": 798456,
                    "business_gmb_cid": business_gmb_CID,
                    "campaign_name": Campaign_name,
                    "keywords_for_analysis": keywords_for_analysis,
                    "grid_type": 7,
                    "grid_distance": 1
                    }
            },
            # # ======================================
            {
                "description": "Get Quick Analysis Campaign with Correct Campaign ID",
                "url": f"https://maps-agency.locafy.com/quick_analysis/campaigns/campaign_id_placeholded/",
                "method": "GET",
                "params":None
            },
            
            {
                "description": "Get Quick Analysis Campaign with Incorrect Campaign ID",
                "url": "https://maps-agency.locafy.com/quick_analysis/campaigns/38685269/",
                "method": "GET",
                "params":None
            },
            # # ======================================
            {
                "description": "Get Campaign Map Rank Score by providing Quick analysis campaign id",
                "url": f"https://maps-agency.locafy.com/graphs/campaign-map-rank-score/campaign_id_placeholded/",
                "method": "GET",
                "params":None
            },
            {
                "description": "Get Keyword Map Rank Score by providing Quick analysis campaign id and keyword name",
                "url": f"https://maps-agency.locafy.com/graphs/keyword-map-rank-score/campaign_id_placeholded/{keywords_for_analysis}",
                "method": "GET",
                "params":None
            },
            {
                "description": "Get Competitor Map Rank Score by providing Quick analysis campaign id and keyword name",
                "url": f"https://maps-agency.locafy.com/graphs/competitor-map-rank-score/campaign_id_placeholded/{keywords_for_analysis}",
                "method": "GET",
                "params":None
            }, 
            # # ======================================
            
            {
                "description": "Delete Quick Analysis Campaigns with campaign id",
                "url": f"https://maps-agency.locafy.com/quick_analysis/campaigns/delete/campaign_id_placeholded/",
                "method": "DELETE",
                "params": None
            },
            
            {
                "description": "Delete Quick Analysis Campaigns with incorrect campaign id",
                "url": f"https://maps-agency.locafy.com/quick_analysis/campaigns/delete/978456185/",
                "method": "DELETE",
                "params": None
            },      
            #     # # ======================================
        ] # Your API list

    # Call the function to hit the APIs and save the results
    result_file = "Mapbooster_API_result.csv"
    hit_apis_and_save_results(api_list, auth_token, result_file)

    # Read the CSV file and convert its content into a list of lists
    with open(result_file, "r", encoding="utf-8") as file:
        result_content = list(reader(file))

    # Skip the header row (first row of the CSV)
    result_content = result_content[1:]
    return result_content
    # Return the data as JSON

    # return jsonify(result)
