import pytest

from Actions.HomePageAction import HomePageAction
from Actions.LoginPageAction import LoginPageAction
from Actions.AccountPageAction import AccountPageAction
from Actions.SearchPageAction import SearchPageAction
from Actions.RegisterPageAction import RegisterPageAction
from Actions.AccountSuccessPageAction import AccountSuccessPageAction
from Utilities import logCreators
from Utilities.configReader import get_Config_Data


@pytest.mark.usefixtures("settingUp_and_Down")
class Test_Login:
    log = logCreators.log_generator()

    def test_valid_login(self):

        self.log.info("Starting Valid Login Test")

        hp = HomePageAction(self.driver)

        self.log.info("Clicking My Account")
        hp.click_my_account()

        self.log.info("Clicking Login")
        hp.click_login()

        lp = LoginPageAction(self.driver)

        self.log.info("Entering Login Credentials")
        lp.login(
            get_Config_Data("login credentials", "username"),
            get_Config_Data("login credentials", "password"),
        )

        ap = AccountPageAction(self.driver)

        self.log.info("Verifying Login Success")
        assert ap.success_login()

        self.log.info("Valid Login Test Passed")

    def test_search_func(self):

        self.log.info("Starting Search Function Test")

        hp = HomePageAction(self.driver)

        self.log.info("Entering Search Word")
        hp.pass_word_SB(get_Config_Data("search", "word"))

        sp = SearchPageAction(self.driver)

        self.log.info("Verifying Search Result")
        assert sp.search_result()

        self.log.info("Search Function Test Passed")

    def test_register_fucn(self):

        self.log.info("Starting Register Test")

        hp = HomePageAction(self.driver)

        self.log.info("Opening Account Menu")
        hp.click_my_account()

        self.log.info("Opening Login Page")
        hp.click_login()

        lp = LoginPageAction(self.driver)

        self.log.info("Clicking Continue for Registration")
        lp.click_Rcontinue()

        rp = RegisterPageAction(self.driver)

        fn = get_Config_Data("register credentials", "fname")
        ln = get_Config_Data("register credentials", "lname")
        email = get_Config_Data("register credentials", "email")
        telephone = get_Config_Data("register credentials", "telephone")
        password = get_Config_Data("register credentials", "password")
        cpassword = get_Config_Data("register credentials", "cpassword")

        self.log.info("Entering Registration Details")

        rp.enter_credentials(fn, ln, email, telephone, password, cpassword)

        asp = AccountSuccessPageAction(self.driver)

        self.log.info("Verifying Registration Success")
        assert asp.success_register()

        self.log.info("Register Test Passed")
