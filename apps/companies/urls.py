from django.urls import path
from . import views


urlpatterns = [

    path("", views.get_companies),

    path("create/", views.create_company),

    path("update/<int:company_id>/", views.update_company),

    path("delete/<int:company_id>/", views.delete_company),

]