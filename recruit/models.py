from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class RecruitmentModel(models.Model):
    name = models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    phone = PhoneNumberField(
        blank=False, null=False)
    roll_no= models.CharField(max_length=100)    
    branch = models.CharField(max_length=100)
    homecity=models.CharField(max_length=100)
    qualities=models.TextField()
    previous_experience=models.TextField()
    dish_describe=models.TextField()
    qualities_for_core=models.TextField()
    upcoming_event_desired=models.TextField()
    
    def __str__(self):
        return self.name