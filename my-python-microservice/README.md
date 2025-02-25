# My Python Microservice

This is a simple microservice built using Flask. The project is structured to separate concerns and facilitate development and testing.

## Project Structure

```
my-python-microservice
├── src
│   ├── __init__.py          # Marks the src directory as a Python package
│   ├── app.py               # Entry point for the application
│   ├── controllers          # Contains controller modules
│   │   └── __init__.py
│   ├── models               # Contains model modules
│   │   └── __init__.py
│   ├── routes               # Contains route definitions
│   │   └── __init__.py
│   └── services             # Contains service modules
│       └── __init__.py
├── tests                    # Contains test modules
│   ├── __init__.py
│   └── test_app.py          # Unit tests for app.py
├── requirements.txt         # Lists the required Python dependencies
└── README.md                # Project documentation and instructions
```

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To run the application, execute:

```
gunicorn src.app:app
```

## Testing

To run the tests, use:

```
pytest
```

## License

This project is licensed under the MIT License.