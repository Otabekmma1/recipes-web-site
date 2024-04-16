from django.urls import path
from .views import (all_recipes, add_Recept, updateRecept, deleteRecept,
                    recipe_detail, by_category, user_login, user_logout,
                    user_register, user_profile, update_profile)


urlpatterns = [
    path('', all_recipes, name='index'),
    path('detail/<recipe_id>/', recipe_detail, name='detail'),
    path('category/<category_id>/', by_category, name='category'),
    # ----------------crud--------------------------
    path('insert/', add_Recept, name="create"),
    path('update/<id>/', updateRecept, name="update"),
    path('delete/<id>/', deleteRecept, name="delete"),
    #------------- login ---------------------------
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
    #----------------user profile -------------------
    path('profile/', user_profile, name='profile'),
    path('update_profile/', update_profile, name='update_profile'),
]
