from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutpage,name='logout'),
    path("register/",views.register,name='register'),
    path("updated/<str:pk>/",views.updated,name='updated'),
    path('deleted/<str:pk>/',views.deleted,name="deleted")
    
]