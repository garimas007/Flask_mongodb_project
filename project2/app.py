"""
Create a form on the frontend that, when submitted, inserts data into MongoDB Atlas.
Upon successful submission, the user should be redirected to another page displaying the message
"Data submitted successfully".
If there's an error during submission, display the error on the same page without redirection.
"""

from flask import Flask, render_template, request, redirect, url_for
import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Connect to MongoDB database from .env
mongo_uri = os.getenv("MONGO_URI")
client = pymongo.MongoClient(mongo_uri)  # Create a MongoDB client
db = client.project2
collection = db['flask_project']

@app.route('/', methods=['GET', 'POST'])

def home():
    if request.method == 'POST':
        try:
            form_data = dict(request.form)
            collection.insert_one(form_data)
            return redirect(url_for('success'))  # Redirect to success page
        except Exception as e:
            error_message = str(e)
            return render_template('index.html', error=error_message)
        
    return render_template('index.html')

@app.route('/success')
def success():
    return "Data submitted successfully"

if __name__ == '__main__':
    app.run(debug=True)