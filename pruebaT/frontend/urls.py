from django.urls import path

from . import views

urlpatterns = [
    #CRUD Productos
    path('Productos/createproduct',views.createProduct,name='crearproducto'),
    path('Productos/listproducts',views.listProducts,name='listarproductos'),
    path('Productos/deleteproductlist/<int:idProducto>',views.deleteProductList,name='eliminarproductolista'),
    path('Productos/deletecreatedproduct/<int:idProducto>',views.deleteCreatedProduct,name='eliminarproductocreado'),
    #Detalles Productos
    path('Productos/searchproductdetail/<int:idProducto>',views.searchProductDetail,name='buscardetalle'),
    path('DetallesProducto/createprductdetail',views.createDetalleProducto,name='creardetalle'),
]