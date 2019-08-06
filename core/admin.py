from django.contrib import admin
from .models import Team, Student, TypeProd, Product, Purchase

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'qtd_students']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'username', 'password', 'email', 'team', 'bill', 'photo']

@admin.register(TypeProd)
class TypeProdAdmin(admin.ModelAdmin):
    list_display = ['id', 'type']

@admin.register(Product)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'type', 'photo']

@admin.register(Purchase)
class TeamAdmin(admin.ModelAdmin):
   list_display = ['id', 'product', 'qtd_prod', 'value']