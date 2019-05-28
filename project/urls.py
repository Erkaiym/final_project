from django.contrib import admin
from django.urls import path, include
from user.views import *
from trip.views import *


urlpatterns = [
    path('', home_view, name='main-page'),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login-page'),
    path('logout/', logout_view, name='logout-page'),
    path('register/', register, name='register-page'),
    path('register/profile/', register_profile, name='register-profile-page'),
    path('profile/update/', update_profile, name='update-profile'),
    path('trip/user/<int:id>', trip_owner, name='trip-owner'),
    path('trip/list/', trip_list, name='trip-list'),
    path('trip/create/', create_trip, name='create-trip'),
    path('trip/<int:id>/', trip_detail, name='trip-detail'),
    path('trip/update/<int:id>/', update_trip, name='update-trip'),
    path('trip/confirm_delete/<int:id>/', confirm_delete_trip, name='confirm-delete-trip'),
    path('trip/delete/<int:id>/', delete_trip, name='delete-trip'),
    path('trips/search/', SearchView.as_view(), name='search'),
    path('user/delete/', user_delete, name='user-delete'),
    path('user/detail/', view_profile, name='user-detail'),
    path('user/confirm_delete/', confirm_delete_user, name='confirm-delete'),



    #path('user_update', UserUpdate.as_view(), name='user-update-view'),
    #path('user_create', UserCreate.as_view(), name='user-create-view'),
]
