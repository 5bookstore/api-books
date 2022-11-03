from django.db import models
import uuid

class Status_Order(models.TextChoices):
    ORDER_CREATED = 'Order created'
    PROCESS_PAYMENT = 'Process payment'
    AUTHORIZED_PAYMENT = 'Authorized payment'
    WAITING_SHIPPING = 'Waiting Shipping'
    SENT = "Sent"
    ORDER_COMPLETED = "Order completed"
class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    status = models.CharField(choices=Status_Order.choices, default=Status_Order.ORDER_CREATED) 
    shipping = models.IntegerField(null=False)
    ammount_items = models.IntegerField(null=False)
    total_value = models.IntegerField(null=False)
