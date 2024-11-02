# Messaging Microservice
### Ishika Shah (ishikashah2510@yahoo.com)
### for selfactualize.ai

## Purpose of the Application
The Messaging Microservice is designed to facilitate the sending of messages through various channels such as email, SMS, and WhatsApp. It includes functionality to log each message's delivery status, ensuring transparency and tracking of message delivery.

## How Does the Application Work
1. The application exposes a single endpoint, `/sendMessage`, which accepts POST requests with a JSON payload containing the message type, recipient, and content.
2. The application validates the input fields and uses a mock function to simulate sending messages via different channels.
3. The status of each message (success or failure) along with relevant information is logged in a SQLite database for later retrieval and analysis.

## Steps to Run the Application on Your Local Machine

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)
- SQLite (for database management)

### Installation Steps
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. **Create a virtual env**
    ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install required packages**
    ```bash
   pip install -r requirements.txt

4. **Setting up the database**
   ```python
   from app import db, app
   
   with app.app_context():
       db.create_all()

5. **Run the application**
    ```bash
    python app.py

**The application should now be running on http://127.0.0.1:5000**

### The endpoint can be tested manually using Postman
**Dummy payload**

    {
        "type": "email",
        "recipient": "user@example.com",
        "content": "Hello, this is a test message."
    }

### Future Work
1. Implement real message-sending functionality using external APIs (e.g., Twilio for SMS, SMTP for email).
2. Add authentication and authorization for secure access to the API.
3. Enhance the logging mechanism to include more details and potential error handling.
4. Create a front-end application to interact with the microservice.


## Significance of Each File

### `app.py`
This is the main application file that sets up the Flask web server, defines the `/sendMessage` endpoint, processes incoming requests, validates the input, simulates message sending, and logs the message details in the database.

### `db_setup.py`
This file sets up the database using SQLAlchemy, defines the `MessageLog` model that represents the structure of the logged messages, including attributes like type, recipient, content, status, and timestamp.

### `mock_send.py`
This module contains the logic for the mock message-sending functionality. It includes functions to validate email and phone number formats and simulate sending messages through various channels (email, SMS, WhatsApp).

### `test.py`
This file contains unit tests for the application. It tests the `/sendMessage` endpoint for various scenarios, including unsupported message types and invalid recipient formats.

### `config.py`
This file holds configuration settings for the application, including the database URI. It can also be expanded to include configurations for message-sending services.


## Deploying on AWS cloud
While I don't have enough free resources left on my account, I normally use AWS
ECS to deploy applications to the cloud. The steps include, creating a docker file,
build a Docker image, set up an ECS and push the docker image onto Amazon ECR, after which
create a task and set it up to use the Docker image. 
