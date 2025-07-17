from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    model = Employee
    list_display = ("email", "emp_name", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    search_fields = ("email", "emp_name")
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "emp_name", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active",
         "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {
         "fields": ("last_login", "created_at", "updated_at")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "emp_name", "password1", "password2", "is_staff", "is_active")}
         ),
    )
