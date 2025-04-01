from django.urls import path
from .views import index_view, detail_view, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('todos/<str:id>/', detail_view, name='detail-view')
]