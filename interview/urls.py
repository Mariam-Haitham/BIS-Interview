from django.contrib import admin
from django.urls import path

from item import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('items/list/', views.list, name = "item-list"),
]
