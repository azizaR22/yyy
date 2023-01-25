from django.db import models

# Create your models here.


class Customer(models.Model):
    fullname = models.CharField(max_length=200, null=False)
    mothername = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    gen=(('male','male'),('female','female'))
    Gender=models.CharField(max_length=50,choices=gen)
    birthday=models.DateField(null=False)
    bloodg=(('A+','A+')),(('A-','A-')),(('B+','B+')),(('B-','B-')),(('AB+','AB+')),(('AB-','AB-')),(('O+','O+')),(('O-','O-'))
    blood_group=models.CharField(max_length=50,choices=bloodg)
    nationality=models.CharField(max_length=200, null=False)
    personalID=models.CharField(max_length=200, null=False,unique=True)
    images=models.ImageField(null=False)
    description = models.TextField(null=True, blank=True)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    license_id=models.CharField(max_length=200, null=False,unique=True)
    vehicle_id=models.CharField(max_length=200, null=False,unique=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return str(self.id)

   


