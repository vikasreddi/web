from django.urls import path

from . import views
app_name='mic'

urlpatterns = [
    #/mic
    path('', views.Indexview.as_view(),name='index'),
    # login
    path('reg/', views.Userformview.as_view(),name='register'),
    #/mic/71
    path('<pk>/',views.Detailview.as_view(),name="detail"),
    #mic/album/add
    path('album/add/',views.Albumcreate.as_view(),name="album-add"),
    #/mic/song
     path('/song/', views.songview.as_view(),name='songdetail'),
    #mic/album
    path('/album/', views.albumview.as_view(),name='albumdetail'),

]