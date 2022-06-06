from django import views
from django.urls import path
from.views import get_answers_of_eachQustions,create_new_answer

urlpatterns = [
    path("<int:id>/",get_answers_of_eachQustions),
    path("create-answer", create_new_answer)
]
    