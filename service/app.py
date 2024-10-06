"""
Lambda function to manage users information
Microservice in python to manage radionets users information.
"""

import json

"""Users information"""
users = [
    {
        "id": 1,
        "name": "Alejandro",
        "last_name": "Perez",
        "role": "Admin",
        "email": "alex@gmail.com",
        "password": "C+I3N5HYBB9akVejtdfrXPMoLo4PnH9S7+vb4AZ3KWTi6BwsoQ==="
    },
    {
        "id": 2,
        "name": "Testing",
        "last_name": "Rodriguez",
        "role": "Admin",
        "email": "testing@gmail.com",
        "password": "3aB1ZNM0nsOptY+LvMjfDheOJLwyW3Rcz9RbpIEytT5H7VEn8Q8w=="
    },
    {
        "id": 3,
        "name": "Mariana",
        "last_name": "Gonzalez",
        "role": "Admin",
        "email": "maring@gmail.com",
        "password": "jth7qUkpZ1/bcF66fHZSjNr+Atk+dIy4TpRn2Y1gTYdKqnEFddM7Q=="
    },
    {
        "id": 4,
        "name": "Gonzalo",
        "last_name": "Lezama",
        "role": "Admin",
        "email": "gonz@gmail.com",
        "password": "jTZMVkJ+vbqNCOFd7xiMba42o1JrF1fkOOkPr2zSvx0oA/l9GH3OA=="
    }
]


def get_users(event, context):
    """
    Lambda function to return all registered radionet users
    """

    return {
        "statusCode": 200,
        "body": json.dumps({
            "response": users
        }),
    }


def get_user(event, context):
    """
    Lambda function to return a user by id
    """

    user_loc = [element for element in users if element['name'] == "Alejandro"]

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": user_loc
        }),
    }


def insert_user(event, context):
    """
    Lambda function to insert a new user
    """

    http_body = event['body']
    name = http_body["name"]
    last_name = http_body["last_name"]
    role = http_body["role"]
    email = http_body["email"]
    password = http_body["password"]

    name = name.lower()
    last_name = last_name.lower()
    role = role.lower()
    email = email.lower()
    password = password.lower()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "User inserted correctly"
        }),
    }
