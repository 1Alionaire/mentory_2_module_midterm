from django.db import models

class Feedback(models.Model):
    user_name = models.CharField(max_length=20)
    email = models.EmailField()
    input_time = models.DateTimeField()
    message = models.TextField()
    def __str__(self):
        return self.user_name

class Animals(models.Model):
    name = models.CharField(max_length=20)
    animal_image = models.ImageField(upload_to='animals')

    def __str__(self):
        return self.name