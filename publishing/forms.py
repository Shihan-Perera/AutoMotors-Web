from django import forms
from .models import publishing
from django.utils.translation import ugettext_lazy as _

class CreateAdForm(forms.ModelForm):
    class Meta:
        model = publishing
        fields = (
        'title',
        'type',
        'brand',
        'model',
        'category',
        'year',
        'transmission',
        'milage',
        'fuel',
        'engine',
        'image1',
        'image2',
        'image3',
        'image4',
        'image5',
        'description',
        'condition',
        'price',
        'tel',
        'city',
        'address',
        'location',
        'location_lat',
        'location_lon',
        )

        widgets = {
        'title':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the Ad title..... e.g- Used Prado for Sale"}),
        'description':forms.Textarea(attrs={"placeholder": "Vehicle description means a description of a vehicle including at a minimum the license information, issuing state, make, model, year, color, body style, and vehicle identification number (VIN)....."}),
        'type':forms.Select(attrs={"class":"form-control"}),
        'brand':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the correct model...... e.g-Toyota"}),
        'model':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the correct model...... e.g-Prado"}),
        'category':forms.Select(attrs={"class":"form-control"}),
        'year':forms.NumberInput(attrs={"class":"form-control","placeholder":"Without spaces or any symbols or latters"}),
        'transmission':forms.Select(attrs={"class":"form-control"}),
        'milage':forms.NumberInput(attrs={"class":"form-control","placeholder":"Without spaces or any symbols or latters"}),
        'fuel':forms.Select(attrs={"class":"form-control"}),
        'engine':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the correct engine details... e.g-V8 4000cc"}),
        'condition':forms.Select(attrs={"class":"form-control"}),
        'price':forms.NumberInput(attrs={"class":"form-control","placeholder":"Without spaces or any symbols or latters"}),
        'tel':forms.TextInput(attrs={"class":"form-control","placeholder":"Without any symbols or latters"}),
        'city':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the nearest city"}),
        'address':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the address"}),
        }

        labels = {
            'title': _('Ad Title'),
            'type': _('Vehicle Type'),
            'brand': _('Vehicle Brand'),
            'model': _('Vehicle Model'),
            'category': _('Vehicle Category'),
            'year': _('Manufacture Year'),
            'transmission': _('Vehicle Transmission Type'),
            'milage': _('Milage of the Vehicle'),
            'fuel': _('Fuel Type'),
            'engine': _('Engine Model and Capacity'),
            'image1': _('Ad Main Image'),
            'image2': _('Ad Image 1'),
            'image3': _('Ad Image 2'),
            'image4': _('Ad Image 3'),
            'image5': _('Ad Image 4'),
            'description': _('Description About the Vehicle'),
            'condition': _('Condition'),
            'price': _('Your Price for the Vehicle'),
            'tel': _('Your Telephone Number'),
            'city': _('Nearest City'),
            'address': _('Adress'),
        }




Manuf_Choices= [
    (1, 'Chevrolet'),
    (2, 'Ford'),
    (3, 'Nissan'),
    (4, 'Jeep'),
    (5, 'Toyota'),
    (6, 'Honda'),
    (7, 'Audi'),
    (8, 'GMC'),
    (9, 'RAM'),
    (10, 'Dodge'),

    ]


Condition_Choices= [
    (1, 'Brand New'),
    (2, 'Like New'),
    (3, 'Excellent'),
    (4, 'Good'),
    (5, 'Fair'),
    (6, 'Salvage'),
    ]


cylinders_Choices= [
    (1, '3 cylinders'),
    (2, '4 cylinders'),
    (3, '5 cylinders'),
    (4, '6 cylinders'),
    (5, '8 cylinders'),
    (6, '10 cylinders'),
    (7, '12 cylinders'),
    (8, 'other'),

    ]

fuel_Choices= [
    (1, 'Petrol'),
    (2, 'Diesel'),
    (3, 'Hybrid'),
    (4, 'Electric'),
    (5, 'Other'),
    ]

transmission_Choices= [
    (1, 'Automatic'),
    (2, 'Manual'),
    (3, 'Other'),
    ]


type_Choices= [
    (1, 'Truck'),
    (2, 'SUV'),
    (3, 'Sedan'),
    (4, 'Pickup'),
    (5, 'Wagon'),
    (6, 'Coupe'),
    (7, 'Hatchback'),
    (8, 'Van'),
    (9, 'Mini-Van'),

    ]

year_Choices= [tuple([x,x]) for x in range(1923,2022)]


class PredictForm(forms.Form):
     model = forms.CharField(label='Model')
     type = forms.IntegerField(widget=forms.Select(choices=type_Choices,attrs={"class":"form-control","placeholder":"Enter the address"}))
     year = forms.IntegerField(label='Enter Manufactured Year',widget=forms.Select(choices=year_Choices))
     manuf = forms.IntegerField(label='Select Manufacturer',widget=forms.Select(choices=Manuf_Choices))
     condition = forms.IntegerField(label='Select Condition',widget=forms.Select(choices=Condition_Choices))
     cylinders = forms.IntegerField(label='Select Engine',widget=forms.Select(choices=cylinders_Choices))
     fuel = forms.IntegerField(label='Select Fuel Type',widget=forms.Select(choices=fuel_Choices))
     odometer = forms.FloatField(label='Odometer')
     transmission = forms.IntegerField(label='Select transmission',widget=forms.Select(choices=transmission_Choices))
