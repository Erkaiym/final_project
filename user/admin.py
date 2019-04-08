from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import User, Profile, UserManager


# devi@gmail.com  -  devi12345


#User = get_user_model()

class ProfileInline(admin.TabularInline):
    model = Profile
    radio_fields = {"sex": admin.HORIZONTAL}
    fields = ('name', 'surname', 'sex', 'birthdate', 'tel_number')
1

class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]
    fields = ('email', 'password', ('active', 'staff', 'admin'))
    search_fields = ['email']
    class Meta:
        model = User

admin.site.register(User, UserAdmin)
# admin.site.register(Profile)
# admin.site.register(UserManager)
