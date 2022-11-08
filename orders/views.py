from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from rest_framework.authentication import TokenAuthentication
from .permissions import isUserOrAdmin
from django.shortcuts import get_object_or_404
from books.models import Book
from rest_framework import status
from django.forms.models import model_to_dict
from rest_framework.response import Response
from pycorreios.pycorreios import Correios
import ipdb
from users.models import User


class OrderListAndCreateViews(generics.ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [isUserOrAdmin]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    """
        FAZER GET DE QUERYSET - FILTRAGEM POR USUARIO 
    def get_queryset(self):
        return super().get_queryset()
    """
    def create(self, request, *args, **kwargs):
        ipdb.set_trace()
        totalValue = 0
        ammount = 0
        listOrders = []
        user = User.objects.get(id=request.user.id)
        fields = {
          "cod": Correios.PAC, 
          "GOCEP": "02912000",
          "HERECEP": user.address.zip_code,
          "peso": "1",
          "formato": "1", # caixa/pacote
          "comprimento": "18",
          "altura": "9",
          "largura": "13.5",
          "diametro": "0"
          }
        test = Correios.frete(Correios.PAC,"02912000",user.address.zip_code,1,1,18,9,13.5,0,1)
        if test['Erro'] != '0':
            print ('Deu erro! :(')
            print (test['Erro'])
            print (test['MsgErro'])
        else:
            print("Valor: R$%s\nPrazo de Entrega: %s" % (test['Valor'],test['PrazoEntrega']))

        for elem in request.data:
            object_book = get_object_or_404(Book, id=elem["books"])
            totalValue += object_book.price * elem["ammount_items"]
            ammount = elem["ammount_items"]
            data = {
                "user":request.user,
                "shipping":4,
                "ammount_items":ammount,
                "total_value":totalValue
            }
            create = Order.objects.create(**data)
            create.books.add(object_book)
            listOrders.append(model_to_dict(create))
        return Response(
            listOrders, status=status.HTTP_201_CREATED
        )
