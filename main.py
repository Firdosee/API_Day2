import json

import requests

bearer_token = None


def test_get_status(self):
    resp = requests.get("https://hbs-ob-stage.herokuapp.com/status")
    code = resp.status_code
    assert code == 200, "Invalid status"


def test_get_otp(self):
    url = 'https://hbs-ob-stage.herokuapp.com/get_register_otp'
    headers = {'content-type': 'application/json'}
    payload = {
        "phone": "+918608561950"
    }
    resp = requests.post(url, data=json.dumps(payload), headers=headers)
    code = resp.status_code
    assert code == 200, "Invalid status"


def test_create_user(self):
    url = 'https://hbs-ob-stage.herokuapp.com/user'
    headers = {'content-type': 'application/json'}
    payload = {
        "name": "user_bro",
        "phone": "+918608561950",
        "email": "userbro@hashedin.com",
        "password": "admin",
        "otp": 111111
    }
    resp = requests.post(url, data=json.dumps(payload), headers=headers)
    code = resp.status_code
    assert code == 201, "Invalid status"


def test_edit_user(self):
    url = 'https://hbs-ob-stage.herokuapp.com/user'
    headers = {'content-type': 'application/json'}
    payload = {
        "name": "user",
        "phone": "+918608561950",
        "email": "userbro@hashedin.com",
        "password": "admin",
        "otp": 111111
    }
    resp = requests.put(url, data=json.dumps(payload), headers=headers)
    code = resp.status_code
    assert code == 200, "Invalid status"


def test_login(self):
    url = 'https://hbs-ob-stage.herokuapp.com/get_otp'
    headers = {'content-type': 'application/json'}
    payload = {
        "phone": "+918608561950"
    }
    resp = requests.post(url, data=json.dumps(payload), headers=headers)
    code = resp.status_code
    assert code == 200, "Invalid status"


def test_authenticate(self):
    global bearer_token
    url = 'https://hbs-ob-stage.herokuapp.com/authenticate'
    headers = {'content-type': 'application/json'}
    payload = {
        "phone": "+918608561950",
        "LoginType": "password",
        "password": "admin"
    }

    resp = requests.post(url, data=json.dumps(payload), headers=headers)
    code = resp.status_code
    assert code == 201, "Invalid status"
    # resp_dict = json.loads(resp)
    data = resp.json()
    print("hello")
    bearer_token = data['access_token']
    print(bearer_token)
    # t1 = Test_API_Day2()
    test_get_otp()


def test_auth_2():
    url2 = 'https://hbs-ob-stage.herokuapp.com/authenticate'
    print('hello')
    print(bearer_token)
    headers2 = {'content-type': 'application/json',
                'Authorization': 'Bearer ' + bearer_token
                }
    payload_2 = {
        "phone": "+918608561950",
        "LoginType": "OTP",
        "otp": 111111

    }
    resp = requests.post(url2, data=json.dumps(payload_2), headers=headers2)
    code = resp.status_code
    assert code == 201, "Invalid status"
