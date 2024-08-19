from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_id = models.IntegerField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.recipe_id) + " " + self.user.username