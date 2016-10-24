# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class IP(models.Model):
	ip = models.CharField(max_length=15, help_text=u'ip')
	name = models.CharField(max_length=255, help_text=u'名称')
	domain = models.CharField(max_length=255, null=True, blank=True, help_text=u'域名')
	update_date = models.DateTimeField(auto_now=True, help_text=u'更新时间')

	def __unicode__(self):
		return self.name

