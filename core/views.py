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
    bill = float(student.bill)
    bill+=value
    student.bill = bill
    student.save()

    link = '/aluno/'+id+'/'

    return redirect(link)

def detail_purchase(request, id, id_purchase):
    data = {}
    purchase = Purchase.objects.get(id=id_purchase)
    data['id'] = id
    data['title'] = 'Compra '+str(purchase.id)
    data['purchase'] = purchase

    return render(request, 'new_purchase.html', data)

def detail_purchase_submit(request, id, id_purchase):
    data = {}
    data['id'] = id
    date = request.POST.get('date')
    p = request.POST.get('prod')
    p = p.split(',')
    product = p[0]
    price = request.POST.get('price')
    qtd_prod = int(request.POST.get('amount'))
    value = float(request.POST.get('value'))
    old_value = float(request.POST.get('old_value'))
    if id_purchase:
        print('oi'+id_purchase)
        purchase = Purchase.objects.get(id=id_purchase)
        #purchase.date = date
        purchase.product_id = product
        purchase.price = price
        purchase.qtd_prod = qtd_prod
        purchase.value = value
        purchase.save()

    student = Student.objects.get(id=id)
    bill = float(student.bill)
    bill+=(value-old_value)
    student.bill = bill
    student.save()

    link = '/aluno/'+id+'/'

    return redirect(link)

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
    value = purchase.value
    purchase.save()
    student = Student.objects.get(id=id)
    student.bill += value
    student.save()
    link = '/aluno/'+id

    return redirect(link)

def delete_purchase(request, id, id_purchase):
    purchase = Purchase.objects.get(id=id_purchase)
    if purchase.active:
        value = purchase.value
        student = Student.objects.get(id=id)
        student.bill -= value
        student.save()
    purchase.delete()


    link = '/aluno/' + id

    return redirect(link)

def categories(request):
    data = {}
    data['title'] = 'Categorias de Produtos'
    data['type_prod'] = TypeProd.objects.all()

    return render(request, 'product_types.html', data)

def category(request, id_cat):
    data = {}
    category = TypeProd.objects.get(id=id_cat)
    data['title'] = category.type
    data['id_cat'] = category.id
    data['products'] = Product.objects.filter(type_id=id_cat)

    return render(request, 'products_list.html', data)

def new_product(request, id_cat):
    data = {}
    data['title'] = 'Novo Produto'
    data['id_cat'] = id_cat
    data['category'] = TypeProd.objects.get(id=id_cat)

    return render(request, 'new_product.html', data)

def new_product_submit(request, id_cat):
    name = request.POST.get('name_prod')
    print(name)
    price = request.POST.get('price')
    category = request.POST.get('category')
    photo = request.FILES.get('photo')

    Product.objects.create(name=name,price=price,type_id=category,photo=photo)
    link = '/categoria/'+id_cat+'/produtos/'
    return redirect(link)

def detail_product(request, id_cat, id_prod):
    data = {}
    data['id_cat'] = id_cat
    data['category'] = TypeProd.objects.get(id=id_cat)
    product = Product.objects.get(id=id_prod)
    data['title'] = product.name
    data['product'] = product

    return render(request, 'new_product.html', data)

def detail_product_submit(request, id_cat, id_prod):
    name = request.POST.get('name_prod')
    print(name)
    price = request.POST.get('price')
    category = request.POST.get('category')
    photo = request.FILES.get('photo')

    product = Product.objects.get(id=id_prod)
    product.name = name
    product.price = price
    product.type_id = category
    if photo:
        product.photo = photo

    product.save()

    link = '/categoria/'+id_cat+'/produtos/'
    return redirect(link)


def delete_product(request, id_cat, id_prod):
    product = Product.objects.get(id=id_prod)
    product.delete()

    link = '/categoria/'+id_cat+'/produtos/'
    return redirect(link)