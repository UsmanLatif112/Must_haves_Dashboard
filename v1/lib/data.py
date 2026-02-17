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

bs_traffic_url = "https://traffic.brandsignals.io/"
bs_project_listing_page = "https://traffic.brandsignals.io/projects/"
bs_campaing_listing_page = "https://traffic.brandsignals.io/projects/{project_id}"
bs_report_page = "https://traffic.brandsignals.io/report/"
bs_campaign_error_page = "https://traffic.brandsignals.io/campaign/errors/"

# tiger_traffic_url = "http://164.92.68.49:3000/"
# tiger_project_listing_page = "http://164.92.68.49:3000/projects/"
# tiger_campaing_listing_page = "http://164.92.68.49:3000/projects/{project_id}"
# tiger_report_page = "http://164.92.68.49:3000/report/"
# tiger_campaign_error_page = "http://164.92.68.49:3000/campaign/errors/"
# tiger_traffic_url = "http://64.23.183.217:3000/"
# tiger_project_listing_page = "http://64.23.183.217:3000/projects/"
# tiger_campaing_listing_page = "http://64.23.183.217:3000/projects/{project_id}"
# tiger_report_page = "http://64.23.183.217:3000/report/"
# tiger_campaign_error_page = "http://64.23.183.217:3000/campaign/errors/"
tiger_traffic_url = "https://tiger.stormbreaker.ai/"
tiger_project_listing_page = "https://tiger.stormbreaker.ai/projects/"
tiger_campaing_listing_page = "https://tiger.stormbreaker.ai/projects/{project_id}"
tiger_report_page = "https://tiger.stormbreaker.ai/report/"
tiger_campaign_error_page = "https://tiger.stormbreaker.ai/campaign/errors/"

# torrential_traffic_url = "http://67.227.136.130:8089/"
# torrential_project_listing_page = "http://67.227.136.130:8089/dashboard/main/"
# torrential_campaing_listing_page = "http://67.227.136.130:8089/dashboard/project_view/{project_id}/"
# torrential_report_page = "http://67.227.136.130:8089/dashboard/reports/"
# torrential_campaign_error_page = "http://67.227.136.130:8089/dashboard/campaign-errors/"
torrential_traffic_url = "https://jkdtraffic.com/"
torrential_project_listing_page = "https://jkdtraffic.com/dashboard/main/"
torrential_campaing_listing_page = "https://jkdtraffic.com/dashboard/project_view/{project_id}/"
torrential_report_page = "https://jkdtraffic.com/dashboard/reports/"
torrential_campaign_error_page = "https://jkdtraffic.com/dashboard/campaign-errors/"

ldr_traffic_url = "http://144.126.155.62:3000/"
ldr_project_listing_page = "http://144.126.155.62:3000/projects/"
ldr_campaing_listing_page = "http://144.126.155.62:3000/projects/{project_id}"
ldr_report_page = "http://144.126.155.62:3000/report/"
ldr_campaign_error_page = "http://144.126.155.62:3000/campaign/errors/"

ce_login_username = os.getenv("CE_LOGIN_USERNAME", "cesuperuser@gmail.com")
ce_login_password = os.getenv("CE_LOGIN_PASSWORD", "AkSx0J#3nCfDy^G%")

tiger_login_username = os.getenv("TIGER_LOGIN_USERNAME", "tiger_admin_qa@gmail.com")
tiger_login_password = os.getenv("TIGER_LOGIN_PASSWORD", "!fFK8JKr2!o&18WY")

# torrential_login_username = os.getenv("TORRENTIAL_LOGIN_USERNAME", "torrential_admin_user")
# torrential_login_password = os.getenv("TORRENTIAL_LOGIN_PASSWORD", "8@J#5!2InMP5uehj")

torrential_login_username = os.getenv("TORRENTIAL_LOGIN_USERNAME", "zulqarnain_qa_1")
torrential_login_password = os.getenv("TORRENTIAL_LOGIN_PASSWORD", "TbdewMaZxBA*^51a")

bs_login_username = os.getenv("BS_LOGIN_USERNAME", "ShakeelKhan@gmail.com")
bs_login_password = os.getenv("BS_LOGIN_PASSWORD", "Shakeel#1133")

ldr_login_username = os.getenv("LDR_LOGIN_USERNAME", "lf_user_team@gmail.com")
ldr_login_password = os.getenv("LDR_LOGIN_PASSWORD", "d2Di49gN9Ajyb4M")

secret_key = os.getenv("SECRET_KEY", "0332033603250309")
sql_alchemy_database_url = os.getenv("SQLALCHEMY_DATABASE_URI", "mysql+pymysql://root:Aleena_Khan786@localhost:3306/agency_apidb")


CE = ["Turing","Google Search No Click","Multiple Session","Organic","Spreadsheet","Squidoosh","Tiered","Wordpress","Youtube","Local Squidoosh"]
Tiger = ["Birthday","Birthday Amazon","Bsr Booster","Lookey","Pathfinder","Rocket","Shopify","Walmart","Squidoosh","Website Specific","Google Search No Click","Multiple Session","Organic","Spreadsheet","Tiered","Wordpress","Youtube"]
Torrential = ["google_search_no_click","multiple_session","Organic","Spreadsheet","Squidoosh","Tiered","Youtube"]
BS = ["Organic","Tiered","multiple_session","google_search_no_click","Rocket"]
LDR = ["Google Search No Click","Multiple Session","Organic","Tiered"]










data = "import pdb; pdb.set_trace()"