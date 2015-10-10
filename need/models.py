from django.db import models
import datetime
from django.utils import timezone

class Need(models.Model):
	what = models.CharField(max_length=200)
	amount = models.PositiveSmallIntegerField(default=1)
	# old way of choosing place
#	where = models.CharField(max_length=200)
	# new way of choosing place
	PLACES = (('H', 'HWBR'), ('E', 'Emporhalle'), ('P', 'Physik'),)
	where = models.CharField(max_length=1, choices=PLACES, default='H')
	pub_date = models.DateTimeField('date published')
	done = models.BooleanField(default=False)
	
	def __str__(self):
		return "%d %s needed at %s" % (self.amount, self.what, self.where)

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
		
	def public_transl(self):
		return self.transl.filter(public=True)

class Transl(models.Model):
	need = models.ForeignKey('need.Need', related_name='transl')
#	author = models.CharField(max_length=200)
#	text = models.TextField()
	text = models.CharField(max_length=200)
	created_date = models.DateTimeField(default=timezone.now)
	public = models.BooleanField(default=False)

	def publish(self):
		self.public = True
		self.save()
		
	def hide(self):
		self.public = False
		self.save()

	def __str__(self):
		return self.text
