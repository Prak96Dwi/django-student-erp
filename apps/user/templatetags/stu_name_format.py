from django import template

register = template.Library()

@register.filter()
def student_name_change(value):
	return value.lower().replace(' ', '-')