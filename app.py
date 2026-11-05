from playwright.sync_api import sync_playwright

from api_client import APIClient
from aws_client import StepFunctionClient
from config import TARGET_RECORD_ID
from utils.report_generator import ReportGenerator

# Store execution results
test_result = {}

# ==========================================
# Playwright Validation
# ==========================================

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto("https://iniapro.relevantz.com/")

    print("\n========================================")
    print("PLAYWRIGHT VALIDATION")
    print("========================================")
    print("Browser Launched Successfully")

    page.wait_for_timeout(5000)

    test_result["playwright"] = "PASS"

    browser.close()


# ==========================================
# API Validation
# ==========================================

api_client = APIClient()

# -------- GET Validation --------

get_response = api_client.get_user()

if get_response.status_code == 200:

    data = get_response.json()["data"]

    print("\n========================================")
    print("GET API VALIDATION")
    print("========================================")
    print(f"Status Code : {get_response.status_code}")
    print(f"ID          : {data['id']}")
    print(f"First Name  : {data['first_name']}")
    print(f"Last Name   : {data['last_name']}")
    print(f"Email       : {data['email']}")

    test_result["get_api"] = "PASS"

else:

    print("GET API Validation Failed")
    test_result["get_api"] = "FAIL"


# -------- POST Validation --------

post_response = api_client.create_user()

if post_response.status_code in [200, 201]:

    data = post_response.json()

    print("\n========================================")
    print("POST API VALIDATION")
    print("========================================")
    print(f"Status Code : {post_response.status_code}")
    print(f"Name        : {data['name']}")
    print(f"Designation : {data['designation']}")
    print(f"User ID     : {data['id']}")
    print(f"Created At  : {data['createdAt']}")

    test_result["post_api"] = "PASS"

else:

    print("POST API Validation Failed")
    test_result["post_api"] = "FAIL"


# -------- PUT Validation --------

put_response = api_client.update_user()

if put_response.status_code == 200:

    data = put_response.json()

    print("\n========================================")
    print("PUT API VALIDATION")
    print("========================================")
    print(f"Status Code : {put_response.status_code}")
    print(f"Name        : {data['name']}")
    print(f"Designation : {data['designation']}")
    print(f"Updated At  : {data['updatedAt']}")

    test_result["put_api"] = "PASS"

else:

    print("PUT API Validation Failed")
    test_result["put_api"] = "FAIL"


# -------- DELETE Validation --------

delete_response = api_client.delete_user()

if delete_response.status_code == 204:

    print("\n========================================")
    print("DELETE API VALIDATION")
    print("========================================")
    print(f"Status Code : {delete_response.status_code}")
    print("Delete Status : SUCCESS")

    test_result["delete_api"] = "PASS"

else:

    print("DELETE API Validation Failed")
    test_result["delete_api"] = "FAIL"


# ==========================================
# AWS Validation
# ==========================================

aws_client = StepFunctionClient()

executions = aws_client.get_latest_executions()

record_found = False

for execution in executions:

    if execution["recordId"] == TARGET_RECORD_ID:
        record_found = True
        break


if record_found:

    print("\n========================================")
    print("AWS VALIDATION")
    print("========================================")
    print(f"Record ID : {TARGET_RECORD_ID}")
    print("Status    : SUCCESS")

    test_result["aws_validation"] = "PASS"

else:

    print("\n========================================")
    print("AWS VALIDATION")
    print("========================================")
    print(f"Record ID : {TARGET_RECORD_ID}")
    print("Status    : FAILURE")

    test_result["aws_validation"] = "FAIL"


# ==========================================
# Generate HTML Report
# ==========================================

ReportGenerator.generate_report(
    test_result=test_result,
    target_record_id=TARGET_RECORD_ID
)