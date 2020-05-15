from django.urls import path
from . import views


app_name = "mail"
urlpatterns = [
    path('', views.BaseView.as_view(), name='home'),
    path('mail/', views.MailView.as_view(), name='mail'),
    path("mail/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("mail/<int:pk>/like/", views.LikeView.as_view(), name="like"),
]

