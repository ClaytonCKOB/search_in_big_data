from django.urls import path

from . import views, ajax

urlpatterns = [
    path('', views.index, name="index"),
    path('loadfiles', ajax.loadFiles, name="files"),
    path('playerSearch', ajax.playerSearch, name="ajax"),
    path('userSearch', ajax.userSearch, name="ajax"),
    path('tagsSearch', ajax.tagsSearch, name="ajax"),
    path('topSearch', ajax.topSearch, name="ajax")
]