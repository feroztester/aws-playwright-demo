from datetime import datetime
import os

class ReportGenerator:

    @staticmethod
    def generate_report(test_result, target_record_id):

        html_report = f"""
        <html>
        <head>
            <title>Automation Execution Report</title>
        </head>

        <body>

        <h1>Python + Playwright + AWS POC Report</h1>

        <p>
            <b>Playwright Status:</b>
            <span style="color:green;font-weight:bold;">
                {test_result['playwright']}
            </span>
        </p>

      <p>
    <b>GET API Validation:</b>
    <span style="color:green;font-weight:bold;">
        {test_result['get_api']}
    </span>
</p>

<p>
    <b>POST API Validation:</b>
    <span style="color:green;font-weight:bold;">
        {test_result['post_api']}
    </span>
</p>

<p>
    <b>PUT API Validation:</b>
    <span style="color:green;font-weight:bold;">
        {test_result['put_api']}
    </span>
</p>

<p>
    <b>DELETE API Validation:</b>
    <span style="color:green;font-weight:bold;">
        {test_result['delete_api']}
    </span>
</p>

        <p>
            <b>AWS Validation:</b>
            <span style="color:green;font-weight:bold;">
                {test_result['aws_validation']}
            </span>
        </p>

        <p><b>Record ID:</b> {target_record_id}</p>

        <p><b>Execution Time:</b> {datetime.now()}</p>

        </body>
        </html>
        """

        os.makedirs("reports", exist_ok=True)

        with open("reports/test_report.html", "w") as report:
            report.write(html_report)

        print("HTML Report Generated Successfully")