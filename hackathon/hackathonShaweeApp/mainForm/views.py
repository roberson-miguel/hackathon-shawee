from django.shortcuts import render, redirect
from .models import Participant
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['teste-shawee']

participantsCollection = db['participants']

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        specialization = request.POST["specialization"]
        knowledge = request.POST["knowledge"]
        
        form = request.POST
        print(form)

        newParticipant = {
            "name" : name,
            "email" : email,
            "specialization" : specialization,
            "knowledge" : knowledge
        }
        
        participantId = participantsCollection.insert_one(newParticipant).inserted_id

        participantsList = participantsCollection.find({"specialization" : "Front-end"}).count()

        print("oi")
        print(participantsList)


        print(participantId)

        return redirect("/")


    return render(request, "index.html")