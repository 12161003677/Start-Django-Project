from django.shortcuts import render, redirect
from .models import Team, Student, TypeProd, Product, Purchase

def index(request):
    data = {}
    data['title'] = 'Index'

    return render(request, 'index.html', data)

def teams(request):
    data = {}
    data['title'] = 'Turmas'
    data['teams'] = Team.objects.all()

    return render(request, 'teams_list.html', data)

def team_students(request, id):
    data = {}
    team = Team.objects.get(id=id)
    data['title'] = team.name
    data['students'] = Student.objects.filter(team_id=team.id)

    return render(request, 'team_students.html', data)

def student(request, id):
    data = {}
    student = Student.objects.get(id=id)
    data['student'] = student
    data['title'] = student.name

    purchases = Purchase.objects.filter(student_id=student.id)
    data['purchases'] = purchases

    #bill = 0
    #for i in purchases:
    #    bill += i.value
    #data['bill'] = bill

    return render(request, 'student.html', data)

