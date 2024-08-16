from django.urls import path
from . import views
urlpatterns = [
    path('display_id/<int:id>/', views.display_id),
    path('display_name/<str:name>/',views.display_name),
    path('display_sal/<str:sal>/',views.display_sal),
    path('display_roll_name/<int:roll>/<str:name>/',views.display_roll_name),
]
