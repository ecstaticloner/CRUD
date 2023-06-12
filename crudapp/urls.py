from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('create', views.create, name='create'),
    path('delete/<int:id>/',views.delete, name='delete'),
    path('update/<int:id>/',views.update, name='update'),
    path('updateRecord/<int:id>', views.updateRecord, name ='updateRecord')
]