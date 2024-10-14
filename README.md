# # FastAPI with MySQL

This project demonstrates how to build a simple user management API using **FastAPI**, **SQLAlchemy ORM**, and **MySQL**. The API allows you to check the age of users, insert new users, update existing users, retrieve user details, and delete users from the database.


## Requirements

The application consists of two main tables:
- Python 3.7+
- FastAPI
- SQLAlchemy
- MySQL Connector
- Uvicorn (ASGI server)

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ponnipa-PJ/FastAPI.git
   cd FastAPI

2. **Create a virtual environment:**
   ```bash
   python -m venv myenv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     myenv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source myenv/bin/activate
     ```

4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt

6. **Create a .env file:**
   ```bash
   DATABASE_URL= "mysql+mysqlconnector://<username>:<password>@<host>:<port>/<database_name>
   ```
       
## API Endpoints
### User Endpoints ###
- **Get user:** ```GET /users/<id>```
    - Retrieve user details by ID.
- **Create a new user**: ```POST /users```
  ```json
  {
  "name": "John Doe",
  "birthDate": "2000-01-01"
  }
  ```
    - Insert a new user into the database.
- **Update a user**: ```PUT /users/<id>```
  ```json
  {
  "name": "Jane Doe",
  "birthDate": "1995-05-05"
  }
  ```
    - Update an existing user by ID.
- **Delete a user**: ```DELETE /users/<id>```
    - Delete a user by ID.
- **Check age**: ```GET /users/check-age/<id>```
    - Check the age of a user by ID and determine if they are over 18.
   
## API Documentation
FastAPI automatically generates interactive API documentation. You can view the documentation at the following URL:

  - Swagger UI: http://127.0.0.1:8000/docs
  - ReDoc: http://127.0.0.1:8000/redoc

## Running the Application 
```bash
    uvicorn main:app --reload
```