from django import views
from django.urls import path
from.views import get_answers_of_eachQustions,create_new_answer ,vote_answer,vote_answer_status

urlpatterns = [
    path("<int:id>/",get_answers_of_eachQustions),
    path("create-answer", create_new_answer),
    path("vote_answer/<int:fk>/",vote_answer,name= "vote_answer"),
    path("answer_status/<int:fk>/",vote_answer_status,name = "vote_answer_status"),

]
     