from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.patient_list,
        name='list'
    ),

    path(
        'add/',
        views.add_patient,
        name='add'
    ),

    path(

    'update/<int:id>/',

    views.update_patient,

    name='update'

    ),

    path(

    'delete/<int:id>/',

    views.delete_patient,

    name='delete'

    ),
]