""" core/views.py """
from itertools import chain
from urllib.parse import urlencode
import datetime

# Importing Core Django modules
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.urls import reverse
from django.views import View
from django.core.mail import send_mail
from django.conf import settings

from .forms import (
	UserDataForm, LoginForm, TeacherWFH, 
	GradeForm, AdminForm, QuestionForm,
    RoomForm
)
from .models import (
	HomeWork, CustomUser, InvitationList,
	StudentInvitation, Faculty
)


def regis_form(request, role=None):
	if request.method == 'POST':
		fm = UserDataForm(request.POST)
		if fm.is_valid():

			if fm.cleaned_data.get('status') == "teacher":
				obj = InvitationList.objects.get(name_fac = fm.cleaned_data.get('full_name'))
				obj.invite_status  = "Accepted"
				obj.save()
			else:
				obj2 = StudentInvitation.objects.get(name_stu = fm.cleaned_data.get('full_name'))
				obj2.invite_status = "Accepted"
				obj2.save()

			fm.save()
			return redirect('login-form')
	else:
		fm = UserDataForm()
	# return render(request, 'registration/regis.html', {'form': fm})
	return render(request, 'registration/regis.html', {'form': fm,'role': role})


def login_form(request):
	if request.method == 'POST':
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			email = login_form.cleaned_data.get('username')
			password = login_form.cleaned_data.get('password')
			user = authenticate(username=email, password=password)
			if user is not None:
				login(request, user)
				return redirect('dash-board')
			else:
				error = "Please enter valid useremail and password"
				return render(request, 'registration/login.html', {'form': login_form, 'key': error})
	else:
		login_form = LoginForm()
	return render(request, 'registration/login.html', {'form': login_form})


def dash_board(request):
	if request.user.status == 'teacher':
		return redirect('fac-dash')
	elif request.user.is_admin:
		return redirect('admin-dash-board')
	else:
		return redirect('stu-dash')
	return render(request, 'dashboard/dashboard.html', {})


@login_required(login_url='')
def faculty_dash(request):
	"""This function display the faculty dashboard"""
	return render(request, 'dashboard/fac_dash.html', {})


def check_wfh(request):
	""" This function will display the data of
			 student homewok submission and 
	     and teacher can give homework according to it """
	obj = HomeWork.objects.filter(class_nm = request.user.class_name)
	return render(request, 'core/check_wfh.html', {'data': obj})


def give_grade_to_student(request, id):
	""" This function will invoke when the teacher
	    will give grade to the students homework """
	if request.method == 'POST':
		fm = GradeForm(request.POST)
		if fm.is_valid():
			obj2 = HomeWork.objects.get(id = id)
			obj2.grade = fm.cleaned_data.get('grade')
			obj2.save()
			return redirect('chech-wfh')
	else:
		fm = GradeForm()
	return render(request, 'core/grade_update.html', {'form': fm})


def saving_data_to_studentwork(request, title, fm):
	obj = CustomUser.objects.filter(status = "student", class_name = request.user.class_name)

	for item in obj:
		HomeWork.objects.create(
			user_id =item.id,
			stu_name = item.full_name, 
			class_nm = request.user.class_name,
			title = title,
			ques  = fm.cleaned_data.get('ques'),
			opt1  = fm.cleaned_data.get('opt1'),
			opt2  = fm.cleaned_data.get('opt2'),
			opt3  = fm.cleaned_data.get('opt3'),
			opt4  = fm.cleaned_data.get('opt4'),
			ans   =  fm.cleaned_data.get('ans'),
			status  =  "None Done"
		 )


@login_required(login_url='')
def teacher_wfh(request):
	""" This function will call when the teacher
	    give homework to the students"""
	if request.method == 'POST':
		fm = QuestionForm(request.POST)
		if fm.is_valid():
			title = fm.cleaned_data.get('title')
			return HttpResponseRedirect(reverse('give_ques-data', args=[title])) 
	else:
		fm = QuestionForm()
	return render(request, 'core/give_homewrk.html', {'form': fm})


@login_required(login_url='')
def question_page_view(request, title):
	""" This function will display the form in which the 
	     teacher can give assignmment questions to their students """
	if request.method == 'POST':
		fm = TeacherWFH(request.POST)
		if fm.is_valid():
			saving_data_to_studentwork(request, title, fm)
			messages.success(request, "Question Submitted successfully")
			return HttpResponseRedirect(reverse('give-ques-data', args=[title]))
	else:
		fm = TeacherWFH()
	return render(request, 'core/question_page.html', {'form': fm, 'title': title})


@login_required(login_url='')
def student_question_list(request):
	""" This function will invoke when the student 
	    submit the question/homework given by the teacher"""

	obj = HomeWork.objects.exclude(status = "Done")
	if request.method == 'POST':
		# obj1 = HomeWork.objects.filter(stu_name = request.user.full_name, status = "Not Done")
		for ele in obj:
			if request.POST.get(str(ele.id)) == ele.ans:
				ele.is_correct = "Right"
			else:
				ele.is_correct = "Wrong"
			ele.status = "Done"
			ele.save()
		return redirect('stu-dash')
	return render(request, 'core/fac_ques_list.html', {'data': obj})


@login_required(login_url='')
def student_answer_data(request):
	""" This function will display the data of student's homework"""
	obj = HomeWork.objects.filter(stu_name = request.user.full_name, class_nm = request.user.class_name)
	return render(request, 'core/stu_result_list.html', {'data': obj})


def student_res_detail(request, title):
	""" This function will display the detail data of student's homework"""
	obj = HomeWork.objects.filter(title = title, stu_name = request.user.full_name, class_nm = request.user.class_name)
	return render(request, 'core/stu_detail_res.html', {'data': obj})


@login_required(login_url='')
def stu_dashboard(request):
	""" This function will display the Student Dashboard """
	return render(request, 'dashboard/stu_dash.html', {})


def logout_view(request):
	""" This function will logout the user and redirect it to the login page"""
	logout(request)
	return redirect('login-form')


def status_update(request, id):
	""" This function updates the sudent's homework status"""
	obj2 = HomeWork.objects.get(id = id)
	obj2.status = "Done"
	obj2.save()
	return redirect('stu-dash')


def send_email_to_client(request, fm):
	""" This function will send email from teacher/admin to student/faculty"""
	recp_list = fm.cleaned_data.get('email_field')
	subject = 'welcome to GFG world'
	msg1 = f'Hi Prakhar dwivedi, I am giving you link to register for this school.  '
	msg2 = "Click here to open the link "
	msg3 = "  127.0.0.1:8000/regis/teacher/"
	msg4 = "  127.0.0.1:8000/regis/student/"
	if request.user.is_superuser:
		message = msg1 + msg2 + msg3
	else:
		message = msg1 + msg2 + msg4
	email_from = settings.EMAIL_HOST_USER
	recipient_list = [recp_list, ]
	send_mail( subject, message, email_from, recipient_list )


@login_required(login_url='')
def admin_dashboard(request):
	""" This function will display the Admin Dashboard """
	return render(request, 'dashboard/admin_dash.html', {})


def admin_send_mail_form(request):
	""" This function will display the form in which admin can
	      send invitation email to faculty"""
	if request.method == 'POST':
		fm = AdminForm(request.POST)
		if fm.is_valid():
			obj = InvitationList.objects.create(
													name_fac = fm.cleaned_data.get('full_name'),
													email_fac = fm.cleaned_data.get('email_field'),
													invite_status = "Not Accepted"
													)

			send_email_to_client(request, fm)
			return redirect('email-success')
	else:
		fm = AdminForm()
	return render(request, 'core/admin_send_mail.html', {'form': fm})


@login_required(login_url='')
def fac_success(request):
	""" This function will successfully display that 
	    email is successfully send"""
	return render(request, 'core/email_fac.html', {})


@login_required(login_url='')
def fac_send_mail_form(request):
	""" This function will display the form in which 
	    faculty can send email to students"""
	if request.method == 'POST':
		fm = AdminForm(request.POST)
		if fm.is_valid():
			obj = StudentInvitation.objects.create(
													name_stu = fm.cleaned_data.get('full_name'),
													email_stu = fm.cleaned_data.get('email_field'),
													invite_status = "Not Accepted"
													)
			
			send_email_to_client(request, fm)
			return redirect('email-success')
	else:
		fm = AdminForm()
	return render(request, 'core/fac_send.html', {'form': fm})


def admin_invitation_link(request):
	"""
	This function will display the form in
	which admin can see invitation list of faculty whom 
	accepted the request and not accepted.
	"""
	data = InvitationList.objects.all()
	return render(request, 'core/invite_list.html', {'data': data})

	
def ajax_send_email_to_share(request):
	friend_email = request.GET.get('email')
	content_id = request.GET.get('formid')
	subject = "Udemy Course Link"
	message = "127.0.0.1:8000/courses/detail/%d/"%(int(content_id,))
	email_from = settings.EMAIL_HOST_USER
	recipient_list = [friend_email, ]
	send_mail(subject, message, email_from, recipient_list)
	choice = ["Send successfully"]
	return JsonResponse(choice, safe=False)
