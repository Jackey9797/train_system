"""web_db URL Configuration

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
from django.urls import path
from mysite import views
from django.views.generic import RedirectView


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='home/', permanent=True)),
    path('collection/', views.collection),
    path('home/', views.home),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('feedback/', views.feedback),
    path('discussion/', views.discussion),
    path('user_homepage/', views.user_homepage),
    path('user_homepage/<username>', views.user_homepage),
    path('logout/', views.logout),
    path('users/', views.users),
    path('add/', views.add),
    path('favorite_pro/', views.favorite),
    path('unfavorite_pro/', views.unfavorite),
    path('teams/', views.teams),
    path('post/info/', views.post_info),
    path('post/introduction/', views.post_intro),
    path('contest/', views.contest),
    path('contest/add/', views.contest_add),
    path('contest/delete/', views.contest_delete),
    path('contest/<int:nid>/edit/', views.contest_edit),
    path('application/', views.application),
    path('application/add/', views.application_add),
    path('application/delete/', views.application_delete),
    path('application/<int:nid>/edit/', views.application_edit),
    path('submission/add/', views.application_submission),
    path('submission/', views.submission_list),
    path('question/add/', views.question_add),
    path('question/delete/', views.question_delete),
    path('question/<int:nid>/edit/', views.question_edit),
    path('rating/<int:nid>/edit/', views.rating_edit),
]
