from django.contrib import admin
from django.urls import path, include

from user.views import home_view, LoginView, view_profile, register, register_profile, logout_view


urlpatterns = [
    path('', home_view, name='main-page'),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login-page'),
    path('logout/', logout_view, name='logout-page'),
    path('register/', register, name='register-page'),
    path('register_profile/', register_profile, name='register-profile-page'),
    path('user_detail/', view_profile, name='user-detail'),
    #path('user_update/', user_update, name='user-update'),


    #path('user_update', UserUpdate.as_view(), name='user-update-view'),
    #path('user_create', UserCreate.as_view(), name='user-create-view'),
]
