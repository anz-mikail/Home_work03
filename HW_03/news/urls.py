from django.urls import path
from .views import PostList, IdPostList, AuthorList, PostSearch, PostCreate_AR, PostCreate_NW, PostUpdate, PostDelete, \
    subscriptions

urlpatterns = [
    path('news/', PostList.as_view(), name='news'),
    path('author/', AuthorList.as_view(), name='author'),
    path('<int:pk>', IdPostList.as_view(), name='new'),
    path('news/search/', PostSearch.as_view(), name='search'),
    path('news/create/', PostCreate_NW.as_view(), name='post_create_NW'),
    path('news/<int:pk>/edit/', PostUpdate.as_view(), name='post_edit_NW'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete_NW'),
    path('articles/create/', PostCreate_AR.as_view(), name='post_create_AR'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='post_edit_AR'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='post_delete_AR'),
    path('subscriptions/', subscriptions, name='subscriptions'),
   # path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
]