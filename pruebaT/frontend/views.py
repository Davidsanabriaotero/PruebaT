from django.shortcuts import render, redirect, HttpResponse
import requests
from django.core.cache import cache
from Api.models import *


# Create your views here.
def createProduct(request):
    if request.method == 'POST':
        url = 'http://127.0.0.1:8000/api/Productos/'
        data = {
            'nombre': request.POST['nombre'],
            'precio': request.POST['precio'],
            'descripcion': request.POST['descripcion']
        }
        response = requests.post(url, data=data)
        if response.status_code == 201:
            return redirect('listarproductos')
    else:
        return render(request, 'views/createProducto.html')

def listProducts(request):
    url = 'http://127.0.0.1:8000/api/Productos/'
    response = requests.get(url)
    productos = response.json()
    return render(request, 'views/listProductos.html', {'data': productos})

def deleteProductList(request,idProducto):
    DProducto = DetalleProductos.objects.filter(idProducto=idProducto)
    print(DProducto)
    for i in DProducto:
        url = 'http://127.0.0.1:8000/api/DetallesProductos/{}/'.format(i.pk)
        response = requests.delete(url)
        if response.status_code == 204:
            print("Objeto eliminado con Exito")
    return redirect('listarproductos')
    

def deleteCreatedProduct(request,idProducto):
    url = 'http://127.0.0.1:8000/api/Productos/{}/'.format(idProducto)
    response = requests.delete(url)
    if response.status_code == 204:
        # Objeto eliminado con éxito
        return redirect('listarproductos')

def searchProductDetail(request,idProducto):
    url = 'http://127.0.0.1:8000/api/DetallesProductos/?producto_id='+str(idProducto)
    response = requests.get(url)
    detalleProducto = response.json()
    return render(request, 'views/detailProducto.html', {'data': detalleProducto})

def createDetalleProducto(request):
    if request.method == 'POST':
        url = 'http://127.0.0.1:8000/api/DetallesProductos/'
        data = {
            'idProducto': request.POST['idProducto'],
            'cantidad': request.POST['cantidad'],
        }
        response = requests.post(url, data=data)
        if response.status_code == 201:
            return redirect('listarproductos')
    else:
        return render(request, 'views/createDetalle.html')