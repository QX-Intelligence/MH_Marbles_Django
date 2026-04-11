from django.urls import path
from . import views


urlpatterns = [

    path("", views.get_collections),

    path("<int:collection_id>/", views.get_collection),

    path("create/", views.create_collection),

    path("update/<int:collection_id>/", views.update_collection),

    path("delete/<int:collection_id>/", views.delete_collection),

]