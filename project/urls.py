from django.contrib import admin
from django.urls import path


from user.views import home_view, UserDetail, LoginView, RegisterView

urlpatterns = [
    path('', home_view, name='main-page'),
    path('admin/', admin.site.urls),
    #path('admin_create/', AdminCreate.as_view(), name='admin-create-page'),
    path('login/', LoginView.as_view(), name='login-page'),
    path('register/', RegisterView.as_view(), name='register-page'),
    path('user_detail', UserDetail.as_view(), name='user-detail-view'),
    #path('user_create', UserCreate.as_view(), name='user-create-view'),
]
