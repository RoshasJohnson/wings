from django.urls import path
from.views import report_item,ReportVIew

urlpatterns = [
    path("answer",report_item,name="report_answer"),
    path("items",ReportVIew.as_view(),name="items")
] 


