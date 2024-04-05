from django.urls import path
from .views import all_recipes, add_Recept, updateRecept, deleteRecept, recipe_detail, by_category

urlpatterns = [
    path('', all_recipes, name='index'),
    path('detail/<id>/', recipe_detail, name='detail'),
    path('category/<category_id>/', by_category, name='category'),
    # crud
    path('insert/', add_Recept, name="create"),
    path('update/<id>/', updateRecept, name="update"),
    path('delete/<id>/', deleteRecept, name="delete"),
]
