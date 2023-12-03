from django.urls import path
from catalog.views import *
app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view()),
    path('blog/', BlogListView.as_view()),
    path('blog_create/', BlogCreateView.as_view()),
    path('blog_update/<int:pk>/', BlogUpdateView.as_view()),
    path('blog_delete/<int:pk>/', BlogDeleteView.as_view()),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('contacts/', contacts),
    path('products/<int:pk>/', ProductDetailView.as_view()),
]
