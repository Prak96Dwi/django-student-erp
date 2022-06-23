""" apps/course/forms.py """
from django import forms


class CourseRegistrationForm(forms.Form):

	sub_name = forms.CharField(label = "Subject Name", max_length = 100,
								widget = forms.TextInput(
								 	attrs = {
								 	'class' : 'form-control'
								 	}
								)
							)

	course_pic = forms.ImageField(label = "Upload Course Image",
								widget = forms.FileInput(
									attrs = {
										'class' : 'form-control'
									}
								)
							)


class CourseEnrollForm(forms.Form):

	sub_name = forms.CharField(
								label="Subject Name",
								max_length=100, 
								widget = forms.TextInput(
									attrs = {
											'class': 'form-control'
											}
										)
								)

