from django.urls import path
from django.views.decorators.cache import cache_page
from . import views


app_name = 'blog'

urlpatterns = [
    path('comment/<int:pk>/', views.CreateComment.as_view(), name='create_comment'),
    path('', views.HomeView.as_view(), name='home'),
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list'),
    path('<slug:slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_single'),
    # path('', cache_page(60 * 15)(views.HomeView.as_view()), name='home')

]