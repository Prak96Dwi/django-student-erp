""" apps/review/models.py """
from django.db import models
from django.conf import settings


class RateReview(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    faculty_name = models.CharField(max_length=100)

    student_name = models.CharField(max_length=100)

    course_name = models.CharField(max_length=100)

    upvotes_member = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='upvoters_full_name',
    )

    rate = models.IntegerField()

    review = models.CharField(max_length=1000)

    review_date = models.DateTimeField(auto_now_add=True)

    number_of_upvotes = models.IntegerField(default=0)


    def __str__(self):
    	"""String representation of RateReview instance."""
    	return f'{self.user}'
