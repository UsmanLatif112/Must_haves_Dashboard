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

torrential_traffic_url = "http://67.227.136.130:8089/"
torrential_project_listing_page = "http://67.227.136.130:8089/dashboard/main/"
torrential_campaing_listing_page = "http://67.227.136.130:8089/dashboard/project_view/{project_id}/"
torrential_report_page = "http://67.227.136.130:8089/dashboard/reports/"
torrential_campaign_error_page = "http://67.227.136.130:8089/dashboard/campaign-errors/"

bs_traffic_url = "http://69.167.137.49:8089/"
bs_project_listing_page = "http://69.167.137.49:8089/dashboard/main/"
bs_campaing_listing_page = "http://69.167.137.49:8089/dashboard/project_view/{project_id}/"
bs_report_page = "http://69.167.137.49:8089/dashboard/reports/"
bs_campaign_error_page = "http://69.167.137.49:8089/dashboard/campaign-errors/"


ce_login_username = os.getenv("CE_LOGIN_USERNAME", "cesuperuser@gmail.com")
ce_login_password = os.getenv("CE_LOGIN_PASSWORD", "ce_super_user1122@")

tiger_login_username = os.getenv("TIGER_LOGIN_USERNAME", "tiger_super_user@gmail.com")
tiger_login_password = os.getenv("TIGER_LOGIN_PASSWORD", "tiger_super_user1122@")

torrential_login_username = os.getenv("TORRENTIAL_LOGIN_USERNAME", "torrential_admin_user")
torrential_login_password = os.getenv("TORRENTIAL_LOGIN_PASSWORD", "8@J#5!2InMP5uehj")

bs_login_username = os.getenv("BS_LOGIN_USERNAME", "production_qa_traffic")
bs_login_password = os.getenv("BS_LOGIN_PASSWORD", "productionqa1122@")

secret_key = os.getenv("SECRET_KEY", "0332033603250309")
sql_alchemy_database_url = os.getenv("SQLALCHEMY_DATABASE_URI", "mysql+pymysql://root:Aleena_Khan786@localhost:3306/agency_apidb")


CE = ["Turing","Google Search No Click","Multiple Session","Organic","Spreadsheet","Squidoosh","Tiered","Wordpress","Youtube","Local Squidoosh"]
Tiger = ["Birthday","Birthday Amazon","Bsr Booster","Lookey","Pathfinder","Rocket","Shopify","Walmart","Squidoosh","Website Specific","Google Search No Click","Multiple Session","Organic","Spreadsheet","Tiered","Wordpress","Youtube"]
Torrential = ["google_search_no_click","multiple_session","Organic","Spreadsheet","Squidoosh","Tiered","Youtube"]
BS = ["Organic","Tiered","multiple_session","google_search_no_click","Rocket"]










data = "import pdb; pdb.set_trace()"