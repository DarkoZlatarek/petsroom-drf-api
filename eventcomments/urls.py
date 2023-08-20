from django.urls import path
from eventcomments import views


urlpatterns = [
    path('eventcomments/', views.EventCommentList.as_view()),
    path('eventcomments/<int:pk>/', views.EventCommentDetail.as_view()),
]
