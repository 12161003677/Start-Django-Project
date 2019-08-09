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

def purchase_pay(request, id, id_purchase):
    purchase = Purchase.objects.get(id=id_purchase)
    purchase.active = False
    v = purchase.value
    purchase.save()
    student = Student.objects.get(id=id)
    student.bill -= v
    student.save()
    link = '/aluno/' + id

    return redirect(link)


def cancel_purchase_pay(request, id, id_purchase):
    purchase = Purchase.objects.get(id=id_purchase)
    purchase.active = True
    v = purchase.value
    purchase.save()
    student = Student.objects.get(id=id)
    student.bill += v
    student.save()
    link = '/aluno/'+id

    return redirect(link)

def new_purchase(request, id):
    data = {}
    data['title'] = 'Nova Compra'
    data['id'] = id
    data['products'] = Product.objects.all()

    return render(request, 'new_purchase.html', data)

def new_purchase_submit(request, id):
    data = {}
    data['id'] = id
    date = request.POST.get('date')
    p = request.POST.get('prod')
    p = p.split(',')
    product = p[0]
    price = request.POST.get('price')
    qtd_prod = int(request.POST.get('amount'))
    value = float(request.POST.get('value'))

    Purchase.objects.create(date=date,student_id=id,product_id=product,price=price,qtd_prod=qtd_prod,value=value,active=True)

    student = Student.objects.get(id=id)
    b = float(student.bill)
    b+=value
    student.bill = b
    student.save()

    link = '/aluno/'+id+'/'

    return redirect(link)

    return render(request, 'new_purchase.html', data)

