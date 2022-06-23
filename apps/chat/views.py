""" apps/chat/views.py """
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


login_required(login_url='')
def room(request, id):
	""" 
	The function will display the one-to-one conversation
	room in which the teacher can chat with her student
    """
	data = ChatGroupList.objects.all()
	chatdata = OnetoOneMessage.objects.all()
	name = request.user.full_name

	if request.method == "POST":
		fm = RoomForm(request.POST, request.FILES)
		if fm.is_valid():
			if fm.cleaned_data.get('myimage') is not None:
				obj = OnetoOneMessage.objects.create(
														e_id = request.user.id,
														e_name = name,
														e_message = fm.cleaned_data.get('mytext'),
														e_image = request.FILES['myimage'],
														e_time =  datetime.datetime.today().time(),
														e_groupid = id
													)
			else:
				obj = OnetoOneMessage.objects.create(
														e_id = request.user.id,
														e_name = name,
														e_message = fm.cleaned_data.get('mytext'),
														e_time =  datetime.datetime.today().time(),
														e_groupid = id
													)
			return HttpResponseRedirect('/chat/one/%d/'%(id))
	else:
		fm = RoomForm()
	mydict = {'groupname': data, 'room_name': id, 'message': chatdata, 'user_name': name, 'form': fm}
	return render(request, 'chat/room.html', mydict)


@login_required(login_url='')
def create_oneroom(request):
	""" 
	This function will create the room for one-to-one conversation
	"""
	data = CustomUser.objects.filter(status = "student", class_name = request.user.class_name)
	channeldata = ChatGroupList.objects.all()

	if request.method == 'POST':
		obj = ChatGroupList.objects.create(
										   admin_name = request.user.full_name,
										   member_name = request.POST.get('members'),
										   )
	return render(request, 'chat/create_one_room.html', {'studata': data, 'channeldata' : channeldata})
