# SDET2024 UI task

Application for testing the **[BankingProject UI](https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager)**

### Testcases
* **Add Customer**  
    Generate a 10-digit `Post Code` number  
    Generate `First Name` based on `Post Code`:
    - every two digits is a letter number of the alphabet (0 - "a", 1 - "b", etc.)
    - if the number is greater than 25, then 26 is 0, 27 is 1, etc.

- **Sort Customers by First Name**

* **Delete the Customer with the name length closest to the average**  
    Determine the average name length  
    Find `Customer` with the name length closest to the average  
    Delete this `Customer`
***


## Requirements
* [Python](https://www.python.org/downloads/) (3.10.15)  
* [Allure](https://allurereport.org/docs/install/) (2.30.0)  
 
The Python packages can be installed by running  
```commandline
python3 -m pip install -r requirements.txt
```
***


## Run `run_task_ui.py` to test the BankingProject
The `pytest-xdist` plugin extends `pytest` to speed up test execution,  
and `allure-pytest` is used for visualizing the results of a test run.

### First `pytest` runs 3 test cases in parallel
```commandline
pytest tests/ -n 3 --alluredir=allure-results --clean-alluredir
```

### Then a file is created with information about the environment (for example)
```
os_platform = Linux
os_release = 6.8.0-40-generic
python_version = Python 3.10.15
```

### Finally, `allure` converts the test results into an HTML report
```commandline
allure generate allure-report --clean --single-file allure-results
```

### And opens it in default browser
```python
import webbrowser
webbrowser.open('index.html')
```
***


### Files and directories:
- `allure-report/index.html` allure report
- `allure-results/` test results directory  
**Note:** These directories will be created after running `run_task_ui.py`

* `locators/` locators modules
* `pages/` web pages modules
* `tests/` test modules
* `requirements.txt` required packages
* `run_task_ui.py` UI testing script
