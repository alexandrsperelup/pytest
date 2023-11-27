from selene import by, browser

class LoginPage:
    def __init__(self):
        self.username_input = browser.element(by.name("username"))
        self.password_input = browser.element(by.name("password"))
        self.login_button = browser.element(by.css(".login-button"))

    def login(self, username, password):
        self.username_input.type(username)
        self.password_input.type(password)
        self.login_button.click()
