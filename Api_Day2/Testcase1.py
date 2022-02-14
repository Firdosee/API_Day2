from Api_Day2.All_Api_methods import Test_API_Day2

bearer_token = "None"


def test_create_user():
    t1 = Test_API_Day2()
    t1.get_status()
    t1.get_otp("919066752239")
    t1.create_user("919066752239", "user2239@hashedin.com")
    t1.edit_user("919066752239", "user2239@hashedin.com", "user_2239")


def test_del_user():
    t1 = Test_API_Day2()
    t1.delete("919066752239")


def test_Log_in():
    global bearer_token
    t1 = Test_API_Day2()
    t1.login("919066752239")
    bea = t1.authenticate("919066752239")
    t1.auth_2(bea, "919066752239")
    t1.login_2(bea)
    bearer_token = bea


def test_log_out():
    t1 = Test_API_Day2()
    t1.logout(bearer_token)
