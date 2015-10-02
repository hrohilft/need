from django.db import models
import datetime
from django.utils import timezone

class Need(models.Model):
	what = models.CharField(max_length=200)
	amount = models.IntegerField(default=1)
	where = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	done = models.BooleanField(default=False)
	
	def __str__(self):
		return "%d %s needed at %s" % (self.amount, self.what, self.where)

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
