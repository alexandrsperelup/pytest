from pages.login_page import LoginPage

class LoginSteps:
    def __init__(self):
        self.login_page = LoginPage()

    def perform_login(self, username, password):
        self.login_page.login(username, password)
