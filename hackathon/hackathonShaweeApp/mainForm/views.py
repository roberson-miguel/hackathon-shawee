from django.shortcuts import render, redirect
from .models import Participant

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        age = request.POST["age"]
        specialization = request.POST["specialization"]
        
        form = request.POST
        print(form)

        newParticipant = Participant(name=name, email=email, age=age, specialization=specialization)
        newParticipant.save()
        
        return redirect("/")


    return render(request, "index.html")