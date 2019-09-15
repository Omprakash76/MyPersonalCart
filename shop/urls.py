from django.urls import path
from . import views
urlpatterns = [
    path("", views.index ,name = "shop"),
    path("about/", views.about ,name = "About"),
    path("contect/", views.contect ,name = "Contect"),
    path("tracker", views.tracker ,name = "tracker"),
    path("search", views.search ,name = "Search"),
    path("productview", views.productView ,name = "ProductView"),
    path("checkout", views.checkout ,name = "Checkout"),
    path("cart", views.cart ,name = "Cart"),
    path("myorder", views.myorder ,name = "MyOrder"),
    path("login", views.login ,name = "Login"),
    path("support", views.support ,name = "Support"),
]