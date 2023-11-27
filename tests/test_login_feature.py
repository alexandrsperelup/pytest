import pytest
from steps.login_steps import LoginSteps

@pytest.fixture(scope="function")
def login_steps():
    return LoginSteps()

def test_login_feature(login_steps):
    login_steps.perform_login("your_username", "your_password")
    # Add assertions or verifications for successful login
    # For example, check for a successful login message or the appearance of a dashboard.
