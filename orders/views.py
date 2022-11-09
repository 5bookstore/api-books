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
from users.models import User
import ipdb
from correios_utils import (
    Cotacao,
    FormatoEncomenda,
    SimNao,
    Servico,
    realizar_cotacao,
    get_descricao_servico,
)


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
        # ipdb.set_trace()
        # print("1" * 1)
        totalValue = 0
        ammount = 0
        listOrders = []
        user = User.objects.get(id=request.user.id)
        address = model_to_dict(user.address)
        for elem in request.data:
            object_book = get_object_or_404(Book, id=elem["books"])
            frete = realizar_cotacao(
                cep_origem="70002900",
                cep_destino=address["zip_code"],
                codigos_servicos=[Servico.PAC, Servico.SEDEX, Servico.SEDEX_10],
                peso=object_book.weigth,
                comprimento=object_book.width,
                altura=object_book.length,
                largura=object_book.width,
                diametro=object_book.diameter,
                formato_encomenda=FormatoEncomenda.CAIXA_PACOTE,
                valor_declarado=object_book.price,
                mao_propria=SimNao.NAO,
                aviso_recebimento=SimNao.NAO,
                codigo_empresa="08082650",
                senha_empresa="564321",
            )
            totalValue += object_book.price * elem["ammount_items"]
            ammount = elem["ammount_items"]
            data = {
                "user":request.user,
                "shipping":frete[0].valor,
                "ammount_items":ammount,
                "total_value":totalValue
            }
            create = Order.objects.create(**data)
            create.books.add(object_book)
            listOrders.append(model_to_dict(create))
        print(frete)
        return Response(
            listOrders, status=status.HTTP_201_CREATED
        )
