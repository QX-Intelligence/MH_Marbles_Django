from django.urls import path
from . import views


urlpatterns = [

    path("", views.get_products),

    path("<int:product_id>/", views.get_product),

    path("create/", views.create_product),

    path("update/<int:product_id>/", views.update_product),

    path("delete/<int:product_id>/", views.delete_product),

]