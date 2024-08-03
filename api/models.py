from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=100,choices=(("IT","IT"),("Non IT","Non IT"),("Mobile Phones","Mobile Phones"))) # choices is nested tuple
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 100)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField()
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50,choices=(
        ("manager","manager"),
        ("software developer","software developer"),
        ("project leader","project leader")
    ))
    company_detail = models.ForeignKey(Company,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.first_name+" "+self.last_name
