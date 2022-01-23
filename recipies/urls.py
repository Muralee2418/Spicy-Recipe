from django.urls import path
from . import views

urlpatterns=[path("",views.recipies_index,name="recipies_index"),
path("home",views.recipies_index,name="recipies_index"),
path("create",views.create_recipies, name="create_recipies"),
path("myrecipies",views.my_recipies, name="my_recipies"),
path("edit",views.edit_recipies, name="edit_recipies"),
path("update",views.update_recipies, name="update_recipies"),
path("delete",views.delete_recipies, name="delete_recipies"),
path("<int:pk>/",views.recipie_details,name="recipie_details"),
path("likerecipies/<int:pk>",views.likerecipie,name="likerecipies"),
path("likedrecipies/",views.likerecipie,name="likedrecipies"),
]