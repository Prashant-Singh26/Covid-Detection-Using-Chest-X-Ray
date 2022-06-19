from django.contrib import admin
from django.urls import path, include
from more_itertools import ichunked

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]