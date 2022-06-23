""" chat/urls.py """
from django.urls import path
from . import views

urlpatterns = [
	# Chat url
	path(
		'chat/one/<int:id>/',
		views.room,
		name='one-room'
	),
	
	path(
		'chat/create/room/',
		views.create_oneroom,
		name='create-one-room'
	)
]
