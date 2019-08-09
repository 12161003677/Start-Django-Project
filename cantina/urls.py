"""cantina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import settings
from core.views import index, teams, team_students, student, purchase_pay, cancel_purchase_pay, new_purchase, new_purchase_submit

#adcione: para imagens junto com o debaixo -> ' urlpatterns += staticfiles_urlpatterns() / urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)'
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
#adcione


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('turmas/', teams, name="teams"),
    path('turma/<id>/alunos/', team_students, name="team_students"),
    path('aluno/<id>/', student, name="student"),
    path('aluno/<id>/nova-compra/', new_purchase, name="new_purchase"),
    path('aluno/<id>/nova-compra/submit', new_purchase_submit),
    path('aluno/<id>/pagar/<id_purchase>', purchase_pay, name="purchase_pay"),
    path('aluno/<id>/cancelar-pagar/<id_purchase>', cancel_purchase_pay, name="cancel_purchase_pay"),
]

#adcione: para imagens
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#adcione