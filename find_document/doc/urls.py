from django.urls import path

from . import views

app_name='doc'

urlpatterns = [
    path("", view=views.index, name='index'),
    path("find/", view=views.getFindPage, name="getFindPage"),
    path('view-pdf/<str:file_name>', views.pdf_view, name='pdf_view'),
]

