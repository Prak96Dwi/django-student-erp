# """ core/admin.py """
# from django.contrib import admin

# from .models import (
# 	CustomUser, HomeWork, InvitationList,
# 	StudentInvitation, ChatGroupList, OnetoOneMessage,
# 	Course, CourseContent, StudentCourseEnroll, 
# 	RateReview, Faculty
# )


# # Display of records of CustomUser
# class CustomUserAdmin(admin.ModelAdmin):
# 	list_display = (
# 		'full_name', 'email', 'status', 'class_name'
# 	)

# admin.site.register(CustomUser, CustomUserAdmin)


# # Display of records of HomeWork
# class HomeWorkAdmin(admin.ModelAdmin):
# 	list_display = (
# 		'user', 'student_name', 'class_name', 'title'
# 	)

# admin.site.register(HomeWork, HomeWorkAdmin)


# # Display of records of InvitationList
# class InvitationListAdmin(admin.ModelAdmin):
# 	list_display = (
# 		'name_fac', 'email_fac'
# 	)

# admin.site.register(InvitationList, InvitationListAdmin)


# # Display of records of ChatGroupList
# class ChatGroupListAdmin(admin.ModelAdmin):
# 	list_display = ('admin_name', 'member_name')

# admin.site.register(ChatGroupList, ChatGroupListAdmin)


# # Display of records of OnetoOneMessage
# class OnetoOneMessageAdmin(admin.ModelAdmin):
# 	list_display = ('e_id', 'e_name', 'e_message', 'e_image', 'e_time', 'e_groupid')

# admin.site.register(OnetoOneMessage, OnetoOneMessageAdmin)


# # Display of records of Course
# class CourseAdmin(admin.ModelAdmin):
# 	list_display = ('user', 'faculty_name', 'name')

# admin.site.register(Course, CourseAdmin)


# # Display of records of CourseContent
# class CourseContentAdmin(admin.ModelAdmin):
# 	list_display = ('faculty_name', 'course_name')

# admin.site.register(CourseContent, CourseContentAdmin)


# class StudentCourseEnrollAdmin(admin.ModelAdmin):
# 	list_display = ('user', 'fac_name')

# admin.site.register(StudentCourseEnroll, StudentCourseEnrollAdmin)


# class RateReviewAdmin(admin.ModelAdmin):
# 	list_display = ('fac_name', 'stu_name')

# admin.site.register(RateReview, RateReviewAdmin)


# class FacultyAdmin(admin.ModelAdmin):
# 	list_display = ('user', 'fac_name', 'fac_status')

# admin.site.register(Faculty, FacultyAdmin)


# admin.site.register(StudentInvitation)



