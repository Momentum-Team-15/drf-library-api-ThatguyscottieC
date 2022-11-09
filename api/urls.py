from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Libary import views

urlpatterns = [
    path('Libary/', views.LibaryList.as_view()),
    path('Libary/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
