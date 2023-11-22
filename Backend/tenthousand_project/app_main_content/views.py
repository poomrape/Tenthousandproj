from django.shortcuts import render, redirect
from .Maps_api import ShopFinder
from .api import api_key
from .forms import LocationForm, RadiusForm

# Create your views here.
shop_finder = ShopFinder(api_key)

global_shop_info_list = []
global_location = []

def maps(request):
    global global_shop_info_list
    global global_location
    location_form = LocationForm()
    radius_form = RadiusForm()

    if request.method == 'POST':
        location_form = LocationForm(request.POST)
        radius_form = RadiusForm(request.POST)
        sort = request.POST.get('sort')
        if location_form.is_valid():
            location = location_form.cleaned_data['location']


        if radius_form.is_valid():
            radius = radius_form.cleaned_data['radius']
            if not radius:
                radius = 4000
            try:
                if not global_shop_info_list: 
                    global_location = shop_finder.get_user_location(location) 
                    global_shop_info_list = shop_finder.get_shop_info_list(global_location, radius)
                sort_by = request.GET.get('sort_by', 'distance')
                if sort_by == 'distance':
                    if sort == 'distanceasc':
                        global_shop_info_list.sort(key=lambda x: x.get('distance', float('inf')))
                    elif sort == 'distancedsc':
                        global_shop_info_list.sort(key=lambda x: x.get('distance', float('inf')), reverse=True)
                return render(request, 'app_main_content/displaymap.html', context={'shop_result': global_shop_info_list, 'sort_by': sort_by, 'start': f'{global_location[0]},{global_location[1]}'})
            except Exception as e:
                error_message = f"An error occurred: {str(e)}"
                return render(request, 'app_main_content/map.html', context={'error_message': error_message})
    global_shop_info_list = []
    return render(request, 'app_main_content/map.html', context={'location_form': location_form, 'radius_form': radius_form})
