from .import views
from django.urls import path

urlpatterns = [
     path('gm/', views.send_emails, name='send_emails'),
    ]