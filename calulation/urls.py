from django.urls import path,include
from . import views

urlpatterns = [
    path('pages/',views.Mycalc,name='pages'),
]