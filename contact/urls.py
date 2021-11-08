from django.urls import path
from contact import views



urlpatterns = [

    path('', views.index, name = 'index'),
    path('addContact',views.addContact, name='addContact'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('edit/<str:pk>', views.edit, name='edit'),
    path('delete/<str:pk>', views.delete, name='delete' ),

]