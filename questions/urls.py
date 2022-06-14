from django.urls import path
from.views import QuestionView, QuestionDetails, create_question, topic_wise, my_question, got_answer

urlpatterns = [
    path("", QuestionView.as_view(), name=""),
    path("create-question", create_question, name="create-question"),
    path("<int:pk>/", QuestionDetails.as_view(), name="question"),
    path("topic-wise/<int:fk>/", topic_wise, name="topic"),
    path("my-question", my_question, name="my-question"),
    path("got_answer", got_answer, name="got_answer")

]
