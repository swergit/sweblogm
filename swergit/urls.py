from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.main, name="main"),
	path('home/', views.home, name="home"),
	path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
	path('blog/', views.post_list, name="blog"),
	path('blogpost/<int:pk>', views.actual_post, name="actual_post"),

]