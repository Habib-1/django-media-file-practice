from django.urls import path
from .import views
urlpatterns = [
   path('',views.home, name='home'),
   path('add_people/',views.add_people,name='add_people'),
   path('delete/<int:pk>/',views.delete,name='delete'),
]