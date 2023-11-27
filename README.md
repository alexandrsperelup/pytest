# PyTest Framework

A Python-based testing framework using pytest, Selene, and Moon2 cluster for end-to-end testing.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/alexandrsperelup/pytest/pytest.git

Navigate to the project directory:
cd testing-framework

Install the required dependencies:
pip install -r requirements.txt

Configuration
Update the config/moon2_config.yaml file with your Moon2 cluster settings and other configurations.

Project Structure
testing-framework/
|-- tests/
|   |-- conftest.py
|   |-- test_login_feature.py
|-- pages/
|   |-- login_page.py
|-- steps/
|   |-- login_steps.py
|-- config/
|   |-- moon2_config.yaml
|-- README.md
|-- requirements.txt


## Running tests
Locally
pytest -k test --chromedriver /path/to/chromedriver

On Moon2 Cluster
pytest -k test --remote

##  Command-Line Options
--local: Run tests locally (default).
--remote: Run tests on the Moon2 cluster.

##  Test Examples
See tests/test_login_feature.py for an example of testing the login feature using steps and page objects.
