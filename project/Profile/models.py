from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.ForeignKey(User, unique=True)
	score = models.IntegerField()

# User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])