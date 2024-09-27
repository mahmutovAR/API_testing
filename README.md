# SDET2024 API task

Application for testing the **[API Service](https://github.com/sun6r0/test-service)**

### Testcases
* **Create a new entity** `POST` `/api/create`
- **Delete entity** `DELETE` `/api/delete/{id}`
* **Get a single entity** `GET` `/api/get/{id}`
- **Get a list of entities** `GET` `/api/getAll`  
* **Partially update an entity** `PATCH` `/api/patch/{id}`  
***


## Requirements
* [Python](https://www.python.org/downloads/) (3.10.15)  
* [Allure](https://allurereport.org/docs/install/) (2.30.0)  
 
The Python packages can be installed by running  
```commandline
python3 -m pip install -r requirements.txt
```
***


## Run `run_test_service.py` to run the API Service

## Run `run_task_api.py` to test the API Service
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
**Note:** These directories will be created after running `run_task_api.py`

* `service_api/` API settings
* `test-service/` API Service
* `tests/` test modules
* `requirements.txt` required packages
* `run_task_api.py` API testing script
