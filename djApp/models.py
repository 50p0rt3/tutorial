from django.db import models
from datetime import datetime
from djApp.choices import gender_choices
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return 'Name: {}'.format(self.name)
    
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'
        ordering=['id']

class Product(models.Model):
    name=models.CharField(max_length=100,unique=True)
    catfk=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product/%Y/%m/%d',null=True,blank=True)
    pricevp=models.DecimalField(default=0.00,max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Product'
        verbose_name_plural='Products'
        ordering=['id']

class Client(models.Model):
    name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    dui=models.CharField(max_length=9,unique=True)
    birthday=models.DateField(default=datetime.now)
    address=models.CharField(max_length=150,null=True,blank=True)
    gender=models.CharField(max_length=1,choices=gender_choices,default='male')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Client'
        verbose_name_plural='Clients'
        ordering=['id']

class Sale(models.Model):
    clntfk=models.ForeignKey(Client,on_delete=models.CASCADE)
    date_joined=models.DateField(default=datetime.now)
    sub_total=models.DecimalField(default=0.00,max_digits=10,decimal_places=2)
    tax=models.DecimalField(default=0.00,max_digits=10,decimal_places=2)
    total=models.DecimalField(default=0.00,max_digits=10,decimal_places=2)

    def __str__(self):
        return self.clntfk.name
    
    class Meta:
        verbose_name='Sale'
        verbose_name_plural='Sales'
        ordering=['id']

class Detailsales(models.Model):
    salefk=models.ForeignKey(Sale,on_delete=models.CASCADE)
    prodfk=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.DecimalField(default=0.00,max_digits=10,decimal_places=2)
    quantity=models.IntegerField(default=0)
    sub_total=models.DecimalField(default=0.00,max_digits=10,decimal_places=2)

    def __str__(self):
        return self.prodfk.name
    
    class Meta:
        verbose_name='Detail_Sale'
        verbose_name_plural='Detail_Sales'
        ordering=['id']

class Employee(models.Model):
    name=models.CharField(max_length=100)
    dui=models.CharField(max_length=9,unique=True)
    date_joined=models.DateField(default=datetime.now)
    date_creation=models.DateTimeField(auto_now=True)
    date_updated=models.DateTimeField(auto_now_add=True)
    age=models.PositiveIntegerField(default=0)
    salary=models.DecimalField(default=0.00,max_digits=10,decimal_places=2)
    state=models.BooleanField(default=True)
    avatar=models.ImageField(upload_to='avatar/%Y/%m/%d',null=True,blank=True)
    cvitae=models.FileField(upload_to='cvitae/%Y/%m/%d',null=True,blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        db_table = 'employee'
        ordering = ['id']

    