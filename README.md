# ChatGPT API Wrapper App

This is an imporved version of the Python Flask application that serves as a wrapper for the ChatGPT API. It features user authentication, message history, and interaction with the OpenAI API. Users can log in, send messages to the OpenAI API, and view their message history.

## Getting Started

### Prerequisites

To run this project, you'll need:

- Python 3.7 or higher
- Flask
- SQLAlchemy

### Installation

1. Clone the repository:
   git clone https://github.com/ShaniAharon/gpt-task-improve

2. Change into the project directory:
   cd gpt-task-improve

3. Set up a virtual environment:
   python3 -m venv venv

4. Activate the virtual environment:

- On Linux/macOS:
  source venv/bin/activate
- On Windows:
  venv\Scripts\activate

5. Install the required dependencies:
   pip install -r requirements.txt

### Configuration

Create a `.env` file in the project root directory with the following content:

OPENAI_API_KEY=<your_openai_api_key>

Replace `<your_openai_api_key>` with your actual OpenAI API key.

## Running the Application

Start the Flask development server:
flask run

The application will be accessible at `http://127.0.0.1:5000`.

## API Endpoints

### GET `/`

Retrieve the login page, after sign up can see the home page
e.g., &quot;Welcome to ChatGPT API Wrapper!&quot;

### POST `/chat`

Send a message to the OpenAI API. and returns the generated response.

### GET `/api/msg`

```response json example for /api/msg
[
  {
    "content": "hi",
    "id": 1,
    "role": "user",
    "ts": "Fri, 07 Apr 2023 12:21:57 GMT"
  },
  {
    "content": "Bot: Hi there! How can I help you?",
    "id": 2,
    "role": "assistant",
    "ts": "Fri, 07 Apr 2023 12:21:57 GMT"
  }
]


```
