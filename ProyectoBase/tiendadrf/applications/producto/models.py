from django.db import models
from django.conf import settings

# Create your models here.
class Marca(models.Model):

    name = models.CharField('Marca', max_length=50)
    #
    #objects
    class Meta:
        verbose_name = 'Marca Producto'
        verbose_name_plural = 'Marcas Productos'

    def __str__(self):
        return str(self.id) + ' - ' + str(self.name)


class Category(models.Model):

    name = models.CharField('categoria', max_length=50)
    #
    #objects
    class Meta:
        verbose_name = 'Categoria Producto'
        verbose_name_plural = 'Categoria Productos'

    def __str__(self):
        return str(self.id) + ' - ' + str(self.name)


class Colors(models.Model):

    color = models.CharField('color hex', max_length=7)
    #
    #objects
    class Meta:
        verbose_name = 'color Producto'
        verbose_name_plural = 'colores Productos'

    def __str__(self):
        return str(self.id) + ' - ' + str(self.name)


class Product(models.Model):
    """Modelo que representa a un Producto"""

    marca = models.ForeignKey(
        Marca,
        on_delete=models.CASCADE,
        related_name='marca_prod'
    )
    category = models.ManyToManyField(Category)
    color = models.ManyToManyField(Colors)
    name = models.CharField('Nombre', max_length=40)
    short_resume = models.CharField(
        'Resumen corto',
        max_length=130,
        blank=True
    ) # Resumen corto del producto
    main_image = models.ImageField('Producto') # imagen principal del producto
    man = models.BooleanField('Para Hombre', default=True)
    woman = models.BooleanField('Para Mujer', default=True)
    image1 = models.ImageField('Imagen 1', blank=True, null=True)
    image2 = models.ImageField('Imagen 2', blank=True, null=True)
    description = models.TextField('Descripcion del Producto')
    video = models.URLField('unboxin', blank=True, null=True)
    precio_compra = models.DecimalField(
        'Precio de Compra',
        max_digits=10,
        decimal_places=3
    )
    precio_venta = models.DecimalField(
        'Precio de Venta',
        max_digits=10,
        decimal_places=2
    )
    stok = models.PositiveIntegerField('Stok', default=0)
    num_ventas = models.PositiveIntegerField('Veces vendido', default=0)
    publicado = models.BooleanField(default=False)
    user_created = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="prod_created",
    )
    #
    # objects = ProductMananger()

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return str(self.id) + ' ' + str(self.name)
