from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargarInicio),
    path('tienda',views.cargarTienda),
    path('login',views.cargarLogin),
    path('registro',views.cargarRegistro),
    path('agregarProducto',views.cargarAgregarProducto),


    path('agregarProductoForm',views.agregarProducto),
    path('agregarUsuarioForm',views.agregarUsuario),

    path('editarProducto/<sku>',views.cargarEditarProducto),

    path('editarProducto',views.editarProducto),
    path('eliminarProducto/<codigo_producto>',views.eliminarProducto),
    path('jardineria',views.cargarJardineria),
    path('semilla',views.cargarSemilla),
    path('planta',views.cargarPlanta)

]