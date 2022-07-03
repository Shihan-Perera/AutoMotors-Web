from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from osm_field.fields import LatitudeField, LongitudeField, OSMField

class publishing(models.Model):
      type_choices = (
      ('Motorbike','Motorbike'),
      ('Scooter','Motorbike'),
      ('Sedan','Sedan'),
      ('Hatchback','Hatchback'),
      ('MPV/Minivan','MPV/Minivan'),
      ('SUV','SUV'),
      ('CUV/Crossover','CUV/Crossover'),
      ('Pickup','Pickup'),
      ('Coupe','Coupe'),
      ('Convertible','Convertible'),
      ('Station Wagon','Station Wagon'),
      ('Van','Van'),
      ('Three-Wheeler','Three-Wheeler'),
      ('Lorry','Lorry'),
      ('Bus','Bus'),
      )

      fuel_choices = (
      ('Gas','Petrol'),
      ('Diesel','Diesel'),
      ('Electric(ECV)','Electric(ECV)'),
      ('Hybrid(HEV)','Hybrid(HEV)'),
      ('LPG Autogas','LPG Autogas'),
      ('Biofuel','Biofuel'),
      )

      transmission_choices=(
      ('Manual','Manual'),
      ('Automatic','Automatic'),
      ('Semi-Automatic','Semi-Automatic'),
      ('CVT','CVT'),
      )

      condition_choices=(
      ('Excellent','Excellent'),
      ('Good','Good'),
      ('Fairly Good','Fairly Good'),
      ('Fairly Poor','Fairly Poor'),
      ('Poor','Poor'),
      )

      category_choices=(
      ('New','New'),
      ('Used','Used'),
      )


      title = models.TextField(max_length=100)
      pub_date = models.DateTimeField(default=datetime.now)
      type = models.TextField(max_length=100, choices = type_choices)
      brand = models.TextField(max_length=100)
      model = models.TextField(max_length=50)
      category = models.TextField(max_length=100, choices = category_choices)
      year = models.IntegerField()
      fuel = models.TextField(max_length=100, choices = fuel_choices)
      transmission = models.TextField(max_length=100, choices = transmission_choices)
      milage = models.IntegerField()
      engine = models.TextField(max_length=50)
      image1 = models.ImageField(upload_to='upload_to=images/%Y/%m/%d/')
      image2 = models.ImageField(upload_to='upload_to=images/%Y/%m/%d/')
      image3 = models.ImageField(upload_to='upload_to=images/%Y/%m/%d/')
      image4 = models.ImageField(upload_to='upload_to=images/%Y/%m/%d/')
      image5 = models.ImageField(upload_to='upload_to=images/%Y/%m/%d/')
      description = models.CharField(max_length=250)
      condition = models.TextField(max_length=100, choices = condition_choices)
      price = models.IntegerField()
      tel = models.TextField(max_length=10)
      city = models.TextField(max_length=50)
      address = models.TextField(max_length=100)
      vote_total = models.IntegerField(default=1)
      owner = models.ForeignKey(User,on_delete=models.CASCADE)
      location = OSMField()
      location_lat = LatitudeField()
      location_lon = LongitudeField()


      def __str__(self):
          return self.title

      def pub_date_pretty(self):
          return pub_date.strftime('%b %e %y')
