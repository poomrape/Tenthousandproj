from django.shortcuts import render, redirect
from .Maps_api import ShopFinder
from .api import api_key
from .forms import LocationForm, RadiusForm

# Create your views here.
shop_finder = ShopFinder(api_key)
user_location = shop_finder.get_user_location()

def maps(request):
    location_form = LocationForm()
    radius_form = RadiusForm()

    if request.method == 'POST':
        location_form = LocationForm(request.POST)
        radius_form = RadiusForm(request.POST)

        if location_form.is_valid():
            location = location_form.cleaned_data['location']
            if not location:
                location = f"{user_location['location']['lat']},{user_location['location']['lng']}"

        if radius_form.is_valid():
            radius = radius_form.cleaned_data['radius']
            if not radius:
                radius = 4000

            try:
                shops_nearby = shop_finder.find_shop_nearby(location, radius)
                shop_info_list = shop_finder.print_shop_info(shops_nearby, location)
                sort_by = request.GET.get('sort_by', 'distance')
                if sort_by == 'distance':
                    shop_info_list.sort(key=lambda x: x.get('distance', float('inf')))

                return render(request, 'app_main_content/map.html', context={'shop_result': shop_info_list, 'sort_by': sort_by})
            except Exception as e:
                error_message = f"An error occurred: {str(e)}"
                return render(request, 'app_main_content/map.html', context={'error_message': error_message})

    return render(request, 'app_main_content/map.html', context={'location_form': location_form, 'radius_form': radius_form})

