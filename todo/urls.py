
from django.urls import path
from todo import views
urlpatterns = [
    path('',views.todo,name="home"),
    path('delete/<int:pk>',views.ondelete,name = 'delete')
]
