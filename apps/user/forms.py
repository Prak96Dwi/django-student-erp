""" user/forms.py """
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import CustomUser


class UserDataForm(UserCreationForm):

	STATUS_CHOICES = [ 
		('-------','-------'),
		('teacher','teacher'),
		('student','student')
	]

	CLASS_CHOICES=[ ('1','1'), ('2','2'), ('3','3'),
		('4','4'), ('5','5'), ('6','6'), ('7','7'), ('8','8'), ('9','9'), ('10','10'),
		('11','11'), ('12','12') ] 

	full_name = forms.CharField(label = "Full Name", max_length = 50, widget = forms.TextInput(
		attrs = {
				'class': 'form-control', 'placeholder':"Full Name"
				}
		)
	)

	father_name = forms.CharField(max_length = 50, widget = forms.TextInput(
		attrs = {
				'class': 'form-control', 'placeholder':"Father Name"
				}
		)
	)

	mother_name = forms.CharField(max_length = 50, widget = forms.TextInput(
		attrs = {
				'class': 'form-control', 'placeholder':"Mother Name"
				}
		)
	)

	status = forms.CharField(label ='Status',
	 	widget = forms.Select(
	 	choices = STATUS_CHOICES,
		attrs = {
				'class': 'form-control', 'placeholder':"Status"
				}
		)
	)

	roll_number = forms.CharField(required = False, max_length = 50, widget = forms.NumberInput(
		attrs = {
				'class': 'form-control', 'placeholder':"Roll Number"
				}
		)
	)

	mobile = forms.CharField(widget = forms.NumberInput(
		attrs = {
				'class': 'form-control', 'placeholder':"Mobile Number"
				}
		)
	)

	class_name = forms.IntegerField(label = 'Class Name', widget = forms.Select(
		choices = CLASS_CHOICES,
		attrs = {
				'class': 'form-control', 'placeholder':"Class Name"
				}
		)
	)

	password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput(
		attrs = {
				'class': 'form-control', 'placeholder':"Password"
				}
		)
	)

	password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput(
		attrs = {
				'class': 'form-control', 'placeholder':" Confirm Password"
				}
		)
	)

	class Meta:
		model = CustomUser
		fields = ['full_name', 'father_name', 'mother_name', 'email', 'status', 'roll_number',
		           'mobile', 'class_name']
		widgets = {
			'email': forms.TextInput(attrs = {'class': 'form-control', 'placeholder':"Email"}),
		}


class LoginForm(forms.Form):

	username = forms.CharField(max_length=50)
	password = forms.CharField(widget=forms.PasswordInput())


class QuestionForm(forms.Form):

	title = forms.CharField(label = "Title", max_length = 100,
							widget = forms.TextInput(
							 	attrs = {
							 			'class': "form-control"
							 			}
							 		)
							 )



class TeacherWFH(forms.Form):

	ANSWER_CHOICES = [
		('Option 1', "Option 1"),
		('Option 2', "Option 2"),
		('Option 3', "Option 3"),
		('Option 4', "Option 4")
	]

	ques = forms.CharField(label = "Questions", max_length = 400, 
							widget = forms.Textarea(
								attrs = {
										'class': "form-control"
										}
								)
							)

	opt1 = forms.CharField(label = "First Option", max_length = 300,
							widget = forms.TextInput(
								attrs = {
										'class' : "form-control"
										}
									)
							)

	opt2 = forms.CharField(label = "Second Option", max_length = 300,
							widget = forms.TextInput(
								attrs = {
										'class' : 'form-control'
										}
									)
							)

	opt3 = forms.CharField(label = "Third Option", max_length = 300,
							widget = forms.TextInput(
								attrs = {
										'class' : 'form-control'
										}
									)
							)

	opt4 = forms.CharField(label = "Fourth Option", max_length = 300,
							widget = forms.TextInput(
								attrs = {
										'class' : 'form-control'
										}
									)
							)

	ans = forms.CharField(label = "Correct Answer", max_length = 300,
							widget = forms.TextInput(
								attrs = {
										'class': "form-control"
										}
								)
							)


class GradeForm(forms.Form):
	GRADE_CHOICES = [(x,x) for x in range(1,11)]
	grade = forms.ChoiceField(choices = GRADE_CHOICES)


class AdminForm(forms.Form):
	full_name = forms.CharField(max_length = 50)
	email_field = forms.EmailField()


class RoomForm(forms.Form):
	mytext = forms.CharField(max_length = 500, required = False, widget = forms.TextInput(
		attrs = {
				'class' : 'form-control',
				'size'  : "100", 
				'id'    : "chat-message-input",
				'placeholder' : "Type Your Message",
				'required' : 'False'
				}
		)
	)

	myimage = forms.FileField(required = False, widget = forms.FileInput())

# class RatingAndReivewForm(forms.Form):
# 	teacher = form.CharField(max_length = 100)
# 	course_name = form.CharField()
