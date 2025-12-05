#minimal application to understand flask app
from flask import Flask, render_template, request
import pymongo
from dotenv import load_dotenv
import os

load_dotenv()  #load environment variables from .env file

#connect to MongoDB database
mongo_uri = os.getenv("MONGO_URI")  #get MongoDB URI from environment variable

client = pymongo.MongoClient(mongo_uri)  #create a MongoDB client
db = client.test
collection = db['flask_tutorial']

app = Flask(__name__)  #create a Flask application instance

@app.route('/') #define a route for the home page
def home(): #handle requests to the home page

    greatings = "This data is sent from bg to fe. Now via form send data from fe to bg" #a simple greeting message
    return render_template('index.html', greatings=greatings) #render an HTML template with the greeting message

@app.route('/signup', methods=['POST']) #define a route to handle form submissions
def signup(): #handle form submissions
    #username = request.form.get('username') #get the username from the form data
    #return f"Signup successful! Welcome, {username}!" #return a success message with the username
    form_data = dict(request.form) #convert form data to a dictionary
    collection.insert_one(form_data) #insert form data into MongoDB collection
    return "Signup successful! Your data has been saved to the database." #return a success message

if __name__ == '__main__': #run the application
    app.run(debug=True) #enable debug mode for development
