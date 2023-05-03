from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from faker import Faker

import random


def index(request):
    return HttpResponse({"Main Page"})


def student(request):
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    age = random.randrange(18, 30)
    student = Student.objects.create(first_name=first_name, last_name=last_name, age=age)
    s = Student.objects.last()
    return HttpResponse({s})


def students(request):
    count = request.GET.get('count')
    try:
        int_c = int(count)
        if int_c <= 100 and int_c > 0:
            for i in range(int(int_c)):
                fake = Faker()
                first_name = fake.first_name()
                last_name = fake.last_name()
                age = random.randrange(18, 30)
                student = Student.objects.create(first_name=first_name, last_name=last_name, age=age)
                get_student = Student.objects.all()
            return render(request, "generate-students.html", {"get_student": get_student})

        return render(request, "generate-students.html", {"error": "Incorrect value"})
    except:
        return render(request, "generate-students.html", {"error": "Incorrect value"})
