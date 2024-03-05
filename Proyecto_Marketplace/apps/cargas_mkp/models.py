from django.db import models
# Create your models here.
class CatProductosmarketplace(models.Model):
    idu_producto = models.BigAutoField(primary_key=True)
    idu_productomirakl = models.CharField(max_length=254)
    num_codigomarketplace = models.BigIntegerField(blank=True, null=True)
    nom_partnumber = models.CharField(max_length=254, blank=True, null=True)
    idu_categoria = models.BigIntegerField()
    fec_creacionmirakl = models.DateTimeField()
    fec_actualizacionmirakl = models.DateTimeField()
    opc_aceptado = models.CharField(max_length=50)
    opc_validado = models.CharField(max_length=50)
    opc_sincronizado = models.CharField(max_length=150)
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    opc_estatus = models.CharField(max_length=10)
    nom_actualiza = models.CharField(max_length=254)
    opc_procesado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_productosmarketplace'

class CatOfertasmarketplace(models.Model):
    idu_oferta = models.BigAutoField(primary_key=True)
    idu_ofertamirakl = models.BigIntegerField()
    nom_partnumber = models.CharField(max_length=254)
    idu_producto = models.ForeignKey('CatProductosmarketplace', models.DO_NOTHING, db_column='idu_producto')
    nom_parentpartnumber = models.CharField(max_length=254)
    imp_preciominimoenvio = models.IntegerField()
    imp_preciominimoenvioadicional = models.IntegerField()
    des_zonaenviominimo = models.CharField(max_length=254)
    des_tipoenviominimo = models.CharField(max_length=254)
    imp_precio = models.IntegerField()
    imp_preciototal = models.IntegerField()
    des_infoadicionalprecio = models.CharField(max_length=254)
    num_cantidad = models.SmallIntegerField()
    des_descripcionoferta = models.CharField(max_length=2048)
    opc_codigocondicion = models.CharField(max_length=150)
    idu_tienda = models.BigIntegerField()
    nom_tienda = models.CharField(max_length=254)
    opc_profesional = models.BooleanField(blank=True, null=True)
    opc_premiun = models.BooleanField(blank=True, null=True)
    opc_logistica = models.CharField(max_length=254)
    opc_activo = models.BooleanField()
    nom_canal = models.CharField(max_length=50)
    opc_eliminar = models.BooleanField()
    imp_preciooriginal = models.IntegerField()
    fec_iniciodescuento = models.DateTimeField()
    fec_findescuento = models.DateTimeField()
    fec_iniciodisponible = models.DateTimeField()
    fec_findisponible = models.DateTimeField()
    imp_preciodescuento = models.IntegerField(blank=True, null=True)
    opc_codigoisomoneda = models.CharField(max_length=50)
    num_diasesperaenvio = models.SmallIntegerField()
    opc_permitecotizacion = models.BooleanField(blank=True, null=True)
    num_mincantidad = models.SmallIntegerField()
    num_maxcantidad = models.SmallIntegerField()
    num_cantidadpaquete = models.SmallIntegerField()
    num_mincantidadorden = models.SmallIntegerField()
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    opc_estatus = models.CharField(max_length=10)
    nom_actualiza = models.CharField(max_length=254)
    opc_procesado = models.SmallIntegerField(blank=True, null=True)
    num_rangofavorito = models.BigIntegerField()
    desc_polizagarantia = models.CharField(max_length=2048)
    nom_periodogarantia = models.CharField(max_length=15)
    num_pesopaquete = models.DecimalField(max_digits=5, decimal_places=2)
    num_alturapaquete = models.DecimalField(max_digits=5, decimal_places=2)
    num_ancho_paquete = models.DecimalField(max_digits=5, decimal_places=2)
    num_longitud_paquete = models.DecimalField(max_digits=5, decimal_places=2)
    idu_tax_producto = models.CharField(max_length=16, blank=True, null=True)

    def __str__(self):
        return self.nom_tienda
    
    
    class Meta:
        managed = False
        db_table = 'cat_ofertasmarketplace'
        unique_together = (('idu_oferta', 'idu_producto'),)
