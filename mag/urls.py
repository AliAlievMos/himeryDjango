from django.urls import path

from .views import index, index_for_last, material_page, index_for_click, search, search_result

urlpatterns = [
    path('', index, name='index'),
    path('mat/<int:material_id>/', material_page, name='material_page'),
    path('maglast/', index_for_last, name='index_for_last'),
    path('maglast/<int:mag_id>/', index_for_click, name='index_for_click'),
    path('search/res/', search_result, name='search_result'),
    path('search/', search,name='search'),
]
