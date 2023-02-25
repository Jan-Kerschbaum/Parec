ℹ️ This folder contains test scripts for the Parec backend. These scripts can be executed to ensure the functionality and performance of the backend.

## ⚙️ Prerequisites 

- Python 3.x
- Required packages are listed in requirements.txt
- A running instance of the Parec backend

## ⚒️ Installation  

1. Clone or download the repository.
2. Install the required packages with the following command: `pip install -r requirements.txt`

## 🚀 Execution  

1. Ensure that the Parec backend is running.
2. Navigate to the [app/tests](parec-backend/app/tests) directory.
3. Execute the tests with the following command: `python -m unittest discover`

## 📈 Test Results 

After executing the tests, the results will be displayed in the terminal. Any failed tests will be reported, along with information about the specific error. Additionally, a test report will be generated in XML format and stored in the `test-reports` directory.