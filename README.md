﻿# PDFRotater

## About the Project
This is a django app made for an assignment of an internship selection process [Vaultedge].
In this django app I have created an API which rotates the page of an an input file, saves the modified pdf and return the url of the pdf.

## Installation 

To install the following app on your local system follow the steps given below:

- Install Python 3.10.7
- Install virtualenv
- Create a folder by whatever name your want to give. Example: Vaultedge
- Open the Vaultedge folder in VS Code. Open the terminal.
- Create a virtual environment: 
    ```
    virtualenv myenv
    ```
- Switch to the newly created environment:
    ```
    cd myenv/Scripts
    ```
    ```
    ./activate
    ```
- Return Back to the parent directory:
    ```
    cd ../../
    ```
- Clone the repository:
    ```
    git clone https://github.com/Vaibhav-22-dm/PDFRotater.git
    ```
- Change directory to newly cloned repository:
    ```
    cd PDFRotater
    ```
- Build the environment using the given requirements:
    ```
    pip install -r requirements.txt
    ```

- Start the django server:
    ```
    python manage.py runserver
    ```

- Install the thunderclient extension on VS Code or use Postman to test the API:

    API URL:
    ```
    http://127.0.0.1:8000/api/getrotatedpdf/
    ```
    Method: 
    ```
    POST
    ```
    Body:
    | key       | value          |
    | --------- | -------------- |
    | file      | 'Flower.pdf'   |
    | page      | 2              |
    | angle     | 90             |

