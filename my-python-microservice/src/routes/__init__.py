from flask import Blueprint

# Create a blueprint for the routes
routes_blueprint = Blueprint('routes', __name__)

# Import controllers here to register routes
from . import example_controller  # Replace with actual controller imports as needed

# Define your routes here
# Example:
# @routes_blueprint.route('/example', methods=['GET'])
# def example_route():
#     return example_controller.example_function()