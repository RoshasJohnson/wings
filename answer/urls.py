from django import views
from django.urls import path
from.views import get_answers_of_eachQustions,AnswerListView

urlpatterns = [
    path("<int:id>/",get_answers_of_eachQustions),
    path("create-answer", AnswerListView.as_view(),name="create-answer"),
    path("vote", AnswerListView.as_view(),name="create-answer")

]
# Compare this snippet from users/urls.py:

