from django.urls import path

from .views import index, index_auth
from .models import Authors

urlpatterns = [
    path('', index, name='index'),
    path('author/<int:author_id>/', index_auth, name='index_auth'),

]
