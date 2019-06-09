from django.contrib import admin
from django.urls import path, include

from .views import *
from proposal.views import *
from user.views import *
from trip.views import *
from comment.views import *


urlpatterns = [
    path('', home_view, name='main-page'),
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('comment/list/', comment_list, name='comment-list'),
    path('comment/<int:id>/', comment_detail, name='comment-detail'),
    path('comment/<int:id>/update', update_comment, name='update-comment'),
    path('comment/create/', create_comment, name='create-comment'),
    path('comment/<int:id>/confirm_delete/', confirm_delete_comment, name='confirm-delete-comment'),
    path('login/', LoginView.as_view(), name='login-page'),
    path('logout/', logout_view, name='logout-page'),
    path('register/', register, name='register-page'),
    path('register/profile/', register_profile, name='register-profile-page'),
    path('profile/update/', update_profile, name='update-profile'),
    #path('trip/user/<int:id>', trip_owner, name='trip-owner'),
    path('trip/list/', trip_list, name='trip-list'),
    path('trip/create/', create_trip, name='create-trip'),
    path('trip/update/<int:id>/', update_trip, name='update-trip'),
    path('trip/confirm_delete/<int:id>/', confirm_delete_trip, name='confirm-delete-trip'),
    path('trip/delete/<int:id>/', delete_trip, name='delete-trip'),
    path('trips/search/', SearchView.as_view(), name='search'),
    path('user/delete/', user_delete, name='user-delete'),
    path('user/detail/', view_profile, name='user-detail'),
    path('user/confirm_delete/', confirm_delete_user, name='confirm-delete'),

]
