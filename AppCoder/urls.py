from django.urls.conf import path
from .views import index, lista_futbolistas, lista_basquetbolistas, lista_tenistas, crear_futbolista, crear_basquetbolista, crear_tenista, contacto

urlpatterns = [
    path('', index, name='index'),
    path('futbolistas/', lista_futbolistas, name='Futbolistas'),
    path('futbolistas/crear/', crear_futbolista, name='Crear_Futbolista'),
    path('basquetbolistas/', lista_basquetbolistas, name='Basquetbolistas'),
    path('basquetbolistas/crear', crear_basquetbolista, name='Crear_Basquetbolista'),
    path('tenistas/', lista_tenistas, name='Tenistas'),
    path('tenistas/crear', crear_tenista, name='Crear_Tenista'),
    path('contacto/', contacto, name='Contacto'),
    
]