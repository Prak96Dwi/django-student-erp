"""
    This module contains some concrete model classes such as
    * class : CustomUser
    * class : HomeWork
"""
from django.db import models
from django.contrib.auth.models import  (
    AbstractBaseUser, BaseUserManager
)
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser):
    """
    Table of Customer model inheriting AbstractUser
    """
    TEACHER = 'teacher'
    ADMIN = 'admin'
    STUDENT = 'student'

    class Meta:
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'

    # Full name of a registered user
    full_name = models.CharField(
        max_length=259,
        help_text=_("Full Name")
    )

    # Email of a registered user
    email = models.EmailField(
        max_length=50,
        unique=True,
        help_text=_("Email")
    )

    # Father's name of a registered user
    father_name = models.CharField(
        max_length=259,
        help_text=_("Father Name")
    )

    # Mother's name of a registered user
    mother_name = models.CharField(
        max_length=259,
        help_text=_("Mother Name")
    )

    # Status of registered user whether he/she is student or not
    status = models.CharField(
        max_length=50,
        null=True,
        help_text=_("Status")
    )


    roll_number = models.CharField(
        max_length=50,
        null=True,
        help_text=_("Roll Number")
    )

    mobile = models.CharField(max_length=50)
    
    class_name = models.IntegerField(null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    is_admin = models.BooleanField(default=False) # a superuser

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __Str__(self) -> str:
        """String representation of a user instance."""
        return f"{self.email}"

    def get_full_name(self) -> str:
        """Full Name of user instance."""
        return f'{self.full_name}'

    def save(self, *args, **kwargs): # pylint: disable=arguments-differ
        """
        save cleaned data of user object
        """
        # self.full_clean()
        super().save(*args, **kwargs)

    # ========================================================================================
    def has_perm(self, perm, obj=None) -> bool:
        """ has permission """
        return self.is_admin

    # ========================================================================================
    def has_module_perms(self, app_label) -> str:
        """ has module permission """
        return self.is_admin


class HomeWork(models.Model):
    """
    """

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    student_name = models.CharField(
        max_length=50
    )
    
    class_name = models.IntegerField()
    
    title = models.CharField(max_length=500)

    question = models.CharField(max_length=500)

    option_1 = models.CharField(max_length=500)

    option_2 = models.CharField(max_length=500)

    option_3 = models.CharField(max_length=500)

    option_4 = models.CharField(max_length=500)

    answer = models.CharField(max_length=500)

    status = models.CharField(max_length=40)

    grade = models.IntegerField(null=True)

    is_correct = models.CharField(
        max_length=50,
        null=True
    )
    
    def __str__(self) -> str:
        """String representation of Homework instance."""
        return f'{self.question}'


class InvitationList(models.Model):

    name_fac = models.CharField(max_length=50)
    email_fac = models.CharField(max_length=50)
    invite_status = models.CharField(max_length=50, null=True)
    invitation_date = models.DateField(auto_now_add=True)


class StudentInvitation(models.Model):

    name_stu = models.CharField(max_length = 50)
    email_stu = models.CharField(max_length = 50)
    invite_status = models.CharField(max_length = 50, null = True)
    date_of_invite = models.DateField(auto_now_add = True)


class Faculty(models.Model):

    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    fac_name = models.CharField(max_length = 100)
    fac_status = models.CharField(max_length = 200, null = True)
    fac_description = models.CharField(max_length = 500, null = True)
    no_of_courses = models.IntegerField(default = 0)
    total_no_of_students = models.IntegerField(default = 0)
    total_no_of_students_rated = models.IntegerField(default = 0)
    average_rate = models.FloatField(default = 0)
