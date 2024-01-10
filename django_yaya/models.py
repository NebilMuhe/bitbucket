from django.db import models
from uuid import uuid4

# Create your models here.


class YayaWallet(models.Model):
    PENDING = 'P'
    SUCCESS = 'S'
    FAILED = 'F'
    STATUS_OPTIONS = [
        (PENDING, 'Pending'),
        (SUCCESS, 'Success'),
        (FAILED, 'Failed'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid4)
    amount = models.FloatField()
    currency = models.CharField(max_length=5, default='ETB')
    created_at = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField()
    cause = models.CharField(max_length=255, default='Testing')
    full_name = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)
    invoice_url = models.URLField()
    # status = models.CharField(max_length=50, choices=STATUS_OPTIONS)

    def __str__(self):
        return f"{self.full_name} {self.amount}"
