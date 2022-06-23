""" apps/review/views.py """
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .models import RateReview


def review_data_sorting_function(sortvalue, content):
	if sortvalue == "newest":
		review_data = RateReview.objects.filter(
								fac_name = content.fac_name, 
								course_name = content.course_name).order_by('-review_date')
	elif sortvalue == "oldest":
		review_data = RateReview.objects.filter(
								fac_name = content.fac_name, 
								course_name = content.course_name).order_by('review_date')
	elif sortvalue == "most-upvotes":
		review_data = RateReview.objects.filter(
								fac_name = content.fac_name, 
								course_name = content.course_name).order_by('-no_of_upvotes')
	elif sortvalue == "least-upvotes":
		review_data = RateReview.objects.filter(
								fac_name = content.fac_name, 
								course_name = content.course_name).order_by('no_of_upvotes')
	else:
		review_data = RateReview.objects.filter(
								fac_name = content.fac_name, 
								course_name = content.course_name).order_by('-review_date')
	return review_data


@login_required(login_url='')
def rate_and_review_form(request):
	""" 
	    This function the form in which student
		can give ratings and reviews 
	    of particular faculty
	"""
	obj = CustomUser.objects.get(status = 'teacher', 
									class_name = request.user.class_name
									)
	subjects = Course.objects.filter(fac_name = obj.full_name)
	if request.method == 'POST':
		rating = request.POST.get('rate')
		course_name = request.POST.get('course_name')
		obj2 = RateReview(
							user = obj,
							fac_name = obj.full_name,
							stu_name = request.user.full_name,
							course_name = course_name,
							rate = request.POST.get('rate'),
							review = request.POST.get('review')
							)
		obj2.save()
		calculate_average_value(rating, course_name, obj)
		return redirect('stu-dash')
	return render(request, 'course/review_form.html', {'teacher_name': obj, 'subjects': subjects})


def view_rating_and_reviews(request):
	rate_data =  RateReview.objects.all()
	return render(request, 'core/view_rating_review.html', {'rate_data': rate_data})


def view_faculty_course_data(request):
	faculty_course = Course.objects.all()
	return render(request, 'course/view_fac_course_content.html', {'faculty_crs': faculty_course})


def view_course_detail(request, id):
	sortvalue = request.GET.get('revsort')

	obj = CustomUser.objects.get(status = 'teacher', 
									class_name = request.user.class_name
									)
	content = Course.objects.get(id = id)

	review_data = review_data_sorting_function(sortvalue, content)
	
	if request.method == 'POST':
		rating = request.POST.get('rate')
		course = content.course_name
		obj3 = RateReview.objects.create(
											user = obj,
											fac_name = obj.full_name,
											stu_name = request.user.full_name,
											course_name = course,
											rate = rating,
											review = request.POST.get('review')
											)
		calculate_average_value(rating, course, obj)
		url = reverse('view-fac-course-detail', kwargs={'id': id})
		return HttpResponseRedirect(url)

	mydict = {'ele': content, 'review_data': review_data}
	return render(request, 'course/view_course_detail.html', mydict)


def calculate_average_value(rating, course_name, obj):
	obs = RateReview.objects.filter(user_id = obj, course_name = course_name)
	obj3 = Course.objects.get(
							fac_name = obj.full_name,
							course_name = course_name
	)
	rate_sum = 0
	for i in obs:
		rate_sum = rate_sum + i.rate

	# Calculating averge value of rate given by students to a particular teacher
	ave_value = rate_sum / obj3.no_of_students_rated
	
	# Updating Course object
	obj3.average_rate = ave_value
	obj3.save()


def adding_upvotes_member_function(request):
	facid = request.GET.get('facregid')
	revid = request.GET.get('reviewid')
	obj = CustomUser.objects.get(id = request.user.id)
	mylist = []

	# Retrieving object from review data and updating
	obj2 = RateReview.objects.get(id = revid)
	obj2.no_of_upvotes = obj2.no_of_upvotes + 1
	number_of_upvotes = obj2.no_of_upvotes

	for i in obj2.upvotes_member.all():
		mylist.append(i)

	# appending element in mylist
	mylist.append(obj)
	obj2.upvotes_member.set(mylist)
	obj2.save()
	
	choice = [number_of_upvotes,]
	return JsonResponse(choice, safe=False)
