# FastAPI Blog Application

This is a FastAPI application designed for blog management. It includes features for user authentication, blog post creation, and data validation.

## Features and Functionalities

- **User Authentication**: The application uses JWT tokens and OAuth2 authentication to ensure secure access. Users can register, log in, and manage their accounts with peace of mind, knowing their data is protected.

- **Blog Management**: Users can create, update, and delete blog posts. The application supports rich text formatting, allowing users to create engaging and visually appealing content.

- **Data Validation**: The application uses Pydantic schemas to validate request and response payloads. This ensures data consistency and integrity, preventing errors and inconsistencies.

- **User Management**: Administrators can manage user accounts, including creating, updating, and deleting users. This feature is crucial for maintaining a healthy and active user base.

- **Secure Password Storage**: Passwords are securely hashed before being stored in the database. This prevents anyone, including database administrators, from viewing user passwords.

- **Database Interactions**: The application uses SQLAlchemy to interact with the database. This provides a high level of abstraction, making it easier to perform complex database operations.


## Directory Structure

- **routers/**: This directory contains router files (`authentication.py`, `user.py`, `blog.py`) that define endpoints for authentication, user management, and blog operations.
- **JWTtoken.py**: This file implements functions for JWT token management, supporting authentication and authorization mechanisms.
- **database.py**: This file configures database connections using SQLAlchemy, facilitating interaction with the underlying database.
- **oauth2.py**: This file contains utility functions for OAuth2 authentication, enhancing the security and usability of the application.
- **models/**: This directory contains Python files defining data models for blog posts (`blog_model.py`) and user management (`user_models.py`).
- **hashing.py**: This file provides functions for password hashing to ensure secure storage and validation of user passwords.
- **main.py**: This file serves as the main entry point for the FastAPI application, initializing and running the API server.
- **repository/**: This directory includes repository files (`blogfile.py`, `userfile.py`) responsible for database operations related to blogs and users.
- **schema.py**: This file defines Pydantic schemas used for validating request and response payloads, ensuring data consistency and integrity.

## Usage

To run the FastAPI application:

1. Install the required dependencies listed in `requirements.txt`.
2. Configure your database connection in `database.py`.
3. Execute `uvicorn main:app --reload` from the project directory to start the FastAPI server with automatic reloading on code changes.

#
![Alt text](screenshot.png)
#

Please note that this application is under development and may undergo significant changes.

