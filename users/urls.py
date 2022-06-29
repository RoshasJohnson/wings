from django.urls import path
from .views import UserListCreate ,login_view,create_profile,get_my_profile,get_connections

urlpatterns = [
    path('create_user/', UserListCreate.as_view()),
    path("login",login_view , name= "login"),
    path("create-profile",create_profile,name = "create-profile"),
    path("myprofile",get_my_profile,name = "myprofile"),
    path("connections",get_connections,name = "connection"),
  
    

]


  

