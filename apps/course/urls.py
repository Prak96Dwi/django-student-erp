""" course/urls.py """
from django.urls import path
from . import views

urlpatterns = [
	# Course Content url
	# path('course/content/', views.course_content_form, name = 'course-content-form'

	path(
		'fac/course/reg/',
		 views.faculty_course_registration,
		 name='fac-course-reg'
	),

	path(
		'fac/course/content/',
		 views.upload_course_content,
		 name='fac-course-content'
	),

	path(
		'fac/view/content/',
		 views.fac_view_course_content,
		 name='fac-view-course-content'
	),

	path(
		'stu/course/enroll/',
		 views.student_course_enroll_form,
		 name='stu-fac-eroll-form'
	),

	path(
		'stu/view/content/',
		 views.stu_view_course_content,
		 name='stu-course-enroll-content'
	)
]
