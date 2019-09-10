from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_superuser(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser, models.Model):
    is_authenticated = True
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone']
    username = models.CharField(max_length=50, verbose_name="用户名", unique=True)
    password = models.CharField(max_length=128, verbose_name="密码")
    phone = models.CharField(max_length=15, verbose_name="手机号", unique=True, null=True)
    nickname = models.CharField(max_length=50, verbose_name="昵称")

    objects = UserManager()

