import pytest
import yaml
from selene import config
from selene.support.shared import browser
from pathlib import Path

# Load Moon2 settings from config file
config_file_path = Path("config/moon2_config.yaml")
moon2_settings = config_file_path.read_text()

# Parse YAML content and set Moon2 cluster URL
moon2_cluster_url = yaml.load(moon2_settings)['moon2']['cluster_url']
config.base_url = moon2_cluster_url

# Fixture to create a browser session on Moon2 or locally
@pytest.fixture(scope="function")
def selenium_browser(request):
    # Get browser capabilities from the command line (if provided)
    capabilities = request.config.getoption('--capabilities') or {}

    # Check if --remote option is provided to run tests remotely (on Moon2)
    if request.config.getoption('--remote'):
        # Set up Moon2 cluster browser configuration
        browser.config.driver = browser.Chrome(**capabilities)
    else:
        # Set up local browser configuration (e.g., ChromeDriver path, etc.)
        capabilities.update({
            'chromeOptions': {
                'args': ['--disable-infobars', '--start-maximized']
            }
        })
        browser.config.driver = browser.Chrome(**capabilities)

    browser.open_url("/")
    yield browser
    browser.quit()
