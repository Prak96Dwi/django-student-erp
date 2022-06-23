""" apps/user/managers.py 

	This modules contains some model manager classes

	* class : CustomerManager

"""
from django.contrib.auth.models import  (
    BaseUserManager
)
from django.conf import settings
 

class CustomUserManager(BaseUserManager):
    """
    Customer Registration manager
    """
    def create_user(self, email, password=None, **kwargs):
        """
        Creates and saves a User with the given email,and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))

        if kwargs.get('full_name'):
            user.full_name = kwargs.get('full_name')
        if kwargs.get('email'):
            user.email = kwargs.get('email')
        if kwargs.get('father_name'):
            user.father_name = kwargs.get('father_name')
        if kwargs.get('mother_name'):
            user.mother_name = kwargs.get('mother_name')
        if kwargs.get('status'):
            user.status = kwargs.get('status')
        if kwargs.get('roll_number'):
            user.roll_number = kwargs.get('roll_number')
        if kwargs.get('mobile'):
            user.mobile = kwargs.get('mobile')
        if kwargs.get('class_name'):
            user.class_name = kwargs.get('class_name')
        if kwargs.get('is_active'):
            user.is_active = kwargs.get('is_active')
        if kwargs.get('is_staff'):
            user.is_staff = kwargs.get('is_staff')
        if kwargs.get('is_admin'):
            user.is_admin = kwargs.get('is_admin')

        user.is_admin = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email, password=password)
        user.status = 'admin'
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user
