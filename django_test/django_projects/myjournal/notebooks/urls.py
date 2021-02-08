from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notebk_list/', views.NotebkListView.as_view(), name='notebk_list'),
    path('notebook/<int:pk>', views.NotebkDetailView.as_view(), name='notebook-detail'),
    path('pages/', views.PageListView.as_view(), name='pages'),
    path('page/<int:pk>', views.PageDetailView.as_view(), name='page-detail'),
]