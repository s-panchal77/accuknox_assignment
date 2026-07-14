from django.db import models


# A simple model to act as the signal sender.
# We need at least one model so that post_save has something to fire on.
# UserProfile is kept intentionally minimal — just a name field.
class UserProfile(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
