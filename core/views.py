from django.shortcuts import render
from django.shortcuts import render
import requests
from favourites.models import Favourite
import re
import random


def home(request):
    # context = {
    #     'variable1': value1,
    #     'variable2': value2,
    #     # Add more variables as needed
    # }
    return render(request, 'home/index.html')


def generate_recipe(request):
	if request.method == 'GET' and 'ingredients' in request.GET:
		ingredients = request.GET.get('ingredients')
		url = "https://api.spoonacular.com/recipes/findByIngredients/"
		params = {
			"apiKey": "3fec000573ee4f46ac617d23060ad34b",
			"ingredients": ingredients
		}
		response = requests.get(url, params=params)
		if response.status_code == 200:
			data = response.json()
			if request.user.is_authenticated:
				user_favorites = Favourite.objects.filter(user=request.user).values_list('recipe_id', flat=True)
			else:
				user_favorites = []
			context = {
				'recipes_list':data,
				'user_favorites':user_favorites,
				'ingredients':ingredients
			} 
			
			return render(request, 'recipe/recipes_list.html', context)
		else:
			print(response.status_code)
			return render(request, 'home/index.html')
		

def recipe_detail(request, pk):
	url = "https://api.spoonacular.com/recipes/"+str(pk)+"/information/"
	params = {
		"apiKey": "3fec000573ee4f46ac617d23060ad34b"
	}
	response = requests.get(url, params=params)

	sentences = re.split(r'(?<=[.!?])\s+', response.json()['summary'])
	description = sentences[:3]

	n = random.randint(100,350) 
	
	context = {
		'recipes':response.json(),
		'description':description,
		'calorie': n,
	}
	return render(request, 'recipe/recipe_detail.html',context)


def recommended_recipe(request):
	fav = Favourite.objects.filter(user=request.user)
	if fav.count() > 0:
		ingredient_names = []
		for f in fav:
			url_recipe = "https://api.spoonacular.com/recipes/"+str(f.recipe_id)+"/information/"
			params_recipe = {
			"apiKey": "3fec000573ee4f46ac617d23060ad34b"
			}
			response = requests.get(url_recipe, params=params_recipe)
			recipe_data = response.json()
			extended_ingredients = recipe_data.get("extendedIngredients", [])
			for ingredient in extended_ingredients:
				ingredient_name = ingredient["nameClean"]
				ingredient_names.append(ingredient_name)

		ingredient_names = [name for name in ingredient_names if isinstance(name, str) and name.strip()]
		ingredient_names_set = set(ingredient_names)
		ingredient_names_list = list(ingredient_names_set)

		ingredient_names_str = ", ".join(ingredient_names_list)

		url = "https://api.spoonacular.com/recipes/findByIngredients/"
		params = {
			"apiKey": "3fec000573ee4f46ac617d23060ad34b",
			"ingredients": ingredient_names_str
		}
		response = requests.get(url, params=params)
		recipe_recommended =response.json()
		if request.user.is_authenticated:
			user_favorites = Favourite.objects.filter(user=request.user).values_list('recipe_id', flat=True)
		else:
			user_favorites = []
		context = {
			'recipes_list':recipe_recommended,
			'user_favorites':user_favorites
		}
		return render(request, 'recipe/recommended_recipes.html', context)

	else:
		print("No favorites")


def get_random_recipe(request):
	url = "https://api.spoonacular.com/recipes/random/"
	params = {
		"apiKey": "3fec000573ee4f46ac617d23060ad34b"
	}
	response = requests.get(url, params=params)
	random_id = response.json()['id']


	url = "https://api.spoonacular.com/recipes/"+str(random_id)+"/similar"
	params = {
		"apiKey": "3fec000573ee4f46ac617d23060ad34b"
	}
	random_data = requests.get(url, params=params)

	data = random_data.json()

	context = {
		'recipes_list':data,
	} 
	
	return render(request, 'recipe/random_list.html', context)