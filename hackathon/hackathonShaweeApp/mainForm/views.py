from django.shortcuts import render, redirect
from .models import Participant
from pymongo import MongoClient
import numpy as np
import math
import random

client = MongoClient('localhost', 27017)

db = client['teste-shawee']

participantsCollection = db['participants']

groupCollection = db['group']

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST["name"]
        gender = request.POST["gender"]
        email = request.POST["email"]
        specialization = request.POST["specialization"]
        knowledge = request.POST["knowledge"]
        
        form = request.POST
        print(form)

        newParticipant = {
            "name" : name,
            "email" : email,
            "gender" : gender,
            "specialization" : specialization,
            "knowledge" : knowledge
        }

        frontend_knowledge_avg = 0
        
        participantId = participantsCollection.insert_one(newParticipant).inserted_id

        frontend = participantsCollection.find({"specialization" : "frontend"})
        backend = participantsCollection.find({"specialization" : "backend"})
        business = participantsCollection.find({"specialization" : "business"})
        ux = participantsCollection.find({"specialization" : "ux"})

        # for f in frontend:
        #     print("bateu aqui")
        #     print(f['name'])  ISSO FUNCIONA

        # ISSO NAO
        def get_participant(lista) :
            final_list =  []
            for l in lista:
                final_list.append({
                "name": l['name'],
                "email": l['email'],
                "gender": l['gender'],
                "specialization": l['specialization'],
                "knowledge": l['knowledge']
            })
            return final_list

        frontend_list = get_participant(frontend)
        backend_list = get_participant(backend)
        business_list = get_participant(business)
        ux_list = get_participant(ux)                                       

        # for f in frontend:
        #     print("bateu aqui")
        #     print(f)
        
        # participants_knowledge_mean = (frontend_knowledge_avg + backend_knowledge_avg + business_knowledge_avg + ux_knowledge_avg) / 4
        group = []

        def get_group(group):
            if newParticipant['specialization'] == "frontend":
                group = [newParticipant, backend_list[random.randint(0, len(backend_list) - 1)], business_list[random.randint(0, len(business_list) - 1)], ux_list[random.randint(0, len(ux_list) - 1)]]
            elif newParticipant['specialization'] == "backend":
                group = [frontend_list[random.randint(0, len(frontend_list) - 1)], newParticipant, business_list[random.randint(0, len(business_list) - 1)], ux_list[random.randint(0, len(ux_list) - 1)]]
            elif newParticipant['specialization'] == "business":
                group = [frontend_list[random.randint(0, len(frontend_list) - 1)], backend_list[random.randint(0, len(backend_list) - 1)], newParticipant, ux_list[random.randint(0, len(ux_list) - 1)]] 
            else:
                group = [frontend_list[random.randint(0, len(frontend_list) - 1)], backend_list[random.randint(0, len(backend_list) - 1)], business_list[random.randint(0, len(business_list) - 1)], newParticipant]
            return group

        # average = 2
        # group_average = 0

        def avg(li):
            meanVar = 0
            for l in li:
                meanVar = meanVar + int(l['knowledge'])
            return meanVar / len(li) 

        frontend_knowledge_avg = avg(frontend_list)
        backend_knowledge_avg = avg(backend_list)
        business_knowledge_avg = avg(business_list)
        ux_knowledge_avg = avg(ux_list)

        average = (frontend_knowledge_avg + backend_knowledge_avg + business_knowledge_avg + ux_knowledge_avg) / 4


        def balance_group(average) :
            new_group = []
            gp_average = 0
            while (gp_average - average) < 0 or (gp_average - average) > 0.25: 
                new_group = get_group(new_group)
                gp_average = avg(new_group)
            print(gp_average)
            return new_group
        
        final_group = balance_group(average)

        groupCollection.insert({"group" : final_group})

        return redirect("/")


    return render(request, "index.html")