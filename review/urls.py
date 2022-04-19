from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
    # path('watch_list/', watch_list),
    # path('add_watchlist/', add_watchlist),
]