import googlemaps
import time

class ShopFinder:
    def __init__(self, api_key):
        self.api = googlemaps.Client(key=api_key)

    def get_user_location(self, location):
        try:
            geocode_result = self.api.geocode(location)
            if geocode_result:
                    return (geocode_result[0]['geometry']['location']['lat'], geocode_result[0]['geometry']['location']['lng'])
        except Exception as e:
            print(f"error getting user location: {str(e)}")
            return None
    
    def find_shop_nearby(self, location, radius, keyword='cafe'):
        try:
            shops = []
            next_page_token = None
            while True:
                places = self.api.places_nearby(location=location, radius=radius, keyword=keyword, page_token=next_page_token)
                shops.extend(places['results'])
                time.sleep(1.85)
                next_page_token = places.get('next_page_token')
                if next_page_token == None:
                    break
            return shops
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
    
    def get_shop_info_list(self, location, radius, keyword='cafe'):
        shops_nearby = self.find_shop_nearby(location, radius, keyword)
        shop_info_list = self.print_shop_info(shops_nearby, location)
        return shop_info_list

    def print_shop_info(self, result, user_location):
        shop_info_list = []
        i = 0
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

            shop_info_list.append(shop_data)

        shop_info_list.append({'total': i+1})
        i += 1
        return shop_info_list
        

# example list
#     shop_data = {
#                 'name': ไก่,
#                 'location': จุฬาซอย10,
#                 'rating': 5,
#                 'type': cafe,
#                 'rating_total': 2000,
#                 'geo_locate_lat': 13.000123,
#                 'geo_locate_lng': 15.000023,
#                  'distance' : 17
#                  'time' : 20
#             }
