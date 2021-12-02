from models.event import *

event1 = Event("Smiths wedding","01.04.2022",50,"Cheviot","wedding")
event2 = Event("Bobs bash","02.04.2022",25,"Highlands","party")
event3 = Event("Tyler gender reveal","03.04.2022",100,"pentland","party")

events = [event1,event2,event3]

def add_new_event(new_event):
    events.append(new_event)
