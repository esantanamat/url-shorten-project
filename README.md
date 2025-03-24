# URL Shortening Service

A simple URL shortening service built using Flask, SQLAlchemy, and PostgreSQL. This API allows you to shorten URLs, update them, delete them, and view statistics about their usage.

## Features

- Shorten long URLs to a more compact form.
- Retrieve the original URL by visiting the shortened URL.
- View the stats of shortened URLs, such as the number of times they have been accessed.
- Update or delete shortened URLs.

## Installation

### Prerequisites

Make sure you have the following installed:

- Python 3.7 or higher
- pip
- PostgreSQL (or another database of your choice)

### Setting up the environment

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/url-shortening-service.git
   cd url-shortening-service
2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
3. Install dependices
   ```bash
   pip install -r requirements.txt
4. Set up your local database using PostgreSQL ( or another option), and ensure your db.py string is correct
5. Run the flask app! It will be available at **127.0.0.1:5000**

## API Endpoints
- **Shorten URL**  
  Endpoint: /shorten  
  Method: POST  
- **Get URL**  
  Endpoint: /shorten/<shorten_name>
  Method: GET  
- **Update URL**  
  Endpoint: /shorten/<shorten_name>
  Method: PUT  
- **Delete URL**
  Endpoint: /shorten/<shorten_name>
  Method: DELETE  
- **Get URL stats**  
  Endpoint: /shorten/<shorten_name>/stats
  Method: GET   
- **Redirect to Original URL**  
  Endpoint: /shorten/<shorten_name>/go
  Method: GET  
## Testing  
You can use Postman or curl to make requests to the endpoints
