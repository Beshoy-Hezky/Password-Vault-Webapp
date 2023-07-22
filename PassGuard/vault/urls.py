from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("aboutus/", views.about_us, name="about_us"),
    path("addpassword/", views.add_password, name="add_password"),
    path("deletepassword/", views.delete_password, name="delete_password"),
    path("reveal/<int:id>", views.reveal, name="reveal")
]
