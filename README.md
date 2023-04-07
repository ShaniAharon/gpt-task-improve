# ChatGPT API Wrapper App

This is a Python Flask application that demonstrates a backend with two routes, one GET and one POST. The POST route sends a message to the OpenAI API, and the GET route shows some text.

## Getting Started

### Prerequisites

To run this project, you'll need:

- Python 3.7 or higher
- Flask

### Installation

1. Clone the repository:
   git clone https://github.com/ShaniAharon/gpt-task

2. Change into the project directory:
   cd gpt-task

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

Retrieve A simple welcome message, e.g., &quot;Welcome to ChatGPT API Wrapper!&quot;

### POST `/chat`

Send a message to the OpenAI API. and returns the generated response.

### Test

test the post api by uncomment the lines 35-40 in the gpt_service.py file
or use postman etc..

#### Request

````json
{
  "message": "Your message here"
}

```response
{
    "received_message_from_gpt": "response",
    "status": "success"
}


````
