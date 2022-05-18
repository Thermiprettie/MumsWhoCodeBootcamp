from django.db import models

#from django.contrib.auth.models import User

#from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User
#users = User.objects.filter(is_superuser=True)

#is_superuser=True
# Create your models here.

# import user model
#first option for importing user model
from django.contrib.auth.models import User

#second option for importing user model

from django.contrib.auth import get_user_model

task_owner = get_user_model()


# Create your models here.
class SearchHistory(models.Model):
    name_of_task = models.CharField(max_length=100)
    city_searched  =  models.TextField()
    date_of_site_visit = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name_of_task
    
    # plural of the model name
    class Meta:
        verbose_name_plural = 'Search history'