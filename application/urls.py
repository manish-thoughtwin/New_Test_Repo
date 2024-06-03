from django.urls import path
from . import views
from django.contrib import admin
		
urlpatterns = [	
    path('signup/',views.signup, name='signup' ),
    path('home/', views.home, name='home' ),
	path('login/', views.login_view, name='login'),
	path('otp_view/',views.otp_view,name='otp_view'),
	path('blog_list/',views.blog_list,name='blog_list'),
	path('update/<id>/',views.blog_update,name='blog_update'),
	path('delete/<id>/',views.blog_delete,name='blog_delete'),
 	path('blog_create/',views.blog_create,name='blog_create')
 
 
 
]