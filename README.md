
### Below is the explanation of the key packages/files/directories/modules in the code:
- `.venv` is a virtual environment I have created and activated using using the `.venv\Scripts\activate `

- The `utils` package defines various utility functions:
    `locators` includes defination of all the locators created in seperate classes identified by its `page name`
    `test_cases` includes the declaration of the all the test cases which are automated.
    `users` includes the the test data.
    `fileUtils` This includes funtion to capture screenshot, but this can be extended to perform any file operations.

- As per the `PAGE OBJECT MODEL`, the `pages` package defines various page classes with element locator definitions and functions defining operations on these elements.
    `BasePage` class include basic functionality and driver initialization.
    `MainPage` is derived from the `BasePage` class, it contains methods related to Main page(`https://www.hudl.com`), which will be used to create test steps.
    `LoginPage` is derived from the `BasePage` class, it contains methods related to Login page, which will be used to create test steps.
    `SignUpPage & HomePage` is currently empty and it can also be defined later based on needs.

- The `tests` package contains the actual tests picking-up from `utils\test_cases`, which use the page class objects for instantiating the webdriver and running tests.
     `BaseTests` which holds basic functionality for my tests i.e. `setup() or tearDown()`, &  hence `Each TestClass should be derrived from BaseTests`
     `LoginTests` incudes test methods, which call various methods in accordance with the steps defined in the test cases from different PageClasses and `perform Assertions`.

- The `TestSuite` package contains the set of testclasses which can be called when running a suite
- The `globalConfig` is a file to store all global configurations suce as Path/directory address

### Setting up and running tests
1. Make sure `Python` extension is installed.
2. Install `selenium` in project dependencies with `pip install -U selenium`
3. If you want to see the list of test cases which are automated, then You can find them at `utils\test_cases.py`
3. If you want to run just a class, you should type: ` python -m unittest tests.LoginTests.LoginTests`
4. If you want to run just a test method, you should type: `python -m unittest tests.LoginTests.LoginTests.test_page_load`
5. If you want to run complete `TestSuite`, you should type `python -m unittest TestSuite.py`

