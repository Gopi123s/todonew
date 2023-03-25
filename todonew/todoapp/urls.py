from django.urls import path
from .import views
from .views import *

# create logout fun in url 
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('login/',Custumlogin.as_view(),name='login'),
    path('register/',Register.as_view(),name='register'),
    path('',Alltask.as_view(),name='home'),
    path('logout/',LogoutView.as_view(next_page='home'),name='logout'),
    path('task-detail/<int:pk>',TaskDetail.as_view(),name='TaskDetail'),
    path('edit-task/<int:pk>',EditTask.as_view(),name='EditTask'),
    path('add-task/',Addtask.as_view(),name='Addtask'),
    path('delete-task/<int:pk>',Deletetask.as_view(),name='Deletetask'),
    path('updatemark/<int:pk>',updatemark,name='updatemark'),
]