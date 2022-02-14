import json

import requests

bearer_token = 'Hi'


class Test_API_Day2:

    def get_status(self):
        resp = requests.get("https://hbs-ob-stage.herokuapp.com/status")
        code = resp.status_code
        assert code == 200, "Invalid status"

    def get_otp(self, getotp):
        url = 'https://hbs-ob-stage.herokuapp.com/get_register_otp'
        headers = {'content-type': 'application/json'}
        payload = {
            "phone": "" + getotp + ""
        }
        resp = requests.post(url, data=json.dumps(payload), headers=headers)
        code = resp.status_code
        print("getting otp for ", getotp)
        print(code)

        assert code == 200, "Invalid status"

    def create_user(self, getotp, email):
        url = 'https://hbs-ob-stage.herokuapp.com/user'
        headers = {'content-type': 'application/json'}
        payload = {
            "name": "user_bro",
            "phone": "" + getotp + "",
            "email": "" + email + "",
            "password": "admin",
            "otp": 111111
        }
        resp = requests.post(url, data=json.dumps(payload), headers=headers)
        code = resp.status_code
        print("creating user")
        print(code)
        assert code == 201, "Invalid status"

    def edit_user(self, getotp, email, user):
        url = 'https://hbs-ob-stage.herokuapp.com/user'
        headers = {'content-type': 'application/json'}
        payload = {
            "name": "" + user + "",
            "phone": "" + getotp + "",
            "email": "" + email + "",
            "password": "admin",
            "otp": 111111
        }
        resp = requests.put(url, data=json.dumps(payload), headers=headers)
        code = resp.status_code
        assert code == 200, "Invalid status"

    def login(self, getotp):
        url = 'https://hbs-ob-stage.herokuapp.com/get_otp'
        headers = {'content-type': 'application/json'}
        payload = {
            "phone": "" + getotp + ""
        }
        resp = requests.post(url, data=json.dumps(payload), headers=headers)
        code = resp.status_code
        print("checking login status")
        print(code)
        assert code == 200, "Invalid status"

    def authenticate(self, getotp):
        global bearer_token
        url = 'https://hbs-ob-stage.herokuapp.com/authenticate'
        headers = {'content-type': 'application/json'}
        payload = {
            "phone": "" + getotp + "",
            "LoginType": "password",
            "password": "admin"
        }

        resp = requests.post(url, data=json.dumps(payload), headers=headers)
        code = resp.status_code
        print("Inside auth_1")
        print(code)

        # resp_dict = json.loads(resp)
        data = resp.json()
        print("auth_1")
        bearer_token = data['access_token']
        print(bearer_token)
        assert code == 201, "Invalid status"
        return bearer_token

    def auth_2(self, bearer, getotp):
        # global bearer_token
        url2 = 'https://hbs-ob-stage.herokuapp.com/authenticate'
        print('auth2')
        print(bearer)
        headers2 = {'content-type': 'application/json',
                    'Authorization': 'Bearer ' + bearer
                    }
        payload_2 = {
            "phone": "" + getotp + "",
            "LoginType": "OTP",
            "otp": 111111

        }
        resp = requests.post(url2, data=json.dumps(payload_2), headers=headers2)
        code = resp.status_code
        print("Inside auth_2")
        print(code)
        assert code == 201, "Invalid status"

    def login_2(self, bearer):
        url = 'https://hbs-ob-stage.herokuapp.com/protected_test'
        headers = {'content-type': 'application/json',
                   'Authorization': 'Bearer ' + bearer
                   }
        resp = requests.get(url, headers=headers)
        code = resp.status_code
        print("Logging in ...")
        print(code)
        assert code == 200, "Invalid status"

    def delete(self, getotp):
        url = 'https://hbs-ob-stage.herokuapp.com/user'
        headers = {'content-type': 'application/json'}
        payload = {
            "phone": "" + getotp + "",
            "otp": 111111
        }

        resp = requests.delete(url, data=json.dumps(payload), headers=headers)
        code = resp.status_code
        print("Deleting user...")
        print(code)
        assert code == 200, "Invalid status"

    def logout(self, bearer):
        url = 'https://hbs-ob-stage.herokuapp.com/logout'
        headers = {'content-type': 'application/json',
                   'Authorization': 'Bearer ' + bearer
                   }
        resp = requests.get(url, headers=headers)
        code = resp.status_code
        print("Logging out ...")
        print(code)
        assert code == 200, "Invalid status"
