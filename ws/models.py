from django.contrib.auth.models import PermissionsMixin, BaseUserManager, Group, Permission
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class EmployeeManager(BaseUserManager):
    def create_user(self, email, emp_name, password=None, **extra_fields):
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, emp_name=emp_name, **extra_fields)
        user.set_password(password)   # hashes password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, emp_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, emp_name, password, **extra_fields)


class Employee(AbstractBaseUser, PermissionsMixin):
    emp_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = EmployeeManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        Group,
        related_name='employee_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='employee_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.email
