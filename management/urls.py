from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_emp, name="show_all"),
    path('new', views.new_emp, name="new_emp"),
    path('edit/<int:id>', views.update_emp, name="update_emp"),
    path('update/<int:id>', views.updates, name="updates"),
    path('delete/<int:id>', views.deletemp, name="deletemp"),
]
