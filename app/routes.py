from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
	links = getAvailibleCitiesLinks()
    return render_template('home.html', cities = links)

@app.route('/<city>')
def city(city):
	html = loadCitiesDict()[city]
    return render_template('currentCityLinks.html')
    

def getAvailibleCitiesLinks():
	pass

def loadCitiesDict():
	pass