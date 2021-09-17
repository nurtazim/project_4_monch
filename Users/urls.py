from django.urls import path
from Users import views

urlpatterns = [
    path("aut/", views.OTPView.as_view()),
    path("confirm/", views.OTPConfermView.as_view())

]
