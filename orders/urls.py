from django.urls import path
from views import (
    OrderListAndCreateViews,
    OrderRetriveUpdateDestroyViews
)


urlpatterns = [
    path("user/<str:book_id>/orders/", OrderListAndCreateViews.as_view()),
    path(
        "user/<str:book_id>/orders/<int:order_id>",
        OrderRetriveUpdateDestroyViews.as_view()
    ),
]
