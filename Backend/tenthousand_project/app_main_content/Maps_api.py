import googlemaps


class ShopFinder:
    def __init__(self, api_key):
        self.api = googlemaps.Client(key=api_key)

    def get_user_location(self):
        try:
            user_location = self.api.geolocate()
            return user_location
        except Exception as e:
            print(f"error getting user location: {str(e)}")
            return None
    
    def find_shop_nearby(self, location, radius, keyword='cafe'):
        try:
            geocode_result = self.api.geocode(location)
            if geocode_result:
                location = [geocode_result[0]['geometry']['location']['lat'], geocode_result[0]['geometry']['location']['lng']]
            places = self.api.places_nearby(location=location, radius=radius, keyword=keyword)
            return places['results']
        except Exception as e:
            print(f"error finding shop nearby: {str(e)}")
            return []
    
    def get_distance_info(self, origin, destination):
        try:
            distance_info = self.api.distance_matrix(origins=origin, destinations=destination)
            return distance_info
        except Exception as e:
            print(f"error getting distance information: {str(e)}")
            return None
    
    def print_shop_info(self, result, user_location):
        list = []
        for i, shop in enumerate(result):
            name_place = shop['name']
            place_location = shop['vicinity']
            rate = shop.get('rating', 'N/A')
            rating_total = shop.get('user_ratings_total', 'N/A')
            type_ = ', '.join(shop['types'])
            geo_locate_lat = shop['geometry']['location']['lat']
            geo_locate_lng = shop['geometry']['location']['lng']
            destination_locate = f"{geo_locate_lat},{geo_locate_lng}"
            distance_info = self.get_distance_info(user_location, destination_locate)

            shop_data = {
                'name': name_place,
                'location': place_location,
                'rating': rate,
                'type': type_,
                'rating_total': rating_total,
                'geo_locate_lat': geo_locate_lat,
                'geo_locate_lng': geo_locate_lng,
            }

            if distance_info and 'distance' in distance_info['rows'][0]['elements'][0]:
                shop_data['distance'] = float(distance_info['rows'][0]['elements'][0]['distance']['text'].replace(' km', ''))
                shop_data['time'] = distance_info['rows'][0]['elements'][0]['duration']['text']

            list.append(shop_data)

        list.append({'total' : i+1})
        return list
        


# shop_finder = ShopFinder(api_key)
    
# user_location = shop_finder.get_user_location()
    
# if user_location:
#     if user_location['accuracy'] > 4000:
#         location = input("กรอกที่อยู่: ")
#     else:
#         location = f"{user_location['location']['lat']},{user_location['location']['lng']}"
#     shops_nearby = shop_finder.find_shop_nearby(location)
#     x = shop_finder.print_shop_info(shops_nearby, location)
        
