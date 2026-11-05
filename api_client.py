import requests

class APIClient:

    BASE_URL = "https://reqres.in/api/users"

    # GET
    def get_user(self):

        response = requests.get(
            f"{self.BASE_URL}/2"
        )

        return response

    # POST
    def create_user(self):

        payload = {
            "name": "Feroz",
            "designation": "Senior Engineer"
        }

        response = requests.post(
            self.BASE_URL,
            json=payload
        )

        return response

    # PUT
    def update_user(self):

        payload = {
            "name": "Feroz",
            "designation": "Automation Tester"
        }

        response = requests.put(
            f"{self.BASE_URL}/2",
            json=payload
        )

        return response

    # DELETE
    def delete_user(self):
        response = requests.delete(
            f"{self.BASE_URL}/2"
        )
        return response