import requests

YELP_API_KEY = "KmvuLdkyn5bCO0zgkcKd30IHzFy-mKkMbuDcgwMh7kRmTvR0ZHbE4Ic6UPKa3D9Ne-hnFLlNexD3Rvzw4Q_s5OXXhhwsmBPMazAPf-KS3k59NEuRbR2U-rr6iZZeZ3Yx"
YELP_URL = "https://api.yelp.com/v3/businesses/search"

def get_village_info(params):
    headers = {
        "Authorization": f"Bearer {YELP_API_KEY}"
    }
    
    response = requests.get(YELP_URL, headers=headers, params=params)
    data = response.json()
    village_info = data["businesses"][0]
    return {
        "name": village_info["name"],
        "address": village_info["location"]["address1"],
        "open_times": village_info.get("hours", [{}])[0].get("open", []),
        "menu_items": village_info.get("categories", []),
        "prices": village_info.get("price", "N/A")
    }

def get_top5_rated_restaurants(params,village_menu_items):
    headers = {
        "Authorization": f"Bearer {YELP_API_KEY}"
    }
    response = requests.get(YELP_URL, headers=headers, params=params)
    restaurants = response.json()
    restaurants = restaurants["businesses"]
    top_rated_restaurants = []
    for restaurant in restaurants:
        menu_items = restaurant.get("categories", [])
        if any(item in village_menu_items for item in menu_items):
            top_rated_restaurants.append({
                "name": restaurant["name"],
                "address": restaurant["location"]["address1"],
                "menu_items": menu_items,
                "prices": restaurant.get("price", "N/A")
            })
    return top_rated_restaurants

def display_info(village_info, top_rated_restaurants):
    print(f"Village Info:\nName: {village_info['name']}\nAddress: {village_info['address']}\nOpen Times: {village_info['open_times']}\nMenu Items: {village_info['menu_items']}\nPrices: {village_info['prices']}\n")
    j=0
    for i, restaurant in enumerate(top_rated_restaurants, 1):
        if(village_info['name']==restaurant['name']):
            continue
        if j==5:
            break
        print(f"Restaurant {i-1} Info:\nName: {restaurant['name']}\nAddress: {restaurant['address']}\nMenu Items: {restaurant['menu_items']}\nPrices: {restaurant['prices']}\n")
        j+=1

if __name__ == "__main__":
    
    #hard coded values
    params = {
        "term": "village the soul of india",
        "location": "Hicksville,NY,usa", 
    }
    village_info = get_village_info(params)
    params1 = {
        "location": "Hicksville,NY,usa",  
        "radius": 2000,
        "sort_by": "rating",
        "limit": 50
    }
    top_rated_restaurants = get_top5_rated_restaurants(params1,village_info["menu_items"])
    display_info(village_info, top_rated_restaurants)