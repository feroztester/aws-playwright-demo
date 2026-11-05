class StepFunctionClient:

    def get_latest_executions(self):
        # Mock data for now
        return [
            {"recordId": "1001"},
            {"recordId": "1002"},
            {"recordId": "1003"},
            {"recordId": "1004"},
            {"recordId": "1005"}
        ]