"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from taskapp import views
from django.conf import settings
from django.conf.urls.static import static
from taskapp.views import TaskListView, TaskCreateView

urlpatterns = [
    # path("", views.index, name="index"),
    path("", TaskListView.as_view(), name="index"),
    path("task/", TaskCreateView.as_view(), name="create-task"),
    path("previous/", views.index, name="previous"),
    path("task/<int:task_id>/delete/", views.index, name="delete-task"),
    path("task/<int:task_id>/item/", views.index, name="create-item"),
    path("task/<int:task_id>/item/<int:check_id>/", views.index, name="check-item"),
    path(
        "task/<int:task_id>/item/<int:check_id>/delete/",
        views.index,
        name="delete-item",
    ),
    path("task/<int:task_id>/", views.index, name="view-item"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
