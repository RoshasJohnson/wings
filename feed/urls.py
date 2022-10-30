
from django import views
from django.urls import path
from.views import FeedListView, ReportView,get_feeds_by_user,get_comment,CommentListView
urlpatterns  = [
    path("",FeedListView.as_view(),name=""),
    path("get_feeds",get_feeds_by_user,name="get_feeds"),
    path("comment/<int:fk>",get_comment,name="comment"),
    path('comment',CommentListView.as_view(),name="comment"),
    path("like",FeedListView.as_view(),name="like"),  
    path("report",ReportView.as_view(),name=""),


]
 