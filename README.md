# Djangommerce

Djangommerce is an online market hub built using Django, designed to allow users to post items for sale, set prices, manage availability, and communicate with potential buyers through a built-in chat system. The primary aim of Djangommerce is to provide a platform for users to showcase their items.

![Djangommerce](https://i.postimg.cc/YqrTTx5C/merged-horizontally.png "Djangommerce demo")

## Application Architecture

Djangommerce follows the MVT (Model-View-Template) architecture of Django Web Framework:

- **Models**: Define the structure of the database including items, users, chat messages, etc.
- **Views**: Manage the business logic, process user input, and interact with the models.
- **Templates**: Handle the presentation logic, rendering templates, and passing data to frontend.

## Local Development

### Requirements

- **Python**: Version 3.10
- **Pipenv**: Install pipenv running `pip install pipenv`

### Setup

Read and follow these steps to set up the project locally:

1. Clone the repo and move into the project's directory:
   ```
   git clone <repository-url>
   cd djangommerce
   ```

2. Follow the instructions in the _.env.example_ file.

3. Create a virtual environment and install the required packages:
   ```
   pipenv shell
   pipenv install
   ```

4. Apply the database migrations:
   ```
   python manage.py migrate
   ```

### Run locally

To run the server locally, use the following command:
   ```
   python manage.py runserver
   ```

Djangommerce will be accessible at **http://localhost:8000**

### Running tests

To run the existing tests, execute the following command:
   ```
   python manage.py test
   ```
