from favourites.models import Favourite
import requests


def recipe_fav(request):
    if request.user.is_authenticated:
        fav = Favourite.objects.filter(user=request.user)
        recipe_array = []
        for f in fav:
            url = "https://api.spoonacular.com/recipes/"+str(f.recipe_id)+"/information/"
            params = {
                "apiKey": "3fec000573ee4f46ac617d23060ad34b"
            }
            response = requests.get(url, params=params)
            recipe_data = response.json()
            print(recipe_data)
            recipe_array.append({
                'recipe_id': recipe_data['id'],
                'recipe_name': recipe_data['title'],
                'recipe_image': recipe_data['image'],
            })
        return {'data': recipe_array}
    return {'status': False}


def liked_recipe_count(request):
    if request.user.is_authenticated:
        fav = Favourite.objects.filter(user=request.user)
        
        return {'count': fav.count}
    return {'count': 0}