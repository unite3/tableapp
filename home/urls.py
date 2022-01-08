from django.contrib import admin
from django.urls import path, include
from home import views
admin.site.site_header = "TableApp admin"
admin.site.site_title = "TableApp admin"
admin.site.index_title = "Welcome to TableApp Admin"
urlpatterns = [

    path('',views.index,name="home"),
    path('login',views.loginuser,name="login"),
    path('logout/',views.logoutuser,name="logout"),
    path("signup/", views.Signup, name="signup"),
]
