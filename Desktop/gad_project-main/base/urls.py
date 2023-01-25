from django.urls import path
from . import views
urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutuser, name="logout"),
    path("register/", views.registration, name="register"),
    path("", views.home ,name='home'),
    path("viewcust/",views.view_cus,name='view-cust'),
    path("add-cust/",views.add_custom,name='add-cust'),
]