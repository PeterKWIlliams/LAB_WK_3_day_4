from app import app
from flask import render_template,request
from models.event_lists import *


@app.route("/events")
def index():
    return render_template("index.html",title ="Home",events = events)

@app.route("/events",methods = ['POST'])
def add_task():
    event_name = request.form["name"]
    event_date = request.form["date"]
    event_num_guests = request["num_guests"]
    event_location = request.form["room_location"]
    event_description = request.form["description"]
    new_event = Event(event_name,event_date,event_num_guests,event_location,event_description)
    add_new_event(new_event)
    return render_template("index.html",tile ="Home",events = events )