import os
from imports import *

USER_Name = "Usman SQA 2"
PASS_Word = "Usman@112"

keyword = "Not selected from options"
campaign_nam = "edited campaign"
Key_countte = "new keyword"


ce_traffic_url = "https://caseengine.live"
ce_project_listing_page = "https://caseengine.live/projects/"
ce_campaing_listing_page = "https://caseengine.live/projects/{project_id}"
ce_report_page = "https://caseengine.live/report/"
ce_campaign_error_page = "https://caseengine.live/campaign/errors/"

tiger_traffic_url = "http://164.92.68.49:3000/"
tiger_project_listing_page = "http://164.92.68.49:3000/projects/"
tiger_campaing_listing_page = "http://164.92.68.49:3000/projects/{project_id}"
tiger_report_page = "http://164.92.68.49:3000/report/"
tiger_campaign_error_page = "http://164.92.68.49:3000/campaign/errors/"


ce_login_username = os.getenv("CE_LOGIN_USERNAME", "ceuser@gmail.com")
ce_login_password = os.getenv("CE_LOGIN_PASSWORD", "cepassword")

tiger_login_username = os.getenv("TIGER_LOGIN_USERNAME", "tigeruser@gmail.com")
tiger_login_password = os.getenv("TIGER_LOGIN_PASSWORD", "tigerpassword@")

secret_key = os.getenv("SECRET_KEY", "0332033603250309")
sql_alchemy_database_url = os.getenv("SQLALCHEMY_DATABASE_URI", "mysql+pymysql://root:Aleena_Khan0786@localhost:3306/agency_apidb")









data = "import pdb; pdb.set_trace()"