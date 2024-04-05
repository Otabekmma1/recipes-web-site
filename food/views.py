from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category, Recipes

# Create your views here.


def all_recipes(request):
    recipes = Recipes.objects.filter(published=True)
    # recip = Recipes.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    context = {
        'title': "Barcha Retseptlar",
        'recipes': recipes,
        'categories': categories,
        # 'recip': recip
    }
    return render(request, 'food/index.html', context)

def recipe_detail(request, id):
    recipe = Recipes.objects.get(id=id)
    return render(request, 'food/detail.html', { 'recipe': recipe})

def by_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    recipes = Recipes.objects.filter(category=category)
    return render(request, 'food/index.html', {'category': category, 'recipes': recipes})
def add_Recept(request):
    recipes = Recipes.objects.filter(published=True)
    categories = Category.objects.all()

    if request.method=="POST":
        name = request.POST.get('name')
        content = request.POST.get('content')
        category =request.POST.get('category')
        photo  = request.POST.get('photo')
        category_instance = Category.objects.get(name=category)
        query=Recipes(name=name, content=content, category=category_instance, photo=photo)
        query.save()
        messages.info(request,"Retsept muvaffaqiyatli qo'shildi")
        return redirect("/insert")
    ctx = {
        'recipes': recipes,
        'categories': categories,
    }
    return render(request,"crud/add.html", context=ctx)


def updateRecept(request,id):
    categories = Category.objects.all()
    if request.method=="POST":
        name = request.POST.get('name')
        content = request.POST.get('content')
        category = request.POST.get('category')
        photo = request.POST.get('photo')
        category_instance = Category.objects.get(name=category)

        edit= Recipes.objects.get(id=id)
        edit.name=name
        edit.content=content
        edit.category=category_instance
        edit.photo=photo
        edit.save()
        messages.warning(request,"Retsept muvaffaqiyatli o'zgartirildi")
        return redirect("/insert")
    recip =Recipes.objects.get(id=id)
    context={
        'recip': recip,
        'categories': categories,
    }
    return render(request,"crud/edit.html",context)

def deleteRecept(request,id):
    recipes =Recipes.objects.get(id=id)
    recipes.delete()
    messages.error(request,"Retsept o'chirildi")
    return redirect("/insert")
