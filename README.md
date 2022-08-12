# FastAPIHomework

## Description
### Welcome! This is 2022 MVCLab Summer training homework, it simulates a company's employee database, and supports finding the best available employee at the moment

### Setup Guide
* **How to run**
    * **Step 1: Install Python Packages**
        * > pip install -r requirements.txt
    * **Step 2: Run by uvicorn (Localhost)**
        * > uvicorn main:app --reload
        * Default host = 127.0.0.1, port = 8000
    * **Step 3: Test your API using Swagger UI**
        * http://127.0.0.1:8000/docs


## JSON Object Data Structure
### Fields
* username:str = Employee's username
* jobdesk: Union[str, None] = Employee's current job, None means a trainee, no job yet
* rating: float = perfomance rating, the higher the better
* available_now: bool = whether available or not at the moment, True means available

## API Documentation
### GET Methods
    * > /list-all-members
        * List all the members in server
    * > /show-female-members
        * Find the female members
    * > /show-male-members
        * Find the male members
### POST Methods
    * > /add-student
        * add new student info to json file
    * > /upload
        * Upload a file to the server

