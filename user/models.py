from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db.models import ForeignKey


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('Пользователи должны иметь адрес электронной почты')
        #if not password:
            #raise ValueError('Пользователи должны иметь пароль')
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.admin = is_admin
        user_obj.staff = is_staff
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_admin=False,
            is_staff=True,
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_admin=True,
            is_staff=True,
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin

    objects = UserManager()


class Profile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birthdate = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    tel_number = models.CharField(max_length=15)
    parent = ForeignKey('self', related_name='children', blank=True, null=True, on_delete=models.CASCADE)


    MAN = 'M'
    WOMAN = 'W'
    SEX_CHOICES = (
        (MAN, 'Мужчина'),
        (WOMAN, 'Женщина'),
    )

    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES, default=None
    )

    def __str__(self):
        return self.name + ' ' + self.surname
