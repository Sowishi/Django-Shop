from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("women", views.women, name="women"),
    path("men", views.men, name="men"),
    path("kids", views.kids, name="kids"),
    path("cart", views.cart, name="cart"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logoutUser, name="logout"),





]


