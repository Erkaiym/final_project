from django.contrib import admin
from django.urls import path, include

from user.views import home_view, LoginView, view_profile, register, register_profile, logout_view, update_profile, \
    user_delete
from trip.views import trip_list, trip_detail, create_trip#, search


urlpatterns = [
    path('', home_view, name='main-page'),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login-page'),
    path('logout/', logout_view, name='logout-page'),
    path('register/', register, name='register-page'),
    path('register_profile/', register_profile, name='register-profile-page'),
    path('user_detail/', view_profile, name='user-detail'),
    path('update_profile/', update_profile, name='update-profile'),
    path('user_delete/', user_delete, name='user-delete'),
    path('trips/', trip_list, name='trip-list'),
    #path('trips/search/', search, name='search'),
    path('trip/<int:id>/', trip_detail, name='trip-detail'),
    path('trip/create/', create_trip, name='create-trip'),



    #path('user_update', UserUpdate.as_view(), name='user-update-view'),
    #path('user_create', UserCreate.as_view(), name='user-create-view'),
]
