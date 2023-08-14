import requests, json

class Vox():
    def __init__(self, token, pin, url):
        self.token=token
        self.pin=pin
        self.url=url
    def get(self):
        try:

            data = {
                "token": self.token,
                "pin": self.pin
            }

            response = requests.post(self.url, data=data)
            Json=response.text
            Json=json.loads(Json)
            return Json
        except requests.exceptions.JSONDecodeError:
            print("Empty or invalid JSON response")
        




