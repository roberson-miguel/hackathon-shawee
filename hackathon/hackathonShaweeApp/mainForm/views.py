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
        age = request.POST["age"]
        specialization = request.POST["specialization"]
        
        form = request.POST
        print(form)

        newParticipant = {
            "name" : name,
            "email" : email,
            "age" : age,
            "specialization" : specialization
        }
        
        participantId = participantsCollection.insert_one(newParticipant).inserted_id

        print(participantId)

        return redirect("/")


    return render(request, "index.html")