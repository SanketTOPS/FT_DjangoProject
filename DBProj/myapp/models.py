from django.db import models

# Create your models here.
class userInfo(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    dob=models.DateField()
    mobile=models.BigIntegerField()
    address=models.TextField()

class signup_master:
    pass