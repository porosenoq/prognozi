from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Match(models.Model):
	LEAGUE_CHOICES = (
	(1, "English Premier League"),
	(2, "Spanish Primera Division"),
	(3, "Bulgarian A PFG"),
	)
	
	created_date = models.DateTimeField(default=timezone.now)
	match_date = models.DateTimeField(blank=True, null=True)
	league = models.IntegerField(choices=LEAGUE_CHOICES)
	hometeam = models.CharField(max_length=255)
	awayteam = models.CharField(max_length=255)
	homecoef = models.DecimalField(max_digits=4, decimal_places=2)
	xcoef = models.DecimalField(max_digits=4, decimal_places=2)
	awaycoef = models.DecimalField(max_digits=4, decimal_places=2)

	def __unicode__(self):
		return self.hometeam + '-' + self.awayteam	
