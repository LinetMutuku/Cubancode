"""
URL configuration for cubancode project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views. home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from app import views
from cubancode import settings

urlpatterns = [
                  path('', views.signin, name='signin'),
                  path('signout', views.signout, name='signout'),
                  path('about', views.about, name='about'),
                  path('home', views.home, name='home'),
                  path('contact', views.contact, name='contact'),
                  path('rooms', views.rooms, name='rooms'),
                  path('view_rooms', views.view_rooms, name='view_rooms'),
                  path('room_details', views.room_details, name='room_details'),
                  path('blog', views.blog, name='blog'),
                  path('booknow', views.booknow, name='book now'),
                   path('guest', views.all_guests, name= "all"),
                   path('guests/<int:guest_id>', views.guest_details, name="details"),
                  path('guests/delete/<int:guest_id>', views.guest_delete, name='delete'),
                  path('guests/update/<int:guest_id>', views.guest_update, name='update'),
                  path('search', views.search_rooms, name='search_rooms'),
                  path('admin/', admin.site.urls),

                  path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
                  path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
                  path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
                       name='password_reset_confirm'),
                  path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
                  path('accounts', include('django.contrib.auth.urls'))

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
