from django.urls import path
from .views import Admin_login_view,UserView,get_statistics
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [

    path("superuser",Admin_login_view ,name= ""),
    path("getuser",UserView.as_view(),name= "getuser"),
    path("editstatus/<int:pk>",UserView.as_view(),name= "getuser"),
    path("deleteuser/<int:pk>",UserView.as_view(),name= "deleteuser"),
    path("get_statistics",get_statistics,name = "get_statistics"),
] 


  

  