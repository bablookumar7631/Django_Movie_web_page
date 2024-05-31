"""MoviesWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "MovieVerse Admin"
admin.site.site_title = "MovieVerse Admin Panel"
admin.site.index_title = "Welcome to MovieVerse Admin Panel"



urlpatterns = [
    path('admin/', admin.site.urls),
    path('postComment/<int:allmovie_id>/', views.postComment, name="postComment"),
    path('delete/<int:allmovie_id>/', views.delete_data, name='deletedata'),
    path('edit-comment', views.editComment, name='update_comment'),
    path('saveFeedbackData/', views.save_feedback, name='feedback'), 

    
    path('', views.indexPage,name='index'),
    path('signup/', views.SignupPage,name='signup'),
    path('login/', views.LoginPage,name='login'),
    path('moviesList', views.MoviesList,name='moviesList'),
    path('moviedetail/<int:id>', views.MovieDetailPage,name='moviedetail'),
    path('reviews', views.ReviewPage,name='reviews'),
    path('logout', views.LogoutPage,name='logout'),
    path('search', views.searchPage, name='search'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


