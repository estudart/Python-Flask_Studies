# Python Flask Planets API

![API_BackEnd](https://github.com/estudart/Python-Flask_Studies/blob/main/API_BackEnd.PNG)

## Description
This repository contains a Flask project for building a RESTful API to manage information about planets and users. It includes endpoints for retrieving, creating, updating, and deleting data.

## Technologies Used
- **Backend**: Flask, SQLAlchemy
- **Database**: SQLite
- **Documentation**: Swagger

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/estudart/Python-Flask_Studies.git
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

1. Run the Flask application:
   ```bash
   python app.py
2. Access the API documentation at http://127.0.0.1:5000/apidocs/ to explore available endpoints and interact with the API.


## Endpoints

[API Documentation](https://estudart.pythonanywhere.com/apidocs/)

![API_BackEnd](https://github.com/estudart/Python-Flask_Studies/blob/main/Doc.PNG)

- `/planets`:
  - `GET`: Retrieve a list of planets.
  - `POST`: Create a new planet.
- `/planet/<id>`:
  - `GET`: Retrieve information about a specific planet.
  - `PUT`: Update information about a specific planet.
  - `DELETE`: Delete a specific planet.
- `/user/<id>`:
  - `GET`: Retrieve information about a specific user.
  - `PUT`: Update information about a specific user.
  - `DELETE`: Delete a specific user.
- `/users`:
  - `GET`: Retrieve a list of all users.
  - `POST`: Create a new user.
- `/create_planets`:
  - `GET`: Populate the database with predefined planet data.
