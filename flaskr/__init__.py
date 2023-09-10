#Import your dependecies
from flask import Flask, jsonify

#Define the create_app function
def create_app(test_config=None):    
# Create and configure the app
# Include the first parameter: Here, __name__ is the name of the current python module.
    app = Flask(__name__)
    
    return app 
