from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
# Create your models here.

class Person(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    plate_num=models.CharField(max_length=8)
    status=models.CharField(max_length=8)
    time_1=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}{}{}{}{}'.format(self.id,self.name,self.plate_num,self.status,self.time_1)

class park_area_data(models.Model):
    id = models.AutoField(primary_key=True)
    slots=models.CharField(max_length=30)
    nu=models.OneToOneField(Person,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return '{}{}{}'.format(self.id,self.slots,self.nu)

class slot_description(models.Model):
    capacity = models.IntegerField()
    description=models.TextField()
    park_area_data = models.ForeignKey(park_area_data, on_delete=models.CASCADE)

    def __str__(self):
        return '{}{}{}'.format(self.capacity,self.description,self.park_area_data,)



