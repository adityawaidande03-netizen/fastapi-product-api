Product Management API

A simple REST API for managing products, built using FastAPI, Python and MySQL.

Tech Used
Python
FastAPI
MySQL
SQLAlchemy
Pydantic
PyMySQL
Uvicorn
Features
Add new products
View all products
View a product by ID
Update product details
Delete products
Input validation using Pydantic
MySQL database for storing product data
Swagger UI for testing the API
Project Structure
├── main.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
├── .env.example
└── .gitignore
How to Run
1. Clone the repository
git clone <repository-url>
cd <project-folder>
2. Create a virtual environment
python -m venv venv

Activate it on Windows PowerShell:

.\venv\Scripts\Activate.ps1
3. Install the required packages
pip install -r requirements.txt
4. Set up MySQL

Create a MySQL database named:

product_db

Create a .env file in the project folder and add your database connection:

DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/product_db

Replace YOUR_PASSWORD with your MySQL password.

5. Start the API
uvicorn main:app --reload

The API will run at:

http://127.0.0.1:8000

Swagger API documentation can be opened at:

http://127.0.0.1:8000/docs
Example Product
{
    "name": "Copper Wire",
    "category": "raw",
    "description": "Copper electrical wire",
    "product_image": "https://example.com/copper.jpg",
    "sku": "COP-001",
    "unit_of_measure": "mtr",
    "lead_time": 7
}
API Endpoints
Method	Endpoint	Purpose
POST	/products	Create a product
GET	/products	Get all products
GET	/products/{id}	Get a product
PUT	/products/{id}	Update a product
DELETE	/products/{id}	Delete a product
Validation

Product data is validated using Pydantic before it is processed by the API. Invalid requests return appropriate validation errors.

Note

The .env file contains local database credentials and is not included in the repository. Use .env.example as a reference for setting up the database connection.


