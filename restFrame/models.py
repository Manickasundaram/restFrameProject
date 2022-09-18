from django.db import models


# Create your models here.
class restFramePost(models.Model):
    name=models.CharField(max_length=200)
    std=models.IntegerField()
    stream=models.CharField(max_length=100)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
