from django.db import models
from django.conf import settings
#
from applications.producto.models import Product


# Create your models here.
class Venta(models.Model):
    """Modelo que representa a una Venta Global"""

    TIPO_INVOCE = (
        ('0', 'BOLETA'),
        ('1', 'FACTURA'),
        ('4', 'OTRO'),
    )

    TIPO_PAYMENT = (
        ('0', 'TARJETA'),
        ('1', 'DEPOSITO'),
    )

    date_venta = models.DateTimeField(
        'Fecha de Venta',
        blank=True,
        null=True
    )
    amount = models.DecimalField(
      'Monto', 
      max_digits=10, 
      decimal_places=2
    )
    count = models.PositiveIntegerField('Cantidad de Productos')
    type_payment = models.CharField(
        'TIPO PAGO',
        max_length=2,
        choices=TIPO_PAYMENT
    )
    type_invoce = models.CharField(
        'TIPO',
        max_length=2,
        choices=TIPO_INVOCE
    )
    cod_transaccion = models.CharField(
        'Codigo de transaccion',
        max_length=30,
        blank=True,
    )
    num_pedido = models.CharField(
        'Numero de Pedido',
        max_length=50,
        blank=True,
    )
    cancelado = models.BooleanField(default=False)
    anulate = models.BooleanField(default=False)
    user_created = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="venta_created",
    )
    user_modified = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="venta_modified",
        blank=True,
        null=True,
        editable=False
    )
    #
    # objects = VentaMananger()

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'ventas'

    def __str__(self):
        return 'Nº [' + str(self.id) + '] - ' + str(self.date_venta)



class DetailVenta(models.Model):
    """Modelo que representa a una venta en detalle"""

    product = models.ForeignKey(
      Product, 
      on_delete=models.CASCADE, 
      verbose_name='Producto'
    )
    venta = models.ForeignKey(
      Venta, 
      on_delete=models.CASCADE, 
      verbose_name='Codigo de Venta'
    )
    count = models.PositiveIntegerField('Cantidad')
    price_compra = models.DecimalField(
      'Precio Compra', 
      max_digits=10, 
      decimal_places=3
    )
    price_venta = models.DecimalField(
      'Precio Venta', 
      max_digits=10, 
      decimal_places=2
    )
    anulate = models.BooleanField(default=False)
    category = models.CharField(
        'Categoria del producto cuando se vendio',
        max_length=50
    )
    igv = models.DecimalField(
        'porcentaje impuesto, igv',
        max_digits=5,
        decimal_places=2
    )
    monto_total = models.DecimalField(
        'precio total de la venta',
        max_digits=10,
        decimal_places=3
    )
    count_reembolso = models.PositiveIntegerField(default=0)
    reembolso = models.BooleanField(default=False)

    #
    # objects = VentaDetailMananger()

    class Meta:
        verbose_name = 'Detalle Venta'
        verbose_name_plural = 'Detalles de una Venta'

    def __str__(self):
        return str(self.product.name) + ' - ' + str(self.venta.id)
