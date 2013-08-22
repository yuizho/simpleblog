from django.db import models

class Content(models.Model):
    #user_id = models.ForeignKey(Poll)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=200)
    date = models.DateTimeField('date')

    def __unicode__(self):
        return self.title
    

"""class user(models.Model):
    user_id = models.CharField(max_length=30)
    user_pass = models.CharField(max_length=30)

    def __unicode__(self):
        return self.user_id
"""

    

