#Basic imports
from flask import Flask
from threading import Thread
#Sets the app
app = Flask('')
#Makes the main link page
@app.route('/')
def home():
    #Just says the text
    return "Tibot Is Online"
#Runs the site
def run():
  app.run(host='0.0.0.0',port=8080)
#Keeps alive
def keep_alive():
    t = Thread(target=run)
    t.start()