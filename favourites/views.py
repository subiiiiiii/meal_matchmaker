from django.http import JsonResponse
from .models import Favourite
from django.template.loader import render_to_string
from meal_matcher.utils import is_ajax
from django.shortcuts import redirect



def likes(request):
    recipe = Favourite.objects.filter(recipe_id=request.POST.get('recipe_id'), user=request.user)
    is_liked = False
    if recipe.exists():
        recipe.delete()
        is_liked = False
    else:
        recipe = Favourite.objects.create(recipe_id=request.POST.get('recipe_id'), user=request.user)
        is_liked = True
    context ={
        'is_liked': is_liked,
        'rep_id': request.POST.get('recipe_id')
    }
    if is_ajax(request=request):
        html = render_to_string('recipe/like_section.html', context, request=request)
        return JsonResponse({'like': html, 'rep_id': request.POST.get('recipe_id')})   

def delete_likes(request):
    recipe = Favourite.objects.get(recipe_id=request.GET.get('recipe_id'), user=request.user)
    recipe.delete()
    return redirect('/')