from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category, Recipes, UserProfile, Comments
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import User


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
def recipe_detail(request, recipe_id):
    recipe = Recipes.objects.get(id=recipe_id)
    comments = Comments.objects.filter(recipe=recipe)
    #comments
    if request.method == 'POST':
        author = request.POST.get('author')
        text = request.POST.get('text')
        if all([author, text]):
            Comments.objects.create(
                author=author,
                text=text,
                recipe=recipe
            )
        messages.success(request, f"Izoh muvaffaqiyatli qo'shildi!")

    recipe.views += 1
    recipe.save()
    ctx = {
        'recipe': recipe,
        'comments': comments,
    }

    return render(request, 'food/detail.html', ctx)




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
    return render(request, 'user/login_form.html', context=ctx)


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
    return render(request, 'user/reg_form.html', ctx)


@login_required(login_url='login')
def user_profile(request):
    username = request.user.username
    user = User.objects.get(username=username)
    recipes = Recipes.objects.filter(author=user)
    ctx = {
        'user': user,
        'recipes': recipes
    }

    try:
        user_profile = UserProfile.objects.get(user=user)
        ctx['user_profile'] = user_profile
    except:
        pass

    return render(request, 'user/profile.html', context=ctx)


@login_required(login_url='login')
def update_profile(request):
    # id = request.user.id
    # current_user = UserProfile.objects.get(id=id)
    # form = UpdateProfileForm(instance=current_user)
    # if request.method == 'POST':
    #     form = UpdateProfileForm(request.POST or None, instance=current_user)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('profile')
    # ctx = {
    #     'form': form,
    # }
    # return render(request, 'user/update_profile.html', context=ctx)

    req = request.POST
    id = request.user.id
    if request.method == "POST":
        first_name = req.get('first_name')
        last_name = req.get('last_name')
        email = req.get('email')
        status = req.get('status')
        addres = req.get('addres')
        phone = req.get('phone')
        chrome = req.get('chrome')
        instagram = req.get('instagram')
        facebook = req.get('facebook')
        photo = req.get('photo')

        edit = UserProfile.objects.get(id=id)
        req_edit = User.objects.get(username=request.user.username)
        req_edit.first_name = first_name
        req_edit.last_name = last_name
        req_edit.email = email
        req_edit.save()
        edit.status = status
        edit.addres = addres
        edit.phone = phone
        edit.chrome = chrome
        edit.instagram = instagram
        edit.facebook = facebook
        edit.photo = photo

        edit.save()
        messages.warning(request, "Sahifa muvaffaqiyatli o'zgartirildi")
        return redirect("/profile")

    id = request.user.id
    username = request.user.username
    current_user = UserProfile.objects.get(id=id)
    user = User.objects.get(username=username)

    context = {
        'current_user': current_user,
        'user': user,
    }
    return render(request, "user/update_profile.html", context)
