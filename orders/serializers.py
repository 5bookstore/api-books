from rest_framework import serializers

from orders.models import Order
from books.models import Book
from users.serializers import UserSerializer
from books.serializers import BookSerializer
import ipdb
from correios_utils import (
    Cotacao,
    FormatoEncomenda,
    SimNao,
    Servico,
    realizar_cotacao,
    get_descricao_servico,
)
from django.shortcuts import get_object_or_404
from books.models import Book

class OrderSerializer(serializers.ModelSerializer):

    books = serializers.UUIDField()
    frete_value = serializers.SerializerMethodField(method_name="frete")
    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "books",
            "shipping",
            "ammount_items",
            "total_value",
            "user",
            "frete_value"
        ]

        read_only_fields = [
            "status",
            "shipping",
            "total_value",
            "user",
        ]

    def frete(self,obj):
        return obj.frete_value()
    
    def create(self, validated_data):
        totalValue = 0
        ammount = 0
        user = UserSerializer(self.context["user"])
        zipCode = user.data["address"]["zip_code"]
        book = validated_data["books"]
        print(book.length)
        frete = realizar_cotacao(
            cep_origem= "70002900",
            cep_destino= zipCode,
            codigos_servicos= [Servico.PAC, Servico.SEDEX, Servico.SEDEX_10],
            peso= book.weigth,
            comprimento= book.width,
            altura= book.length,
            largura= book.width,
            diametro= book.diameter,
            formato_encomenda= FormatoEncomenda.CAIXA_PACOTE,
            valor_declarado= book.price,
            mao_propria= SimNao.NAO,
            aviso_recebimento= SimNao.NAO,
            codigo_empresa= "08082650",
            senha_empresa= "564321",
            )
        totalValue += book.price * validated_data["ammount_items"]
        ammount = validated_data["ammount_items"]
        data = {
            "user":self.context["user"],
            "shipping":frete[0].valor,
            "ammount_items":ammount,
            "total_value":totalValue
            }
        create = Order.objects.create(**data)
        create.books.add(book)
        return create