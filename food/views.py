from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category, Recipes
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import login, logout



#Barcha retseptlar
def all_recipes(request):
    recipes = Recipes.objects.filter(published=True)
    categories = Category.objects.all()
    context = {
        'title': "Barcha Retseptlar",
        'recipes': recipes,
        'categories': categories,
    }
    return render(request, 'food/index.html', context)




#id orqali retsept malumotlarini olish
def recipe_detail(request, id):
    recipe = Recipes.objects.get(id=id)

    recipe.views += 1
    recipe.save()

    return render(request, 'food/detail.html', { 'recipe': recipe})



# kategoriya orqali retseptni olish
def by_category(request, category_id):
    categories = Category.objects.all()
    recipes = Recipes.objects.filter(category_id=category_id)
    return render(request, 'food/index.html', {'categories': categories, 'recipes': recipes})



#-------------- crud -------------------------
def add_Recept(request):
    recipes = Recipes.objects.filter(published=True)
    categories = Category.objects.all()
    req = request.POST
    if request.method=="POST":
        name = req.get('name')
        content = req.get('content')
        category = req.get('category')
        photo  = req.get('photo')
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
    req = request.POST
    if request.method=="POST":
        name = req.get('name')
        content = req.get('content')
        category = req.get('category')
        photo = req.get('photo')
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

#----------------- end crud -----------------------


#------------ login and register ----------------------

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Saytga xush kelibsiz! {user.username}")
            return redirect('index')
        if form.errors:
            messages.error(request, "Taxallus yoki parol xato!")
    ctx = {
        'title': 'Kirish'
    }
    return render(request, 'reg_and_login/login_form.html', context=ctx)


def user_logout(request):
    logout(request)
    messages.warning(request, "Siz saytdan chiqdingiz!")
    return redirect('index')

def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz !!!")
            return redirect('login')
        if form.errors:
            messages.warning(request, "Xatolik! Iltimos, ma'lumotlaringizni qaytadan kiriting.")
    else:
        form = RegistrationForm()
    ctx = {
        'form': form,
        'title': "Ro'yxatdan o'tish"
    }
    return render(request, 'reg_and_login/reg_form.html', ctx)

