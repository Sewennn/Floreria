from django.shortcuts import render, redirect
from .models import *
import os
from django.conf import settings

# Create your views here.
def cargarInicio(request):
    return render(request,"inicio.html")

def cargarTienda(request):
    productos = Producto.objects.all()
    return render(request,"tienda.html",{"producto":productos})

def cargarJardineria(request):
    productos = Producto.objects.all()
    cate_producto_jardineria = Producto.objects.filter(categoriaId = 1)
    return render(request,"tienda_jardineria.html",{"producto":productos,"cate_jardineria": cate_producto_jardineria})

def cargarPlanta(request):
    productos = Producto.objects.all()
    cate_producto_planta = Producto.objects.filter(categoriaId = 3)
    return render(request,"tienda_planta.html",{"producto":productos,"cate_planta": cate_producto_planta})

def cargarSemilla(request):
    productos = Producto.objects.all()
    cate_producto_semilla = Producto.objects.filter(categoriaId = 2)
    return render(request,"tienda_semilla.html",{"producto":productos,"cate_semilla": cate_producto_semilla})


def cargarLogin(request):
    return render(request,"login.html")

def cargarRegistro(request):
    return render(request,"registro.html")

def agregarProducto(request):
    #print("AGREGAR PRODUCTOS", request.POST)

    v_categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoria'])

    v_sku = request.POST['txtSku']
    v_nombre = request.POST['txtnombre']
    v_precio = request.POST['txtprecio']
    v_stock = request.POST['txtStock']
    v_descripcion = request.POST['txtDescripcion']
    v_imagen = request.FILES['txtImagen']

    Producto.objects.create(sku = v_sku, nombre = v_nombre, precio = v_precio,stock = v_stock, descripcion = v_descripcion, imagenUrl=v_imagen,categoriaId = v_categoria)
    
    return redirect('/agregarProducto')

def agregarUsuario(request):
    v_nombre = request.POST['txtNombre']
    v_apellido = request.POST['txtApellido']
    v_telefono = request.POST['txtTelefono']
    v_rut = request.POST['txtRut']
    v_email = request.POST['txtEmail']
    v_contraseña = request.POST['txtContraseña']
    v_suscripcion = request.POST['booleanSuscripcion']

    

    Usuario.objects.create(rut = v_rut, nombre = v_nombre, apellido = v_apellido, telefono = v_telefono, email = v_email, contraseña = v_contraseña, suscripcion = v_suscripcion)
    return redirect('/login')


def cargarAgregarProducto(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request,"agregarProducto.html",{"cate":categorias,"prod":productos})

def cargarEditarProducto(request,sku):
    prod = Producto.objects.get(sku = sku)
    categorias = Categoria.objects.all()
    return render(request,"editarProducto.html",{"prod":prod, "cate":categorias})

def editarProducto(request):
    v_categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoria'])

    v_sku = request.POST['txtSku']
    productoBD = Producto.objects.get(sku = v_sku)
    v_nombre = request.POST['txtnombre']
    v_precio = request.POST['txtprecio']
    v_stock = request.POST['txtStock']
    v_descripcion = request.POST['txtDescripcion']


    try:
        v_imagen = request.FILES['txtImagen']
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(productoBD.imagenUrl))
        os.remove(ruta_imagen)
    except:
        v_imagen = productoBD.imagenUrl

    productoBD.nombre = v_nombre
    productoBD.precio = v_precio
    productoBD.stock = v_stock
    productoBD.descripcion = v_descripcion
    productoBD.categoriaId = v_categoria
    productoBD.imagenUrl = v_imagen
    
    productoBD.save()

    return redirect('/agregarProducto')



def eliminarProducto(request,codigo_producto):
    producto = Producto.objects.get(sku = codigo_producto)
    ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(producto.imagenUrl))
    os.remove(ruta_imagen)
    producto.delete()
    return redirect('/agregarProducto')