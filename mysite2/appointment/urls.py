from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("appointment", views.appointment, name="appointment"),
    path("print", views.print, name="print"),
    path("view", views.viewAppointment, name="view"),
    path("delete", views.deleteAppointment, name="delete"),
    path("edit", views.editAppointment, name="edit"),
    path("show", views.showList, name="show")
]