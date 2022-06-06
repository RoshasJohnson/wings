from django.urls import path
from.views import QuestionView, QuestionDetails,create_question,topic_wise

urlpatterns = [ 
    path("", QuestionView.as_view(), name=""),
    path("create-question",create_question,name = "create-question"),
    path("<int:pk>/", QuestionDetails.as_view(), name="question"),
     path("topic-wise/<int:fk>/",topic_wise, name="topic"),

]
  