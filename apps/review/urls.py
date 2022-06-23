""" review/urls.py """
from django.urls import path
from . import views


urlpatterns = [
  # Rate and Review url
  path(
    'rate/review/form/',
    views.rate_and_review_form,
    name='rate-review-form'
    ),

  path(
    'rate/review/view/',
    views.view_rating_and_reviews,
    name='rate-review-view'
    ),

  path(
    'view/courses/',
    views.view_faculty_course_data,
    name='view-fac-course-content'
    ),

  path(
    'courses/detail/<int:id>/',
    views.view_course_detail,
    name='view-fac-course-detail'
    ),

  path(
    'add/upvotes/',
    views.adding_upvotes_member_function,
    name='adding-upvotes-member'
  )

]
