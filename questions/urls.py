from django.urls import path
from.views import QuestionView, QuestionDetails

urlpatterns = [
    path("", QuestionView.as_view(), name=""),
    path("<int:pk>/", QuestionDetails.as_view(), name="question"),

]
