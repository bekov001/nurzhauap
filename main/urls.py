"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("create", views.CreateQuestion.as_view(), name="create"),
    path('post/<int:pk>', views.Detail.as_view(), name='post'),
    path('post/<int:pk>/update', views.PostUpdate.as_view(), name='update'),
    path('post/<int:pk>/delete', views.DeletePost.as_view(), name='delete'),
    path('register', views.RegisterUser.as_view(), name='register'),
    path("404", views.test, name="test")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
