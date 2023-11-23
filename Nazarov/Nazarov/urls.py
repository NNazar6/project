
from django.contrib import admin
from django.urls import path
from Nazarov_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('full_name/', views.full_name, kwargs={'name': 'Nazarov Nazar Michailovich', 'age': 5, 'interesting': 'python'}),
    path('about/', views.about, kwargs={'from_town': 'Dzerginsk','grade': 'Otlichno', 'school': 'loved shool!!!'}),
    path('contacts/', views.contacts, kwargs={'contacts': 89524606381}),
]
