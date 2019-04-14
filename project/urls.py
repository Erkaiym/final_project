from django.contrib import admin
from django.urls import path


from user.views import home_view, LoginView, view_profile, register, logout_view

urlpatterns = [
    path('', home_view, name='main-page'),
    path('admin/', admin.site.urls),
    #path('admin_create/', AdminCreate.as_view(), name='admin-create-page'),
    path('login/', LoginView.as_view(), name='login-page'),
    path('logout/', logout_view, name='logout-page'),
    path('register/', register, name='register-page'),
    path('user_detail/', view_profile, name='user-detail-view'),
    #path('user_update', UserUpdate.as_view(), name='user-update-view'),
    #path('user_create', UserCreate.as_view(), name='user-create-view'),
]
