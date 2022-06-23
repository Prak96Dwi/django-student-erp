""" apps/course/views.py """
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='')
def faculty_course_registration(request):
	""" 
	This function will display the form in which
	faculty can register her course for teaching and
	uploading pdf and videos.
	"""
	if request.method == 'POST':
		fm = CourseistrationForm(request.POST, request.FILES)
		if fm.is_valid():
			obj = CustomUser.objects.get(id = request.user.id)
			obj1 = Course.objects.create(
													  user = obj,
													  fac_name = request.user.full_name,
													  course_name = fm.cleaned_data.get('sub_name'),
													  course_pic = request.FILES['course_pic']
													  )
			messages.success(request, "Course Submitted successfully")

			# Create Faculty data object
			# obj2 = Faculty.objects.create(
			# 								  user = obj,
			# 								  fac_name = request.user.full_name,
			# 								  no_of_courses = 1,

			# 								 )
			return redirect('fac-course-content')
	else:
		fm = CourseistrationForm()
	return render(request, 'course/fac_course_reg.html', {'form': fm})



@login_required(login_url='')
def fac_view_course_content(request):
	"""
	This function will display the course 
	content of that particular faculty
	"""
	faculty_course = Course.objects.filter(fac_name = request.user.full_name)
	data = CourseContent.objects.filter(fac_name = request.user.full_name)
	return render(request, 'course/view_course_content.html', {'data': data, 'faculty_crs': faculty_course})


@login_required(login_url='')
def upload_course_content(request):
	""" 
	This function will display the 
	form in which the faculty 
	can upload course content including 
	pdf and video tutorial
	"""
	course_content = Course.objects.filter(fac_name = request.user.full_name)

	if request.method == "POST":
		if  request.FILES['pdfcontent'] and request.FILES['videocontent']:
			obj = CourseContent.objects.create(
												fac_name = request.user.full_name,
												course_name = request.POST.get('course_name'),
												subject_title = request.POST.get('subject_title'),
												pdf_content = request.FILES['pdfcontent'],
												video_content = request.FILES['videocontent']
												)
		return redirect('fac-view-course-content')
	return render(request, 'course/upload_course_content.html', {'course_content': course_content})


@login_required(login_url='')
def student_course_enroll_form(request):
	""" 
	This function will display the form
    in which student can enroll
	in a particular course of her class teacher
	"""
	obj = CustomUser.objects.get(status = 'teacher', class_name = request.user.class_name)
	subjects = Course.objects.filter(fac_name = obj.full_name)

	if request.method == 'POST':
		# Retrieving object of particular user		
		obj1 = CustomUser.objects.get(id = request.user.id)
		course_name = request.POST.get('course_name')

		# Creating an object in Student Course Enroll Data
		obj2 = StudentCourseEnroll.objects.create(
													 user = obj1,
													 fac_name = obj.full_name,
													 stu_name = request.user.full_name,
													 course_name = course_name
													)

		# Update Number of students in Faculty Course Registration Data
		obj3 = Course.objects.get(fac_name = obj.full_name, course_name = course_name)
		obj3.no_of_students_enrolled += 1
		obj3.save() 
		return redirect('stu-course-enroll-content')
	else:
		fm = CourseEnrollForm()
	mydict = {'data': subjects, 'class_teacher': obj}
	return render(request, 'course/course_enrol_form.html', mydict)


@login_required(login_url='')
def stu_view_course_content(request):
	""" 
	This function will display the course
	content of registered faculty
	"""
	mysubjectlist = []
	obj = CustomUser.objects.get(status = 'teacher', class_name = request.user.class_name)
	faculty_course = Course.objects.filter(fac_name = obj.full_name)
	data2 = StudentCourseEnroll.objects.filter(user__id = request.user.id,
												 fac_name = obj.full_name)

	for item in data2:
		for item2 in CourseContent.objects.filter(fac_name = item.fac_name,
													 course_name = item.course_name):
			mysubjectlist.append(item2)
	mydict = {'data': mysubjectlist, 'faculty_crs': faculty_course}
	return render(request, 'course/view_course_content.html', mydict)
