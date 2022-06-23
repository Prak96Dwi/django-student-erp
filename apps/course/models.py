""" course/models.py """
from django.db import models
from django.conf import settings


class Course(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    faculty_name = models.CharField(max_length=100)

    name = models.CharField(max_length=100)

    image = models.ImageField(upload_to='course_pic/')

    description = models.TextField(max_length=500)

    number_of_students_enrolled = models.IntegerField(default=0)
    number_of_students_rated = models.IntegerField(default=0)
    average_rate = models.FloatField(default=0)

    def __str__(self):
        """String representation of Course instance"""
        return f'{self.faculty_name}'


class CourseContent(models.Model):

    faculty_name = models.CharField(max_length=100)
    
    course_name = models.CharField(max_length=100)
    
    subject_title = models.CharField(max_length=100)
    
    pdf_content = models.FileField(
        null=True,
        upload_to = 'pdf_tutorial/'
    )

    video_content = models.FileField(
        null=True,
        upload_to='video_tutorial/'
    )

    def __str__(self):
        """String representation of CourseContent instance."""
        return f'{self.faculty_name}'


class StudentCourseEnroll(models.Model):

    user = models.ForeignKey(
    	settings.AUTH_USER_MODEL,
    	on_delete=models.CASCADE
    )
    fac_name = models.CharField(max_length=100)
    stu_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
