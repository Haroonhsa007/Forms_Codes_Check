from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='harvest-home'),
    path('about/', views.about, name='harvest-about'),
    path('people/', views.people, name='harvest-people'),
    path('add_person', views.add_person, name='harvest-add_person'),
    path('edit_person/<person_id>', views.edit_person, name='harvest-edit_person'),
]
