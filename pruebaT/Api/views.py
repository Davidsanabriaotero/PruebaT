from .models import *
from .serializers import *
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action



class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductosSerializer

class DetallesProductosViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = DetallesProductosSerializer

    def get_queryset(self):
        queryset = DetalleProductos.objects.all()
        producto_id = self.request.query_params.get('producto_id')
        if producto_id:
            queryset = queryset.filter(idProducto=producto_id)
        return queryset

    @action(detail=True, methods=['post'])
    def eliminar_detalles(self, request, pk=None):
        producto = self.get_object()
        detalles = DetalleProductos.objects.filter(idProducto=producto)
        detalles.delete()
        return Response({'mensaje': f'Los detalles del producto {producto.nombre} han sido eliminados.'}, status=status.HTTP_200_OK)
"""


@api_view(['POST'])
def postBlog(request):
    data = request.data
    Blog = blog.objects.create(
        body=data['body']
    )
    serializer = BlogSerializer(Blog,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def putBlog(request,pk):
    data = request.data
    Blog = blog.objects.get(id=pk)
    serializer = BlogSerializer(instance=Blog,data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['Delete'])
def deleteBlog(request,pk):
    Blog = blog.objects.get(id=pk)
    Blog.delete()
    return Response('Blog deleted successfully')
"""