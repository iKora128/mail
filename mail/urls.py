from django.urls import path
from . import views


urlpatterns = [
    path('', views.BaseView.as_view(), name='home'),
    path('mail/', views.MailView.as_view(), name='mail'),
]

