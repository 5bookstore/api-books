import ipdb
from users.serializers import UserSerializer
from books.serializers import BookSerializer
from books.models import Book

from correios_utils import (
    Cotacao,
    FormatoEncomenda,
    SimNao,
    Servico,
    realizar_cotacao,
    get_descricao_servico,
)
from django.shortcuts import get_object_or_404


def frete(*args, **kwargs):
    totalValue = 0
    ammount = 0
    # user = UserSerializer(self.context["user"])
    zipCode = kwargs['user'].address.zip_code
    book = get_object_or_404(Book, id=kwargs['data']['books'])
    ipdb.set_trace()

    frete = realizar_cotacao(
        cep_origem="70002900",
        cep_destino=zipCode,
        codigos_servicos=[Servico.PAC, Servico.SEDEX, Servico.SEDEX_10],
        peso=book.weigth,
        comprimento=book.width,
        altura=book.length,
        largura=book.width,
        diametro=book.diameter,
        formato_encomenda=FormatoEncomenda.CAIXA_PACOTE,
        valor_declarado=book.price,
        mao_propria=SimNao.NAO,
        aviso_recebimento=SimNao.NAO,
        codigo_empresa="08082650",
        senha_empresa="564321",
    )

    # totalValue += book.price * validated_data["ammount_items"]
    # ammount = validated_data["ammount_items"]
    # data = {
    #     "user": self.context["user"],
    #     "shipping": frete[0].valor,
    #     "ammount_items": ammount,
    #     "total_value": totalValue
    # }
    create = Order.objects.create(**data)
    create.books.add(book)
    return create
