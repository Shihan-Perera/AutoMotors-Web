from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from publishing.models import publishing
from django.core.paginator import Paginator
#map
import pandas as pd
import folium
from folium import plugins
from folium.plugins import MarkerCluster
from django.views.generic import TemplateView

def location_map(request):
    data= pd.read_csv('main_dataset.csv')

    if 'sedan' in request.GET:
        sedan = request.GET['sedan']
        if sedan:
            data= pd.read_csv('types/sedan.csv')

    if 'suv' in request.GET:
        suv = request.GET['suv']
        if suv:
            data= pd.read_csv('types/SUV.csv')

    if 'coupe' in request.GET:
        coupe = request.GET['coupe']
        if coupe:
            data= pd.read_csv('types/coupe.csv')

    if 'pickup' in request.GET:
         pickup = request.GET['pickup']
         if pickup:
             data= pd.read_csv('types/pickup.csv')

    if 'Convertible' in request.GET:
        Convertible = request.GET['Convertible']
        if Convertible:
            data= pd.read_csv('types/convertible.csv')

    if 'Hatchback' in request.GET:
         Hatchback = request.GET['Hatchback']
         if Hatchback:
             data= pd.read_csv('types/hatchback.csv')

    if 'MPV/Minivan' in request.GET:
        MPV = request.GET['MPV/Minivan']
        if MPV:
            data= pd.read_csv('types/mini-van.csv')

    if 'Station Wagon' in request.GET:
        Station = request.GET['Station Wagon']
        if Station:
            data= pd.read_csv('types/wagon.csv')

    if 'van' in request.GET:
        van = request.GET['van']
        if van:
            data= pd.read_csv('types/van.csv')

    if 'lorry' in request.GET:
        lorry = request.GET['lorry']
        if lorry:
            data= pd.read_csv('types/truck.csv')

    lat_lon = data[["lat","long"]].values[:15000]
    map = folium.Map(location=[35.4676, -97.5164],tiles='CartoDB dark_matter',zoom_start=4)
    marker_cluster = MarkerCluster().add_to(map)

    for point in range(0, 1000):
        folium.Marker(lat_lon[point],popup=data['type'][point],icon=folium.Icon(color='darkblue', icon_color='white', icon='car', angle=0, prefix='fa') ).add_to(marker_cluster)

    map=map._repr_html_()
    context = {
      'nodes': map,
    }

    return render(request, 'location_map.html', context)



def index(request):
    publish = publishing.objects.order_by('-pub_date')

    return render(request, 'index.html',{'publish': publish,'count':publish.count() })




def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        #send Email
        send_mail(
           subject,#Subject
           message+ ' from '+email,#message
           email,#from
           ['denukasandeepa@gmail.com'],#to
        )

        return render(request,'contact.html',{ 'name' :  name })
    else:
        return render(request,'contact.html')



def type(request):
    type = publishing.objects.order_by('-pub_date')

    if 'sedan' in request.GET:
      sedan = request.GET['sedan']
      if sedan:
        type = type.filter(type__icontains=sedan)

    if 'suv' in request.GET:
      suv = request.GET['suv']
      if suv:
        type = type.filter(type__icontains=suv)

    if 'coupe' in request.GET:
      coupe = request.GET['coupe']
      if coupe:
        type = type.filter(type__icontains=coupe)

    if 'pickup' in request.GET:
      pickup = request.GET['pickup']
      if pickup:
        type = type.filter(type__icontains=pickup)

    if 'CUV/Crossover' in request.GET:
      Crossover = request.GET['CUV/Crossover']
      if Crossover:
        type = type.filter(type__icontains='CUV/Crossover')

    if 'Convertible' in request.GET:
      Convertible = request.GET['Convertible']
      if Convertible:
        type = type.filter(type__icontains='Convertible')

    if 'Hatchback' in request.GET:
      Hatchback = request.GET['Hatchback']
      if Hatchback:
        type = type.filter(type__icontains=Hatchback)

    if 'MPV/Minivan' in request.GET:
      MPV = request.GET['MPV/Minivan']
      if MPV:
        type = type.filter(type__icontains='MPV/Minivan')

    if 'Station Wagon' in request.GET:
      Station = request.GET['Station Wagon']
      if Station:
        type = type.filter(type__icontains='Station Wagon')

    if 'van' in request.GET:
      van = request.GET['van']
      if van:
        type = type.filter(type__icontains=van)

    if 'bus' in request.GET:
      bus = request.GET['bus']
      if bus:
        type = type.filter(type__icontains=bus)

    if 'lorry' in request.GET:
      lorry = request.GET['lorry']
      if lorry:
        type = type.filter(type__icontains=lorry)

    if 'motorbike' in request.GET:
      motorbike = request.GET['motorbike']
      if motorbike:
        type = type.filter(type__icontains=motorbike)

    if 'scooter' in request.GET:
      scooter = request.GET['scooter']
      if scooter:
        type = type.filter(type__icontains=scooter)


    if 'Three-Wheeler' in request.GET:
      Three = request.GET['Three-Wheeler']
      if Three:
        type = type.filter(type__icontains='Three-Wheeler')

    paginator = Paginator(type, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
         'count':type.count(),
         'page':paged_listings,
         'searched': request.GET
    }
    return render(request, 'publishing/search.html', context)
