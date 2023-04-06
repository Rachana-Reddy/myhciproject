from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("contact", views.contact, name="contact"),
    path("logout", views.logout, name="logout"),
    path("eventpage/<str:id>", views.eventpage, name="eventpage"),
    path("eventcategories", views.eventcategories, name="eventcategories"),
    path("careerevents", views.careerevents,name="careerevents"),
    path("sportsevents", views.sportsevents,name="sportsevents"),
    path("tripsevents", views.tripsevents,name="tripsevents"),
    path("giftcards", views.giftcards,name="giftcards"),
    path("billing", views.billing,name="billing"),
    path("about", views.about, name="about"),
    path("aboutorg",views.aboutorg,name="aboutorg"),
    path("moreinfo",views.moreinfo,name="moreinfo"),
    path("payments",views.payments,name="payments"),

]