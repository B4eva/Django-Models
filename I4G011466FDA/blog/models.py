from django.db import models
from django.contrib.auth import get_user_model 

# Create your models here.

 
class Post(models.Model):
    title = models.CharField(max_length= 200)
    text = models.TextField()
     ##    Return the User model that is active in this project.
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    def __str__(self) -> str:
      return self.title
    
    def __str__(self) -> str:
      return self.text