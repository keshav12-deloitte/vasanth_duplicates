# Accumulus Web Automation Testing


Language: _Python 3.X_

Tool: _Pycharm, Selenium Webdriver_

Testing framework: _pytest_

Reporting: _allure_

Structure: _POM_ 

**Packages to be installed:**
Run a command in terminal `pip install -r requirments.txt`

**Update .env file:**
Update / check the values in `.env` file before executing the Automation Test cases

**different type of markers**
`smoke`

**Command to run test from Pycharm Terminal with marker(smoke):** 
`pytest -v -s -m <marker type>`

**Command to run test from Pycharm Terminal:** 
`pytest -v -s <test file to be executed>`

**Command to run test in parallel from Pycharm Terminal:** 
`pytest -v -s -n <number of parallel executions> <test file to be executed>`

**Command to run only the failed test cases in last run from Pycharm Terminal:** 
`pytest -v -s --lf`

**Command to run test by specifying browser & Headless mode from Pycharm Terminal:**
`pytest -v -s --browser <CHROME,FIREFOX> --headless <True,False> <test file to be executed>`

**Command to generate allure report:** 
**`pytest --alluredir=path_of_reports_folder -v -s <test files to be executed>`**

**Command to view the allure report in browser:**
**Allure has to be downloaded** 
**To view the allure report**
`allure serve <path_of_reports_folder>`

