from django.db import models


class District(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
     
class City(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name
    
class Person(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField(auto_now_add=False)
    age = models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)
    address = models.TextField()
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    ACCOUNT_CHOICES = (
        ('C', 'Current'),
        ('S', 'Savings'),
    )
    account_type = models.CharField(max_length=1, choices=ACCOUNT_CHOICES)
    Materials_Provide = models.BooleanField("Materials Required:", null=True, default=True)
    Debit = models.BooleanField("Debit Card", default=False)
    Credit = models.BooleanField("Credit Card", default=False)
    Passbook = models.BooleanField("Passbook", default=False)
    
    
    def __str__(self):
        return self.name




