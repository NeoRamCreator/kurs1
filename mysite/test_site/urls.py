from django.urls import path, include
from .views import *

urlpatterns = [
    path('test1/', test1, name='test1'),
    path('test2/', test2, name='test2'),
    # path('', index, name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),

    path('', HomeNews.as_view(), name='home'),



    path('t1/', def_view_test_index1, name='home_t1'),
    # path('category_test1/<int:category_id>/', get_category_test1, name='category_t1'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    # path('news/add-news/', add_news, name='add_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
]
