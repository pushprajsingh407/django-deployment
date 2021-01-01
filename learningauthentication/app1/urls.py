from django.urls import path
from . import views

#Template URLs
app_name = 'app1'

urlpatterns= [
    path('registration/', views.registration, name='registration'),
    path('user_login/', views.user_login, name='login')
]
