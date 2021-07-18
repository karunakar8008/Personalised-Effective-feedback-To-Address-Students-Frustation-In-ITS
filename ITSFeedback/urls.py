from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
	       path("index.html", views.index, name="ITSFeedback"),
	       path("Admin.html", views.Admin, name="Admin"),
	       path("AdminLogin", views.AdminLogin, name="AdminLogin"),
	       path("BuildModel", views.BuildModel, name="BuildModel"),
	       path("DetectState.html", views.DetectState, name="DetectState"),
	       path("AffectState", views.AffectState, name="AffectState"),
]