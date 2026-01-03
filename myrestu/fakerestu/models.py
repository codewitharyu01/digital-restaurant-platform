from django.db import models

# Create your models here.

class FeedbackForm(models.Model):
    email=models.EmailField(max_length=100)
    name=models.CharField(max_length=200)
    feedback=models.CharField(max_length=200)
    review=models.IntegerField(max_length=10)
    
class BookingTable(models.Model):
    persons=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    name=models.CharField(max_length=200)
    request=models.CharField(max_length=200)
    date=models.DateField(max_length=10)
    time=models.TimeField(max_length=10)
    phone=models.BigIntegerField()

class FoodDiliver(models.Model):
    name=models.CharField(max_length=200)
    phone=models.BigIntegerField()
    items=models.CharField(max_length=200)
    food=models.CharField(max_length=200)
    pin=models.IntegerField(max_length=10000)
    address=models.CharField(max_length=200)

class EmailOTP(models.Model):
    email=models.EmailField(unique=True) 
    otp=models.CharField(max_length=6)
    is_verified=models.CharField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return self.email
    
class CreateNewAccount(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    password=models.CharField(default=False)

class Repass(models.Model):
    repassword=models.CharField(max_length=200)  
    
    

     


