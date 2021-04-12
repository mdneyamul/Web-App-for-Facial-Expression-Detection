from django.urls import path
from .import views

urlpatterns = [
    path("",views.upload_img, name="UploadImage"),
    path('success', views.success, name = 'success'),
    path('cc/',views.cc, name = 'CC'),
    path('show/',views.display,name = 'show'),
    path('contact/',views.contact,name = 'contact')


]