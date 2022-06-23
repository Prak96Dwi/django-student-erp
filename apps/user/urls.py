""" user/urls.py """
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views


urlpatterns  = [
  # Login  URL
  path(
    '',
    views.login_form,
    name='login-form'
  ),

  # Registration URL
  path(
    'regis/<str:role>/',
    views.regis_form,
    name='reg-form'
  ),

  path(
    'regis/',
    views.regis_form,
    name='reg-form'
  ),

  path(
    'log-out/',
    views.logout_view,
    name='log-out'
  ),

  # Dashboard URL
  path(
    'dash/',
    views.dash_board, name = 'dash-board'
    ),

  path(
    'stu/dash/',
    views.stu_dashboard, name = 'stu-dash'
  ),

  path(
    'fac/dash/',
    views.faculty_dash, name = 'fac-dash'
  ),

  path(
    'admin-dash/',
    views.admin_dashboard, name = 'admin-dash-board'
  ),

  # Email URL
  path(
    'stu-suc/',
    views.fac_send_mail_form, name = 'fac-send-email'
  ),

  path(
    'fac-suc/',
    views.fac_success,
    name='email-success'
  ),

  path(
    'adm-sendmail/',
    views.admin_send_mail_form,
    name='admin-send-mail'
  ),

  path(
    'tch/',
    views.teacher_wfh,
    name='teach-wfh'
  ),

  path(
    'sta-btn/<int:id>/',
    views.status_update ,
    name='status-done'
  ),

  path(
    'ch-wfh/',
    views.check_wfh,
    name='chech-wfh'
  ),

  path(
    'grde-udt/<int:id>/',
    views.give_grade_to_student,
    name='grade-update'
  ),

  path(
    'ad-list/',
    views.admin_invitation_link,
    name='admin-invite-list'
  ),

  path(
    'stu/ans/data/',
    views.student_answer_data,
    name="stu-ans-data"
  ),

  path(
    'stu/ques/list/',
    views.student_question_list,
    name="stu-ques-data"
  ),

  path(
    'ques/<str:title>/',
    views.question_page_view,
    name='give-ques-data'
  ),

  path(
    'stu/res/<str:title>/',
    views.student_res_detail,
    name='stu-obj-detail'
  ),

  # Ajax URL
  path(
    'send/url/',
    views.ajax_send_email_to_share,
    name='ajax-send-url-link'
  )
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
