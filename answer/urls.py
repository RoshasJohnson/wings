from django import views
from django.urls import path
from.views import get_answers_of_eachQustions

urlpatterns = [
    path("<int:id>/",get_answers_of_eachQustions,)
]
   