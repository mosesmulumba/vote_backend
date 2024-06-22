## E-Voting System API
This repository contains the backend code for an E-Voting System API built using Flask, SQLAlchemy, and Flask-RESTX. The API provides secure, efficient, and scalable endpoints for managing users, candidates, and votes, along with additional functionalities for handling election results and management.

# Features
* User Authentication and Authorization
    * JWT Authentication: Secure user login using JSON Web Tokens (JWT) to protect endpoints and manage user sessions.
    * Role-Based Access Control: Implemented to restrict access to specific endpoints based on user roles (e.g., admin, voter).
* CRUD Operations
    *  Users: Create, read, update, and delete user accounts.
    * Candidates: Manage candidate information including creation, retrieval, updating, and deletion.
    * Votes: Cast votes, and track vote timestamps to ensure integrity.
* Data Validation and Serialization
    * Input Validation: Utilizes Flask-RESTX's ns.expect for validating incoming data to ensure correct data types and required fields.
    * Response Formatting: Uses ns.marshal_with for consistent response formatting.
* Database Models and Relationships
    * QLAlchemy Models: Defines User, Candidate, and Vote models with relationships using SQLAlchemy ORM.
    * Database Migrations: Managed using Flask-Migrate to handle schema changes without data loss.
* Additional Features
    * Election Management: Endpoints to create and close elections, ensuring proper election lifecycle management.
    * Election Results: Provides aggregated results of votes for each candidate, ensuring transparent and accurate result reporting.
* Error Handling
    * Custom Error Responses: Implements custom error handlers to provide meaningful error messages and appropriate HTTP status codes for different types of errors.

## You can clone this repository by on this link
https://github.com/mosesmulumba/vote_backend.git

## Then run a change directory command to checkout the repository directory
cd vote_backend

## Create an environment where you will install the required extensions and libraries
  *  python3 -m venv <name_of_environment>

   * source <namr_of_environment>/bin/activate

   * pip3 install -r requirements.txt
