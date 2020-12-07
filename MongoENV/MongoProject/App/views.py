from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Student
# Create your views here.

# user   Mongo
# Password    MongoDB

def home(request):
    return render(request,"home.html")

@csrf_exempt
def submit(request):
    if request.method == "POST":
        Name = request.POST['Name']
        Age = request.POST['Age']
        Phone = request.POST['Phone']
        Student(Name = Name, Age = Age, Phone = Phone).save()
        msg = "Record Stored into Database"
        return render(request,"home.html",{'msg':msg})
    else:
        return HttpResponse("404 - Not Found")