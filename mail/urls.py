from django.urls import path
from . import views


app_name = "mail"
urlpatterns = [
    path('', views.BaseView.as_view(), name='home'),
    path('mail/', views.MailView.as_view(), name='mail'),
]

