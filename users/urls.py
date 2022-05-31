from django.urls import path
from .views import UserListCreate ,login_view
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    path('create_user/', UserListCreate.as_view()),
    path("login",login_view , name= "login")
]




