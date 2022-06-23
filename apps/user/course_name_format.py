from django import template

register = template.Library()

@register.filter(name='course_name_change')
def course_name_change(value):
	return value.lower().replace(' ', '-')