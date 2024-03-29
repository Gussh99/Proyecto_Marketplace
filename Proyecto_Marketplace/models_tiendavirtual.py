# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class FilaActual(models.Model):
    numareaweb = models.SmallIntegerField(blank=True, null=True)
    nomareaweb = models.CharField(max_length=50, blank=True, null=True)
    numarea = models.SmallIntegerField(blank=True, null=True)
    parent_numarea_web = models.SmallIntegerField(blank=True, null=True)
    meta_keyword = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ordenamiento = models.SmallIntegerField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    flag_menu_left = models.SmallIntegerField(blank=True, null=True)
    num_nivel = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_fila_actual'


class Af0797RespuestasOs(models.Model):
    des_solicitudcliente = models.BigIntegerField(blank=True, null=True)
    des_tiendagenera = models.CharField(max_length=50, blank=True, null=True)
    clv_tipoos = models.CharField(max_length=50, blank=True, null=True)
    clv_respuesta = models.CharField(max_length=50, blank=True, null=True)
    fec_respuesta = models.DateField(blank=True, null=True)
    fec_movimiento = models.DateField(blank=True, null=True)
    folioid = models.IntegerField(blank=True, null=True)
    flag_alta = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'af0797_respuestas_os'


class Afectacommerce(models.Model):
    opc_afectacommerce = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'afectacommerce'
# Unable to inspect table 'area'
# The error was: permission denied for table area


class Areas(models.Model):
    area_id = models.SmallIntegerField(primary_key=True)
    area_name = models.CharField(max_length=50, blank=True, null=True)
    area_description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areas'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BatchJobExecution(models.Model):
    job_execution_id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField(blank=True, null=True)
    job_instance = models.ForeignKey('BatchJobInstance', models.DO_NOTHING)
    create_time = models.DateTimeField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    exit_code = models.CharField(max_length=2500, blank=True, null=True)
    exit_message = models.CharField(max_length=2500, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    job_configuration_location = models.CharField(max_length=2500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batch_job_execution'


class BatchJobExecutionContext(models.Model):
    job_execution = models.OneToOneField(BatchJobExecution, models.DO_NOTHING, primary_key=True)
    short_context = models.CharField(max_length=2500)
    serialized_context = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batch_job_execution_context'


class BatchJobExecutionParams(models.Model):
    job_execution = models.ForeignKey(BatchJobExecution, models.DO_NOTHING)
    type_cd = models.CharField(max_length=6)
    key_name = models.CharField(max_length=100)
    string_val = models.CharField(max_length=250, blank=True, null=True)
    date_val = models.DateTimeField(blank=True, null=True)
    long_val = models.BigIntegerField(blank=True, null=True)
    double_val = models.FloatField(blank=True, null=True)
    identifying = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'batch_job_execution_params'


class BatchJobInstance(models.Model):
    job_instance_id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField(blank=True, null=True)
    job_name = models.CharField(max_length=100)
    job_key = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'batch_job_instance'
        unique_together = (('job_name', 'job_key'),)


class BatchStepExecution(models.Model):
    step_execution_id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    step_name = models.CharField(max_length=100)
    job_execution = models.ForeignKey(BatchJobExecution, models.DO_NOTHING)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    commit_count = models.BigIntegerField(blank=True, null=True)
    read_count = models.BigIntegerField(blank=True, null=True)
    filter_count = models.BigIntegerField(blank=True, null=True)
    write_count = models.BigIntegerField(blank=True, null=True)
    read_skip_count = models.BigIntegerField(blank=True, null=True)
    write_skip_count = models.BigIntegerField(blank=True, null=True)
    process_skip_count = models.BigIntegerField(blank=True, null=True)
    rollback_count = models.BigIntegerField(blank=True, null=True)
    exit_code = models.CharField(max_length=2500, blank=True, null=True)
    exit_message = models.CharField(max_length=2500, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batch_step_execution'


class BatchStepExecutionContext(models.Model):
    step_execution = models.OneToOneField(BatchStepExecution, models.DO_NOTHING, primary_key=True)
    short_context = models.CharField(max_length=2500)
    serialized_context = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batch_step_execution_context'


class CargaAtributos(models.Model):
    identifier = models.CharField(primary_key=True, max_length=35)
    type = models.CharField(max_length=35)
    attributetype = models.CharField(max_length=35)
    category = models.CharField(max_length=35)
    sequence = models.SmallIntegerField()
    displayable = models.BooleanField(blank=True, null=True)
    searchable = models.IntegerField()
    comparable = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=264)
    description = models.TextField()
    allowedvalue1 = models.CharField(max_length=264)
    borrable = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'carga_atributos'


class CargaAtributosProductos(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=35)
    attributeidentifier = models.CharField(max_length=35)
    valueidentifier = models.CharField(max_length=35)
    value = models.TextField()
    lenceria = models.BooleanField()
    usage = models.CharField(max_length=35)
    sequence = models.IntegerField()
    beneficio = models.TextField()
    borrable = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'carga_atributos_productos'
        unique_together = (('partnumber', 'attributeidentifier', 'value'),)


class CargaCategorias(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    numareaweb = models.SmallIntegerField()
    groupidentifier = models.CharField(max_length=254)
    topgroup = models.BooleanField(blank=True, null=True)
    nivel = models.IntegerField()
    parentgroupidentifier = models.CharField(max_length=254)
    sequence = models.IntegerField()
    name = models.CharField(max_length=254)
    titulo = models.CharField(max_length=254)
    metakeyword = models.CharField(max_length=254)
    metadescription = models.CharField(max_length=254, blank=True, null=True)
    borrable = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'carga_categorias'
        unique_together = (('numarea', 'numareaweb'),)


class CargaClientes(models.Model):
    logonid = models.CharField(primary_key=True, max_length=64)
    temppassword = models.CharField(max_length=32)
    lastname = models.CharField(max_length=256)
    firstname = models.CharField(max_length=256)
    displayname = models.CharField(max_length=256)
    address3 = models.CharField(max_length=256)
    address2 = models.CharField(max_length=256)
    address1 = models.CharField(max_length=256)
    addressfield1 = models.CharField(max_length=256)
    addressfield2 = models.CharField(max_length=256)
    addressfield3 = models.CharField(max_length=256)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    zipcode = models.CharField(max_length=32)
    phone1 = models.CharField(max_length=32)
    email1 = models.CharField(max_length=64)
    gender = models.CharField(max_length=64)
    userprofilefield = models.CharField(max_length=64)
    employeeid = models.IntegerField()
    dateofbirth = models.CharField(max_length=64)
    mobilephone1 = models.CharField(max_length=32)
    idorigen = models.IntegerField()
    idfacebook = models.BigIntegerField(blank=True, null=True)
    registertype = models.IntegerField()
    receiveemail = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    extrafield1 = models.CharField(max_length=32)
    extrafield2 = models.CharField(max_length=32)
    extrafield3 = models.CharField(max_length=32)
    extrafield4 = models.CharField(max_length=32)
    extrafield5 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'carga_clientes'


class CargaGtin(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    numcodigo = models.IntegerField()
    gtin = models.CharField(max_length=14, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    fechacarga = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carga_gtin'
        unique_together = (('numarea', 'numcodigo'),)


class CargaProductos(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=35)
    numarea = models.SmallIntegerField()
    numdepto = models.SmallIntegerField()
    numclase = models.SmallIntegerField()
    numfamilia = models.SmallIntegerField()
    dcf = models.CharField(max_length=6)
    numcodigo = models.IntegerField()
    talla = models.CharField(max_length=6)
    precioventa = models.IntegerField()
    preciocredito = models.IntegerField()
    numbodega = models.SmallIntegerField()
    disponible = models.IntegerField()
    existencia = models.SmallIntegerField()
    type = models.CharField(max_length=120)
    isproduct = models.BooleanField(blank=True, null=True)
    parentpartnumber = models.CharField(max_length=120)
    parentgroupidentifier = models.CharField(max_length=120)
    nivelmenu = models.IntegerField()
    sequence = models.CharField(max_length=2)
    languageid = models.SmallIntegerField()
    name = models.CharField(max_length=120)
    marca = models.CharField(max_length=120)
    shortdescription = models.CharField(max_length=255)
    longdescription = models.TextField()
    available = models.SmallIntegerField()
    published = models.SmallIntegerField()
    availabilitydate = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)
    field4 = models.CharField(max_length=255)
    promotionpricecurrency = models.CharField(max_length=3)
    promotionprice = models.CharField(max_length=10)
    rebajaprice = models.CharField(max_length=10)
    flagprecio = models.SmallIntegerField()
    fechainicialpromo = models.CharField(max_length=32)
    fechafinalpromo = models.CharField(max_length=32)
    buyable = models.SmallIntegerField()
    borrable = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'carga_productos'
        unique_together = (('partnumber', 'numarea', 'numcodigo'),)


class CargaStoresnodos(models.Model):
    storename = models.CharField(max_length=-1)
    coppelcodecity = models.SmallIntegerField()
    stateid = models.SmallIntegerField()
    languageid = models.SmallIntegerField()
    namecoppelcity = models.CharField(max_length=-1)
    namegeoloccity = models.CharField(max_length=-1)
    nodoname = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'carga_storesnodos'


class CargasArg(models.Model):
    carga_id = models.BigIntegerField(primary_key=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cargas_arg'


class CatAccionesCobroenvio(models.Model):
    nombre = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'cat_acciones_cobroenvio'


class CatAdministradorBanner(models.Model):
    idu_banner = models.AutoField()
    idu_tipo_banner = models.IntegerField()
    desc_url_banner = models.CharField(max_length=200)
    nom_imagen = models.CharField(max_length=100)
    desc_alt_imagen = models.CharField(max_length=100)
    fec_inicio_banner = models.DateField()
    fec_final_banner = models.DateField()
    num_status = models.IntegerField()
    num_width = models.IntegerField()
    num_height = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cat_administrador_banner'


class CatAdministradorMenuLeftCoppel(models.Model):
    idu_menu = models.AutoField()
    desc_url = models.CharField(max_length=200)
    nom_articulo = models.CharField(max_length=80)
    num_area = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cat_administrador_menu_left_coppel'


class CatAreas(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    descarea = models.CharField(unique=True, max_length=12)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cat_areas'


class CatAreasArg(models.Model):
    num_area = models.SmallIntegerField(primary_key=True)
    nom_area = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'cat_areas_arg'


class CatAreasweb(models.Model):
    numareaweb = models.OneToOneField('self', models.DO_NOTHING, db_column='numareaweb', primary_key=True)
    nomareaweb = models.CharField(max_length=50)
    numarea = models.ForeignKey(CatAreas, models.DO_NOTHING, db_column='numarea')
    parent_numarea_web = models.SmallIntegerField()
    meta_keyword = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ordenamiento = models.SmallIntegerField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    flag_menu_left = models.SmallIntegerField(blank=True, null=True)
    num_nivel = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_areasweb'


class CatAreaswebRespmarketplace(models.Model):
    numareaweb = models.SmallIntegerField(blank=True, null=True)
    nomareaweb = models.CharField(max_length=50, blank=True, null=True)
    numarea = models.SmallIntegerField(blank=True, null=True)
    parent_numarea_web = models.SmallIntegerField(blank=True, null=True)
    meta_keyword = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ordenamiento = models.SmallIntegerField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    flag_menu_left = models.SmallIntegerField(blank=True, null=True)
    num_nivel = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_areasweb_respmarketplace'


class CatArticulos(models.Model):
    numarea = models.OneToOneField('CatMarcas', models.DO_NOTHING, db_column='numarea', primary_key=True)
    numdepto = models.SmallIntegerField()
    numclase = models.SmallIntegerField()
    numfamilia = models.SmallIntegerField()
    numcodigo = models.IntegerField()
    modelo = models.CharField(max_length=35)
    nummarca = models.SmallIntegerField()
    nomarticulo = models.CharField(max_length=120)
    descarticulo = models.TextField()
    fechaalta = models.DateTimeField()
    preciovntaint = models.IntegerField()
    preciovntafrontera = models.IntegerField()
    exclusivo = models.SmallIntegerField()
    publicar = models.SmallIntegerField()
    nuevo = models.SmallIntegerField()
    numestatus = models.ForeignKey('CatEstatus', models.DO_NOTHING, db_column='numestatus')
    meta_keyword = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    numdisponibilidad = models.ForeignKey('CatDisponibilidades', models.DO_NOTHING, db_column='numdisponibilidad')
    comprar = models.SmallIntegerField()
    entrada = models.SmallIntegerField()
    tipoarticulo = models.SmallIntegerField()
    flagpromocion = models.SmallIntegerField()
    nomarticuloweb = models.CharField(max_length=120)
    meta_title = models.CharField(max_length=255)
    opc_descontinuado = models.BooleanField(blank=True, null=True)
    num_ordendos = models.SmallIntegerField()
    num_ordentres = models.SmallIntegerField()
    opc_vendible = models.SmallIntegerField(blank=True, null=True)
    fechapublicado = models.DateTimeField()
    usuariopublico = models.BigIntegerField()
    modoentrega = models.CharField(max_length=1)
    nacoimp = models.CharField(max_length=1)
    clv_novtaporr = models.SmallIntegerField()
    num_diasespera = models.IntegerField()
    gtin = models.CharField(unique=True, max_length=14, blank=True, null=True)
    observaciones = models.CharField(max_length=500, blank=True, null=True)
    secuencia = models.IntegerField(blank=True, null=True)
    reutilizado = models.SmallIntegerField()
    num_garantiaenmeses = models.SmallIntegerField()
    num_seccion = models.SmallIntegerField()
    flag_manejaiva = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_articulos'
        unique_together = (('numarea', 'numcodigo'),)


class CatArticulosArg(models.Model):
    num_area = models.SmallIntegerField(primary_key=True)
    num_departamento = models.SmallIntegerField()
    num_clase = models.SmallIntegerField()
    num_familia = models.SmallIntegerField()
    num_codigo = models.IntegerField()
    des_articulo = models.CharField(max_length=-1)
    des_marca = models.CharField(max_length=-1)
    des_modelo = models.CharField(max_length=-1)
    fec_alta = models.DateField()
    opc_descontinuado = models.IntegerField()
    des_complemento = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'cat_articulos_arg'
        unique_together = (('num_area', 'num_departamento', 'num_clase', 'num_familia', 'num_codigo'),)


class CatArticulosManualesRel(models.Model):
    numarea = models.OneToOneField(CatArticulos, models.DO_NOTHING, db_column='numarea', primary_key=True)
    numcodigo = models.IntegerField()
    nombre = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    observaciones = models.CharField(max_length=500, blank=True, null=True)
    foto = models.BooleanField(blank=True, null=True)
    copy = models.BooleanField(blank=True, null=True)
    fechaalta = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cat_articulos_manuales_rel'
        unique_together = (('numarea', 'numcodigo'),)


class CatArticulosMuebles(models.Model):
    num_bodega = models.SmallIntegerField(blank=True, null=True)
    idu_tipotasa = models.SmallIntegerField(blank=True, null=True)
    num_tienda = models.SmallIntegerField(blank=True, null=True)
    escelular = models.CharField(max_length=1, blank=True, null=True)
    num_dcf = models.IntegerField(blank=True, null=True)
    idu_ciudad = models.SmallIntegerField(blank=True, null=True)
    num_codigo = models.IntegerField(blank=True, null=True)
    imp_preciovta = models.IntegerField(blank=True, null=True)
    imp_promo = models.IntegerField(blank=True, null=True)
    imp_credito = models.FloatField(blank=True, null=True)
    tasainteres = models.SmallIntegerField(blank=True, null=True)
    imp_promocredito = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_articulos_muebles'


class CatArticulosReclasificados(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    numcodigo = models.IntegerField()
    numdeptoant = models.SmallIntegerField()
    numclaseant = models.SmallIntegerField()
    numfamiliaant = models.SmallIntegerField()
    numdeptonuevo = models.SmallIntegerField()
    numclasenuevo = models.SmallIntegerField()
    numfamilianuevo = models.SmallIntegerField()
    usuarioatendio = models.CharField(max_length=50, blank=True, null=True)
    fechaatendido = models.DateTimeField()
    fechaactualizado = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cat_articulos_reclasificados'
        unique_together = (('numarea', 'numcodigo'),)


class CatArticulosgera(models.Model):
    numdepto = models.SmallIntegerField(blank=True, null=True)
    numclase = models.SmallIntegerField(blank=True, null=True)
    numfamilia = models.SmallIntegerField(blank=True, null=True)
    publicados = models.BigIntegerField(blank=True, null=True)
    npublicados = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_articulosgera'


class CatArticulosgera0(models.Model):
    numdepto = models.SmallIntegerField(blank=True, null=True)
    numclase = models.SmallIntegerField(blank=True, null=True)
    numfamilia = models.SmallIntegerField(blank=True, null=True)
    npublicados = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_articulosgera_0'


class CatArticulosgera1(models.Model):
    numdepto = models.SmallIntegerField(blank=True, null=True)
    numclase = models.SmallIntegerField(blank=True, null=True)
    numfamilia = models.SmallIntegerField(blank=True, null=True)
    publicados = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_articulosgera_1'


class CatArticulosmuebles(models.Model):
    numarea = models.OneToOneField('CatMarcas', models.DO_NOTHING, db_column='numarea', primary_key=True)
    numdepto = models.SmallIntegerField()
    numclase = models.SmallIntegerField()
    numfamilia = models.SmallIntegerField()
    numcodigo = models.IntegerField()
    modelo = models.CharField(max_length=35)
    nummarca = models.SmallIntegerField()
    nomarticulo = models.CharField(max_length=120)
    descarticulo = models.TextField()
    fechaalta = models.DateTimeField()
    preciovntaint = models.IntegerField()
    preciovntafrontera = models.IntegerField()
    exclusivo = models.SmallIntegerField()
    publicar = models.SmallIntegerField()
    nuevo = models.SmallIntegerField()
    numestatus = models.ForeignKey('CatEstatus', models.DO_NOTHING, db_column='numestatus')
    meta_keyword = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    numdisponibilidad = models.ForeignKey('CatDisponibilidades', models.DO_NOTHING, db_column='numdisponibilidad')
    comprar = models.SmallIntegerField()
    entrada = models.SmallIntegerField()
    tipoarticulo = models.SmallIntegerField()
    flagpromocion = models.SmallIntegerField()
    nomarticuloweb = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'cat_articulosmuebles'
        unique_together = (('numarea', 'numcodigo'),)


class CatAtributosecommerce(models.Model):
    idu_atributoecommerce = models.BigAutoField(primary_key=True)
    nom_atributoecommerce = models.CharField(max_length=254)
    opc_activo = models.BooleanField()
    num_nivel = models.BigIntegerField()
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    nom_actualiza = models.CharField(max_length=254)
    idu_categoria = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'cat_atributosecommerce'


class CatAtributosmarketplace(models.Model):
    idu_atributo = models.BigAutoField(primary_key=True)
    des_codigoatributo = models.CharField(max_length=254)
    idu_categoria = models.BigIntegerField()
    des_codigocategoria = models.CharField(max_length=254)
    des_atributoen = models.CharField(max_length=254)
    des_atributomx = models.CharField(max_length=254)
    opc_nivelrequerido = models.CharField(max_length=254)
    opc_tipoatributo = models.CharField(max_length=254)
    des_tipoparametro = models.CharField(max_length=254)
    opc_variante = models.BooleanField()
    opc_activo = models.BooleanField()
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    opc_estatus = models.CharField(max_length=10)
    nom_actualiza = models.CharField(max_length=254)
    opc_procesado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_atributosmarketplace'


class CatBannersTiposTamaniosTiendas(models.Model):
    cod_bnr_tp_tmn_tda = models.AutoField(primary_key=True)
    cod_tipo_tienda = models.ForeignKey('CatTiposTiendas', models.DO_NOTHING, db_column='cod_tipo_tienda')
    cod_tamanio = models.ForeignKey('CatTamaniosTiendas', models.DO_NOTHING, db_column='cod_tamanio', blank=True, null=True)
    cod_banner = models.ForeignKey('CatImgsliderKiosko', models.DO_NOTHING, db_column='cod_banner')
    cod_tipo_banner = models.ForeignKey('CatTiposBanners', models.DO_NOTHING, db_column='cod_tipo_banner')
    estado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cat_banners_tipos_tamanios_tiendas'
        unique_together = (('cod_tipo_tienda', 'cod_tamanio', 'cod_tipo_banner', 'cod_banner'),)


class CatBodegas(models.Model):
    idubodega = models.IntegerField(primary_key=True)
    nomsiglas = models.CharField(max_length=4)
    nombodega = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'cat_bodegas'


class CatBodegasmarket(models.Model):
    idu_bodega = models.BigAutoField(primary_key=True)
    num_bodega = models.SmallIntegerField()
    num_area = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_bodegasmarket'
        unique_together = (('idu_bodega', 'num_bodega'),)


class CatBodzonasoficialescentralizadasetl(models.Model):
    num_bodega = models.SmallIntegerField()
    num_ciudad = models.SmallIntegerField()
    num_zona = models.IntegerField()
    nom_zona = models.CharField(max_length=30)
    num_ruta = models.SmallIntegerField()
    num_ciudadpertenece = models.SmallIntegerField()
    num_orden = models.IntegerField()
    des_latitud = models.CharField(max_length=20)
    des_longitud = models.CharField(max_length=20)
    des_estado = models.CharField(max_length=35)
    des_ciudad = models.CharField(max_length=60)
    des_colonia = models.CharField(max_length=60)
    num_codigopostal = models.IntegerField()
    fec_ultimomovto = models.DateField()
    nom_empultimomovto = models.CharField(max_length=60)
    num_prioridad = models.SmallIntegerField()
    flg_actualizado = models.SmallIntegerField()
    keyx = models.AutoField()
    num_cedisropa = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_bodzonasoficialescentralizadasetl'


class CatBodzonasoficialescentralizadasetlPett(models.Model):
    num_bodega = models.SmallIntegerField(blank=True, null=True)
    num_ciudad = models.SmallIntegerField(blank=True, null=True)
    num_zona = models.IntegerField(blank=True, null=True)
    nom_zona = models.CharField(max_length=30, blank=True, null=True)
    num_ruta = models.SmallIntegerField(blank=True, null=True)
    num_ciudadpertenece = models.SmallIntegerField(blank=True, null=True)
    num_orden = models.IntegerField(blank=True, null=True)
    des_latitud = models.CharField(max_length=20, blank=True, null=True)
    des_longitud = models.CharField(max_length=20, blank=True, null=True)
    des_estado = models.CharField(max_length=35, blank=True, null=True)
    des_ciudad = models.CharField(max_length=60, blank=True, null=True)
    des_colonia = models.CharField(max_length=60, blank=True, null=True)
    num_codigopostal = models.IntegerField(blank=True, null=True)
    fec_ultimomovto = models.DateField(blank=True, null=True)
    nom_empultimomovto = models.CharField(max_length=60, blank=True, null=True)
    num_prioridad = models.SmallIntegerField(blank=True, null=True)
    flg_actualizado = models.SmallIntegerField(blank=True, null=True)
    keyx = models.IntegerField(blank=True, null=True)
    num_cedisropa = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_bodzonasoficialescentralizadasetl_pett'


class CatBodzonasoficialescentralizadasetlRes15(models.Model):
    num_bodega = models.SmallIntegerField()
    num_ciudad = models.SmallIntegerField()
    num_zona = models.IntegerField()
    nom_zona = models.CharField(max_length=30)
    num_ruta = models.SmallIntegerField()
    num_ciudadpertenece = models.SmallIntegerField()
    num_orden = models.IntegerField()
    des_latitud = models.CharField(max_length=20)
    des_longitud = models.CharField(max_length=20)
    des_estado = models.CharField(max_length=35)
    des_ciudad = models.CharField(max_length=60)
    des_colonia = models.CharField(max_length=60)
    num_codigopostal = models.IntegerField()
    fec_ultimomovto = models.DateField()
    nom_empultimomovto = models.CharField(max_length=60)
    num_prioridad = models.SmallIntegerField()
    flg_actualizado = models.SmallIntegerField()
    keyx = models.AutoField()
    num_cedisropa = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_bodzonasoficialescentralizadasetl_res15'


class CatBpcodicionarticulo(models.Model):
    num_condicion = models.SmallIntegerField(primary_key=True)
    nom_condicion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_bpcodicionarticulo'


class CatBpconfirmacion(models.Model):
    num_confirmacion = models.SmallIntegerField(primary_key=True)
    nom_confirmacion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_bpconfirmacion'


class CatBpstatus(models.Model):
    num_status = models.SmallIntegerField(primary_key=True)
    nom_status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_bpstatus'


class CatBptipoempaque(models.Model):
    num_tipoempaque = models.SmallIntegerField(primary_key=True)
    nom_tipoempaque = models.CharField(max_length=50, blank=True, null=True)
    des_tipoempaque = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_bptipoempaque'


class CatCampanias(models.Model):
    idu_campania = models.IntegerField(primary_key=True)
    nom_campania = models.CharField(max_length=100)
    fec_inicio = models.DateField()
    fec_fin = models.DateField()
    fec_limitecanje = models.DateField()
    fec_limitecanjepremio = models.DateField()
    num_importeparticipa = models.IntegerField()
    num_tipocampania = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_campanias'


class CatCamposadicionalesmarketplace(models.Model):
    opc_tipocampoadicional = models.SmallAutoField()
    des_tipocampoadicional = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'cat_camposadicionalesmarketplace'


class CatCanalventa(models.Model):
    idu_canalventa = models.AutoField()
    desc_canalventa = models.CharField(max_length=20, blank=True, null=True)
    desc_canal = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_canalventa'


class CatCaracteristicas(models.Model):
    numcaracteristica = models.AutoField(primary_key=True)
    nomcaracteristica = models.CharField(max_length=120)
    numarea = models.IntegerField(blank=True, null=True)
    numdepartamento = models.IntegerField(blank=True, null=True)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cat_caracteristicas'


class CatCargasdetrabajo(models.Model):
    idu_perfilusuario = models.IntegerField(primary_key=True)
    nom_perfilusuario = models.CharField(max_length=50)
    opc_activo = models.BooleanField()
    fec_alta = models.DateTimeField()
    fec_movimiento = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cat_cargasdetrabajo'


class CatCarrusel(models.Model):
    id_cat_carrusel = models.AutoField(primary_key=True)
    nom_cat_carrusel = models.TextField(blank=True, null=True)
    estatus = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_carrusel'


class CatCategorias(models.Model):
    numcategoria = models.AutoField(primary_key=True)
    nomcategoria = models.CharField(max_length=50)
    numarea = models.IntegerField(blank=True, null=True)
    ordenamiento = models.IntegerField(blank=True, null=True)
    publicar = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_categorias'
        unique_together = (('nomcategoria', 'numarea'),)


class CatCategoriasArg(models.Model):
    groupidentifier = models.CharField(primary_key=True, max_length=64)
    topgroup = models.CharField(max_length=5)
    parentgroupidentifier = models.CharField(max_length=64)
    sequence = models.IntegerField()
    name = models.CharField(max_length=254)
    shortdescription = models.CharField(max_length=254)
    longdescription = models.CharField(max_length=4000)
    thumbnail = models.CharField(max_length=254)
    fullimage = models.CharField(max_length=254)
    published = models.SmallIntegerField()
    keyword = models.CharField(max_length=254)
    urlkeyword = models.CharField(max_length=254)
    pagetitle = models.CharField(max_length=254)
    metadescription = models.CharField(max_length=1024)
    delete = models.SmallIntegerField()
    field1 = models.CharField(max_length=254)
    field2 = models.CharField(max_length=254)
    hash = models.BigIntegerField()
    carga_id = models.BigIntegerField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cat_categorias_arg'
        unique_together = (('carga_id', 'groupidentifier'),)


class CatCategoriasDataImportArg(models.Model):
    carga_id = models.BigIntegerField(primary_key=True)
    groupidentifier = models.CharField(max_length=64)
    topgroup = models.CharField(max_length=5)
    parentgroupidentifier = models.CharField(max_length=64)
    sequence = models.IntegerField()
    name = models.CharField(max_length=254)
    shortdescription = models.CharField(max_length=254)
    longdescription = models.CharField(max_length=4000)
    thumbnail = models.CharField(max_length=254)
    fullimage = models.CharField(max_length=254)
    published = models.SmallIntegerField()
    keyword = models.CharField(max_length=254)
    urlkeyword = models.CharField(max_length=254)
    pagetitle = models.CharField(max_length=254)
    metadescription = models.CharField(max_length=1024)
    delete = models.SmallIntegerField()
    field1 = models.CharField(max_length=254)
    field2 = models.CharField(max_length=254)
    hash = models.BigIntegerField()
    order = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_categorias_data_import_arg'
        unique_together = (('carga_id', 'groupidentifier'),)


class CatCategoriasDeltaArg(models.Model):
    carga_id = models.BigIntegerField(primary_key=True)
    groupidentifier = models.CharField(max_length=64)
    topgroup = models.CharField(max_length=5)
    parentgroupidentifier = models.CharField(max_length=64)
    sequence = models.IntegerField()
    name = models.CharField(max_length=254)
    shortdescription = models.CharField(max_length=254)
    longdescription = models.CharField(max_length=4000)
    thumbnail = models.CharField(max_length=254)
    fullimage = models.CharField(max_length=254)
    published = models.SmallIntegerField()
    keyword = models.CharField(max_length=254)
    urlkeyword = models.CharField(max_length=254)
    pagetitle = models.CharField(max_length=254)
    metadescription = models.CharField(max_length=1024)
    delete = models.SmallIntegerField()
    field1 = models.CharField(max_length=254)
    field2 = models.CharField(max_length=254)
    hash = models.BigIntegerField()
    order = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_categorias_delta_arg'
        unique_together = (('carga_id', 'groupidentifier'), ('carga_id', 'hash', 'groupidentifier'),)


class CatCategoriasmarketplace(models.Model):
    idu_categoria = models.BigAutoField(primary_key=True)
    des_codigocategoria = models.CharField(unique=True, max_length=254)
    des_categoriaen = models.CharField(max_length=254)
    des_categoriamx = models.CharField(max_length=254)
    idu_categoriapadre = models.SmallIntegerField()
    des_codigocategoriapadre = models.CharField(max_length=254)
    num_nivel = models.SmallIntegerField()
    opc_activo = models.BooleanField(blank=True, null=True)
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    opc_estatus = models.CharField(max_length=10)
    nom_actualiza = models.CharField(max_length=254)
    opc_procesado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_categoriasmarketplace'


class CatCausasbanco(models.Model):
    id = models.AutoField()
    nom_causabanco = models.CharField(max_length=-1)
    nom_descripcion = models.CharField(max_length=-1, blank=True, null=True)
    num_validacion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_causasbanco'


class CatCausascredito(models.Model):
    id = models.AutoField()
    clv_tipoprocesoventa = models.IntegerField(blank=True, null=True)
    clv_tipoopcionventa = models.IntegerField(blank=True, null=True)
    nom_descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_causascredito'


class CatCediscross(models.Model):
    num_ciudadpertenece = models.IntegerField()
    nom_nombrelargo = models.CharField(max_length=-1)
    nom_nombrecorto = models.CharField(max_length=-1)
    num_bodega = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cat_cediscross'


class CatCenciudades(models.Model):
    idu_ciudad = models.SmallIntegerField(primary_key=True)
    nom_abreviatura = models.CharField(max_length=4)
    nom_largociudad = models.CharField(max_length=30)
    num_bodega = models.IntegerField()
    des_regioncelular = models.CharField(max_length=3)
    imp_tasainteres = models.SmallIntegerField()
    imp_tasaiva = models.SmallIntegerField()
    des_servidor = models.CharField(max_length=15)
    cvl_local = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cat_cenciudades'


class CatCentrosdistribucion(models.Model):
    idu_ciudadcodigo = models.IntegerField(primary_key=True)
    des_ciudad = models.CharField(max_length=21)
    idu_bodegacodigo = models.IntegerField()
    des_bodega = models.CharField(max_length=14)
    idu_centrodistribucion = models.IntegerField()
    des_centrodistribucion = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'cat_centrosdistribucion'


class CatCiudades(models.Model):
    ciudad = models.IntegerField()
    bodega = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cat_ciudades'


class CatCiudadesArg(models.Model):
    num_ciudad = models.IntegerField(primary_key=True)
    nom_ciudad = models.CharField(max_length=-1)
    des_inicial = models.CharField(max_length=4)
    num_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_ciudades_arg'


class CatCiudadestados(models.Model):
    ciudad = models.SmallIntegerField(blank=True, null=True)
    estado = models.SmallIntegerField(blank=True, null=True)
    keyx = models.AutoField()

    class Meta:
        managed = False
        db_table = 'cat_ciudadestados'


class CatClases(models.Model):
    numarea = models.OneToOneField('CatDepartamentos', models.DO_NOTHING, db_column='numarea', primary_key=True)
    numdepto = models.SmallIntegerField()
    numclase = models.SmallIntegerField()
    descclase = models.CharField(max_length=50)
    activo = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_clases'
        unique_together = (('numarea', 'numdepto', 'numclase'),)


class CatClasesArg(models.Model):
    num_area = models.SmallIntegerField(primary_key=True)
    num_departamento = models.SmallIntegerField()
    num_clase = models.SmallIntegerField()
    nom_clase = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'cat_clases_arg'
        unique_together = (('num_area', 'num_departamento', 'num_clase'),)


class CatClasesmedidas(models.Model):
    numarea = models.SmallIntegerField()
    numdepto = models.SmallIntegerField()
    numclase = models.SmallIntegerField()
    descripcion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cat_clasesmedidas'


class CatClasesnopublicar(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numdepto = models.SmallIntegerField(blank=True, null=True)
    numclase = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_clasesnopublicar'


class CatClientes(models.Model):
    numusuario = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellidopaterno = models.CharField(max_length=30)
    apellidomaterno = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=-1)
    ciudad = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    calle = models.CharField(max_length=40)
    colonia = models.CharField(max_length=30)
    numcasa = models.CharField(max_length=12)
    clientecoppel = models.CharField(max_length=2)
    numclientecoppel = models.IntegerField()
    telefono = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    ext = models.CharField(max_length=20)
    cp = models.CharField(max_length=5)
    saldo = models.DecimalField(max_digits=65535, decimal_places=65535)
    otra = models.CharField(max_length=5)
    registro = models.CharField(max_length=1)
    correovalido = models.IntegerField()
    confirmado = models.CharField(max_length=1)
    interior = models.CharField(max_length=12)
    numciudad = models.IntegerField()
    numcolonia = models.IntegerField()
    numcalle = models.IntegerField()
    fechanacimiento = models.DateField()
    sexo = models.BooleanField()
    fecharegistro = models.DateField()
    celular = models.CharField(max_length=128, blank=True, null=True)
    entrecalles = models.CharField(max_length=-1, blank=True, null=True)
    domicilioobservaciones = models.CharField(max_length=-1, blank=True, null=True)
    id = models.AutoField()
    fechacreacion = models.DateTimeField(blank=True, null=True)
    fec_actualizacion = models.DateTimeField(blank=True, null=True)
    tipo_registro = models.IntegerField()
    nom_completousuario = models.CharField(max_length=100, blank=True, null=True)
    num_origenregistro = models.IntegerField()
    num_empleado = models.IntegerField()
    fbid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_clientes'


class CatClientesFraudeCoppel(models.Model):
    numusuario = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellidopaterno = models.CharField(max_length=30)
    apellidomaterno = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=-1)
    ciudad = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    calle = models.CharField(max_length=40)
    colonia = models.CharField(max_length=30)
    numcasa = models.CharField(max_length=12)
    clientecoppel = models.CharField(max_length=2)
    numclientecoppel = models.IntegerField()
    telefono = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    ext = models.CharField(max_length=20)
    cp = models.CharField(max_length=5)
    saldo = models.DecimalField(max_digits=65535, decimal_places=65535)
    otra = models.CharField(max_length=5)
    registro = models.CharField(max_length=1)
    correovalido = models.IntegerField()
    confirmado = models.CharField(max_length=1)
    interior = models.CharField(max_length=12)
    numciudad = models.IntegerField()
    numcolonia = models.IntegerField()
    numcalle = models.IntegerField()
    fechanacimiento = models.DateField()
    sexo = models.BooleanField()
    fecharegistro = models.DateField()
    celular = models.CharField(max_length=128, blank=True, null=True)
    entrecalles = models.CharField(max_length=-1, blank=True, null=True)
    domicilioobservaciones = models.CharField(max_length=-1, blank=True, null=True)
    id = models.AutoField()
    fechacreacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_clientes_fraude_coppel'


class CatClientesTrigg(models.Model):
    email = models.CharField(max_length=50, blank=True, null=True)
    numusuario_ant = models.IntegerField()
    numcliente_ant = models.IntegerField()
    password_ant = models.CharField(max_length=-1, blank=True, null=True)
    numusuario_act = models.IntegerField()
    numcliente_act = models.IntegerField()
    password_act = models.CharField(max_length=-1, blank=True, null=True)
    ipproceso = models.GenericIPAddressField(blank=True, null=True)
    nom_usuario = models.CharField(max_length=-1, blank=True, null=True)
    des_schema = models.CharField(max_length=-1, blank=True, null=True)
    nom_funcion = models.CharField(max_length=-1, blank=True, null=True)
    fec_movto = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_clientes_trigg'


class CatClientespromolg(models.Model):
    nombrecompleto = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    numfactura = models.IntegerField()
    promocorreos = models.SmallIntegerField()
    fecharegistro = models.DateField()

    class Meta:
        managed = False
        db_table = 'cat_clientespromolg'


class CatCodigoCobroservicio(models.Model):
    num_codigo = models.IntegerField(blank=True, null=True)
    num_precioventa = models.IntegerField(blank=True, null=True)
    num_costoenvio = models.IntegerField(blank=True, null=True)
    nom_descripcion = models.CharField(max_length=50, blank=True, null=True)
    num_area = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_codigo_cobroservicio'


class CatCodigosregionestelcel(models.Model):
    num_codigogeneral = models.CharField(max_length=-1)
    num_codigoregion = models.IntegerField()
    num_regiontelcel = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'cat_codigosregionestelcel'


class CatColores(models.Model):
    numcolor = models.SmallIntegerField(primary_key=True)
    desccolor = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cat_colores'


class CatCondicionproductomarketplace(models.Model):
    idu_condicion = models.BigIntegerField(primary_key=True)
    opc_codigocondicion = models.CharField(max_length=254)
    nom_condicion = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'cat_condicionproductomarketplace'
        unique_together = (('idu_condicion', 'opc_codigocondicion'),)
# Unable to inspect table 'cat_configs_feedmarketplace'
# The error was: permission denied for table cat_configs_feedmarketplace


class CatConfiguracionconvenios(models.Model):
    idu_configuracion = models.IntegerField()
    nom_configuracion = models.CharField(max_length=-1, blank=True, null=True)
    nom_valor = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_configuracionconvenios'


class CatConfiguraciones(models.Model):
    idu_configuracion = models.IntegerField(blank=True, null=True)
    des_valor1 = models.CharField(max_length=50, blank=True, null=True)
    des_valor2 = models.CharField(max_length=50, blank=True, null=True)
    des_valor3 = models.CharField(max_length=50, blank=True, null=True)
    des_configuracion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_configuraciones'


class CatConfiguracionesCobroenvio(models.Model):
    id = models.IntegerField(blank=True, null=True)
    nombreconfig = models.CharField(max_length=50, blank=True, null=True)
    value1 = models.IntegerField(blank=True, null=True)
    value2 = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    usuario = models.CharField(max_length=-1, blank=True, null=True)
    fechamodif = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_configuraciones_cobroenvio'


class CatConfiguracionvariables(models.Model):
    idu_configuracion = models.IntegerField(primary_key=True)
    des_configuracion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cat_configuracionvariables'


class CatCp99(models.Model):
    num_bodega = models.SmallIntegerField(blank=True, null=True)
    num_ciudad = models.SmallIntegerField(blank=True, null=True)
    num_codigopostal = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_cp99'


class CatCrciudades(models.Model):
    ciudad = models.SmallIntegerField(blank=True, null=True)
    nombreciudad = models.CharField(max_length=20, blank=True, null=True)
    keyx = models.AutoField()
    tipociudad = models.SmallIntegerField(blank=True, null=True)
    nivelvencido = models.SmallIntegerField(blank=True, null=True)
    antiguedadplaza = models.SmallIntegerField(blank=True, null=True)
    num_regioncobranzas = models.SmallIntegerField(blank=True, null=True)
    num_regiontienda = models.SmallIntegerField()
    prc_ctesbuenos = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_crciudades'


class CatCuentasbanco(models.Model):
    cuentabancoid = models.IntegerField(primary_key=True)
    numcodigo = models.ForeignKey('CatEstablecimientos', models.DO_NOTHING, db_column='numcodigo', blank=True, null=True)
    servicio = models.CharField(max_length=40)
    clave = models.CharField(max_length=40, blank=True, null=True)
    convenio = models.CharField(max_length=20, blank=True, null=True)
    sucursal = models.CharField(max_length=20, blank=True, null=True)
    cuenta = models.CharField(max_length=20, blank=True, null=True)
    longitudreferencia = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cat_cuentasbanco'


class CatCustomlabels(models.Model):
    idu_customlabel = models.AutoField(primary_key=True)
    nom_customlabel = models.TextField(unique=True)
    num_customlabel = models.IntegerField()
    nom_alias = models.TextField()

    class Meta:
        managed = False
        db_table = 'cat_customlabels'


class CatCustomlabelsMkp(models.Model):
    idu_customlabel = models.AutoField(primary_key=True)
    nom_customlabel = models.TextField(unique=True)
    num_customlabel = models.IntegerField()
    nom_alias = models.TextField()

    class Meta:
        managed = False
        db_table = 'cat_customlabels_mkp'


class CatDcfcelulares(models.Model):
    idu_registro = models.AutoField()
    nom_dcf = models.CharField(max_length=15)
    des_empresa = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'cat_dcfcelulares'


class CatDcfcelularesBackup(models.Model):
    idu_registro = models.IntegerField(blank=True, null=True)
    nom_dcf = models.CharField(max_length=15, blank=True, null=True)
    des_empresa = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_dcfcelulares_backup'


class CatDepartamentos(models.Model):
    numarea = models.OneToOneField(CatAreas, models.DO_NOTHING, db_column='numarea', primary_key=True)
    numdepto = models.SmallIntegerField()
    descdepto = models.CharField(max_length=50)
    activo = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_departamentos'
        unique_together = (('numarea', 'numdepto'),)


class CatDepartamentosArg(models.Model):
    num_area = models.SmallIntegerField(primary_key=True)
    num_departamento = models.SmallIntegerField()
    nom_departamento = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'cat_departamentos_arg'
        unique_together = (('num_area', 'num_departamento'),)


class CatDescripcioncuentacoppel(models.Model):
    idu_cuenta = models.SmallIntegerField(primary_key=True)
    nom_cuenta = models.CharField(max_length=50)
    des_cuenta = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cat_descripcioncuentacoppel'


class CatDetallescaracteristicas(models.Model):
    numcaracteristica = models.OneToOneField(CatCaracteristicas, models.DO_NOTHING, db_column='numcaracteristica', primary_key=True)
    numdetallecaracteristica = models.AutoField()
    nomdetallecaracteristica = models.CharField(max_length=150)
    beneficio = models.CharField(max_length=350)
    primario = models.IntegerField()
    activo = models.BooleanField()
    flag_indexacion = models.BooleanField(blank=True, null=True)
    idu_carga_masiva = models.ForeignKey('CtlCargasMasivasAtributos', models.DO_NOTHING, db_column='idu_carga_masiva', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_detallescaracteristicas'
        unique_together = (('numcaracteristica', 'numdetallecaracteristica'),)


class CatDiasinhabilesentregaropa(models.Model):
    descpais = models.CharField(max_length=-1)
    fechainhabil = models.DateField()
    opc_oficinaenvios = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_diasinhabilesentregaropa'


class CatDisponibilidades(models.Model):
    numdisponibilidad = models.SmallIntegerField(primary_key=True)
    disponibilidad = models.CharField(max_length=1)
    descdisponibilidad = models.CharField(max_length=65)
    fechaalta = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cat_disponibilidades'


class CatDivisiondeptos(models.Model):
    idudivisiondepto = models.AutoField(primary_key=True)
    nomdivisiondepto = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'cat_divisiondeptos'


class CatDnspoliticasCobroenvio(models.Model):
    num_bodega = models.SmallIntegerField(blank=True, null=True)
    nom_dns = models.CharField(max_length=60, blank=True, null=True)
    num_direccionip = models.CharField(max_length=30, blank=True, null=True)
    dnsdefault = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_dnspoliticas_cobroenvio'


class CatDomicilios(models.Model):
    nombre = models.CharField(max_length=-1, blank=True, null=True)
    apellidopaterno = models.CharField(max_length=-1, blank=True, null=True)
    apellidomaterno = models.CharField(max_length=-1, blank=True, null=True)
    estado = models.CharField(max_length=-1, blank=True, null=True)
    ciudad = models.CharField(max_length=-1, blank=True, null=True)
    colonia = models.CharField(max_length=-1, blank=True, null=True)
    calle = models.CharField(max_length=-1, blank=True, null=True)
    entrecalles = models.CharField(max_length=-1, blank=True, null=True)
    codigopostal = models.CharField(max_length=-1, blank=True, null=True)
    numcasa = models.CharField(max_length=10, blank=True, null=True)
    observaciones = models.CharField(max_length=-1, blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    id = models.AutoField()
    numciudad = models.IntegerField(blank=True, null=True)
    estatusborrado = models.IntegerField(blank=True, null=True)
    numcolonia = models.IntegerField(blank=True, null=True)
    alias = models.CharField(max_length=-1, blank=True, null=True)
    numinterior = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_domicilios'


class CatDomingoshabiles(models.Model):
    des_pais = models.CharField(max_length=-1)
    fec_domingohabil = models.DateField()

    class Meta:
        managed = False
        db_table = 'cat_domingoshabiles'


class CatEmbalajesoe(models.Model):
    idu_oficinadeenvios = models.BigIntegerField()
    num_tipoembalaje = models.SmallAutoField()
    nom_embalaje = models.CharField(max_length=-1)
    num_largo = models.IntegerField()
    num_ancho = models.IntegerField()
    num_alto = models.IntegerField()
    num_peso = models.IntegerField()
    flag_activo = models.SmallIntegerField()
    num_codigocondicion = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_embalajesoe'


class CatEmpresasaceptadas(models.Model):
    idu_empresa = models.SmallIntegerField()
    des_empresa = models.CharField(max_length=50)
    opc_empresaactiva = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cat_empresasaceptadas'


class CatEquivalenciaatributos(models.Model):
    idu_equivalencia = models.BigAutoField()
    des_valida = models.CharField(max_length=30)
    des_invalida = models.CharField(max_length=30)
    des_atributo = models.CharField(max_length=30)
    num_area = models.SmallIntegerField(primary_key=True)
    num_depto = models.SmallIntegerField()
    num_clase = models.SmallIntegerField()
    num_familia = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_equivalenciaatributos'
        unique_together = (('num_area', 'num_depto', 'num_clase', 'num_familia', 'des_valida', 'des_invalida'),)


class CatEstablecimientos(models.Model):
    numcodigo = models.CharField(primary_key=True, max_length=2)
    nomestablecimiento = models.CharField(max_length=20)
    nomabreviatura = models.CharField(max_length=5)
    longitud = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cat_establecimientos'


class CatEstados(models.Model):
    estado = models.SmallIntegerField(blank=True, null=True)
    nombreestado = models.CharField(max_length=25, blank=True, null=True)
    nombrecorto = models.CharField(max_length=4, blank=True, null=True)
    rango1 = models.IntegerField(blank=True, null=True)
    rango2 = models.IntegerField(blank=True, null=True)
    keyx = models.AutoField()

    class Meta:
        managed = False
        db_table = 'cat_estados'


class CatEstadosArg(models.Model):
    num_estado = models.SmallIntegerField(primary_key=True)
    nom_estado = models.CharField(max_length=-1)
    num_pais = models.SmallIntegerField()
    nom_pais = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'cat_estados_arg'


class CatEstatus(models.Model):
    numestatus = models.SmallIntegerField(primary_key=True)
    descestatus = models.CharField(max_length=55)

    class Meta:
        managed = False
        db_table = 'cat_estatus'


class CatEstatusReclasificados(models.Model):
    idu_codigo = models.BigAutoField()
    codigo = models.SmallIntegerField()
    descripcion = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'cat_estatus_reclasificados'


class CatEstatusbloqueo(models.Model):
    num_estatusbloqueo = models.SmallIntegerField(blank=True, null=True)
    des_estatusbloqueo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cat_estatusbloqueo'


class CatEstatuscodigoscommerce(models.Model):
    idu_estatus = models.AutoField(primary_key=True)
    nom_estatus = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cat_estatuscodigoscommerce'


class CatEstatuscodigoscoppel(models.Model):
    idu_estatus = models.AutoField(primary_key=True)
    nom_estatus = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cat_estatuscodigoscoppel'


class CatEstatuscodigosmarketplace(models.Model):
    idu_estatus = models.AutoField(primary_key=True)
    nom_estatus = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cat_estatuscodigosmarketplace'


class CatEstatuscorreomoto(models.Model):
    num_estatusmoto = models.IntegerField(blank=True, null=True)
    des_estatusmoto = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_estatuscorreomoto'


class CatEstatusemails(models.Model):
    num_estatus = models.SmallIntegerField(primary_key=True)
    des_estatus = models.CharField(max_length=50)
    fec_actualiza = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_estatusemails'


class CatEstatusordenmarketplace(models.Model):
    idu_estatusordenmk = models.AutoField(primary_key=True)
    nom_estatus = models.CharField(max_length=30)
    des_estatus = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'cat_estatusordenmarketplace'


class CatEstatuspedidocommerce(models.Model):
    idu_estatus = models.AutoField(primary_key=True)
    nom_estatus = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'cat_estatuspedidocommerce'


class CatEstatuspedidocoppel(models.Model):
    idu_estatus = models.AutoField(primary_key=True)
    nom_estatus = models.CharField(max_length=250)
    opc_afectacommerce = models.IntegerField()
    nom_estatus_tracking = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_estatuspedidocoppel'


class CatEstatuspendienteentregamoto(models.Model):
    num_estatusmoto = models.SmallIntegerField(primary_key=True)
    des_pendienteentregamoto = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cat_estatuspendienteentregamoto'


class CatEstatusreenvio(models.Model):
    id_estatus = models.SmallIntegerField(blank=True, null=True)
    tipo_estatus = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_estatusreenvio'


class CatEstatustarjetas(models.Model):
    num_estatus = models.SmallIntegerField(primary_key=True)
    des_estatus = models.CharField(max_length=50)
    fec_actualiza = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_estatustarjetas'


class CatEtiquetas(models.Model):
    idu_etiqueta = models.AutoField(primary_key=True)
    nom_area = models.TextField(blank=True, null=True)
    num_sku = models.IntegerField()
    nom_etiqueta = models.TextField()
    fec_asignacion = models.DateField()
    idu_customlabel = models.ForeignKey(CatCustomlabels, models.DO_NOTHING, db_column='idu_customlabel')

    class Meta:
        managed = False
        db_table = 'cat_etiquetas'
        unique_together = (('num_sku', 'nom_area', 'idu_customlabel'),)


class CatEtiquetasMkp(models.Model):
    idu_etiqueta = models.AutoField(primary_key=True)
    num_sku = models.TextField()
    nom_etiqueta = models.TextField()
    fec_asignacion = models.DateField()
    idu_customlabel = models.ForeignKey(CatCustomlabels, models.DO_NOTHING, db_column='idu_customlabel')

    class Meta:
        managed = False
        db_table = 'cat_etiquetas_mkp'
        unique_together = (('num_sku', 'idu_customlabel'),)


class CatEtiquetasfijas(models.Model):
    num_condicion = models.SmallIntegerField(primary_key=True)
    nom_condicion = models.CharField(max_length=50, blank=True, null=True)
    num_codigocondicion = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    idu_proceso = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_etiquetasfijas'


class CatEtiquetasinvespecial(models.Model):
    num_condicion = models.SmallIntegerField(primary_key=True)
    nom_condicion = models.CharField(max_length=50, blank=True, null=True)
    num_codigocondicion = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_etiquetasinvespecial'


class CatExistenciasminimas(models.Model):
    num_area = models.SmallIntegerField(primary_key=True)
    num_existenciaminima = models.SmallIntegerField()
    num_existenciaminimacommerce = models.SmallIntegerField()
    num_existenciaminimadescontinuado = models.SmallIntegerField()
    num_existenciaminima_productspredict = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_existenciasminimas'


class CatExistenciasminimasExclusivosCoppel(models.Model):
    num_area = models.SmallIntegerField()
    num_existenciaminima = models.SmallIntegerField()
    fec_actualizacion = models.DateTimeField(blank=True, null=True)
    editado_por = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_existenciasminimas_exclusivos_coppel'


class CatFamilias(models.Model):
    numarea = models.OneToOneField(CatClases, models.DO_NOTHING, db_column='numarea', primary_key=True)
    numdepto = models.SmallIntegerField()
    numclase = models.SmallIntegerField()
    numfamilia = models.SmallIntegerField()
    descfamilia = models.CharField(max_length=50)
    activo = models.SmallIntegerField()
    flagriesgo = models.SmallIntegerField()
    clv_plazo = models.SmallIntegerField()
    age_group = models.TextField()
    size_type = models.TextField()

    class Meta:
        managed = False
        db_table = 'cat_familias'
        unique_together = (('numarea', 'numdepto', 'numclase', 'numfamilia'),)


class CatFamiliasArg(models.Model):
    num_area = models.SmallIntegerField(primary_key=True)
    num_departamento = models.SmallIntegerField()
    num_clase = models.SmallIntegerField()
    num_familia = models.SmallIntegerField()
    nom_familia = models.CharField(max_length=-1)
    num_flagriesgo = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_familias_arg'
        unique_together = (('num_area', 'num_departamento', 'num_clase', 'num_familia'),)


class CatFamiliasendi(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numdepto = models.SmallIntegerField(blank=True, null=True)
    numclase = models.SmallIntegerField(blank=True, null=True)
    numfamilia = models.SmallIntegerField(blank=True, null=True)
    descfamilia = models.CharField(max_length=50, blank=True, null=True)
    activo = models.SmallIntegerField(blank=True, null=True)
    flagriesgo = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_familiasendi'


class CatFamiliasnopublicar(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    numdepto = models.SmallIntegerField()
    numclase = models.SmallIntegerField()
    numfamilia = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_familiasnopublicar'
        unique_together = (('numarea', 'numdepto', 'numclase', 'numfamilia'),)


class CatFamiliasnovendibles(models.Model):
    num_area = models.SmallIntegerField()
    num_depto = models.SmallIntegerField()
    num_clase = models.SmallIntegerField()
    num_familia = models.SmallIntegerField()
    num_activo = models.SmallIntegerField()
    fec_alta = models.DateField()

    class Meta:
        managed = False
        db_table = 'cat_familiasnovendibles'
# Unable to inspect table 'cat_feedmarketplace_generado'
# The error was: permission denied for table cat_feedmarketplace_generado
# Unable to inspect table 'cat_feedmarketplace_pendiente'
# The error was: permission denied for table cat_feedmarketplace_pendiente
# Unable to inspect table 'cat_feedmarketplace_publicado'
# The error was: permission denied for table cat_feedmarketplace_publicado


class CatFinalAsignacionInventarioArg(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=64)
    fulfillmentcentername = models.CharField(max_length=254)
    quantity = models.IntegerField()
    delete = models.SmallIntegerField()
    carga_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_final_asignacion_inventario_arg'
        unique_together = (('partnumber', 'fulfillmentcentername'),)


class CatFinalFiltroCategoriaArg(models.Model):
    catalogfilterid = models.CharField(max_length=10)
    catalogfiltername = models.CharField(max_length=64)
    storeidentifier = models.CharField(max_length=254)
    catalogidentifier = models.CharField(max_length=254)
    selectiontype = models.CharField(max_length=10)
    cataloggroupidentifier = models.CharField(max_length=254)
    comnditiongrouprelation = models.CharField(max_length=5)
    delete = models.SmallIntegerField()
    carga_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_final_filtro_categoria_arg'


class CatFinalInformacionCategoriasArg(models.Model):
    groupidentifier = models.CharField(max_length=64)
    topgroup = models.CharField(max_length=5)
    parentgroupidentifier = models.CharField(max_length=64)
    sequence = models.IntegerField()
    name = models.CharField(max_length=254)
    shortdescription = models.CharField(max_length=254)
    longdescription = models.CharField(max_length=1024)
    thumbnail = models.CharField(max_length=254)
    fullimage = models.CharField(max_length=254)
    published = models.SmallIntegerField()
    keyword = models.CharField(max_length=254)
    urlkeyword = models.CharField(max_length=254)
    pagetitle = models.CharField(max_length=254)
    metadescription = models.CharField(max_length=1024)
    delete = models.SmallIntegerField()
    field1 = models.CharField(max_length=254)
    field2 = models.CharField(max_length=254)
    carga_id = models.BigIntegerField(primary_key=True)
    order = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_final_informacion_categorias_arg'
        unique_together = (('carga_id', 'order'),)


class CatFinalInformacionProductosArg(models.Model):
    partnumber = models.CharField(max_length=20)
    type = models.CharField(max_length=15)
    parentpartnumber = models.CharField(max_length=20)
    parentgroupidentifier = models.CharField(max_length=30)
    name = models.CharField(max_length=128)
    shortdescription = models.CharField(max_length=254)
    longdescription = models.TextField()
    thumbnail = models.CharField(max_length=254)
    fullimage = models.CharField(max_length=254)
    available = models.SmallIntegerField()
    published = models.SmallIntegerField()
    buyable = models.SmallIntegerField()
    manufacturer = models.CharField(max_length=64)
    keyword = models.CharField(max_length=254)
    delete = models.SmallIntegerField()
    urlkeyword = models.CharField(max_length=254)
    metadescription = models.CharField(max_length=1024)
    pagetitle = models.CharField(max_length=254)
    carga_id = models.BigIntegerField(primary_key=True)
    order = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_final_informacion_productos_arg'
        unique_together = (('carga_id', 'order'),)


class CatFinalPrecioListaArg(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=20)
    listprice = models.IntegerField()
    currencycode = models.CharField(max_length=5)
    startdate = models.CharField(max_length=30)
    enddate = models.CharField(max_length=30)
    delete = models.SmallIntegerField()
    carga_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_final_precio_lista_arg'


class CatFinalPrecioOfertaArg(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=20)
    price = models.IntegerField()
    currencycode = models.CharField(max_length=5)
    startdate = models.CharField(max_length=30)
    enddate = models.CharField(max_length=30)
    delete = models.SmallIntegerField()
    carga_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_final_precio_oferta_arg'


class CatFinalRelacionCategoriaProductoArg(models.Model):
    partnumber = models.CharField(max_length=64)
    parentgroupidentifier = models.CharField(max_length=64)
    sequence = models.IntegerField()
    delete = models.SmallIntegerField()
    carga_id = models.BigIntegerField(primary_key=True)
    order = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_final_relacion_categoria_producto_arg'
        unique_together = (('carga_id', 'order'),)


class CatFuncionesTdavirtual(models.Model):
    idu_funcion = models.AutoField(primary_key=True)
    nom_funcion = models.CharField(max_length=80)
    num_tipofuncion = models.IntegerField(blank=True, null=True)
    num_area = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_funciones_tdavirtual'


class CatGaleriaarticulo(models.Model):
    numarea = models.ForeignKey(CatArticulos, models.DO_NOTHING, db_column='numarea')
    numcodigo = models.IntegerField()
    nomimagen = models.CharField(max_length=30)
    numgaleria = models.BigAutoField()
    fecha = models.DateTimeField(blank=True, null=True)
    des_textoalternativo = models.TextField()
    num_imagenes = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_galeriaarticulo'


class CatGaleriaarticuloPett(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    nomimagen = models.CharField(max_length=30, blank=True, null=True)
    numgaleria = models.BigIntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    des_textoalternativo = models.TextField(blank=True, null=True)
    num_imagenes = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_galeriaarticulo_pett'


class CatGuias(models.Model):
    nu_guia = models.IntegerField(primary_key=True)
    guia_inicial = models.IntegerField()
    guia_final = models.IntegerField()
    fh_alta_guia = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cat_guias'
# Unable to inspect table 'cat_homologacion_dcf_mkp'
# The error was: permission denied for table cat_homologacion_dcf_mkp


class CatIconosAreasweb(models.Model):
    idu_icono = models.AutoField(primary_key=True)
    numareaweb = models.OneToOneField(CatAreasweb, models.DO_NOTHING, db_column='numareaweb')
    img_icono = models.TextField()
    fec_alta = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cat_iconos_areasweb'


class CatIdentificadorunico(models.Model):
    numarea = models.OneToOneField(CatArticulos, models.DO_NOTHING, db_column='numarea', primary_key=True)
    numcodigo = models.IntegerField()
    numidentificador = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_identificadorunico'
        unique_together = (('numarea', 'numcodigo'),)


class CatImgslider(models.Model):
    nomimagen = models.CharField(max_length=170, blank=True, null=True)
    linkimagen = models.CharField(max_length=255, blank=True, null=True)
    linktexto = models.CharField(max_length=255, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_expira = models.DateField(blank=True, null=True)
    titulo = models.CharField(max_length=150, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    orden = models.AutoField()

    class Meta:
        managed = False
        db_table = 'cat_imgslider'


class CatImgsliderKiosko(models.Model):
    nomimagen = models.CharField(max_length=170, blank=True, null=True)
    linkimagen = models.CharField(max_length=255, blank=True, null=True)
    linktexto = models.CharField(max_length=255, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_expira = models.DateField(blank=True, null=True)
    titulo = models.CharField(max_length=150, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    orden = models.AutoField()

    class Meta:
        managed = False
        db_table = 'cat_imgslider_kiosko'


class CatIptiendasTdv(models.Model):
    idu_tienda = models.SmallIntegerField()
    nom_tienda = models.CharField(max_length=30)
    num_ciudad = models.SmallIntegerField()
    nom_ciudad = models.CharField(max_length=50)
    num_iva = models.SmallIntegerField()
    num_direccionip = models.TextField(unique=True)  # This field type is a guess.
    num_flagliberado = models.SmallIntegerField()
    keyx = models.AutoField()
    cod_tipo_tienda = models.ForeignKey('CatTiposTiendas', models.DO_NOTHING, db_column='cod_tipo_tienda', blank=True, null=True)
    cod_tamanio_tienda = models.ForeignKey('CatTamaniosTiendas', models.DO_NOTHING, db_column='cod_tamanio_tienda', blank=True, null=True)
    idu_dispositivo = models.IntegerField()
    idu_geonode = models.IntegerField()
    idu_identifier = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'cat_iptiendas_tdv'


class CatIptiendasTdvRes(models.Model):
    idu_tienda = models.SmallIntegerField()
    nom_tienda = models.CharField(max_length=30)
    num_ciudad = models.SmallIntegerField()
    nom_ciudad = models.CharField(max_length=50)
    num_iva = models.SmallIntegerField()
    num_direccionip = models.TextField()  # This field type is a guess.
    num_flagliberado = models.SmallIntegerField()
    keyx = models.AutoField()
    cod_tipo_tienda = models.ForeignKey('CatTiposTiendas', models.DO_NOTHING, db_column='cod_tipo_tienda', blank=True, null=True)
    cod_tamanio_tienda = models.ForeignKey('CatTamaniosTiendas', models.DO_NOTHING, db_column='cod_tamanio_tienda', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_iptiendas_tdv_res'


class CatIptiendastdvdispositivos(models.Model):
    idu_dispositivo = models.IntegerField(primary_key=True)
    des_dispositivo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cat_iptiendastdvdispositivos'


class CatLenceria(models.Model):
    numdepto = models.SmallIntegerField(primary_key=True)
    numclase = models.SmallIntegerField()
    numfamilia = models.SmallIntegerField()
    descripcion = models.CharField(max_length=264, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_lenceria'
        unique_together = (('numdepto', 'numclase', 'numfamilia'),)


class CatLinks(models.Model):
    id_subcomponente = models.IntegerField(primary_key=True)
    id_tipo = models.IntegerField()
    nom_link = models.CharField(max_length=200)
    ban_promocion = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cat_links'
        unique_together = (('id_subcomponente', 'id_tipo'),)


class CatLogTiempoAire(models.Model):
    idu_log = models.AutoField(primary_key=True)
    desc_log = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cat_log_tiempo_aire'


class CatMacrocategorias(models.Model):
    idu_macrocategoria = models.SmallAutoField(primary_key=True)
    nom_macrocategoria = models.TextField(unique=True)
    num_orden = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_macrocategorias'


class CatMarcas(models.Model):
    numarea = models.OneToOneField(CatAreas, models.DO_NOTHING, db_column='numarea', primary_key=True)
    nummarca = models.IntegerField()
    descmarca = models.CharField(max_length=30)
    exclusivacoppel = models.SmallIntegerField()
    activo = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_marcas'
        unique_together = (('numarea', 'nummarca'),)


class CatMatrizreglasconvenios(models.Model):
    idu_matriz = models.IntegerField()
    nom_situacionfinanciera = models.CharField(max_length=-1, blank=True, null=True)
    nom_montovencido = models.CharField(max_length=-1, blank=True, null=True)
    idu_montominimopagar = models.IntegerField(blank=True, null=True)
    nom_montominimopagar = models.CharField(max_length=-1, blank=True, null=True)
    nom_desctiempopago = models.CharField(max_length=-1, blank=True, null=True)
    dias_tiempopago = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_matrizreglasconvenios'


class CatMensajeriaactiva(models.Model):
    num_mensajeria = models.IntegerField(primary_key=True)
    nom_mensajeria = models.CharField(max_length=50, blank=True, null=True)
    flag_enabled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_mensajeriaactiva'


class CatMensajeriaestatus(models.Model):
    num_mensajeria = models.ForeignKey(CatMensajeriaactiva, models.DO_NOTHING, db_column='num_mensajeria', blank=True, null=True)
    idu_clave = models.CharField(primary_key=True, max_length=2)
    nom_descripcion = models.CharField(max_length=50)
    nom_tipomovimiento = models.CharField(max_length=10, blank=True, null=True)
    num_estatuscoppel = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_mensajeriaestatus'
        unique_together = (('idu_clave', 'nom_descripcion'),)


class CatMensajeticket(models.Model):
    idu_mensaje = models.IntegerField(primary_key=True)
    des_mensaje = models.CharField(max_length=150)
    opc_tipoticket = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_mensajeticket'


class CatMenuespeciales(models.Model):
    nummenu = models.BigAutoField(primary_key=True)
    numarea = models.IntegerField(blank=True, null=True)
    nombremenu = models.TextField(blank=True, null=True)
    ordenamiento = models.IntegerField(blank=True, null=True)
    publicar = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_menuespeciales'


class CatModulosSistema(models.Model):
    idmodulo = models.AutoField(primary_key=True)
    nommodulo = models.TextField(blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_modulos_sistema'


class CatMotivosCancelacion(models.Model):
    idu_motivos = models.AutoField(primary_key=True)
    desc_motivoscancelacion = models.CharField(max_length=-1)
    flag_mostrar_cat = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_motivos_cancelacion'


class CatMotivosdevolucion(models.Model):
    idu_motivo = models.IntegerField()
    nom_motivo = models.CharField(max_length=-1, blank=True, null=True)
    nom_trigger = models.CharField(max_length=-1, blank=True, null=True)
    des_devolucioncopy = models.CharField(max_length=-1, blank=True, null=True)
    des_codigobarraropa = models.CharField(max_length=-1, blank=True, null=True)
    des_codigobarramuebles = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_motivosdevolucion'


class CatMovimientoregistroempleado(models.Model):
    idu_movimientoregistroempelado = models.SmallIntegerField()
    des_movimiento = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_movimientoregistroempleado'


class CatMulticarrier(models.Model):
    idu_multicarrier = models.IntegerField()
    des_multicarrier = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'cat_multicarrier'


class CatNodosLogisticosV9(models.Model):
    numbodega = models.IntegerField(blank=True, null=True)
    nomstore = models.CharField(max_length=-1, blank=True, null=True)
    xcitystore_id = models.IntegerField(blank=True, null=True)
    code_city = models.IntegerField(blank=True, null=True)
    coppel_name_city = models.CharField(max_length=-1, blank=True, null=True)
    geoloc_name_city = models.CharField(max_length=-1, blank=True, null=True)
    stateprovabbr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_nodos_logisticos_v9'


class CatOeBodegas(models.Model):
    idu_bodega = models.AutoField(unique=True)
    num_bodega = models.IntegerField(primary_key=True)
    nom_bodega = models.CharField(max_length=-1)
    opc_activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cat_oe_bodegas'
        unique_together = (('num_bodega', 'opc_activo'),)


class CatOecarta(models.Model):
    id_carta = models.AutoField()
    des_carta = models.CharField(max_length=20, blank=True, null=True)
    idu_oficinadeenvios = models.BigIntegerField(blank=True, null=True)
    padding_left = models.CharField(max_length=10, blank=True, null=True)
    padding_right = models.CharField(max_length=10, blank=True, null=True)
    padding_top = models.CharField(max_length=10, blank=True, null=True)
    font_size = models.CharField(max_length=10, blank=True, null=True)
    margin_top = models.CharField(max_length=10, blank=True, null=True)
    margin_bottom = models.CharField(max_length=10, blank=True, null=True)
    margin_left = models.CharField(max_length=10, blank=True, null=True)
    margin_right = models.CharField(max_length=10, blank=True, null=True)
    opc_activo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_oecarta'


class CatOedocumentacion(models.Model):
    idu_documento = models.AutoField()
    nom_documento = models.CharField(max_length=-1, blank=True, null=True)
    flag_activo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_oedocumentacion'


class CatOeipsOficinadeenvios(models.Model):
    idu_direccionip = models.AutoField()
    num_direccionip = models.TextField(primary_key=True)  # This field type is a guess.
    idu_oficinadeenvios = models.IntegerField()
    opc_activo = models.BooleanField()
    fec_registro = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    num_empleadoalta = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_oeips_oficinadeenvios'
        unique_together = (('num_direccionip', 'idu_oficinadeenvios', 'opc_activo'),)


class CatOerangocolores(models.Model):
    idu_color = models.AutoField()
    num_rango_inicio = models.IntegerField()
    num_rango_final = models.IntegerField()
    num_codigo_color = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'cat_oerangocolores'


class CatOfertasNoPublicadas(models.Model):
    offer_id = models.IntegerField(blank=True, null=True)
    product_sku = models.CharField(max_length=-1, blank=True, null=True)
    min_shipping_price = models.CharField(max_length=-1, blank=True, null=True)
    min_shipping_price_additional = models.CharField(max_length=-1, blank=True, null=True)
    min_shipping_zone = models.CharField(max_length=-1, blank=True, null=True)
    min_shipping_type = models.CharField(max_length=-1, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True)
    price_additional_info = models.CharField(max_length=-1, blank=True, null=True)
    quantity = models.CharField(max_length=-1, blank=True, null=True)
    description = models.CharField(max_length=-1, blank=True, null=True)
    state_code = models.CharField(max_length=-1, blank=True, null=True)
    shop_id = models.IntegerField(blank=True, null=True)
    shop_name = models.CharField(max_length=-1, blank=True, null=True)
    professional = models.CharField(max_length=-1, blank=True, null=True)
    premium = models.CharField(max_length=-1, blank=True, null=True)
    logistic_class = models.CharField(max_length=-1, blank=True, null=True)
    active = models.CharField(max_length=-1, blank=True, null=True)
    favorite_rank = models.CharField(max_length=-1, blank=True, null=True)
    channels = models.CharField(max_length=-1, blank=True, null=True)
    deleted = models.CharField(max_length=-1, blank=True, null=True)
    origin_price = models.CharField(max_length=-1, blank=True, null=True)
    discount_start_date = models.CharField(max_length=-1, blank=True, null=True)
    discount_end_date = models.CharField(max_length=-1, blank=True, null=True)
    available_start_date = models.CharField(max_length=-1, blank=True, null=True)
    available_end_date = models.CharField(max_length=-1, blank=True, null=True)
    discount_price = models.CharField(max_length=-1, blank=True, null=True)
    currency_iso_code = models.CharField(max_length=-1, blank=True, null=True)
    discount_ranges = models.CharField(max_length=-1, blank=True, null=True)
    leadtime_to_ship = models.CharField(max_length=-1, blank=True, null=True)
    allow_quote_requests = models.CharField(max_length=-1, blank=True, null=True)
    price_ranges = models.CharField(max_length=-1, blank=True, null=True)
    fulfillment_center_code = models.CharField(max_length=-1, blank=True, null=True)
    shop_sku = models.CharField(max_length=-1, blank=True, null=True)
    cfwarrantypolicy = models.CharField(max_length=-1, blank=True, null=True)
    cfwarrantyperiod = models.CharField(max_length=-1, blank=True, null=True)
    cfshippingpackageweight = models.CharField(max_length=-1, blank=True, null=True)
    cfshippingpackageheight = models.CharField(max_length=-1, blank=True, null=True)
    cfshippingpackagelength = models.CharField(max_length=-1, blank=True, null=True)
    cfshippingpackagewidth = models.CharField(max_length=-1, blank=True, null=True)
    cfproducttaxid = models.CharField(max_length=-1, blank=True, null=True)
    measurement_units = models.CharField(max_length=-1, blank=True, null=True)
    imkp = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_ofertas_no_publicadas'


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

    class Meta:
        managed = False
        db_table = 'cat_ofertasmarketplace'
        unique_together = (('idu_oferta', 'idu_producto'),)


class CatOficinasdeenvios(models.Model):
    idu_oficinadeenvios = models.BigIntegerField()
    nom_oficinadeenvios = models.CharField(max_length=-1, blank=True, null=True)
    num_bodega = models.IntegerField()
    fec_registro = models.DateTimeField(blank=True, null=True)
    fec_actualizacion = models.DateTimeField(blank=True, null=True)
    num_empleadoalta = models.BigIntegerField()
    opc_activo = models.BooleanField()
    des_empresa = models.CharField(max_length=-1)
    des_contacto = models.CharField(max_length=-1)
    des_telefono = models.CharField(max_length=-1)
    des_direccion = models.CharField(max_length=-1)
    des_colonia = models.CharField(max_length=-1)
    clv_direccion = models.CharField(max_length=-1)
    des_ciudad = models.CharField(max_length=-1)
    des_codigo_pais = models.CharField(max_length=-1)
    num_codigo_postal = models.CharField(max_length=-1)
    des_codigo_estado = models.CharField(max_length=-1)
    nom_conf_basedatos = models.CharField(max_length=-1, blank=True, null=True)
    des_numero = models.CharField(max_length=-1, blank=True, null=True)
    des_referencia = models.CharField(max_length=-1, blank=True, null=True)
    des_ciudad_email = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_oficinasdeenvios'


class CatOpcionbloqueo(models.Model):
    num_estatusbloqueo = models.SmallIntegerField()
    num_opcionbloqueo = models.SmallIntegerField(blank=True, null=True)
    des_opcionbloqueo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cat_opcionbloqueo'
# Unable to inspect table 'cat_origen_devoluciones'
# The error was: permission denied for table cat_origen_devoluciones


class CatOutstock(models.Model):
    idu_outstock = models.TextField(primary_key=True)
    num_ropa_linea = models.IntegerField()
    num_ropa_saldo = models.IntegerField()
    num_muebles_enlinea = models.IntegerField()
    num_muebles_descontinuados = models.IntegerField()
    num_muebles_ventafuturo = models.IntegerField()
    fec_outstock = models.DateField()
    num_marketplace = models.IntegerField()
    num_ropa_minimo_stock = models.IntegerField(blank=True, null=True)
    num_muebles_minimo_stock = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_outstock'


class CatPaginasEstaticas(models.Model):
    id_pagina = models.AutoField()
    titulo = models.CharField(max_length=70)
    meta_description = models.CharField(max_length=250)
    meta_keywords = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    tipo_pagina = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_paginas_estaticas'


class CatPaginasEstaticasDl(models.Model):
    id_pagina = models.AutoField()
    categoria = models.CharField(max_length=70)
    titulo = models.CharField(max_length=70)
    meta_description = models.CharField(max_length=250)
    meta_keywords = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    tipo_pagina = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_paginas_estaticas_dl'


class CatPalabrasreemplazar(models.Model):
    numpalabra = models.SmallIntegerField(blank=True, null=True)
    descpalabra = models.CharField(max_length=10, blank=True, null=True)
    descpalabrareemplazar = models.CharField(max_length=50)
    activo = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_palabrasreemplazar'


class CatPaqueteras(models.Model):
    idu_paquetera = models.IntegerField()
    des_paquetera = models.CharField(max_length=-1)
    nom_trigger = models.CharField(max_length=-1, blank=True, null=True)
    des_link_rastreo = models.CharField(max_length=-1, blank=True, null=True)
    num_tel_paquetera = models.CharField(max_length=-1, blank=True, null=True)
    num_ext_paquetera = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_paqueteras'


class CatPartnumberproductosmarketplace(models.Model):
    idu_productomirakl = models.CharField(max_length=254)
    nom_partnumber = models.CharField(max_length=254)
    idu_categoria = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_partnumberproductosmarketplace'


class CatPerfiles(models.Model):
    idperfil = models.AutoField(primary_key=True)
    nomperfil = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_perfiles'


class CatPermisosadminmarketplace(models.Model):
    idu_permiso = models.SmallIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    fec_alta = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cat_permisosadminmarketplace'


class CatPermisosoe(models.Model):
    idu_permiso = models.IntegerField(blank=True, null=True)
    des_permiso = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_permisosoe'


class CatPlantillascorreo(models.Model):
    idu_plantilla = models.AutoField(primary_key=True)
    nom_trigger = models.CharField(max_length=100)
    nom_plantilla = models.CharField(max_length=250)
    des_plantilla = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'cat_plantillascorreo'


class CatPosicioneslayout(models.Model):
    idu_posicion = models.AutoField(primary_key=True)
    num_pasillo = models.IntegerField()
    nom_posicion = models.CharField(max_length=20)
    nom_letra = models.CharField(max_length=20)
    num_nivel = models.IntegerField()
    num_columna = models.IntegerField()
    opc_activo = models.BooleanField()
    num_letraspasillo = models.IntegerField()
    num_codigobarra = models.BigIntegerField()
    num_bodega = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cat_posicioneslayout'


class CatPosicionesracks(models.Model):
    idu_rack = models.IntegerField(primary_key=True)
    nom_letrarack = models.CharField(max_length=10, blank=True, null=True)
    num_codigobarra = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_posicionesracks'
        unique_together = (('idu_rack', 'num_codigobarra'),)


class CatPrecioArg(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=20)
    price = models.IntegerField()
    carga_id = models.BigIntegerField()
    updated = models.DateTimeField()
    offerprice = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cat_precio_arg'


class CatPrecioDeltaArg(models.Model):
    carga_id = models.BigIntegerField(primary_key=True)
    partnumber = models.CharField(max_length=20)
    price = models.IntegerField(blank=True, null=True)
    offerprice = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cat_precio_delta_arg'
        unique_together = (('carga_id', 'partnumber'),)


class CatPrecioNuevoArg(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=20)
    price = models.IntegerField()
    offerprice = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cat_precio_nuevo_arg'


class CatPreferenciasUsuarios(models.Model):
    idu_preferencias = models.AutoField(primary_key=True)
    desc_preferencias_clientes = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'cat_preferencias_usuarios'


class CatPreguntas(models.Model):
    idu_pregunta = models.IntegerField()
    nom_pregunta = models.CharField(max_length=-1, blank=True, null=True)
    flag_activo = models.BooleanField(blank=True, null=True)
    num_orden = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_preguntas'


class CatPreposiciones(models.Model):
    numpreposicion = models.SmallIntegerField()
    descpreposicion = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'cat_preposiciones'


class CatProcesosOficinadeenvios(models.Model):
    idu_proceso = models.AutoField()
    nom_proceso = models.CharField(max_length=-1, blank=True, null=True)
    fec_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_procesos_oficinadeenvios'


class CatProcesosTdavirtual(models.Model):
    idu_proceso = models.AutoField(primary_key=True)
    nom_proceso = models.CharField(max_length=80)
    des_proceso = models.CharField(max_length=100)
    hor_ejecucion = models.TimeField()

    class Meta:
        managed = False
        db_table = 'cat_procesos_tdavirtual'


class CatProductoCategoriaRelArg(models.Model):
    partnumber = models.OneToOneField('CatProductosArg', models.DO_NOTHING, db_column='partnumber', primary_key=True)
    parentgroupidentifier = models.ForeignKey(CatCategoriasArg, models.DO_NOTHING, db_column='parentgroupidentifier')
    sequence = models.IntegerField()
    delete = models.SmallIntegerField()
    carga_id = models.BigIntegerField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cat_producto_categoria_rel_arg'
        unique_together = (('partnumber', 'parentgroupidentifier'), ('carga_id', 'partnumber', 'parentgroupidentifier'),)


class CatProductoCategoriaRelArgPrueba(models.Model):
    partnumber = models.CharField(max_length=64, blank=True, null=True)
    parentgroupidentifier = models.CharField(max_length=64, blank=True, null=True)
    sequence = models.FloatField(blank=True, null=True)
    delete = models.SmallIntegerField(blank=True, null=True)
    carga_id = models.BigIntegerField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_producto_categoria_rel_arg_prueba'


class CatProductoCategoriaRelDataImportArg(models.Model):
    carga_id = models.BigIntegerField(primary_key=True)
    partnumber = models.CharField(max_length=64)
    parentgroupidentifier = models.CharField(max_length=64)
    sequence = models.IntegerField()
    delete = models.SmallIntegerField()
    order = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_producto_categoria_rel_data_import_arg'
        unique_together = (('carga_id', 'partnumber', 'parentgroupidentifier'),)


class CatProductoCategoriaRelDeltaArg(models.Model):
    carga_id = models.BigIntegerField(primary_key=True)
    partnumber = models.CharField(max_length=64)
    parentgroupidentifier = models.CharField(max_length=64)
    sequence = models.IntegerField()
    delete = models.SmallIntegerField()
    order = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_producto_categoria_rel_delta_arg'
        unique_together = (('carga_id', 'partnumber', 'parentgroupidentifier'),)


class CatProductoDataImportArg(models.Model):
    carga_id = models.BigIntegerField(primary_key=True)
    partnumber = models.CharField(max_length=20)
    type = models.CharField(max_length=15)
    parentpartnumber = models.CharField(max_length=20)
    parentgroupidentifier = models.CharField(max_length=30)
    name = models.CharField(max_length=128)
    shortdescription = models.CharField(max_length=254)
    longdescription = models.TextField()
    thumbnail = models.CharField(max_length=254)
    fullimage = models.CharField(max_length=254)
    available = models.SmallIntegerField()
    published = models.SmallIntegerField()
    buyable = models.SmallIntegerField()
    manufacturer = models.CharField(max_length=64)
    keyword = models.CharField(max_length=254)
    delete = models.SmallIntegerField()
    urlkeyword = models.CharField(max_length=254)
    metadescription = models.CharField(max_length=1024)
    pagetitle = models.CharField(max_length=254)
    hash = models.BigIntegerField()
    order = models.BigIntegerField()
    num_area = models.SmallIntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_producto_data_import_arg'
        unique_together = (('carga_id', 'partnumber'),)


class CatProductosArg(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=20)
    type = models.CharField(max_length=15)
    parentpartnumber = models.CharField(max_length=20)
    parentgroupidentifier = models.CharField(max_length=30)
    name = models.CharField(max_length=128)
    shortdescription = models.CharField(max_length=254)
    longdescription = models.TextField()
    thumbnail = models.CharField(max_length=254)
    fullimage = models.CharField(max_length=254)
    available = models.SmallIntegerField()
    published = models.SmallIntegerField()
    buyable = models.SmallIntegerField()
    manufacturer = models.CharField(max_length=64)
    keyword = models.CharField(max_length=254)
    delete = models.SmallIntegerField()
    urlkeyword = models.CharField(max_length=254)
    metadescription = models.CharField(max_length=1024)
    pagetitle = models.CharField(max_length=254)
    hash = models.BigIntegerField()
    num_area = models.SmallIntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.SmallIntegerField()
    carga_id = models.SmallIntegerField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cat_productos_arg'
        unique_together = (('carga_id', 'partnumber'),)


class CatProductosArgPrueba(models.Model):
    partnumber = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=15, blank=True, null=True)
    parentpartnumber = models.CharField(max_length=20, blank=True, null=True)
    parentgroupidentifier = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    shortdescription = models.CharField(max_length=254, blank=True, null=True)
    longdescription = models.TextField(blank=True, null=True)
    thumbnail = models.CharField(max_length=254, blank=True, null=True)
    fullimage = models.CharField(max_length=254, blank=True, null=True)
    available = models.SmallIntegerField(blank=True, null=True)
    published = models.SmallIntegerField(blank=True, null=True)
    buyable = models.SmallIntegerField(blank=True, null=True)
    manufacturer = models.CharField(max_length=64, blank=True, null=True)
    keyword = models.CharField(max_length=254, blank=True, null=True)
    delete = models.SmallIntegerField(blank=True, null=True)
    urlkeyword = models.CharField(max_length=254, blank=True, null=True)
    metadescription = models.CharField(max_length=1024, blank=True, null=True)
    pagetitle = models.CharField(max_length=254, blank=True, null=True)
    hash = models.BigIntegerField(blank=True, null=True)
    num_area = models.SmallIntegerField(blank=True, null=True)
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.SmallIntegerField(blank=True, null=True)
    carga_id = models.SmallIntegerField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_productos_arg_prueba'


class CatProductosArgTmp(models.Model):
    partnumber = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=15, blank=True, null=True)
    parentpartnumber = models.CharField(max_length=20, blank=True, null=True)
    parentgroupidentifier = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    shortdescription = models.TextField(blank=True, null=True)
    longdescription = models.TextField(blank=True, null=True)
    thumbnail = models.CharField(max_length=1024, blank=True, null=True)
    fullimage = models.CharField(max_length=1024, blank=True, null=True)
    available = models.SmallIntegerField(blank=True, null=True)
    published = models.SmallIntegerField(blank=True, null=True)
    buyable = models.SmallIntegerField(blank=True, null=True)
    manufacturer = models.CharField(max_length=64, blank=True, null=True)
    keyword = models.CharField(max_length=1024, blank=True, null=True)
    delete = models.SmallIntegerField(blank=True, null=True)
    urlkeyword = models.CharField(max_length=1024, blank=True, null=True)
    metadescription = models.CharField(max_length=1024, blank=True, null=True)
    pagetitle = models.CharField(max_length=1024, blank=True, null=True)
    hash = models.BigIntegerField(blank=True, null=True)
    num_area = models.SmallIntegerField(blank=True, null=True)
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.SmallIntegerField(blank=True, null=True)
    carga_id = models.SmallIntegerField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_productos_arg_tmp'


class CatProductosDeltaArg(models.Model):
    carga_id = models.BigIntegerField(primary_key=True)
    partnumber = models.CharField(max_length=20)
    type = models.CharField(max_length=15)
    parentpartnumber = models.CharField(max_length=20)
    parentgroupidentifier = models.CharField(max_length=30)
    name = models.CharField(max_length=128)
    shortdescription = models.CharField(max_length=254)
    longdescription = models.TextField()
    thumbnail = models.CharField(max_length=254)
    fullimage = models.CharField(max_length=254)
    available = models.SmallIntegerField()
    published = models.SmallIntegerField()
    buyable = models.SmallIntegerField()
    manufacturer = models.CharField(max_length=64)
    keyword = models.CharField(max_length=254)
    delete = models.SmallIntegerField()
    urlkeyword = models.CharField(max_length=254)
    metadescription = models.CharField(max_length=1024)
    pagetitle = models.CharField(max_length=254)
    hash = models.BigIntegerField()
    order = models.BigIntegerField()
    num_area = models.SmallIntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_productos_delta_arg'
        unique_together = (('carga_id', 'partnumber'), ('carga_id', 'hash', 'partnumber'),)
# Unable to inspect table 'cat_productosconsultados_gmc'
# The error was: permission denied for table cat_productosconsultados_gmc


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


class CatProductosmiraklApi(models.Model):
    offer_id = models.IntegerField(blank=True, null=True)
    product_sku = models.CharField(max_length=-1, blank=True, null=True)
    min_shipping_price = models.CharField(max_length=-1, blank=True, null=True)
    min_shipping_price_additional = models.CharField(max_length=-1, blank=True, null=True)
    min_shipping_zone = models.CharField(max_length=-1, blank=True, null=True)
    min_shipping_type = models.CharField(max_length=-1, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True)
    price_additional_info = models.CharField(max_length=-1, blank=True, null=True)
    quantity = models.CharField(max_length=-1, blank=True, null=True)
    description = models.CharField(max_length=-1, blank=True, null=True)
    state_code = models.CharField(max_length=-1, blank=True, null=True)
    shop_id = models.IntegerField(blank=True, null=True)
    shop_name = models.CharField(max_length=-1, blank=True, null=True)
    professional = models.CharField(max_length=-1, blank=True, null=True)
    premium = models.CharField(max_length=-1, blank=True, null=True)
    logistic_class = models.CharField(max_length=-1, blank=True, null=True)
    active = models.CharField(max_length=-1, blank=True, null=True)
    favorite_rank = models.CharField(max_length=-1, blank=True, null=True)
    channels = models.CharField(max_length=-1, blank=True, null=True)
    deleted = models.CharField(max_length=-1, blank=True, null=True)
    origin_price = models.CharField(max_length=-1, blank=True, null=True)
    discount_start_date = models.CharField(max_length=-1, blank=True, null=True)
    discount_end_date = models.CharField(max_length=-1, blank=True, null=True)
    available_start_date = models.CharField(max_length=-1, blank=True, null=True)
    available_end_date = models.CharField(max_length=-1, blank=True, null=True)
    discount_price = models.CharField(max_length=-1, blank=True, null=True)
    currency_iso_code = models.CharField(max_length=-1, blank=True, null=True)
    discount_ranges = models.CharField(max_length=-1, blank=True, null=True)
    leadtime_to_ship = models.CharField(max_length=-1, blank=True, null=True)
    allow_quote_requests = models.CharField(max_length=-1, blank=True, null=True)
    price_ranges = models.CharField(max_length=-1, blank=True, null=True)
    fulfillment_center_code = models.CharField(max_length=-1, blank=True, null=True)
    shop_sku = models.CharField(max_length=-1, blank=True, null=True)
    cfwarrantypolicy = models.CharField(max_length=-1, blank=True, null=True)
    cfwarrantyperiod = models.CharField(max_length=-1, blank=True, null=True)
    cfshippingpackageweight = models.CharField(max_length=-1, blank=True, null=True)
    cfshippingpackageheight = models.CharField(max_length=-1, blank=True, null=True)
    cfshippingpackagelength = models.CharField(max_length=-1, blank=True, null=True)
    cfshippingpackagewidth = models.CharField(max_length=-1, blank=True, null=True)
    cfproducttaxid = models.CharField(max_length=-1, blank=True, null=True)
    measurement_units = models.CharField(max_length=-1, blank=True, null=True)
    imkp = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_productosmirakl_api'


class CatPromocionesmarketplace(models.Model):
    idu_promocion = models.BigAutoField(primary_key=True)
    idu_tienda = models.BigIntegerField()
    num_codigopromocion = models.CharField(max_length=254)
    fec_creacionmirakl = models.DateTimeField()
    fec_finpromocion = models.DateTimeField()
    des_descripcion = models.CharField(max_length=2048)
    des_url = models.CharField(max_length=254)
    num_porcientodescuento = models.IntegerField()
    num_descuento = models.IntegerField()
    num_regalos = models.SmallIntegerField()
    opc_recompensacompra = models.BooleanField()
    fec_iniciopromocion = models.DateTimeField()
    opc_estado = models.CharField(max_length=50)
    opc_tipo = models.CharField(max_length=50)
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    opc_estatus = models.CharField(max_length=10)
    nom_actualiza = models.CharField(max_length=254)
    opc_procesado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_promocionesmarketplace'
        unique_together = (('idu_promocion', 'idu_tienda'),)


class CatPuestosvendedorligueclientesdig(models.Model):
    numpuesto = models.IntegerField(blank=True, null=True)
    nombrepuesto = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_puestosvendedorligueclientesdig'


class CatRangoprecios(models.Model):
    numrango = models.AutoField(primary_key=True)
    descrango = models.CharField(max_length=32)
    preciomin = models.IntegerField(blank=True, null=True)
    preciomax = models.IntegerField(blank=True, null=True)
    numarea = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_rangoprecios'


class CatRangosTiempoVentas(models.Model):
    id_rango_tiempo = models.AutoField(primary_key=True)
    tiempo = models.IntegerField()
    unidad = models.CharField(max_length=3)
    descripcion = models.CharField(max_length=50)
    tipo_grafica = models.CharField(max_length=3)
    estatus = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_rangos_tiempo_ventas'


class CatRazones(models.Model):
    idu_razon = models.AutoField(primary_key=True)
    des_razon = models.CharField(max_length=60)
    opc_status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_razones'


class CatRechazoscredito(models.Model):
    num_area = models.IntegerField(primary_key=True)
    idu_causa = models.IntegerField()
    des_causa = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'cat_rechazoscredito'
        unique_together = (('num_area', 'idu_causa'),)


class CatRedirectLandingpage(models.Model):
    keyword = models.CharField(unique=True, max_length=50)
    category = models.CharField(max_length=50)
    search_type = models.CharField(max_length=20)
    redirect_url = models.CharField(max_length=220)

    class Meta:
        managed = False
        db_table = 'cat_redirect_landingpage'


class CatRegionPeriodico(models.Model):
    idu_region_periodico = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_region_periodico'


class CatRelCiudadesbodegas(models.Model):
    ciudad = models.SmallIntegerField(blank=True, null=True)
    bodegas = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_rel_ciudadesbodegas'


class CatRelCiudadesbodegasEtl(models.Model):
    ciudad = models.SmallIntegerField(blank=True, null=True)
    bodegas = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_rel_ciudadesbodegas_etl'


class CatRelCiudadesbodegasEtlProd(models.Model):
    ciudad = models.SmallIntegerField(blank=True, null=True)
    bodegas = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_rel_ciudadesbodegas_etl_prod'


class CatRelCiudadesbodegasEtlProdAnterior(models.Model):
    ciudad = models.SmallIntegerField(blank=True, null=True)
    bodegas = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_rel_ciudadesbodegas_etl_prod_anterior'


class CatResolucionoe(models.Model):
    num_resolucion = models.IntegerField(blank=True, null=True)
    des_resolucion = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_resolucionoe'


class CatRespuestas(models.Model):
    idu_pregunta = models.IntegerField()
    idu_respuesta = models.IntegerField()
    nom_respuesta = models.CharField(max_length=-1, blank=True, null=True)
    idu_pregunta_corresponde = models.IntegerField(blank=True, null=True)
    puntaje = models.FloatField(blank=True, null=True)
    flag_activo = models.BooleanField(blank=True, null=True)
    num_orden = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_respuestas'


class CatRibbon(models.Model):
    flag_price = models.CharField(primary_key=True, max_length=10)
    clave_identificacion = models.CharField(max_length=-1, blank=True, null=True)
    name_price = models.CharField(max_length=-1, blank=True, null=True)
    color_price = models.CharField(max_length=-1, blank=True, null=True)
    flag_prioridad = models.IntegerField(blank=True, null=True)
    identifier = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_ribbon'


class CatRutasimagenes(models.Model):
    num_areaweb = models.SmallIntegerField()
    nom_areaweb = models.CharField(max_length=80)
    dir_rutaimagencategoria = models.CharField(max_length=250)
    num_indicadoractivo = models.SmallIntegerField()
    fec_altaruta = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cat_rutasimagenes'


class CatSecuenciasproductos(models.Model):
    idu_registro = models.AutoField(primary_key=True)
    des_negocio = models.CharField(max_length=2)
    des_categoria = models.TextField()
    des_partnumber = models.TextField()
    des_identifier = models.TextField()
    des_categoria_hcl = models.TextField()
    num_secuencia_2 = models.BigIntegerField()
    num_secuencia_3 = models.BigIntegerField()
    num_nivel = models.IntegerField()
    opc_flag_ultimonivel = models.TextField()  # This field type is a guess.
    fec_actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cat_secuenciasproductos'


class CatSellermarketplace(models.Model):
    idu_seller = models.BigAutoField(primary_key=True)
    idu_tienda = models.BigIntegerField()
    nom_tienda = models.CharField(max_length=254)
    opc_estatustienda = models.CharField(max_length=254)
    nom_ciudadenvio = models.CharField(max_length=254)
    num_plazoaprobacion = models.BigIntegerField()
    num_tasaaprobacion = models.FloatField()
    des_banner = models.CharField(max_length=254)
    nom_canal = models.CharField(max_length=254)
    fec_cerradodesde = models.DateTimeField()
    fec_cerradohasta = models.DateTimeField()
    opc_codigoisomoneda = models.CharField(max_length=50)
    fec_creacionmirakl = models.DateTimeField()
    des_dominio = models.CharField(max_length=254)
    des_descripcion = models.CharField(max_length=2048)
    num_evaluacion = models.BigIntegerField()
    opc_enviogratis = models.BooleanField()
    num_grado = models.SmallIntegerField()
    fec_inmunidad = models.DateTimeField()
    opc_profesional = models.BooleanField()
    fec_ultimamodificacion = models.DateTimeField()
    des_logo = models.CharField(max_length=254)
    num_cantidadofertas = models.BigIntegerField()
    idu_operador = models.CharField(max_length=254)
    num_tiemporespuesta = models.BigIntegerField()
    num_cantidadordenes = models.BigIntegerField()
    opc_premium = models.BooleanField()
    opc_estatuspremium = models.CharField(max_length=254)
    des_razonsocial = models.CharField(max_length=254)
    des_rfc = models.CharField(max_length=254)
    prc_iva = models.CharField(max_length=254)
    des_politicadevolucion = models.CharField(max_length=2048)
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    opc_estatus = models.CharField(max_length=10)
    nom_actualiza = models.CharField(max_length=50)
    opc_procesado = models.SmallIntegerField()
    opc_estatuscoppelpay = models.IntegerField()
    excluir_feed = models.BooleanField()
    fec_excluir_feed = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_sellermarketplace'
        unique_together = (('idu_seller', 'idu_tienda'),)


class CatSemaforoServiciosVentas(models.Model):
    id_semaforo = models.AutoField(primary_key=True)
    porc_falla_min = models.DecimalField(max_digits=15, decimal_places=2)
    porc_falla_max = models.DecimalField(max_digits=15, decimal_places=2)
    color = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_semaforo_servicios_ventas'


class CatSepomex(models.Model):
    numcodigopostal = models.IntegerField()
    colonia = models.CharField(max_length=65)
    asentamiento = models.CharField(max_length=65)
    municipio = models.CharField(max_length=65)
    estado = models.CharField(max_length=65)
    ciudad = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'cat_sepomex'


class CatServicioscedis(models.Model):
    idu_oficinadeenvios = models.BigIntegerField(blank=True, null=True)
    nom_oficinadeenvios = models.CharField(max_length=-1, blank=True, null=True)
    idu_bodega = models.IntegerField(blank=True, null=True)
    num_cedisregional = models.SmallIntegerField(blank=True, null=True)
    des_urlservicioguia = models.CharField(max_length=-1, blank=True, null=True)
    des_urlservicioconfirm = models.CharField(max_length=-1, blank=True, null=True)
    status_enviocorreo_analistas = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cat_servicioscedis'


class CatSituacionetiquetas(models.Model):
    idu_situacionetiqueta = models.SmallIntegerField(primary_key=True)
    des_situacionetiqueta = models.CharField(max_length=150)
    sort = models.SmallIntegerField(blank=True, null=True)
    activo = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_situacionetiquetas'


class CatStatuscuentasconvencido(models.Model):
    num_status = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_statuscuentasconvencido'


class CatStatuspreconveniosdepago(models.Model):
    idu_status = models.IntegerField()
    nom_status = models.CharField(max_length=100)
    desc_status = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'cat_statuspreconveniosdepago'


class CatStatusseguimientopedido(models.Model):
    clavemovto = models.SmallIntegerField()
    causa = models.SmallIntegerField()
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    cambiodom = models.CharField(max_length=1, blank=True, null=True)
    mensaje = models.CharField(max_length=250, blank=True, null=True)
    keyx = models.AutoField()

    class Meta:
        managed = False
        db_table = 'cat_statusseguimientopedido'


class CatStores(models.Model):
    idu_store = models.AutoField(primary_key=True)
    nom_store = models.CharField(max_length=50)
    bodegas = models.CharField(max_length=-1)
    num_bodegaprincipal = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cat_stores'


class CatStoresEtl(models.Model):
    idu_store = models.IntegerField(blank=True, null=True)
    bodegas = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_stores_etl'


class CatSubcripcionesClientes(models.Model):
    idu_email = models.CharField(max_length=50)
    idu_correo = models.BooleanField(blank=True, null=True)
    idu_sms = models.BooleanField(blank=True, null=True)
    desc_preferencias = models.TextField()
    fecha_registro = models.DateField()

    class Meta:
        managed = False
        db_table = 'cat_subcripciones_clientes'
# Unable to inspect table 'cat_subcuentascreadas_gmc'
# The error was: permission denied for table cat_subcuentascreadas_gmc
# Unable to inspect table 'cat_subcuentaspendientes_gmc'
# The error was: permission denied for table cat_subcuentaspendientes_gmc


class CatSurtidoresoe(models.Model):
    id_tipo_surtidor = models.AutoField()
    nom_tipo_surtidor = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'cat_surtidoresoe'


class CatTallasExc(models.Model):
    numdepto = models.SmallIntegerField(blank=True, null=True)
    numclase = models.SmallIntegerField(blank=True, null=True)
    numfamilia = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_tallas_exc'
# Unable to inspect table 'cat_tallas_ranking'
# The error was: permission denied for table cat_tallas_ranking


class CatTallasarticulos(models.Model):
    numarea = models.OneToOneField(CatArticulos, models.DO_NOTHING, db_column='numarea', primary_key=True)
    numcodigo = models.IntegerField()
    numtalla = models.SmallIntegerField()
    precioventa = models.IntegerField()
    comprar = models.SmallIntegerField()
    desctalla = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cat_tallasarticulos'
        unique_together = (('numarea', 'numcodigo', 'numtalla'),)


class CatTallascalzado(models.Model):
    numareaweb = models.SmallIntegerField()
    cm = models.FloatField()
    talla = models.FloatField()

    class Meta:
        managed = False
        db_table = 'cat_tallascalzado'


class CatTallasequivalencia(models.Model):
    num_area = models.SmallIntegerField(primary_key=True)
    num_departamento = models.SmallIntegerField()
    num_clase = models.SmallIntegerField()
    num_talla = models.SmallIntegerField()
    des_talla = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'cat_tallasequivalencia'
        unique_together = (('num_area', 'num_departamento', 'num_clase', 'num_talla'),)


class CatTallaslenceria(models.Model):
    numtalla = models.IntegerField(primary_key=True)
    equivalencia = models.CharField(max_length=64, blank=True, null=True)
    descripcion = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_tallaslenceria'


class CatTamaniosTiendas(models.Model):
    cod_tamanio = models.AutoField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=45)
    abreviatura = models.CharField(unique=True, max_length=5)

    class Meta:
        managed = False
        db_table = 'cat_tamanios_tiendas'


class CatTasainteres(models.Model):
    numarea = models.OneToOneField(CatAreas, models.DO_NOTHING, db_column='numarea', primary_key=True)
    tasainteres = models.SmallIntegerField()
    tasainteresriesgo = models.SmallIntegerField()
    num_tasainteres18riesgo = models.SmallIntegerField()
    num_tasainteres24 = models.SmallIntegerField()
    num_tasainteres24riesgo = models.SmallIntegerField()
    num_tasainteres18 = models.SmallIntegerField()
    num_tasainteresmarketplace = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_tasainteres'


class CatTextoalterno(models.Model):
    id_textoalterno = models.AutoField(unique=True)
    nom_textoalterno = models.CharField(max_length=-1)
    num_orden = models.SmallIntegerField()
    num_activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cat_textoalterno'


class CatTiendas(models.Model):
    num_tienda = models.IntegerField(primary_key=True)
    nom_tienda = models.CharField(max_length=50)
    des_direccion = models.CharField(max_length=250)
    num_telefono = models.CharField(max_length=50)
    num_ciudad = models.IntegerField()
    nom_ciudad = models.CharField(max_length=50)
    des_nomenclatura = models.CharField(max_length=10)
    nom_estado = models.CharField(max_length=50)
    des_region = models.CharField(max_length=10)
    des_division = models.CharField(max_length=20)
    fec_apertura = models.DateTimeField()
    fec_remodelacion = models.DateTimeField()
    des_formato = models.CharField(max_length=30)
    opc_banco = models.BooleanField()
    opc_optica = models.BooleanField()
    des_propiedadlocal = models.CharField(max_length=20)
    des_m2pv = models.CharField(max_length=20)
    clv_ventamuebles = models.CharField(max_length=5)
    clv_ventaropa = models.CharField(max_length=5)
    nom_gerente = models.CharField(max_length=80)
    num_celgerente = models.CharField(max_length=20)
    nom_zona = models.CharField(max_length=30)
    nom_emailgerente = models.CharField(max_length=230)
    num_tiendabase = models.CharField(max_length=20)
    num_telefonotdabase = models.CharField(max_length=50)
    hor_tienda = models.CharField(max_length=150)
    num_latitud = models.FloatField()
    num_longitud = models.FloatField()
    num_ipservidor = models.CharField(max_length=20)
    num_codigopostal = models.CharField(max_length=10)
    nom_colonia = models.CharField(max_length=50)
    nom_calle = models.CharField(max_length=50)
    num_exterior = models.IntegerField()
    num_interior = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cat_tiendas'


class CatTiendasArg(models.Model):
    num_tienda = models.IntegerField(primary_key=True)
    nom_tienda = models.CharField(max_length=-1)
    des_calle = models.CharField(max_length=-1)
    des_colonia = models.CharField(max_length=-1)
    num_interior = models.SmallIntegerField()
    clv_bodega = models.IntegerField()
    des_ip_tienda = models.CharField(max_length=-1)
    num_ciudad = models.IntegerField()
    des_estado = models.CharField(max_length=-1)
    num_tipotienda = models.SmallIntegerField()
    num_tipoconstruccion = models.SmallIntegerField()
    des_horario = models.CharField(max_length=-1)
    des_codigopostal = models.CharField(max_length=-1)
    des_latitud = models.CharField(max_length=-1)
    des_longitud = models.CharField(max_length=-1)
    des_telefono = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'cat_tiendas_arg'


class CatTiendasKiosko(models.Model):
    id = models.AutoField()
    num_tienda = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_tiendas_kiosko'


class CatTiendasmesaregalos(models.Model):
    idu_tienda = models.SmallIntegerField()
    nom_tienda = models.CharField(max_length=30)
    num_ciudad = models.SmallIntegerField()
    nom_ciudad = models.CharField(max_length=50)
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'cat_tiendasmesaregalos'


class CatTiendavirtualguiastallasfamilia(models.Model):
    numdepto = models.SmallIntegerField()
    numclase = models.SmallIntegerField()
    numfamilia = models.SmallIntegerField()
    numtalla = models.SmallIntegerField()
    desctalla = models.CharField(max_length=-1, blank=True, null=True)
    fec_proceso = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cat_tiendavirtualguiastallasfamilia'


class CatTipoCliente(models.Model):
    id_tipo_cliente = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cat_tipo_cliente'


class CatTipoProcesoCompra(models.Model):
    id_tipo_proceso = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cat_tipo_proceso_compra'


class CatTipocambio(models.Model):
    numtipocambio = models.SmallIntegerField(primary_key=True)
    desctipocambio = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_tipocambio'


class CatTipocampania(models.Model):
    idu_campania = models.SmallIntegerField(primary_key=True)
    des_campania = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cat_tipocampania'


class CatTipocolores(models.Model):
    numtipocolor = models.SmallIntegerField(primary_key=True)
    desctipocolor = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cat_tipocolores'


class CatTipopagos(models.Model):
    id = models.IntegerField(blank=True, null=True)
    tipopago = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_tipopagos'


class CatTipopagosdetalle(models.Model):
    num_tipopago = models.IntegerField()
    num_cvebanco = models.IntegerField(blank=True, null=True)
    des_tipopago = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'cat_tipopagosdetalle'


class CatTiporeportesoperativos(models.Model):
    num_reporte = models.IntegerField()
    des_reporte = models.CharField(max_length=50)
    opc_activo = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_tiporeportesoperativos'


class CatTipos(models.Model):
    id_tipo = models.IntegerField(primary_key=True)
    nom_tipo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cat_tipos'


class CatTiposBanners(models.Model):
    cod_tipo_banner = models.AutoField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=45)
    abreviatura = models.CharField(unique=True, max_length=5)
    es_carrusel = models.BooleanField()
    desc_img = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cat_tipos_banners'


class CatTiposTiendas(models.Model):
    cod_tipo_tienda = models.AutoField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=60)
    abreviatura = models.CharField(unique=True, max_length=5)

    class Meta:
        managed = False
        db_table = 'cat_tipos_tiendas'


class CatTiposValidaciones(models.Model):
    idu_tipos = models.AutoField(primary_key=True)
    desc_validacion = models.TextField()

    class Meta:
        managed = False
        db_table = 'cat_tipos_validaciones'


class CatTiposregistros(models.Model):
    idu_registro = models.IntegerField(primary_key=True)
    des_tiporegistro = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cat_tiposregistros'


class CatUnificacioncorreos(models.Model):
    nom_correo = models.CharField(max_length=150)
    num_cliente = models.BigIntegerField()
    nom_tablaorigen = models.CharField(max_length=20)
    fec_alta = models.DateField()
    fec_grabado = models.DateField()

    class Meta:
        managed = False
        db_table = 'cat_unificacioncorreos'


class CatUrlamigables(models.Model):
    idu_registro = models.AutoField()
    nom_urlamigable = models.TextField()
    nom_urldinamica = models.TextField()
    nom_menuweb = models.CharField(max_length=-1)
    fec_movimiento = models.DateField(blank=True, null=True)
    num_mostrar_sitemap = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cat_urlamigables'


class CatUrlslider(models.Model):
    numurl = models.AutoField(primary_key=True)
    url = models.CharField(max_length=400)
    posicion = models.CharField(max_length=-1)
    numimg = models.IntegerField()
    tipo = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'cat_urlslider'


class CatUrlsliderKiosko(models.Model):
    numurl = models.AutoField()
    url = models.CharField(max_length=300)
    posicion = models.CharField(max_length=-1)
    numimg = models.IntegerField()
    tipo = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'cat_urlslider_kiosko'


class CatUsuarios(models.Model):
    numempleado = models.IntegerField(primary_key=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    idperfil = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_usuarios'


class CatUsuariosoficinadeenvios(models.Model):
    idu_usuario = models.AutoField(primary_key=True)
    num_empleado = models.IntegerField()
    nom_usuario = models.CharField(max_length=120)
    nom_email = models.CharField(max_length=50)
    opc_activo = models.BooleanField()
    num_bodega = models.IntegerField()
    fec_alta = models.DateTimeField()
    fec_movimiento = models.DateTimeField()
    idu_direccionip = models.IntegerField()
    id_rol = models.IntegerField(blank=True, null=True)
    id_tipo_surtidor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_usuariosoficinadeenvios'


class CatValoresatributosmarketplace(models.Model):
    idu_listavalores = models.BigAutoField(primary_key=True)
    nom_codigolista = models.CharField(max_length=254)
    des_listavaloresen = models.CharField(max_length=254)
    des_listavaloresmx = models.CharField(max_length=254)
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    opc_estatus = models.CharField(max_length=10)
    opc_activo = models.BooleanField()
    nom_actualiza = models.CharField(max_length=254)
    opc_procesado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cat_valoresatributosmarketplace'


class CatWebservicesConvenios(models.Model):
    keyx = models.AutoField()
    descripcion_ws = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_webservices_convenios'


class CatZonas(models.Model):
    ciudad = models.SmallIntegerField(blank=True, null=True)
    colonia = models.SmallIntegerField(blank=True, null=True)
    nombrezona = models.CharField(max_length=30, blank=True, null=True)
    poblacion = models.CharField(max_length=25, blank=True, null=True)
    municipio = models.CharField(max_length=25, blank=True, null=True)
    planocoordenadas = models.CharField(max_length=5, blank=True, null=True)
    rumbo = models.CharField(max_length=31, blank=True, null=True)
    flagunidadhabitacional = models.SmallIntegerField(blank=True, null=True)
    calleunidadhabitacional = models.IntegerField(blank=True, null=True)
    casaunidadhabitacional = models.IntegerField(blank=True, null=True)
    codigopostal = models.IntegerField(blank=True, null=True)
    flagencuestas = models.SmallIntegerField(blank=True, null=True)
    ciudadcobranzas = models.SmallIntegerField(blank=True, null=True)
    numerocobranzas = models.SmallIntegerField(blank=True, null=True)
    numempleadojefe = models.IntegerField(blank=True, null=True)
    numempleadosupervisor = models.IntegerField(blank=True, null=True)
    clavelada = models.SmallIntegerField(blank=True, null=True)
    tipozonahabitacional = models.CharField(max_length=1, blank=True, null=True)
    keyx = models.AutoField()
    centro = models.IntegerField(blank=True, null=True)
    tipozona = models.CharField(max_length=1, blank=True, null=True)
    numempleadochofer = models.IntegerField(blank=True, null=True)
    numempleadogerente = models.IntegerField(blank=True, null=True)
    numempleadoabogado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_zonas'


class CatZonasBanco(models.Model):
    numerociudad = models.IntegerField()
    numerocolonia = models.IntegerField()
    nombrezona = models.CharField(max_length=32, blank=True, null=True)
    poblacionzona = models.CharField(max_length=27, blank=True, null=True)
    municipiozona = models.CharField(max_length=27, blank=True, null=True)
    codigopostalzona = models.IntegerField(blank=True, null=True)
    supervisorzona = models.IntegerField(blank=True, null=True)
    choferzona = models.IntegerField(blank=True, null=True)
    jefegrupozona = models.IntegerField(blank=True, null=True)
    gerentezona = models.IntegerField(blank=True, null=True)
    abogadozona = models.IntegerField(blank=True, null=True)
    centro = models.IntegerField(blank=True, null=True)
    ciudadcobranzas = models.IntegerField(blank=True, null=True)
    numerocobranzas = models.IntegerField(blank=True, null=True)
    numerociudadcoppel = models.IntegerField(blank=True, null=True)
    numerocoloniacoppel = models.IntegerField(blank=True, null=True)
    nombrezonacoppel = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_zonas_banco'


class CatZonasBancoEtl(models.Model):
    numerociudad = models.IntegerField(blank=True, null=True)
    numerocolonia = models.IntegerField(blank=True, null=True)
    nombrezona = models.CharField(max_length=32, blank=True, null=True)
    poblacionzona = models.CharField(max_length=27, blank=True, null=True)
    municipiozona = models.CharField(max_length=27, blank=True, null=True)
    codigopostalzona = models.IntegerField(blank=True, null=True)
    supervisorzona = models.IntegerField(blank=True, null=True)
    choferzona = models.IntegerField(blank=True, null=True)
    jefegrupozona = models.IntegerField(blank=True, null=True)
    gerentezona = models.IntegerField(blank=True, null=True)
    abogadozona = models.IntegerField(blank=True, null=True)
    centro = models.IntegerField(blank=True, null=True)
    ciudadcobranzas = models.IntegerField(blank=True, null=True)
    numerocobranzas = models.IntegerField(blank=True, null=True)
    numerociudadcoppel = models.IntegerField(blank=True, null=True)
    numerocoloniacoppel = models.IntegerField(blank=True, null=True)
    nombrezonacoppel = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_zonas_banco_etl'


class CatZonasExclusiones(models.Model):
    ciudad = models.SmallIntegerField(blank=True, null=True)
    colonia = models.SmallIntegerField(blank=True, null=True)
    nombrezona = models.CharField(max_length=30, blank=True, null=True)
    poblacion = models.CharField(max_length=25, blank=True, null=True)
    municipio = models.CharField(max_length=25, blank=True, null=True)
    planocoordenadas = models.CharField(max_length=5, blank=True, null=True)
    rumbo = models.CharField(max_length=31, blank=True, null=True)
    flagunidadhabitacional = models.SmallIntegerField(blank=True, null=True)
    calleunidadhabitacional = models.IntegerField(blank=True, null=True)
    casaunidadhabitacional = models.IntegerField(blank=True, null=True)
    codigopostal = models.IntegerField(blank=True, null=True)
    flagencuestas = models.SmallIntegerField(blank=True, null=True)
    ciudadcobranzas = models.SmallIntegerField(blank=True, null=True)
    numerocobranzas = models.SmallIntegerField(blank=True, null=True)
    numempleadojefe = models.IntegerField(blank=True, null=True)
    numempleadosupervisor = models.IntegerField(blank=True, null=True)
    clavelada = models.SmallIntegerField(blank=True, null=True)
    tipozonahabitacional = models.CharField(max_length=1, blank=True, null=True)
    keyx = models.AutoField()
    centro = models.IntegerField(blank=True, null=True)
    tipozona = models.CharField(max_length=1, blank=True, null=True)
    numempleadochofer = models.IntegerField(blank=True, null=True)
    numempleadogerente = models.IntegerField(blank=True, null=True)
    numempleadoabogado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_zonas_exclusiones'


class CatZonasdistribucioncedis(models.Model):
    num_bodega = models.SmallIntegerField(blank=True, null=True)
    num_ciudad = models.SmallIntegerField(blank=True, null=True)
    num_zona = models.IntegerField(blank=True, null=True)
    nom_zona = models.CharField(max_length=30, blank=True, null=True)
    num_codigopostal = models.IntegerField(blank=True, null=True)
    num_bodega_destino = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_zonasdistribucioncedis'


class Catgpenrel(models.Model):
    catgroup_id = models.BigIntegerField(primary_key=True)
    catalog_id = models.BigIntegerField()
    catentry_id = models.BigIntegerField()
    rule = models.CharField(max_length=254, blank=True, null=True)
    sequence = models.FloatField()
    lastupdate = models.DateTimeField(blank=True, null=True)
    field1 = models.CharField(max_length=254, blank=True, null=True)
    field2 = models.IntegerField(blank=True, null=True)
    field3 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    optcounter = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'catgpenrel'
        unique_together = (('catgroup_id', 'catentry_id', 'catalog_id'),)


class Catgroup(models.Model):
    catgroup_id = models.BigIntegerField(primary_key=True)
    member_id = models.BigIntegerField()
    identifier = models.CharField(max_length=254, blank=True, null=True)
    markfordelete = models.IntegerField()
    lastupdate = models.DateTimeField(blank=True, null=True)
    field1 = models.CharField(max_length=254, blank=True, null=True)
    field2 = models.CharField(max_length=254, blank=True, null=True)
    oid = models.CharField(max_length=64, blank=True, null=True)
    rank = models.FloatField(blank=True, null=True)
    up_identifier = models.CharField(max_length=254, blank=True, null=True)
    dynamic = models.IntegerField(blank=True, null=True)
    optcounter = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'catgroup'


class Catgrpdesc(models.Model):
    language_id = models.IntegerField()
    catgroup_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=254)
    shortdescription = models.CharField(max_length=254, blank=True, null=True)
    longdescription = models.CharField(max_length=4000, blank=True, null=True)
    thumbnail = models.CharField(max_length=254, blank=True, null=True)
    fullimage = models.CharField(max_length=254, blank=True, null=True)
    published = models.IntegerField()
    display = models.CharField(max_length=254, blank=True, null=True)
    keyword = models.CharField(max_length=4000, blank=True, null=True)
    note = models.CharField(max_length=4000, blank=True, null=True)
    up_name = models.CharField(max_length=254, blank=True, null=True)
    up_shortdesc = models.CharField(max_length=254, blank=True, null=True)
    optcounter = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'catgrpdesc'
        unique_together = (('catgroup_id', 'language_id'),)


class Cdesvalor(models.Model):
    des_valor1 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cdesvalor'
# Unable to inspect table 'cf_notificaciones_proactivas'
# The error was: permission denied for table cf_notificaciones_proactivas
# Unable to inspect table 'ciudad_por_nodo'
# The error was: permission denied for table ciudad_por_nodo


class Ciudades(models.Model):
    ciudad = models.IntegerField()
    nombre = models.CharField(max_length=-1, blank=True, null=True)
    inicial = models.CharField(max_length=4, blank=True, null=True)
    apertura = models.DateField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    lada = models.IntegerField(blank=True, null=True)
    region = models.IntegerField(blank=True, null=True)
    cdauxiliar = models.IntegerField(blank=True, null=True)
    municipio = models.CharField(max_length=-1, blank=True, null=True)
    operador = models.CharField(max_length=-1, blank=True, null=True)
    fcapturamod = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ciudades'


class ClientesSorteo(models.Model):
    token = models.CharField(unique=True, max_length=12, blank=True, null=True)
    numcliente = models.BigIntegerField(blank=True, null=True)
    cliente = models.CharField(max_length=100, blank=True, null=True)
    correoelectronico = models.CharField(max_length=200, blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=-1, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes_sorteo'


class Cmensaje(models.Model):
    des_mensaje = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cmensaje'


class Cnomarticuloweb(models.Model):
    substring = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cnomarticuloweb'


class CodExclusivosecomerceLinea(models.Model):
    numcodigo = models.IntegerField()
    tipocodigo = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'cod_exclusivosecomerce_linea'


class Codigossicomprar(models.Model):
    numcodigo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'codigossicomprar'


class ConfigCarteras(models.Model):
    servidor = models.CharField(max_length=50)
    basedatos = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    puerto = models.CharField(max_length=50)
    fecha = models.DateTimeField(blank=True, null=True)
    fecha_correo = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config_carteras'


class ConnectbyInt(models.Model):
    keyid = models.IntegerField(blank=True, null=True)
    parent_keyid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'connectby_int'


class ConnectbyText(models.Model):
    keyid = models.TextField(blank=True, null=True)
    parent_keyid = models.TextField(blank=True, null=True)
    pos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'connectby_text'


class Cosa(models.Model):
    field_column_field = models.BigIntegerField(db_column='?column?', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'cosa'


class Countt(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countt'


class Cp(models.Model):
    cp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cp'


class Cresultados(models.Model):
    parentgroupidentifier = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cresultados'


class Ct(models.Model):
    id = models.IntegerField(blank=True, null=True)
    rowclass = models.TextField(blank=True, null=True)
    rowid = models.TextField(blank=True, null=True)
    attribute = models.TextField(blank=True, null=True)
    val = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ct'


class Cth(models.Model):
    id = models.AutoField()
    rowid = models.TextField(blank=True, null=True)
    rowdt = models.DateTimeField(blank=True, null=True)
    attribute = models.TextField(blank=True, null=True)
    val = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cth'


class CtlActivardevolucionesoe(models.Model):
    idu_opcion = models.IntegerField(blank=True, null=True)
    flag_activado = models.IntegerField(blank=True, null=True)
    des_opcion = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_activardevolucionesoe'


class CtlActivarnotificacionesoe(models.Model):
    idu_opcion = models.IntegerField(blank=True, null=True)
    flag_activado = models.IntegerField(blank=True, null=True)
    des_opcion = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_activarnotificacionesoe'


class CtlActualizaTipo6(models.Model):
    numcodigo = models.IntegerField(blank=True, null=True)
    tipoarticulo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_actualiza_tipo6'


class CtlAdmImagenes(models.Model):
    idu_imagen = models.BigAutoField(primary_key=True)
    nombre_imagen = models.CharField(max_length=-1)
    ruta_imagen = models.CharField(max_length=-1)
    fecha_registro = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_adm_imagenes'


class CtlAdmPartesCuerpo(models.Model):
    idu_parte_cuerpo = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=-1)
    desc_instrucciones = models.CharField(max_length=-1)
    estatus = models.BooleanField()
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_adm_partes_cuerpo'


class CtlAdminpage(models.Model):
    idu_page = models.IntegerField()
    idu_seccion = models.IntegerField()
    idu_consecutivo = models.IntegerField()
    nom_urlimagen = models.CharField(max_length=-1)
    nom_tooltip = models.CharField(max_length=-1)
    nom_urllink = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ctl_adminpage'


class CtlAdminzonasdistribucioncedis(models.Model):
    num_empleado = models.BigIntegerField(blank=True, null=True)
    idu_oficinadeenvios = models.IntegerField(blank=True, null=True)
    admin = models.BooleanField(blank=True, null=True)
    read_only = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_adminzonasdistribucioncedis'


class CtlAlertashabilitadas(models.Model):
    idu_alertashabilitadas = models.TextField(primary_key=True)
    opc_generadocorrecto = models.BooleanField()
    opc_generadoerror = models.BooleanField()
    opc_publicadocorrecto = models.BooleanField()
    opc_publicadoerror = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ctl_alertashabilitadas'


class CtlAlertashabilitadasMkp(models.Model):
    idu_alertashabilitadas = models.TextField(primary_key=True)
    opc_generadocorrecto = models.BooleanField()
    opc_generadoerror = models.BooleanField()
    opc_publicadocorrecto = models.BooleanField()
    opc_publicadoerror = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ctl_alertashabilitadas_mkp'


class CtlApalineaapartadociudad(models.Model):
    ciudadnum = models.SmallIntegerField(primary_key=True)
    local = models.SmallIntegerField()
    orden = models.SmallIntegerField()
    dias = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_apalineaapartadociudad'
        unique_together = (('ciudadnum', 'local', 'orden'),)


class CtlApartadodevolucionRopa(models.Model):
    num_orden = models.IntegerField()
    idu_pedido = models.IntegerField()
    num_folioropa = models.IntegerField()
    num_empleado = models.IntegerField(blank=True, null=True)
    fec_devolucion_proc = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_apartadodevolucion_ropa'


class CtlApuestas(models.Model):
    id = models.AutoField()
    nom_abuelo = models.CharField(max_length=-1, blank=True, null=True)
    nom_padre = models.CharField(max_length=-1, blank=True, null=True)
    nom_hijo = models.CharField(max_length=-1, blank=True, null=True)
    nom_descripcion = models.CharField(max_length=-1, blank=True, null=True)
    nom_url = models.TextField(blank=True, null=True)
    num_orden = models.SmallIntegerField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_apuestas'


class CtlApuestasCatalogo(models.Model):
    id = models.AutoField()
    nom_abuelo = models.CharField(max_length=-1, blank=True, null=True)
    nom_padre = models.CharField(max_length=-1, blank=True, null=True)
    nom_hijo = models.CharField(max_length=-1, blank=True, null=True)
    nom_descripcion = models.CharField(max_length=-1, blank=True, null=True)
    nom_url = models.TextField(blank=True, null=True)
    num_orden = models.SmallIntegerField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_apuestas_catalogo'


class CtlAreasWebExcepciones(models.Model):
    idu_excepcion = models.AutoField()
    num_areaweb = models.IntegerField()
    nom_areaweb = models.CharField(max_length=100)
    num_especial = models.IntegerField()
    fec_ingreso = models.DateField()

    class Meta:
        managed = False
        db_table = 'ctl_areas_web_excepciones'


class CtlAreasweb(models.Model):
    numarea = models.ForeignKey(CatFamilias, models.DO_NOTHING, db_column='numarea')
    numdepto = models.SmallIntegerField()
    numclase = models.SmallIntegerField()
    numfamilia = models.SmallIntegerField()
    numareaweb = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_areasweb'


class CtlAreaswebMarketplaceRespaldo(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numdepto = models.SmallIntegerField(blank=True, null=True)
    numclase = models.SmallIntegerField(blank=True, null=True)
    numfamilia = models.SmallIntegerField(blank=True, null=True)
    numareaweb = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_areasweb_marketplace_respaldo'


class CtlAreawebTemplate(models.Model):
    id = models.AutoField()
    num_areaweb = models.IntegerField(blank=True, null=True)
    num_template = models.IntegerField(blank=True, null=True)
    nom_elemento = models.CharField(max_length=20, blank=True, null=True)
    nom_ruta_imagen = models.CharField(max_length=200, blank=True, null=True)
    nom_ruta_enlace = models.CharField(max_length=200, blank=True, null=True)
    nom_alt = models.CharField(max_length=200, blank=True, null=True)
    nom_descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_areaweb_template'


class CtlArticulodescripcion(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    numcodigo = models.IntegerField()
    descarticulo = models.TextField()
    nomarticulo = models.CharField(max_length=120)
    nomareaweb = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ctl_articulodescripcion'
        unique_together = (('numarea', 'numcodigo'),)


class CtlArticuloscolores(models.Model):
    numarea = models.OneToOneField(CatArticulos, models.DO_NOTHING, db_column='numarea', primary_key=True)
    numcodigo = models.IntegerField()
    numcolor = models.ForeignKey(CatColores, models.DO_NOTHING, db_column='numcolor')
    numtipocolor = models.ForeignKey(CatTipocolores, models.DO_NOTHING, db_column='numtipocolor')

    class Meta:
        managed = False
        db_table = 'ctl_articuloscolores'
        unique_together = (('numarea', 'numcodigo', 'numcolor', 'numtipocolor'),)


class CtlArticuloscomplementarios(models.Model):
    numcodigo = models.IntegerField(blank=True, null=True)
    num_prioridad = models.SmallIntegerField(blank=True, null=True)
    idu_area = models.IntegerField(blank=True, null=True)
    idu_departamento = models.IntegerField(blank=True, null=True)
    idu_clase = models.IntegerField(blank=True, null=True)
    idu_familia = models.IntegerField(blank=True, null=True)
    idu_familiapivote = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_articuloscomplementarios'


class CtlArticulosdetcaracteristicas(models.Model):
    numarea = models.OneToOneField(CatArticulos, models.DO_NOTHING, db_column='numarea', primary_key=True)
    numcodigo = models.IntegerField()
    numcaracteristica = models.IntegerField()
    numdetallecaracteristica = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_articulosdetcaracteristicas'
        unique_together = (('numarea', 'numcodigo', 'numcaracteristica', 'numdetallecaracteristica'),)


class CtlArticulosexistenciaminima(models.Model):
    num_area = models.IntegerField(blank=True, null=True)
    num_codigo = models.IntegerField(primary_key=True)
    num_existenciaminima = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_articulosexistenciaminima'


class CtlAsignacioncargaempleado(models.Model):
    num_empleado = models.BigIntegerField()
    num_pasillo = models.IntegerField()
    nom_letra = models.CharField(max_length=-1)
    num_tipoasignacion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_asignacioncargaempleado'


class CtlBacthMarketplaceImagenes(models.Model):
    idu_batch = models.BigAutoField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_bacth_marketplace_imagenes'


class CtlBajacambiosprecio(models.Model):
    numarea = models.SmallIntegerField()
    numtalla = models.SmallIntegerField()
    numcodigo = models.IntegerField()
    fechabaja = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_bajacambiosprecio'


class CtlBajatallasarticulos(models.Model):
    numarea = models.SmallIntegerField()
    numcodigo = models.IntegerField()
    numtalla = models.IntegerField()
    fechaactualiza = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_bajatallasarticulos'


class CtlBannerCatalogoPromociones(models.Model):
    id_subcomponente = models.IntegerField()
    id_tipo = models.IntegerField(primary_key=True)
    url_image = models.TextField(blank=True, null=True)
    nom_web1 = models.CharField(max_length=60, blank=True, null=True)
    nom_web2 = models.CharField(max_length=60, blank=True, null=True)
    nom_web3 = models.CharField(max_length=60, blank=True, null=True)
    url_enlace = models.TextField()

    class Meta:
        managed = False
        db_table = 'ctl_banner_catalogo_promociones'
        unique_together = (('id_tipo', 'id_subcomponente'),)
# Unable to inspect table 'ctl_bitacora_proceso_compra'
# The error was: permission denied for table ctl_bitacora_proceso_compra
# Unable to inspect table 'ctl_bitacora_proceso_compra_detalle'
# The error was: permission denied for table ctl_bitacora_proceso_compra_detalle


class CtlBitacoraProcesoCompraDetalleHistorial(models.Model):
    id_detalle_compra = models.BigAutoField(primary_key=True)
    id_proceso_compra = models.IntegerField()
    id_tipo_proceso = models.ForeignKey(CatTipoProcesoCompra, models.DO_NOTHING, db_column='id_tipo_proceso')
    fecha_llamado = models.DateTimeField(blank=True, null=True)
    exitoso = models.BooleanField(blank=True, null=True)
    descripcion_error = models.TextField(blank=True, null=True)
    folio_apartado = models.CharField(max_length=15, blank=True, null=True)
    desacople = models.BooleanField(blank=True, null=True)
    metodo_pago = models.CharField(max_length=150, blank=True, null=True)
    tiempo_respuesta = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    request_load = models.TextField(blank=True, null=True)
    response_load = models.TextField(blank=True, null=True)
    info_load = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_bitacora_proceso_compra_detalle_historial'


class CtlBitacoraProcesoCompraHistorial(models.Model):
    id_proceso_compra = models.BigAutoField(primary_key=True)
    orden_id = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    num_cliente = models.CharField(max_length=15, blank=True, null=True)
    exitoso = models.BooleanField(blank=True, null=True)
    descripcion_error = models.TextField(blank=True, null=True)
    id_tipo_cliente = models.ForeignKey(CatTipoCliente, models.DO_NOTHING, db_column='id_tipo_cliente')
    fecha_llamado = models.DateTimeField(blank=True, null=True)
    is_market_place = models.BooleanField(blank=True, null=True)
    field3 = models.TextField(blank=True, null=True)
    num_server = models.CharField(max_length=250, blank=True, null=True)
    nom_correo = models.CharField(max_length=150, blank=True, null=True)
    plataforma = models.CharField(max_length=30, blank=True, null=True)
    version = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_bitacora_proceso_compra_historial'


class CtlBitacoramarketplace(models.Model):
    num_folio = models.BigIntegerField(blank=True, null=True)
    num_folioplataforma = models.BigIntegerField(blank=True, null=True)
    num_foliopago = models.BigIntegerField(blank=True, null=True)
    fec_registro = models.DateTimeField(blank=True, null=True)
    des_observaciones = models.CharField(max_length=250, blank=True, null=True)
    num_empleado = models.IntegerField(blank=True, null=True)
    nom_empleado = models.CharField(max_length=50, blank=True, null=True)
    num_estatus = models.SmallIntegerField(blank=True, null=True)
    num_factura = models.IntegerField()
    num_nota = models.IntegerField()
    des_origen = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_bitacoramarketplace'


class CtlBitacoratrackingomnicanal(models.Model):
    fecha = models.DateTimeField()
    numero_seguimiento = models.CharField(max_length=-1, blank=True, null=True)
    codigo = models.IntegerField(blank=True, null=True)
    mensaje = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_bitacoratrackingomnicanal'


class CtlBloqueos(models.Model):
    idu_bloqueo = models.AutoField()
    id_orden = models.BigIntegerField()
    clv_tarjetadecredito = models.CharField(max_length=128)
    clv_bloqueo = models.IntegerField(blank=True, null=True)
    fec_registro = models.DateTimeField()
    des_nota = models.CharField(max_length=400)
    num_estatus = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_bloqueos'


class CtlBpdetguiassurtido(models.Model):
    num_lote = models.CharField(max_length=21)
    num_codigo = models.IntegerField()
    num_talla = models.IntegerField()
    num_precio = models.DecimalField(max_digits=16, decimal_places=2)
    num_cantidad = models.IntegerField()
    nom_descripcion = models.CharField(max_length=50)
    num_condicion = models.IntegerField()
    num_flagscanneado = models.SmallIntegerField()
    num_flagsobrante = models.CharField(max_length=1)
    num_flagconfirmado = models.SmallIntegerField()
    fec_registro = models.DateTimeField()
    keyx = models.AutoField()
    flag_surtidooe = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_bpdetguiassurtido'


class CtlBpdetguiassurtidohist(models.Model):
    num_lote = models.CharField(max_length=21)
    num_codigo = models.IntegerField()
    num_talla = models.IntegerField()
    num_precio = models.DecimalField(max_digits=16, decimal_places=2)
    num_cantidad = models.IntegerField()
    nom_descripcion = models.CharField(max_length=50)
    num_condicion = models.IntegerField()
    num_flagscanneado = models.SmallIntegerField()
    num_flagsobrante = models.CharField(max_length=1)
    num_flagconfirmado = models.SmallIntegerField()
    fec_registro = models.DateTimeField()
    keyx = models.AutoField()

    class Meta:
        managed = False
        db_table = 'ctl_bpdetguiassurtidohist'


class CtlBpdetguiassurtidohistresp(models.Model):
    num_lote = models.CharField(max_length=21, blank=True, null=True)
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.IntegerField(blank=True, null=True)
    num_precio = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    num_cantidad = models.IntegerField(blank=True, null=True)
    nom_descripcion = models.CharField(max_length=50, blank=True, null=True)
    num_condicion = models.IntegerField(blank=True, null=True)
    num_flagscanneado = models.SmallIntegerField(blank=True, null=True)
    num_flagsobrante = models.CharField(max_length=1, blank=True, null=True)
    num_flagconfirmado = models.SmallIntegerField(blank=True, null=True)
    fec_registro = models.DateTimeField(blank=True, null=True)
    keyx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_bpdetguiassurtidohistresp'


class CtlBpdiferenciasurtido(models.Model):
    num_lote = models.CharField(primary_key=True, max_length=21)
    num_codigo = models.IntegerField()
    num_talla = models.IntegerField(blank=True, null=True)
    num_precio = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    num_cantidad = models.IntegerField(blank=True, null=True)
    nom_descripcion = models.CharField(max_length=50, blank=True, null=True)
    num_codicion = models.IntegerField(blank=True, null=True)
    num_acumulado = models.IntegerField(blank=True, null=True)
    num_unidadeslote = models.IntegerField(blank=True, null=True)
    num_unidadesleidas = models.IntegerField(blank=True, null=True)
    fec_registro = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_bpdiferenciasurtido'
        unique_together = (('num_lote', 'num_codigo', 'fec_registro'),)


class CtlBpencguiassurtido(models.Model):
    num_lote = models.CharField(primary_key=True, max_length=21)
    num_tipoempaque = models.SmallIntegerField()
    num_sincho1 = models.BigIntegerField()
    num_sincho2 = models.BigIntegerField()
    num_status = models.SmallIntegerField()
    num_statusrecepcion = models.SmallIntegerField()
    num_confirmacion = models.SmallIntegerField()
    num_unidades = models.BigIntegerField()
    num_empleadoentrega = models.BigIntegerField()
    nom_empleadoentrega = models.CharField(max_length=100)
    num_empleadorecibe = models.BigIntegerField()
    nom_empleadorecibe = models.CharField(max_length=100)
    num_flagpreconfirmado = models.SmallIntegerField()
    num_flagconfirmado = models.SmallIntegerField()
    fec_registro = models.DateTimeField()
    num_flagjabavacia = models.SmallIntegerField()
    fec_confirmacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_bpencguiassurtido'
        unique_together = (('num_lote', 'num_sincho1', 'num_sincho2'),)


class CtlBpencguiassurtidohist(models.Model):
    num_lote = models.CharField(primary_key=True, max_length=21)
    num_tipoempaque = models.SmallIntegerField()
    num_sincho1 = models.BigIntegerField()
    num_sincho2 = models.BigIntegerField()
    num_status = models.SmallIntegerField()
    num_statusrecepcion = models.SmallIntegerField()
    num_confirmacion = models.SmallIntegerField()
    num_unidades = models.BigIntegerField()
    num_empleadoentrega = models.BigIntegerField()
    nom_empleadoentrega = models.CharField(max_length=100)
    num_empleadorecibe = models.BigIntegerField()
    nom_empleadorecibe = models.CharField(max_length=100)
    num_flagpreconfirmado = models.SmallIntegerField()
    num_flagconfirmado = models.SmallIntegerField()
    fec_registro = models.DateTimeField()
    num_flagjabavacia = models.SmallIntegerField()
    fec_confirmacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_bpencguiassurtidohist'
        unique_together = (('num_lote', 'num_sincho1', 'num_sincho2'),)


class CtlBpencguiassurtidohist2017(models.Model):
    num_lote = models.CharField(max_length=21, blank=True, null=True)
    num_tipoempaque = models.SmallIntegerField(blank=True, null=True)
    num_sincho1 = models.BigIntegerField(blank=True, null=True)
    num_sincho2 = models.BigIntegerField(blank=True, null=True)
    num_status = models.SmallIntegerField(blank=True, null=True)
    num_statusrecepcion = models.SmallIntegerField(blank=True, null=True)
    num_confirmacion = models.SmallIntegerField(blank=True, null=True)
    num_unidades = models.BigIntegerField(blank=True, null=True)
    num_empleadoentrega = models.BigIntegerField(blank=True, null=True)
    nom_empleadoentrega = models.CharField(max_length=100, blank=True, null=True)
    num_empleadorecibe = models.BigIntegerField(blank=True, null=True)
    nom_empleadorecibe = models.CharField(max_length=100, blank=True, null=True)
    num_flagpreconfirmado = models.SmallIntegerField(blank=True, null=True)
    num_flagconfirmado = models.SmallIntegerField(blank=True, null=True)
    fec_registro = models.DateTimeField(blank=True, null=True)
    num_flagjabavacia = models.SmallIntegerField(blank=True, null=True)
    fec_confirmacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_bpencguiassurtidohist2017'


class CtlBpencguiassurtidohistresp(models.Model):
    num_lote = models.CharField(max_length=21, blank=True, null=True)
    num_tipoempaque = models.SmallIntegerField(blank=True, null=True)
    num_sincho1 = models.BigIntegerField(blank=True, null=True)
    num_sincho2 = models.BigIntegerField(blank=True, null=True)
    num_status = models.SmallIntegerField(blank=True, null=True)
    num_statusrecepcion = models.SmallIntegerField(blank=True, null=True)
    num_confirmacion = models.SmallIntegerField(blank=True, null=True)
    num_unidades = models.BigIntegerField(blank=True, null=True)
    num_empleadoentrega = models.BigIntegerField(blank=True, null=True)
    nom_empleadoentrega = models.CharField(max_length=100, blank=True, null=True)
    num_empleadorecibe = models.BigIntegerField(blank=True, null=True)
    nom_empleadorecibe = models.CharField(max_length=100, blank=True, null=True)
    num_flagpreconfirmado = models.SmallIntegerField(blank=True, null=True)
    num_flagconfirmado = models.SmallIntegerField(blank=True, null=True)
    fec_registro = models.DateTimeField(blank=True, null=True)
    num_flagjabavacia = models.SmallIntegerField(blank=True, null=True)
    fec_confirmacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_bpencguiassurtidohistresp'


class CtlCambiodomicilio(models.Model):
    id = models.AutoField()
    folio = models.IntegerField(blank=True, null=True)
    token = models.CharField(max_length=-1, blank=True, null=True)
    usado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_cambiodomicilio'


class CtlCambiomodelos(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    modelo = models.CharField(max_length=35, blank=True, null=True)
    fechaactualiza = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_cambiomodelos'


class CtlCambiosdcfarticulos(models.Model):
    numarea = models.SmallIntegerField()
    numdepto = models.SmallIntegerField()
    numclase = models.SmallIntegerField()
    numfamilia = models.SmallIntegerField()
    numcodigo = models.IntegerField()
    fechaactualiza = models.DateTimeField()
    numdeptoant = models.SmallIntegerField()
    numclaseant = models.SmallIntegerField()
    numfamiliaant = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_cambiosdcfarticulos'


class CtlCambiosdescarticulo(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    descarticulo = models.TextField(blank=True, null=True)
    fechaactualiza = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_cambiosdescarticulo'


class CtlCambiosnomarticulo(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    nomarticulo = models.CharField(max_length=120, blank=True, null=True)
    fechaactualiza = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_cambiosnomarticulo'


class CtlCambiosprecio(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    numcodigo = models.IntegerField()
    numtalla = models.SmallIntegerField()
    preciovta = models.IntegerField()
    tipocambio = models.SmallIntegerField()
    fechainicio = models.DateTimeField()
    fechafin = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_cambiosprecio'
        unique_together = (('numarea', 'numcodigo', 'numtalla'),)


class CtlCambiostipoivaarticulos(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    flag_manejaiva = models.SmallIntegerField(blank=True, null=True)
    fechaactualiza = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_cambiostipoivaarticulos'


class CtlCampaniasCoppel(models.Model):
    id_serial = models.AutoField()
    nomareawebabuelo = models.CharField(max_length=150)
    nomareawebpadre = models.CharField(max_length=150)
    nomareabwebhijo = models.CharField(max_length=150)
    desc_codigos = models.CharField(max_length=100)
    nom_imagen = models.CharField(max_length=100)
    desc_url = models.CharField(max_length=300)
    fec_inicio = models.DateField()
    fec_final = models.DateField()
    desc_sort = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'ctl_campanias_coppel'


class CtlCamposadicionalessellermarketplace(models.Model):
    idu_seller = models.BigIntegerField()
    idu_envioseller = models.BigIntegerField()
    des_codigo = models.CharField(max_length=254)
    des_tipo = models.CharField(max_length=50)
    des_valor = models.CharField(max_length=254)
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    opc_estatus = models.CharField(max_length=10)
    nom_actualiza = models.CharField(max_length=50)
    opc_procesado = models.SmallIntegerField()
    opc_tipocampoadicional = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_camposadicionalessellermarketplace'


class CtlCancelacionitemmarketplace(models.Model):
    idu_cancelacionitem = models.BigAutoField(primary_key=True)
    idu_detallepedidomk = models.ForeignKey('CtlDetallepedidosmarketplace', models.DO_NOTHING, db_column='idu_detallepedidomk')
    num_monto = models.DecimalField(max_digits=10, decimal_places=2)
    fec_creacion = models.DateTimeField()
    idu_solicitud = models.CharField(max_length=-1)
    num_articulo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_cancelacionitemmarketplace'


class CtlCargaMasivaCsv(models.Model):
    idu_carga_masiva_csv = models.BigAutoField(primary_key=True)
    idu_carga_masiva = models.ForeignKey('CtlCargasMasivasAtributos', models.DO_NOTHING, db_column='idu_carga_masiva')
    sku = models.IntegerField()
    numarea = models.SmallIntegerField()
    num_caracteristica = models.CharField(max_length=-1)
    num_detallecaracteristica = models.CharField(max_length=-1)
    desc_detallecaracteristica = models.CharField(max_length=-1)
    num_flag_csv = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ctl_carga_masiva_csv'


class CtlCargaMasivaRevert(models.Model):
    idu_revert_carga_masiva = models.BigAutoField(primary_key=True)
    idu_carga_masiva = models.ForeignKey('CtlCargasMasivasAtributos', models.DO_NOTHING, db_column='idu_carga_masiva')
    numempleado = models.IntegerField()
    desc_revert = models.CharField(max_length=-1)
    fec_revert = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_carga_masiva_revert'
# Unable to inspect table 'ctl_cargas_inventario'
# The error was: permission denied for table ctl_cargas_inventario


class CtlCargasMarketplace(models.Model):
    idu_carga = models.BigAutoField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.SmallIntegerField()
    error = models.TextField()

    class Meta:
        managed = False
        db_table = 'ctl_cargas_marketplace'


class CtlCargasMasivasAtributos(models.Model):
    idu_carga_masiva = models.BigAutoField(primary_key=True)
    num_empleado = models.IntegerField()
    num_totalcambios = models.SmallIntegerField()
    fec_subida = models.DateTimeField()
    desc_link_csv = models.CharField(max_length=-1)
    desc_comentario = models.CharField(max_length=-1)
    isrevert = models.IntegerField()
    error_carga = models.BooleanField()
    ind_processo = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ctl_cargas_masivas_atributos'


class CtlCargasdetrabajoPasillos(models.Model):
    idu_perfilusuario = models.BigIntegerField()
    num_pasillo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_cargasdetrabajo_pasillos'


class CtlCargasdetrabajoUsuarios(models.Model):
    idu_usuario = models.ForeignKey(CatUsuariosoficinadeenvios, models.DO_NOTHING, db_column='idu_usuario', blank=True, null=True)
    idu_perfilusuario = models.ForeignKey(CatCargasdetrabajo, models.DO_NOTHING, db_column='idu_perfilusuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_cargasdetrabajo_usuarios'


class CtlCarrito(models.Model):
    idsession = models.CharField(max_length=50, blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    numarea = models.SmallIntegerField(blank=True, null=True)
    cantidad = models.SmallIntegerField(blank=True, null=True)
    talla = models.CharField(max_length=10, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    id = models.AutoField()
    flag_sesion = models.CharField(max_length=64, blank=True, null=True)
    disponibilidadarticulo = models.IntegerField(blank=True, null=True)
    fechaentregaarticulo = models.DateField(blank=True, null=True)
    armararticulo = models.IntegerField(blank=True, null=True)
    preciocontadounitario = models.IntegerField(blank=True, null=True)
    articulonuevo = models.IntegerField(blank=True, null=True)
    preciopromocion = models.IntegerField(blank=True, null=True)
    disponibilidadmuebles = models.IntegerField(blank=True, null=True)
    fechaentregamuebles = models.DateField(blank=True, null=True)
    preciocreditounitario = models.IntegerField(blank=True, null=True)
    flag_armado = models.IntegerField(blank=True, null=True)
    preciooriginal = models.IntegerField(blank=True, null=True)
    idu_carrito = models.BigIntegerField(blank=True, null=True)
    num_foliotelcel = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_carrito'
        unique_together = (('idsession', 'numcodigo', 'numarea', 'talla'),)
# Unable to inspect table 'ctl_carritodatosentregapromesa'
# The error was: permission denied for table ctl_carritodatosentregapromesa


class CtlCarritoentregadetalle(models.Model):
    folio = models.IntegerField()
    numcodigo = models.IntegerField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    bodega = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    num_codigoanterior = models.IntegerField()
    fec_entregafuturo = models.DateField()
    num_flagventafuturo = models.IntegerField()
    num_cantidadventafuturo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_carritoentregadetalle'


class CtlCarritopedido(models.Model):
    idsession = models.CharField(max_length=50, blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    numarea = models.SmallIntegerField(blank=True, null=True)
    cantidad = models.SmallIntegerField(blank=True, null=True)
    talla = models.CharField(max_length=10, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    id = models.AutoField()
    flag_sesion = models.CharField(max_length=64, blank=True, null=True)
    folio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_carritopedido'


class CtlCarrusel(models.Model):
    numarea = models.IntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    id_cat_carrusel = models.IntegerField(blank=True, null=True)
    estatus = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_carrusel'


class CtlCarteraordenesdisponibles(models.Model):
    idu_registro = models.AutoField()
    idu_orden = models.IntegerField(blank=True, null=True)
    num_tabla = models.IntegerField(blank=True, null=True)
    opc_cita = models.SmallIntegerField(blank=True, null=True)
    fec_actualizacion = models.DateField()

    class Meta:
        managed = False
        db_table = 'ctl_carteraordenesdisponibles'


class CtlCarteraordenesdisponiblesDatoscliente(models.Model):
    idu_registro = models.BigIntegerField()
    idu_orden = models.IntegerField(blank=True, null=True)
    clavecliente = models.IntegerField(blank=True, null=True)
    nombrecliente = models.CharField(max_length=-1, blank=True, null=True)
    email_de = models.CharField(max_length=-1, blank=True, null=True)
    telefono_casa = models.CharField(max_length=-1, blank=True, null=True)
    telefono_cel = models.CharField(max_length=-1, blank=True, null=True)
    num_tabla = models.IntegerField(blank=True, null=True)
    opc_cita = models.SmallIntegerField(blank=True, null=True)
    fec_actualizacion = models.DateField()
    tipopago = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_carteraordenesdisponibles_datoscliente'


class CtlCategoriaarticulos(models.Model):
    numarea = models.OneToOneField(CatArticulos, models.DO_NOTHING, db_column='numarea', primary_key=True)
    numcodigo = models.IntegerField()
    numcategoria = models.ForeignKey(CatCategorias, models.DO_NOTHING, db_column='numcategoria')

    class Meta:
        managed = False
        db_table = 'ctl_categoriaarticulos'
        unique_together = (('numarea', 'numcodigo', 'numcategoria'),)


class CtlCedisenvios(models.Model):
    num_cedisregional = models.SmallIntegerField(primary_key=True)
    nom_cedisregional = models.CharField(max_length=25)
    nom_ipregional = models.CharField(max_length=20)
    clv_tipocedis = models.SmallIntegerField()
    nom_tipocedis = models.CharField(max_length=20)
    num_cedissoporte = models.SmallIntegerField()
    nom_cedissoporte = models.CharField(max_length=25)
    nom_ipsoporte = models.CharField(max_length=20)
    clv_predeterminado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_cedisenvios'


class CtlCedisnodosdisponibleecommerce(models.Model):
    num_cedisprincipal = models.SmallIntegerField(primary_key=True)
    num_cedissoporte = models.SmallIntegerField()
    opc_soporteconoficinaenvios = models.SmallIntegerField()
    clv_activo = models.SmallIntegerField()
    fec_ultimaactualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_cedisnodosdisponibleecommerce'
        unique_together = (('num_cedisprincipal', 'num_cedissoporte'),)


class CtlCelularesseg(models.Model):
    folio = models.IntegerField(blank=True, null=True)
    idsession = models.CharField(max_length=-1, blank=True, null=True)
    celular = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_celularesseg'


class CtlCifrascontrolVentaropa(models.Model):
    des_mensaje = models.CharField(max_length=30, blank=True, null=True)
    num_total_inicial = models.IntegerField(blank=True, null=True)
    num_total_vendido = models.IntegerField(blank=True, null=True)
    num_total_actual = models.IntegerField(blank=True, null=True)
    num_uni_sininventario = models.IntegerField(blank=True, null=True)
    fec_movimiento = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_cifrascontrol_ventaropa'


class CtlCitasordenes(models.Model):
    idu_cita = models.AutoField(primary_key=True)
    idu_orden = models.IntegerField()
    fec_cita = models.DateTimeField()
    num_telefono = models.BigIntegerField()
    opc_status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_citasordenes'


class CtlCiudadesRegionPeriodico(models.Model):
    idu_ciudad = models.IntegerField(primary_key=True)
    nom_ciudad = models.CharField(max_length=-1)
    idu_region_periodico = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_ciudades_region_periodico'
        unique_together = (('idu_ciudad', 'idu_region_periodico'),)


class CtlCiudadesbodega(models.Model):
    num_ciudad = models.IntegerField()
    num_bodega = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_ciudadesbodega'


class CtlCiudadesparticipantescatalogovirtual(models.Model):
    num_ciudad = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_ciudadesparticipantescatalogovirtual'


class CtlCiudadestelcel(models.Model):
    idu_ciudadestelcel = models.AutoField(primary_key=True)
    nom_ciudadtelcel = models.CharField(max_length=100)
    nom_estado = models.CharField(max_length=100)
    num_estado = models.SmallIntegerField()
    num_plaza = models.IntegerField()
    num_lada = models.SmallIntegerField()
    num_ciudadcoppel = models.IntegerField()
    nom_ciudadcoppel = models.CharField(max_length=100)
    num_region = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_ciudadestelcel'


class CtlCiudadestelcelc(models.Model):
    idu_ciudadestelcel = models.AutoField(primary_key=True)
    nom_ciudadtelcel = models.CharField(max_length=100)
    nom_estado = models.CharField(max_length=100)
    num_estado = models.SmallIntegerField()
    num_plaza = models.IntegerField()
    num_lada = models.SmallIntegerField()
    num_ciudadcoppel = models.IntegerField()
    nom_ciudadcoppel = models.CharField(max_length=100)
    num_region = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_ciudadestelcelc'


class CtlClienteivr(models.Model):
    numorden = models.IntegerField(primary_key=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    numtarjeta = models.CharField(max_length=16, blank=True, null=True)
    anio = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    cvv = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    idllamada = models.CharField(max_length=300, blank=True, null=True)
    idagente = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_clienteivr'


class CtlClientes(models.Model):
    idusuario = models.AutoField()
    nombre = models.CharField(max_length=30)
    apellidopaterno = models.CharField(max_length=30)
    apellidomaterno = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=-1)
    ciudad = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    calle = models.CharField(max_length=40)
    colonia = models.CharField(max_length=30)
    numcasa = models.CharField(max_length=12)
    clientecoppel = models.CharField(max_length=2)
    numclientecoppel = models.IntegerField()
    telefono = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    ext = models.CharField(max_length=20)
    cp = models.CharField(max_length=5)
    saldo = models.DecimalField(max_digits=65535, decimal_places=65535)
    otra = models.CharField(max_length=5)
    registro = models.CharField(max_length=1)
    correovalido = models.IntegerField()
    confirmado = models.CharField(max_length=1)
    interior = models.CharField(max_length=12)
    numciudad = models.IntegerField()
    numcolonia = models.IntegerField()
    numcalle = models.IntegerField()
    fechanacimiento = models.DateField()
    sexo = models.BooleanField()
    fecharegistro = models.DateField()
    celular = models.CharField(max_length=128, blank=True, null=True)
    entrecalles = models.CharField(max_length=-1, blank=True, null=True)
    domicilioobservaciones = models.CharField(max_length=-1, blank=True, null=True)
    token = models.CharField(max_length=100)
    nom_completousuario = models.CharField(max_length=100, blank=True, null=True)
    opc_recibirpromocion = models.SmallIntegerField(blank=True, null=True)
    opc_recibirmensaje = models.SmallIntegerField(blank=True, null=True)
    num_tiporegistro = models.IntegerField()
    num_origenregistro = models.IntegerField()
    num_empleado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_clientes'


class CtlClientesaenviaredocta(models.Model):
    numclientecoppel = models.IntegerField()
    nombre = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1)
    fecenviado = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_clientesaenviaredocta'


class CtlCodigosNoMostrarTalla(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numdepto = models.SmallIntegerField(blank=True, null=True)
    numclase = models.SmallIntegerField(blank=True, null=True)
    numfamilia = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_codigos_no_mostrar_talla'


class CtlCodigosNoMostrarTallaant(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numdepto = models.SmallIntegerField(blank=True, null=True)
    numclase = models.SmallIntegerField(blank=True, null=True)
    numfamilia = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_codigos_no_mostrar_tallaant'


class CtlCodigosNoPublicar(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    numcodigo = models.IntegerField()
    comentario = models.CharField(max_length=25)
    fec_movimiento = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_codigos_no_publicar'
        unique_together = (('numarea', 'numcodigo'),)


class CtlCodigosbaja(models.Model):
    numarea = models.IntegerField()
    numcodigo = models.IntegerField()
    fechabaja = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_codigosbaja'


class CtlCodigosbajamaeexistencias(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numbodega = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    numtalla = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_codigosbajamaeexistencias'


class CtlCodigoscelularesregion(models.Model):
    num_area = models.OneToOneField(CatArticulos, models.DO_NOTHING, db_column='num_area', primary_key=True)
    num_codigo = models.IntegerField()
    des_region = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'ctl_codigoscelularesregion'
        unique_together = (('num_area', 'num_codigo'),)


class CtlCodigosenuso(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.BigIntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_codigosenuso'


class CtlCodigosriesgo(models.Model):
    numcodigo = models.IntegerField(blank=True, null=True)
    flagriesgo = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_codigosriesgo'


class CtlCodigossituacionetiquetas(models.Model):
    num_area = models.SmallIntegerField(primary_key=True)
    num_codigo = models.IntegerField()
    idu_situacionetiqueta = models.ForeignKey(CatSituacionetiquetas, models.DO_NOTHING, db_column='idu_situacionetiqueta')

    class Meta:
        managed = False
        db_table = 'ctl_codigossituacionetiquetas'
        unique_together = (('num_area', 'num_codigo', 'idu_situacionetiqueta'),)


class CtlComponentes(models.Model):
    id_componente = models.IntegerField(primary_key=True)
    id_template = models.IntegerField()
    id_subcomponente = models.IntegerField()
    num_orden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_componentes'
        unique_together = (('id_componente', 'id_subcomponente'),)


class CtlComprasClientes(models.Model):
    num_cliente = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_compras_clientes'


class CtlComprasClientesCodigos(models.Model):
    num_cliente = models.BigIntegerField()
    num_area = models.SmallIntegerField()
    num_depto = models.SmallIntegerField()
    num_clase = models.SmallIntegerField()
    num_familia = models.SmallIntegerField()
    fec_compra = models.DateTimeField()
    fec_corte = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_compras_clientes_codigos'


class CtlCondicionalesBitacora(models.Model):
    id = models.IntegerField()
    id_tipo_proceso = models.IntegerField()
    valor = models.CharField(max_length=350)
    tipo = models.CharField(max_length=10)
    conversion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ctl_condicionales_bitacora'


class CtlConfAutomatizacion(models.Model):
    idu_conf_automatizacion = models.TextField(primary_key=True)
    num_intervalorepeticion = models.IntegerField()
    hrs_cronjob_ejecucion = models.TimeField()
    opc_habilitarcronjob = models.BooleanField()
    fec_hrs_ultima_ejecucion = models.DateTimeField(blank=True, null=True)
    fol_token = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_conf_automatizacion'


class CtlConfAutomatizacionMkp(models.Model):
    idu_conf_automatizacion = models.TextField(primary_key=True)
    num_intervalorepeticion = models.IntegerField()
    hrs_cronjob_ejecucion = models.TimeField()
    opc_habilitarcronjob = models.BooleanField()
    fec_hrs_ultima_ejecucion = models.DateTimeField(blank=True, null=True)
    fol_token = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_conf_automatizacion_mkp'


class CtlConfFechaPromesa(models.Model):
    idu_configuracion = models.AutoField(primary_key=True)
    des_variable = models.CharField(max_length=50)
    num_valor = models.CharField(max_length=2048)

    class Meta:
        managed = False
        db_table = 'ctl_conf_fecha_promesa'
# Unable to inspect table 'ctl_config_bodegas_oms'
# The error was: permission denied for table ctl_config_bodegas_oms


class CtlConfigCedisropa(models.Model):
    num_cedis = models.IntegerField(blank=True, null=True)
    nom_cedis = models.CharField(max_length=-1, blank=True, null=True)
    num_estatus = models.BooleanField(blank=True, null=True)
    num_tipoconfiguracion = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_config_cedisropa'


class CtlConfiguracionarchivozonas(models.Model):
    idu_archivo = models.AutoField()
    nom_rutaarchivo = models.CharField(max_length=150)
    nom_archivo = models.CharField(max_length=150)
    fec_alta = models.DateField()

    class Meta:
        managed = False
        db_table = 'ctl_configuracionarchivozonas'


class CtlConfiguracionfeedGoogleproductcategory(models.Model):
    descdepto = models.TextField()
    descclase = models.TextField()
    descfamilia = models.TextField()
    google_product_category = models.TextField()

    class Meta:
        managed = False
        db_table = 'ctl_configuracionfeed_googleproductcategory'


class CtlConfiguracionfeedproductos(models.Model):
    idu_configuracion = models.IntegerField()
    des_variable = models.CharField(max_length=50)
    num_valor = models.TextField()

    class Meta:
        managed = False
        db_table = 'ctl_configuracionfeedproductos'


class CtlConfiguracionmarketplace(models.Model):
    idu_configuracion = models.BigAutoField(primary_key=True)
    des_variable = models.CharField(max_length=50)
    num_valor = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'ctl_configuracionmarketplace'


class CtlConfiguracionoficinadeenvios(models.Model):
    idu_configuracion = models.AutoField()
    des_variable = models.CharField(max_length=50)
    num_valor = models.CharField(max_length=100)
    des_descripcion = models.CharField(max_length=50)
    num_tipoconfiguracion = models.SmallIntegerField()
    num_bodega = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_configuracionoficinadeenvios'


class CtlConfiguracionpasillos(models.Model):
    idu_configuracion = models.AutoField()
    num_pasillo = models.SmallIntegerField()
    num_letras = models.SmallIntegerField()
    num_bodega = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_configuracionpasillos'


class CtlConfiguracionratingsreviews(models.Model):
    idu_configuracion = models.IntegerField(primary_key=True)
    des_descripcion = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ctl_configuracionratingsreviews'


class CtlConfiguracionvariables(models.Model):
    idu_configuracion = models.AutoField(primary_key=True)
    des_variable = models.CharField(max_length=50)
    num_valor = models.CharField(max_length=50)
    num_tipoconfiguracion = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_configuracionvariables'


class CtlConfirmacionarticulos(models.Model):
    num_empleado = models.IntegerField()
    num_notafactura = models.IntegerField()
    idu_pedido = models.IntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.SmallIntegerField()
    num_area = models.SmallIntegerField()
    nom_articulo = models.CharField(max_length=120)
    id_serial = models.IntegerField(blank=True, null=True)
    num_cantidad = models.IntegerField()
    num_preciocompra = models.IntegerField()
    num_precioetiqueta = models.IntegerField()
    num_condicion = models.SmallIntegerField()
    nom_url = models.CharField(max_length=-1, blank=True, null=True)
    flag_confirmado = models.SmallIntegerField(blank=True, null=True)
    flag_clasificado = models.SmallIntegerField()
    num_bodega = models.IntegerField()
    fec_registro = models.DateTimeField()
    fec_confirmacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_confirmacionarticulos'


class CtlContactosellermarketplace(models.Model):
    idu_seller = models.BigIntegerField()
    nom_ciudad = models.CharField(max_length=254)
    des_estadocivil = models.CharField(max_length=254)
    nom_pais = models.CharField(max_length=254)
    des_email = models.CharField(max_length=254)
    des_fax = models.CharField(max_length=254)
    nom_nombre = models.CharField(max_length=254)
    nom_apellido = models.CharField(max_length=254)
    num_telefono = models.CharField(max_length=254)
    num_telefono2 = models.CharField(max_length=254)
    nom_estado = models.CharField(max_length=254)
    nom_calle1 = models.CharField(max_length=254)
    nom_calle2 = models.CharField(max_length=254)
    des_sitioweb = models.CharField(max_length=254)
    num_codigopostal = models.CharField(max_length=254)
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    opc_estatus = models.CharField(max_length=10)
    nom_actualiza = models.CharField(max_length=50)
    opc_procesado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_contactosellermarketplace'


class CtlControlprocesamientoordenesventa(models.Model):
    ordenprocesandose = models.BigIntegerField()
    fechainicial_proc = models.DateTimeField()
    fechafinal_proc = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_controlprocesamientoordenesventa'


class CtlControltokenTa(models.Model):
    csession = models.CharField(max_length=64)
    ctoken = models.CharField(max_length=-1, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    flag = models.SmallIntegerField()
    correo = models.CharField(max_length=-1, blank=True, null=True)
    numcliente = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_controltoken_ta'


class CtlCorreosreporteguias(models.Model):
    num_empleado = models.IntegerField()
    nombre = models.CharField(max_length=-1, blank=True, null=True)
    fecha_alta = models.DateField(blank=True, null=True)
    estatus = models.IntegerField(blank=True, null=True)
    correo = models.CharField(max_length=-1, blank=True, null=True)
    permiso_admin = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_correosreporteguias'
        unique_together = (('num_empleado', 'correo'),)


class CtlCpATramite(models.Model):
    idu_cp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_cp_a_tramite'


class CtlCrossselling(models.Model):
    idu_lareacodigo = models.SmallIntegerField(blank=True, null=True)
    idu_ldeptocodigo = models.SmallIntegerField(blank=True, null=True)
    idu_lclasecodigo = models.SmallIntegerField(blank=True, null=True)
    idu_lfamiliacodigo = models.SmallIntegerField(blank=True, null=True)
    idu_rareacodigo = models.SmallIntegerField(blank=True, null=True)
    idu_rdeptocodigo = models.SmallIntegerField(blank=True, null=True)
    idu_rclasecodigo = models.SmallIntegerField(blank=True, null=True)
    idu_rfamiliacodigo = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_crossselling'


class CtlCuentacorrientevtaempleados(models.Model):
    fol_orden = models.IntegerField(primary_key=True)
    fol_nota_ropa = models.IntegerField()
    fol_factura_muebles = models.IntegerField()
    imp_ropa_pago_cuenta_corriente = models.IntegerField()
    imp_ropa_pago_tarjeta_credito = models.IntegerField()
    imp_ropa_descuento = models.IntegerField()
    imp_muebles_pago_cta_corriente = models.IntegerField()
    imp_muebles_pago_tarjeta_credito = models.IntegerField()
    imp_muebles_descuento = models.IntegerField()
    imp_num_empleado = models.IntegerField()
    fec_registro = models.DateField()
    hor_registro = models.TimeField()

    class Meta:
        managed = False
        db_table = 'ctl_cuentacorrientevtaempleados'


class CtlCuentasconvencido(models.Model):
    idu_cuentasconvencido = models.AutoField()
    num_status = models.IntegerField(blank=True, null=True)
    idu_convenio = models.IntegerField()
    num_tipocuenta = models.IntegerField()
    clv_cuenta = models.CharField(max_length=1)
    des_tipocuenta = models.CharField(max_length=30)
    num_factura = models.CharField(max_length=50)
    imp_saldo = models.IntegerField()
    imp_saldacon = models.IntegerField()
    imp_vencido = models.IntegerField()
    imp_abonobase = models.IntegerField()
    num_porcentaje = models.FloatField()
    imp_montocliente = models.IntegerField()
    fec_registro = models.DateTimeField()
    fec_actualizo = models.DateTimeField(blank=True, null=True)
    num_cliente = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_cuentasconvencido'


class CtlDatoscreditoordenes(models.Model):
    fol_orden = models.BigIntegerField(primary_key=True)
    num_cliente = models.IntegerField()
    des_situacionespecial = models.CharField(max_length=1)
    num_causasituacionespecial = models.IntegerField()
    num_plazo_ropa = models.IntegerField()
    imp_enganchepropuesto_ropa = models.IntegerField()
    imp_enganchecliente_ropa = models.IntegerField()
    imp_contado_ropa = models.IntegerField()
    imp_credito_ropa = models.IntegerField()
    imp_sobreprecioinicial_ropa = models.IntegerField()
    imp_sobrepreciofinal_ropa = models.IntegerField()
    imp_abono_ropa = models.IntegerField()
    imp_nuevosaldo_ropa = models.IntegerField()
    imp_nuevoabono_ropa = models.IntegerField()
    num_parametricoaltoriesgo_ropa = models.IntegerField()
    prc_saturacion_ropa = models.IntegerField()
    imp_nuevosaldoparametrico_ropa = models.IntegerField()
    imp_pagoultimosdocemeses_ropa = models.IntegerField()
    num_tasainteres_ropa = models.IntegerField()
    num_plazo_muebles = models.IntegerField()
    imp_enganchepropuesto_muebles = models.IntegerField()
    imp_enganchecliente_muebles = models.IntegerField()
    imp_contado_muebles = models.IntegerField()
    imp_credito_muebles = models.IntegerField()
    imp_sobreprecioinicial_muebles = models.IntegerField()
    imp_sobrepreciofinal_muebles = models.IntegerField()
    imp_abono_muebles = models.IntegerField()
    num_parametricoaltoriesgo_muebles = models.IntegerField()
    num_parametricocelulares = models.IntegerField()
    prc_saturacion_muebles = models.IntegerField()
    imp_nuevosaldoparametrico_muebles = models.IntegerField()
    imp_pagoultimosdocemeses_muebles = models.BigIntegerField()
    num_prepuntajealtoriesgo = models.IntegerField()
    imp_pagorequeridomuebles = models.IntegerField()
    imp_pagorequeridoropa = models.IntegerField()
    num_flagplazo = models.SmallIntegerField()
    fec_registro = models.DateField()

    class Meta:
        managed = False
        db_table = 'ctl_datoscreditoordenes'


class CtlDeltasCelularesTelcel(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    numcodigo = models.IntegerField()
    partnumber = models.CharField(max_length=64)
    parentpartnumber = models.CharField(max_length=64)
    modelo = models.CharField(max_length=35)
    color = models.CharField(max_length=35)
    numcodigo_parent = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_deltas_celulares_telcel'
        unique_together = (('numarea', 'numcodigo'),)


class CtlDeltasmarketplaceAtributos(models.Model):
    idu_atributomarketplace = models.BigIntegerField(primary_key=True)
    idu_atributoecommerce = models.BigIntegerField()
    name = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'ctl_deltasmarketplace_atributos'


class CtlDeltasmarketplaceCategorias(models.Model):
    idu_numareaweb = models.IntegerField(primary_key=True)
    groupidentifier = models.CharField(max_length=254)
    fec_creacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_deltasmarketplace_categorias'


class CtlDeltasmarketplaceRelacionproductoatributo(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=64)
    attributeidentifier = models.CharField(max_length=254)
    valueidentifier = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'ctl_deltasmarketplace_relacionproductoatributo'
        unique_together = (('partnumber', 'attributeidentifier'),)


class CtlDeltasmarketplaceRelacionproductocategoria(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=64)
    parentgroupidentifier = models.CharField(max_length=254)
    sellerid = models.BigIntegerField()
    published = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_deltasmarketplace_relacionproductocategoria'
        unique_together = (('partnumber', 'parentgroupidentifier'),)


class CtlDeltasmarketplaceRelacionproductoitem(models.Model):
    des_valoratributo = models.CharField(primary_key=True, max_length=254)
    idu_producto = models.BigIntegerField()
    partnumber = models.CharField(max_length=254)
    parentpartnumber = models.CharField(max_length=64, blank=True, null=True)
    sequence = models.BigIntegerField(blank=True, null=True)
    delete = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_deltasmarketplace_relacionproductoitem'
        unique_together = (('des_valoratributo', 'idu_producto', 'partnumber'),)


class CtlDeltasmarketplaceRollback(models.Model):
    idu_record = models.BigAutoField(primary_key=True)
    bloque = models.BigIntegerField()
    tablename = models.CharField(max_length=50)
    key1 = models.CharField(max_length=25)
    key2 = models.CharField(max_length=25)
    key3 = models.CharField(max_length=25)
    keyvalue1 = models.CharField(max_length=30)
    keyvalue2 = models.CharField(max_length=30)
    keyvalue3 = models.CharField(max_length=30)
    field = models.CharField(max_length=25)
    field2 = models.CharField(max_length=25)
    value = models.CharField(max_length=60)
    value2 = models.CharField(max_length=60)
    old_value = models.CharField(max_length=60)
    old_value2 = models.CharField(max_length=60)
    action = models.CharField(max_length=1)
    idu_carga = models.ForeignKey(CtlCargasMarketplace, models.DO_NOTHING, db_column='idu_carga')
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_deltasmarketplace_rollback'


class CtlDescontinuadosPromocion(models.Model):
    codigo = models.IntegerField(blank=True, null=True)
    articulo = models.CharField(max_length=30, blank=True, null=True)
    marca = models.CharField(max_length=30, blank=True, null=True)
    modelo = models.CharField(max_length=30, blank=True, null=True)
    depto = models.SmallIntegerField(blank=True, null=True)
    clase = models.SmallIntegerField(blank=True, null=True)
    familia = models.SmallIntegerField(blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    fechadescontinuado = models.DateTimeField(blank=True, null=True)
    existbodega = models.IntegerField(blank=True, null=True)
    preciovta = models.IntegerField(blank=True, null=True)
    promocion = models.IntegerField(blank=True, null=True)
    precioventainicial = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_descontinuados_promocion'


class CtlDescontinuadosPromocion2(models.Model):
    num_codigo = models.IntegerField(primary_key=True)
    fec_creacion = models.DateTimeField()
    fec_actualiza = models.DateTimeField()
    num_empleado = models.IntegerField()
    opc_activo = models.SmallIntegerField()
    num_publicar = models.SmallIntegerField()
    num_depto = models.SmallIntegerField()
    num_clase = models.IntegerField()
    num_familia = models.IntegerField()
    porcentaje = models.FloatField()
    precioventainicial = models.IntegerField()
    promocion = models.IntegerField()
    preciodeventafrontera = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_descontinuados_promocion_2'


class CtlDescripcionareasweb(models.Model):
    numarea = models.SmallIntegerField()
    numcodigo = models.IntegerField()
    nomareaweb = models.CharField(max_length=50, blank=True, null=True)
    nomareaweb1 = models.CharField(max_length=50, blank=True, null=True)
    nomareaweb2 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_descripcionareasweb'


class CtlDescripcionesseo(models.Model):
    id_descripcion = models.AutoField(unique=True)
    num_area = models.SmallIntegerField()
    num_areaweb = models.IntegerField()
    nom_areaweb = models.CharField(max_length=50)
    des_contenido = models.CharField(max_length=50)
    des_contenidofinal = models.CharField(max_length=130)
    num_activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ctl_descripcionesseo'


class CtlDetGuias(models.Model):
    id_ctl_det_guias = models.AutoField(primary_key=True)
    nu_guia = models.CharField(max_length=25)
    nu_factura = models.IntegerField()
    fh_asignacion_guia = models.DateTimeField()
    sn_guia_asignada = models.BooleanField()
    sn_guia_cancelada = models.BooleanField(blank=True, null=True)
    de_cancelacion_guia = models.TextField(blank=True, null=True)
    fh_reemplazo_guia = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_det_guias'


class CtlDetInventarioTienda(models.Model):
    id_inventario = models.IntegerField()
    numcodigo = models.IntegerField()
    talla = models.IntegerField()
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    folio = models.IntegerField()
    nomarticulo = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ctl_det_inventario_tienda'


class CtlDetallearticuloserror(models.Model):
    num_folio = models.BigIntegerField()
    num_orderitem = models.BigIntegerField()
    des_statuscodigo = models.CharField(max_length=-1)
    fec_movimiento = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_detallearticuloserror'


class CtlDetalleguiasmarketplace(models.Model):
    num_guia = models.CharField(max_length=-1)
    idu_ordenlogistica = models.CharField(max_length=-1)
    idu_devolucion = models.CharField(max_length=-1)
    idu_linea = models.CharField(max_length=-1)
    send_or23 = models.BooleanField()
    send_or74 = models.BooleanField()
    pdf_guia = models.CharField(max_length=-1, blank=True, null=True)
    id_rate = models.IntegerField(blank=True, null=True)
    id_order_ec = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_detalleguiasmarketplace'


class CtlDetalleordenesbloqueadas(models.Model):
    idu_bloqueo = models.BigIntegerField()
    id_orden = models.CharField(max_length=64)
    num_codigo = models.IntegerField()
    des_codigo = models.CharField(max_length=120)
    num_area = models.SmallIntegerField()
    num_totalcodigos = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_detalleordenesbloqueadas'


class CtlDetalleordenesrecuperadas(models.Model):
    id_folio = models.ForeignKey('CtlOrdenesrecuperadas', models.DO_NOTHING, db_column='id_folio')
    num_cantidad = models.SmallIntegerField()
    num_codigo = models.IntegerField()
    num_area = models.SmallIntegerField()
    num_talla = models.CharField(max_length=10)
    num_preciocontado = models.IntegerField()
    num_preciocredito = models.IntegerField()
    flag_promocion = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_detalleordenesrecuperadas'


class CtlDetallepedidos(models.Model):
    idu_pedido = models.IntegerField(blank=True, null=True)
    nom_sitem = models.CharField(max_length=50, blank=True, null=True)
    num_area = models.SmallIntegerField(blank=True, null=True)
    num_talla = models.IntegerField(blank=True, null=True)
    num_codigo = models.IntegerField(blank=True, null=True)
    num_cantidad = models.IntegerField(blank=True, null=True)
    num_ganodineroe = models.IntegerField(blank=True, null=True)
    num_gastodineroe = models.IntegerField(blank=True, null=True)
    num_preciooriginal = models.IntegerField(blank=True, null=True)
    num_preciocreditounitario = models.IntegerField(blank=True, null=True)
    num_preciopromocion = models.IntegerField(blank=True, null=True)
    num_foliotelcel = models.BigIntegerField()
    des_articulo = models.CharField(max_length=12)
    num_tipoprecio = models.SmallIntegerField()
    num_tipodescuento = models.SmallIntegerField()
    num_preciodescuentoempleado = models.IntegerField()
    num_orderitem = models.BigIntegerField()
    nom_articuloweb = models.CharField(max_length=120, blank=True, null=True)
    num_codigochip = models.IntegerField()
    num_codigoanterior = models.IntegerField()
    num_preciocreditocoppel = models.IntegerField()
    num_dcfmkp = models.IntegerField()
    clv_ordenoms = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_detallepedidos'


class CtlDetallepedidosmarketplace(models.Model):
    idu_ordenlogistica = models.CharField(max_length=-1)
    num_ordenitem = models.BigIntegerField()
    idu_linea = models.CharField(max_length=-1)
    des_statuslinea = models.CharField(max_length=-1)
    des_razoncodigostatuslinea = models.CharField(max_length=-1)
    des_razonstatuslinea = models.CharField(max_length=-1)
    prc_ivacomision = models.DecimalField(max_digits=10, decimal_places=2)
    imp_comisionsiniva = models.DecimalField(max_digits=10, decimal_places=2)
    imp_ivacomision = models.DecimalField(max_digits=10, decimal_places=2)
    imp_totalcomision = models.DecimalField(max_digits=10, decimal_places=2)
    idu_factura = models.IntegerField()
    fec_entrega = models.DateField()
    idu_detallepedidomk = models.BigAutoField(primary_key=True)
    idu_pedidosmkpl = models.ForeignKey('CtlPedidosmarketplace', models.DO_NOTHING, db_column='idu_pedidosmkpl')
    opc_incidenteabierto = models.BooleanField()
    opc_rembolso = models.BooleanField()
    fec_creacion = models.DateTimeField()
    fec_debito = models.DateTimeField()
    fec_ultimaactualizacion = models.DateTimeField()
    clv_codigostatusoferta = models.CharField(max_length=15)
    fec_recepcion = models.DateTimeField()
    fec_envio = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_detallepedidosmarketplace'


class CtlDetallepedidospbmasiva(models.Model):
    idu_pedido = models.IntegerField(blank=True, null=True)
    nom_sitem = models.CharField(max_length=50, blank=True, null=True)
    num_area = models.SmallIntegerField(blank=True, null=True)
    num_talla = models.IntegerField(blank=True, null=True)
    num_codigo = models.IntegerField(blank=True, null=True)
    num_cantidad = models.IntegerField(blank=True, null=True)
    num_ganodineroe = models.IntegerField(blank=True, null=True)
    num_gastodineroe = models.IntegerField(blank=True, null=True)
    num_preciooriginal = models.IntegerField(blank=True, null=True)
    num_preciocreditounitario = models.IntegerField(blank=True, null=True)
    num_preciopromocion = models.IntegerField(blank=True, null=True)
    num_foliotelcel = models.BigIntegerField(blank=True, null=True)
    des_articulo = models.CharField(max_length=12, blank=True, null=True)
    num_tipoprecio = models.SmallIntegerField(blank=True, null=True)
    num_tipodescuento = models.SmallIntegerField(blank=True, null=True)
    num_preciodescuentoempleado = models.IntegerField(blank=True, null=True)
    num_orderitem = models.BigIntegerField(blank=True, null=True)
    nom_articuloweb = models.CharField(max_length=120, blank=True, null=True)
    num_codigochip = models.IntegerField(blank=True, null=True)
    num_codigoanterior = models.IntegerField(blank=True, null=True)
    num_preciocreditocoppel = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_detallepedidospbmasiva'


class CtlDetalleplantilla(models.Model):
    numdetalleplantilla = models.AutoField(primary_key=True)
    numdetallecaracteristica = models.IntegerField()
    numarea = models.SmallIntegerField(blank=True, null=True)
    numdepto = models.SmallIntegerField(blank=True, null=True)
    numclase = models.SmallIntegerField(blank=True, null=True)
    numfamilia = models.SmallIntegerField(blank=True, null=True)
    idu_carga_masiva = models.ForeignKey(CtlCargasMasivasAtributos, models.DO_NOTHING, db_column='idu_carga_masiva', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_detalleplantilla'


class CtlDetcarritoinvitado(models.Model):
    keyx = models.ForeignKey('CtlEnccarritoinvitado', models.DO_NOTHING, db_column='keyx', blank=True, null=True)
    numarea = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    nomarticuloweb = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'ctl_detcarritoinvitado'


class CtlDevolucionRopa(models.Model):
    num_folio_devolucion = models.IntegerField()
    num_folio_reembolso = models.IntegerField(blank=True, null=True)
    num_total_reembolso = models.IntegerField(blank=True, null=True)
    num_folioropa = models.IntegerField()
    id_serial = models.IntegerField(blank=True, null=True)
    nom_cliente = models.CharField(max_length=200, blank=True, null=True)
    fec_devolucion = models.DateField(blank=True, null=True)
    nom_empleado_devolucion = models.IntegerField(blank=True, null=True)
    idu_motivo = models.IntegerField(blank=True, null=True)
    flag_devolucion_parcial = models.SmallIntegerField(blank=True, null=True)
    num_bodega_oficina_envios = models.IntegerField(blank=True, null=True)
    num_importe = models.IntegerField(blank=True, null=True)
    nom_estatusdevolucion = models.CharField(max_length=-1, blank=True, null=True)
    idu_origen_devolucion = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_devolucion_ropa'


class CtlDiasCancelacionAutomaticas(models.Model):
    num_areaweb = models.IntegerField()
    desc_areas = models.CharField(max_length=-1)
    num_dia = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_dias_cancelacion_automaticas'


class CtlDineroelectronicocontado(models.Model):
    num_folio = models.BigIntegerField(primary_key=True)
    imp_gastoderopa = models.IntegerField()
    imp_gastodemuebles = models.IntegerField()
    opc_generaventa = models.SmallIntegerField()
    fec_orden = models.DateField()
    imp_saldodealafecha = models.IntegerField()
    num_cliente = models.BigIntegerField()
    opc_segenerodineroelectronico = models.IntegerField()
    opc_correodineroelectronico = models.IntegerField()
    imp_generoderopa = models.IntegerField()
    imp_generodemuebles = models.IntegerField()
    fec_generodineroelectronico = models.DateTimeField()
    fec_enviocorreodineroelectronico = models.DateTimeField()
    opc_seprocesoordenpendientepago = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_dineroelectronicocontado'
        unique_together = (('num_folio', 'num_cliente'),)


class CtlDineroelectronicopendiente(models.Model):
    num_folioorden = models.BigIntegerField(primary_key=True)
    des_montos = models.TextField()
    des_request = models.TextField()
    opc_tipocliente = models.CharField(max_length=8)
    opc_procesado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_dineroelectronicopendiente'


class CtlDineroelectronicowebsphere(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    precio_o_dscto = models.IntegerField(blank=True, null=True)
    fechainicia = models.DateField(blank=True, null=True)
    fechafinal = models.DateField(blank=True, null=True)
    flagagotarexistencia = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_dineroelectronicowebsphere'


class CtlDireccionentrega(models.Model):
    idu_pedido = models.IntegerField(primary_key=True)
    nom_completo = models.CharField(max_length=100, blank=True, null=True)
    num_estado = models.IntegerField(blank=True, null=True)
    num_ciudad = models.IntegerField(blank=True, null=True)
    num_colonia = models.IntegerField(blank=True, null=True)
    nom_calle = models.CharField(max_length=-1, blank=True, null=True)
    nom_entrecalles = models.CharField(max_length=-1, blank=True, null=True)
    num_casa = models.IntegerField(blank=True, null=True)
    num_codigopostal = models.CharField(max_length=-1, blank=True, null=True)
    num_coloniareferencia = models.IntegerField(blank=True, null=True)
    des_observaciones = models.CharField(max_length=-1, blank=True, null=True)
    num_interior = models.CharField(max_length=7)
    num_telefono = models.CharField(max_length=20)
    opc_celular = models.BooleanField()
    des_coloniacommerce = models.CharField(max_length=200)
    num_telefono2 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_direccionentrega'


class CtlDireccionipstiendas(models.Model):
    idu_tienda = models.SmallIntegerField()
    nom_tienda = models.CharField(max_length=30)
    num_ciudad = models.SmallIntegerField()
    nom_ciudad = models.CharField(max_length=50)
    num_iva = models.SmallIntegerField()
    num_direccionip = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ctl_direccionipstiendas'


class CtlDistcoppelresponse(models.Model):
    num_guia = models.CharField(max_length=-1, blank=True, null=True)
    idu_estatus = models.CharField(max_length=-1, blank=True, null=True)
    fecha_recibido = models.DateTimeField(blank=True, null=True)
    nom_quienrecibio = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_distcoppelresponse'


class CtlDivisiondeptosfamilias(models.Model):
    idudivisiondepto = models.IntegerField()
    numdepto = models.IntegerField()
    numclase = models.IntegerField()
    numfamilia = models.IntegerField()
    idudivisiondeptosfamilias = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'ctl_divisiondeptosfamilias'


class CtlDomiciliosbloqueados(models.Model):
    idu_bloqueo = models.BigIntegerField()
    nom_personaentrega = models.CharField(max_length=30)
    nom_apellidopaternoentrega = models.CharField(max_length=30)
    nom_apellidomaternoentrega = models.CharField(max_length=30, blank=True, null=True)
    nom_calleentrega = models.CharField(max_length=50)
    num_exteriorentrega = models.CharField(max_length=12)
    num_estadoentrega = models.IntegerField()
    num_ciudadentrega = models.IntegerField()
    nom_coloniaentrega = models.CharField(max_length=50)
    num_codigopostalentrega = models.IntegerField()
    nom_entrecalles = models.CharField(max_length=-1, blank=True, null=True)
    clv_bloqueo = models.IntegerField()
    fec_registro = models.DateTimeField()
    num_estatus = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_domiciliosbloqueados'


class CtlEmpleadoregistrado(models.Model):
    idu_registroempleado = models.IntegerField()
    num_empleado = models.IntegerField()
    nom_completo = models.CharField(max_length=100, blank=True, null=True)
    nom_email = models.CharField(max_length=50, blank=True, null=True)
    idu_empresa = models.SmallIntegerField()
    num_ciudad = models.IntegerField()
    opc_estatusempleado = models.BooleanField()
    opc_genero = models.SmallIntegerField()
    fec_nacimiento = models.DateField()
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    idu_movimientoregistroempleado = models.SmallIntegerField()
    num_empleado_sesion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_empleadoregistrado'


class CtlEnccarritoinvitado(models.Model):
    keyx = models.BigAutoField(primary_key=True)
    fecha = models.DateTimeField()
    idsession = models.CharField(max_length=50, blank=True, null=True)
    idu_carrito = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    enviocat = models.SmallIntegerField(blank=True, null=True)
    envioemailing = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_enccarritoinvitado'


class CtlEntregaArticulosBodega(models.Model):
    num_folio = models.BigIntegerField()
    idu_pedido = models.IntegerField()
    num_area = models.SmallIntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.SmallIntegerField()
    num_bodegaentrega = models.IntegerField()
    fec_entrega = models.DateField()
    fec_movto = models.DateField()
    fec_entregafuturo = models.DateField()
    num_cantidadventafuturo = models.IntegerField()
    num_estatusbodegaropa = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_entrega_articulos_bodega'


class CtlEnvioclickpaquetera(models.Model):
    idu_envioclick = models.BigAutoField(primary_key=True)
    id_order_ec = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=256)
    detalle_estatus = models.CharField(max_length=256)
    recibidopor = models.CharField(max_length=256)
    fecha_llegada = models.DateTimeField()
    fecha_real_recoleccion = models.DateTimeField()
    fecha_real_entrega = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_envioclickpaquetera'


class CtlEnvioclickpaqueteras(models.Model):
    idu_envioclick = models.BigAutoField(primary_key=True)
    ordenlogistica = models.CharField(max_length=-1)
    codigopostal_origen = models.IntegerField()
    codigopostal_destino = models.IntegerField()
    nombre_paquetera = models.CharField(max_length=256)
    costo_guia = models.IntegerField()
    fecha_estimada_entrega = models.DateTimeField()
    fecha_entrega = models.DateTimeField()
    fecha_creacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_envioclickpaqueteras'
# Unable to inspect table 'ctl_enviocorreoentregadomkp'
# The error was: permission denied for table ctl_enviocorreoentregadomkp


class CtlEnviocorreoentregapedido(models.Model):
    num_orden = models.IntegerField(blank=True, null=True)
    num_guia = models.CharField(max_length=-1, blank=True, null=True)
    nom_cliente = models.CharField(max_length=-1, blank=True, null=True)
    fecha_entrega = models.CharField(max_length=-1, blank=True, null=True)
    paquetera = models.CharField(max_length=-1, blank=True, null=True)
    fecha_procesamiento = models.DateTimeField()
    id_sesion = models.IntegerField(blank=True, null=True)
    flag_enviado = models.BooleanField(blank=True, null=True)
    nom_correo = models.CharField(max_length=-1, blank=True, null=True)
    des_paquetera = models.CharField(max_length=-1, blank=True, null=True)
    idu_notificacion = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_enviocorreoentregapedido'


class CtlEnviocorreoentregapedidomkp(models.Model):
    num_orden = models.IntegerField(blank=True, null=True)
    idu_ordenlogistica = models.CharField(max_length=-1, blank=True, null=True)
    nom_cliente = models.CharField(max_length=-1, blank=True, null=True)
    fecha_entrega = models.CharField(max_length=-1, blank=True, null=True)
    paquetera = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_enviocorreoentregapedidomkp'


class CtlEnvios(models.Model):
    id_envio = models.AutoField(primary_key=True)
    nu_control = models.IntegerField()
    nu_guia = models.CharField(max_length=25)
    fh_generacion_envio = models.DateTimeField()
    sn_envio_cancelado = models.BooleanField()
    de_envio_cancelado = models.CharField(max_length=255, blank=True, null=True)
    sn_paquete_enviado = models.BooleanField()
    fh_confirmacion_envio = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_envios'


class CtlEnviossellermarketplace(models.Model):
    idu_envioseller = models.BigAutoField()
    idu_seller = models.BigIntegerField()
    num_enviogratis = models.BigIntegerField()
    des_tipoenvio = models.CharField(max_length=254)
    des_tipoetiquetaenvio = models.CharField(max_length=254)
    des_codigozonaenvio = models.CharField(max_length=254)
    des_etiquetazonaenvio = models.CharField(max_length=254)
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    opc_estatus = models.CharField(max_length=10)
    nom_actualiza = models.CharField(max_length=50)
    opc_procesado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_enviossellermarketplace'


class CtlErroresCargamasiva(models.Model):
    idu_cargamasiva_error = models.BigAutoField(primary_key=True)
    sku_error = models.CharField(max_length=-1)
    campo_error = models.CharField(max_length=-1)
    descripcion_error = models.CharField(max_length=-1)
    id_carga_masiva = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_errores_cargamasiva'


class CtlErrorregistroguiasmarketplace(models.Model):
    idu_ordenlogistica = models.CharField(primary_key=True, max_length=-1)
    idu_linea = models.CharField(max_length=-1)
    tipo_guia = models.IntegerField()
    nom_carrier = models.CharField(max_length=-1, blank=True, null=True)
    error_msg = models.CharField(max_length=-1, blank=True, null=True)
    fec_creacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_errorregistroguiasmarketplace'


class CtlEstadisticasFiltradas(models.Model):
    orden_gral = models.IntegerField(blank=True, null=True)
    grupo = models.CharField(max_length=-1, blank=True, null=True)
    numdepto = models.IntegerField(blank=True, null=True)
    numclase = models.IntegerField(blank=True, null=True)
    numfamilia = models.IntegerField(blank=True, null=True)
    codigo = models.IntegerField(blank=True, null=True)
    orden_col = models.IntegerField(blank=True, null=True)
    corte = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_estadisticas_filtradas'


class CtlEstadisticasFiltradasRopa(models.Model):
    orden_gral = models.IntegerField(blank=True, null=True)
    grupo = models.CharField(max_length=-1, blank=True, null=True)
    numdepto = models.IntegerField(blank=True, null=True)
    numclase = models.IntegerField(blank=True, null=True)
    numfamilia = models.IntegerField(blank=True, null=True)
    codigo = models.IntegerField(blank=True, null=True)
    orden_col = models.IntegerField(blank=True, null=True)
    corte = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_estadisticas_filtradas_ropa'


class CtlEstadisticasFiltradasRopaCexis(models.Model):
    orden_gral = models.IntegerField(blank=True, null=True)
    grupo = models.CharField(max_length=-1, blank=True, null=True)
    numdepto = models.IntegerField(blank=True, null=True)
    numclase = models.IntegerField(blank=True, null=True)
    numfamilia = models.IntegerField(blank=True, null=True)
    codigo = models.IntegerField(blank=True, null=True)
    orden_col = models.IntegerField(blank=True, null=True)
    corte = models.DateTimeField(blank=True, null=True)
    disponible = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_estadisticas_filtradas_ropa_cexis'


class CtlEstadisticasFiltradasRopaSexis(models.Model):
    orden_gral = models.IntegerField(blank=True, null=True)
    grupo = models.CharField(max_length=-1, blank=True, null=True)
    numdepto = models.IntegerField(blank=True, null=True)
    numclase = models.IntegerField(blank=True, null=True)
    numfamilia = models.IntegerField(blank=True, null=True)
    codigo = models.IntegerField(blank=True, null=True)
    orden_col = models.IntegerField(blank=True, null=True)
    corte = models.DateTimeField(blank=True, null=True)
    disponible = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_estadisticas_filtradas_ropa_sexis'


class CtlEstadisticasMuebles(models.Model):
    numarea = models.IntegerField(blank=True, null=True)
    numdepto = models.IntegerField(blank=True, null=True)
    numclase = models.IntegerField(blank=True, null=True)
    numfamilia = models.IntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    publicar = models.IntegerField(blank=True, null=True)
    num_imagenes = models.IntegerField(blank=True, null=True)
    descestatus = models.TextField(blank=True, null=True)
    nomarticulo = models.TextField(blank=True, null=True)
    nomarticuloweb = models.TextField(blank=True, null=True)
    caracteristicas = models.IntegerField(blank=True, null=True)
    tipo6_numbodegas = models.IntegerField(blank=True, null=True)
    excluir = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_estadisticas_muebles'


class CtlEstadisticasRopa(models.Model):
    numarea = models.IntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    numdepto = models.IntegerField(blank=True, null=True)
    numclase = models.IntegerField(blank=True, null=True)
    numfamilia = models.IntegerField(blank=True, null=True)
    numdisponibilidad = models.IntegerField(blank=True, null=True)
    disponibilidad = models.CharField(max_length=1, blank=True, null=True)
    comprar = models.IntegerField(blank=True, null=True)
    entrada = models.IntegerField(blank=True, null=True)
    publicar = models.IntegerField(blank=True, null=True)
    numestatus = models.IntegerField(blank=True, null=True)
    tipoarticulo = models.TextField(blank=True, null=True)
    flagimagen = models.IntegerField(blank=True, null=True)
    numtipoarticulo = models.IntegerField(blank=True, null=True)
    existencia = models.IntegerField(blank=True, null=True)
    comprar_talla = models.IntegerField(blank=True, null=True)
    num_imagenes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_estadisticas_ropa'


class CtlEstadospaqueteras(models.Model):
    idu_estado = models.IntegerField()
    idu_paquetera = models.IntegerField()
    idu_oficinadeenvios = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_estadospaqueteras'


class CtlEstafetaresponse(models.Model):
    idu_pedido = models.IntegerField(blank=True, null=True)
    num_folio = models.BigIntegerField(blank=True, null=True)
    num_guia = models.CharField(max_length=25, blank=True, null=True)
    desc_status = models.CharField(max_length=20, blank=True, null=True)
    fec_recibido = models.DateTimeField(blank=True, null=True)
    nom_quienrecibio = models.CharField(max_length=-1, blank=True, null=True)
    flag_enviadomotor = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_estafetaresponse'


class CtlEstatusaccertify(models.Model):
    num_folio = models.BigIntegerField(blank=True, null=True)
    num_tipopago = models.IntegerField(blank=True, null=True)
    des_estatus_accertify = models.CharField(max_length=-1, blank=True, null=True)
    fec_fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_estatusaccertify'


class CtlEstatuscodigos(models.Model):
    idu_registro = models.BigIntegerField(primary_key=True)
    num_folio = models.BigIntegerField()
    idu_estatuscodigo = models.IntegerField()
    num_area = models.IntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.IntegerField()
    num_cantidad = models.IntegerField()
    num_orderitem = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_estatuscodigos'


class CtlEstatuscodigospermitidos(models.Model):
    idu_estatuscodigospermitidos = models.AutoField(primary_key=True)
    num_estatuscodigo = models.IntegerField()
    num_estatuscodigopermitido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_estatuscodigospermitidos'


class CtlEstatusemails(models.Model):
    nom_email = models.CharField(unique=True, max_length=100)
    num_estatus = models.ForeignKey(CatEstatusemails, models.DO_NOTHING, db_column='num_estatus')
    sec_serial = models.AutoField()
    num_nodo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_estatusemails'


class CtlEstatuspedido(models.Model):
    num_folio = models.BigIntegerField(primary_key=True)
    num_cliente = models.BigIntegerField()
    idu_estatuspedido = models.IntegerField()
    fec_estimadaropa = models.DateTimeField()
    fec_promesamuebles = models.DateTimeField()
    fec_promesaropa = models.DateTimeField()
    fec_entregaropa = models.DateTimeField()
    fec_entregamuebles = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_estatuspedido'


class CtlEstatustarjetas(models.Model):
    clv_tarjetacredito = models.CharField(max_length=128)
    num_estatus = models.ForeignKey(CatEstatustarjetas, models.DO_NOTHING, db_column='num_estatus')
    sec_serial = models.AutoField()
    num_nodo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_estatustarjetas'


class CtlExclusionemarsys(models.Model):
    sku = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=-1, blank=True, null=True)
    categoria = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_exclusionemarsys'


class CtlExistenciaCedissurtenocom(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numbodega = models.SmallIntegerField(blank=True, null=True)
    numfolio = models.IntegerField(blank=True, null=True)
    numtalla = models.SmallIntegerField(blank=True, null=True)
    cantidad = models.SmallIntegerField(blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    idupedido = models.IntegerField(blank=True, null=True)
    existencia = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_existencia_cedissurtenocom'


class CtlExistenciasV9(models.Model):
    partnumber = models.CharField(max_length=-1, blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    numarea = models.SmallIntegerField(blank=True, null=True)
    numtalla = models.SmallIntegerField(blank=True, null=True)
    existencia = models.IntegerField(blank=True, null=True)
    flagventar = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_existencias_v9'


class CtlFacturacion(models.Model):
    id = models.IntegerField(blank=True, null=True)
    rfc = models.CharField(max_length=-1, blank=True, null=True)
    razonsocial = models.CharField(max_length=-1, blank=True, null=True)
    ciudad = models.CharField(max_length=-1, blank=True, null=True)
    estado = models.CharField(max_length=-1, blank=True, null=True)
    colonia = models.CharField(max_length=-1, blank=True, null=True)
    calle = models.CharField(max_length=-1, blank=True, null=True)
    codigopostal = models.IntegerField(blank=True, null=True)
    referencia = models.CharField(max_length=-1, blank=True, null=True)
    cliente = models.CharField(max_length=-1, blank=True, null=True)
    numerocasa = models.IntegerField(blank=True, null=True)
    numerointerior = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_facturacion'


class CtlFacturaciontelcel(models.Model):
    idu_facturacion = models.BigAutoField(primary_key=True)
    idsession = models.CharField(max_length=50)
    fol_orden = models.IntegerField()
    fol_factura = models.IntegerField()
    num_codigo = models.IntegerField()
    imp_unitario = models.IntegerField()
    num_cantidad = models.SmallIntegerField()
    nom_estado = models.CharField(max_length=100)
    num_ciudadcoppel = models.IntegerField()
    nom_ciudadtelcel = models.CharField(max_length=100)
    num_lada = models.SmallIntegerField()
    num_plaza = models.IntegerField()
    num_region = models.SmallIntegerField()
    fec_factura = models.DateField()
    hor_factura = models.TimeField()
    num_telefono = models.BigIntegerField()
    num_cliente = models.BigIntegerField()
    nom_cliente = models.CharField(max_length=100)
    des_direccion = models.CharField(max_length=250)
    des_mensaje = models.CharField(max_length=150)
    opc_estatus = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_facturaciontelcel'


class CtlFechasPromesaModelos(models.Model):
    num_folio = models.BigIntegerField(blank=True, null=True)
    field2 = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_fechas_promesa_modelos'


class CtlFoliosestadisticasanalytics(models.Model):
    idu_folio = models.AutoField()
    num_folio = models.IntegerField()
    num_consulta = models.IntegerField()
    fec_registro = models.DateField()
    hor_registro = models.TimeField()

    class Meta:
        managed = False
        db_table = 'ctl_foliosestadisticasanalytics'


class CtlFoliosgeneracioncfdi(models.Model):
    idu_folio = models.BigAutoField()
    num_folio = models.IntegerField()
    num_foliofacturacionmuebles = models.CharField(max_length=25)
    num_foliofacturacionropa = models.CharField(max_length=25)
    fec_movimiento = models.DateField()
    hor_movimiento = models.TimeField()

    class Meta:
        managed = False
        db_table = 'ctl_foliosgeneracioncfdi'


class CtlFoliostransitoconfirmados(models.Model):
    nom_folio = models.CharField(max_length=20)
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.SmallIntegerField(blank=True, null=True)
    num_cantidad = models.IntegerField(blank=True, null=True)
    num_area = models.SmallIntegerField(blank=True, null=True)
    num_cedis = models.SmallIntegerField()
    num_empleado = models.IntegerField(blank=True, null=True)
    fec_recibo = models.DateField()

    class Meta:
        managed = False
        db_table = 'ctl_foliostransitoconfirmados'


class CtlFoliostransitogenerados(models.Model):
    nom_folio = models.CharField(max_length=20)
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.SmallIntegerField(blank=True, null=True)
    num_cantidad = models.IntegerField(blank=True, null=True)
    num_area = models.SmallIntegerField(blank=True, null=True)
    num_cedis = models.SmallIntegerField()
    num_empleado = models.IntegerField(blank=True, null=True)
    fec_generado = models.DateField()

    class Meta:
        managed = False
        db_table = 'ctl_foliostransitogenerados'


class CtlFormadepago(models.Model):
    idu_pedido = models.OneToOneField('CtlPedidos', models.DO_NOTHING, db_column='idu_pedido', primary_key=True)
    num_tipopago = models.SmallIntegerField()
    num_pagoinicialropa = models.IntegerField()
    num_pagoinicialmuebles = models.IntegerField()
    flag_dineroelectronico = models.IntegerField()
    num_dineroelectronicoropa = models.IntegerField()
    num_dineroelectronicomuebles = models.IntegerField()
    num_importetdcropa = models.IntegerField()
    num_importetdcmuebles = models.IntegerField()
    num_porcentajedescuento = models.SmallIntegerField()
    num_margencompra = models.IntegerField()
    num_margencredito = models.IntegerField()
    num_sobrepreciomuebles = models.IntegerField()
    num_tarjeta = models.IntegerField()
    num_referencia = models.CharField(max_length=50)
    cve_banco = models.CharField(max_length=5, blank=True, null=True)
    imp_tdcmarketplace = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_formadepago'


class CtlFticancelados(models.Model):
    idu_foliotransitointernocancelado = models.BigAutoField()
    nom_foliotransito = models.CharField(max_length=20)
    num_empleado = models.IntegerField(blank=True, null=True)
    fec_cancelacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_fticancelados'


class CtlFticonfirmados(models.Model):
    idu_foliotransitointerno = models.BigAutoField()
    nom_foliotransito = models.CharField(max_length=20)
    num_empleado = models.IntegerField(blank=True, null=True)
    fec_confirmacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_fticonfirmados'


class CtlFtigenerados(models.Model):
    idu_foliotransitointernogenerado = models.BigAutoField()
    nom_folio = models.CharField(max_length=20)
    num_cantidad = models.IntegerField(blank=True, null=True)
    num_area = models.SmallIntegerField(blank=True, null=True)
    num_empleado = models.IntegerField(blank=True, null=True)
    fec_generado = models.DateField()

    class Meta:
        managed = False
        db_table = 'ctl_ftigenerados'


class CtlGeneradeordenes(models.Model):
    fol_orden = models.BigIntegerField(blank=True, null=True)
    imp_ganoderopa = models.IntegerField(blank=True, null=True)
    imp_ganodemuebles = models.IntegerField(blank=True, null=True)
    fec_orden = models.DateField(blank=True, null=True)
    num_cliente = models.IntegerField()
    clv_origen = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_generadeordenes'


class CtlGenerardeordenescontado(models.Model):
    num_folio = models.BigIntegerField()
    imp_ganoderopa = models.IntegerField()
    imp_ganodemuebles = models.IntegerField()
    fec_orden = models.DateField()
    num_cliente = models.BigIntegerField()
    clv_origen = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_generardeordenescontado'


class CtlGenerardeordenescontadodetalle(models.Model):
    num_folio = models.BigIntegerField()
    clv_area = models.SmallIntegerField()
    num_skuproducto = models.IntegerField()
    num_talla = models.IntegerField()
    num_cantidad = models.IntegerField()
    num_campana = models.IntegerField()
    imp_ganode = models.IntegerField()
    clv_origen = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_generardeordenescontadodetalle'


class CtlGenerardeordenesdetalle(models.Model):
    fol_orden = models.BigIntegerField(blank=True, null=True)
    clv_area = models.SmallIntegerField(blank=True, null=True)
    sku_producto = models.IntegerField(blank=True, null=True)
    num_talla = models.IntegerField(blank=True, null=True)
    num_cantidad = models.IntegerField(blank=True, null=True)
    num_campana = models.IntegerField(blank=True, null=True)
    imp_ganode = models.IntegerField(blank=True, null=True)
    clv_origen = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_generardeordenesdetalle'


class CtlGenerosnewsletter(models.Model):
    nom_email = models.CharField(primary_key=True, max_length=230)
    idu_genero = models.CharField(max_length=1, blank=True, null=True)
    fec_alta = models.DateTimeField(blank=True, null=True)
    fec_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_generosnewsletter'


class CtlGuiareenviooe(models.Model):
    idu_pedido = models.IntegerField()
    num_notafactura = models.IntegerField(blank=True, null=True)
    num_guiaoriginal = models.CharField(max_length=-1, blank=True, null=True)
    num_guiadevolucion = models.CharField(max_length=-1, blank=True, null=True)
    num_guiareenvio = models.CharField(max_length=-1, blank=True, null=True)
    flag_cancelacion = models.SmallIntegerField(blank=True, null=True)
    fec_registro = models.DateTimeField(blank=True, null=True)
    num_empleado = models.IntegerField(blank=True, null=True)
    idu_oficinadeenvios = models.BigIntegerField()
    observaciones = models.CharField(max_length=-1, blank=True, null=True)
    estatus = models.SmallIntegerField(blank=True, null=True)
    num_orden = models.BigIntegerField()
    fecha_reenvio = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_guiareenviooe'


class CtlGuiareenviooe20434483(models.Model):
    idu_pedido = models.IntegerField(blank=True, null=True)
    num_notafactura = models.IntegerField(blank=True, null=True)
    num_guiaoriginal = models.CharField(max_length=-1, blank=True, null=True)
    num_guiadevolucion = models.CharField(max_length=-1, blank=True, null=True)
    num_guiareenvio = models.CharField(max_length=-1, blank=True, null=True)
    flag_cancelacion = models.SmallIntegerField(blank=True, null=True)
    fec_registro = models.DateTimeField(blank=True, null=True)
    num_empleado = models.IntegerField(blank=True, null=True)
    idu_oficinadeenvios = models.BigIntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=-1, blank=True, null=True)
    estatus = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_guiareenviooe_20434483'


class CtlGuiareenviooeCi610132(models.Model):
    idu_pedido = models.IntegerField(blank=True, null=True)
    num_notafactura = models.IntegerField(blank=True, null=True)
    num_guiaoriginal = models.CharField(max_length=-1, blank=True, null=True)
    num_guiadevolucion = models.CharField(max_length=-1, blank=True, null=True)
    num_guiareenvio = models.CharField(max_length=-1, blank=True, null=True)
    flag_cancelacion = models.SmallIntegerField(blank=True, null=True)
    fec_registro = models.DateTimeField(blank=True, null=True)
    num_empleado = models.IntegerField(blank=True, null=True)
    idu_oficinadeenvios = models.BigIntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=-1, blank=True, null=True)
    estatus = models.SmallIntegerField(blank=True, null=True)
    num_orden = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_guiareenviooe_ci610132'


class CtlGuiasBodega(models.Model):
    num_guia = models.CharField(primary_key=True, max_length=15)
    resp_webservice = models.IntegerField()
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_guias_bodega'


class CtlGuiasTallas(models.Model):
    idu_guia_talla = models.BigAutoField(primary_key=True)
    num_depto = models.SmallIntegerField()
    num_clase = models.SmallIntegerField()
    num_familia = models.SmallIntegerField()
    nom_guia_talla = models.CharField(max_length=-1)
    numempleado = models.IntegerField()
    id_imagen = models.BigIntegerField()
    fecha = models.DateTimeField()
    fecha_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_guias_tallas'


class CtlGuiasTallasXsku(models.Model):
    idu_guia_talla_sku = models.BigAutoField(primary_key=True)
    num_codigo = models.IntegerField()
    num_area = models.SmallIntegerField()
    numempleado = models.IntegerField()
    id_imagen = models.BigIntegerField()
    fecha = models.DateTimeField()
    fecha_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_guias_tallas_xsku'


class CtlHeadercatalogo(models.Model):
    id_header = models.AutoField()
    nom_abuelo = models.CharField(max_length=-1, blank=True, null=True)
    nom_padre = models.CharField(max_length=-1, blank=True, null=True)
    nom_hijo = models.CharField(max_length=-1, blank=True, null=True)
    url_imagen = models.TextField(blank=True, null=True)
    url_destino = models.TextField(blank=True, null=True)
    flag_promocion = models.BooleanField(blank=True, null=True)
    url_destino_catalogo = models.TextField()

    class Meta:
        managed = False
        db_table = 'ctl_headercatalogo'
# Unable to inspect table 'ctl_historial_feedmkp'
# The error was: permission denied for table ctl_historial_feedmkp


class CtlIdentidadesbloqueadas(models.Model):
    id_orden = models.BigIntegerField()
    idu_bloqueo = models.BigIntegerField()
    nombre_cliente = models.CharField(max_length=30)
    nom_apellidopaternocliente = models.CharField(max_length=30)
    nom_apellidomaternocliente = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=50)
    num_telefonofijo = models.CharField(max_length=20)
    num_celular = models.CharField(max_length=20)
    num_ip = models.CharField(max_length=255, blank=True, null=True)
    clv_tarjetadecredito = models.CharField(max_length=128)
    clv_bloqueo = models.IntegerField(blank=True, null=True)
    des_nota = models.CharField(max_length=100)
    fec_registro = models.DateTimeField()
    num_estatus = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_identidadesbloqueadas'


class CtlIndexacion(models.Model):
    fec_actualizacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_indexacion'


class CtlInformacionmarketregistro2(models.Model):
    idu_registro = models.BigAutoField()
    num_producto = models.BigIntegerField(primary_key=True)
    num_tiporegistro = models.IntegerField()
    des_skuerp = models.CharField(max_length=-1)
    des_atributo1 = models.CharField(max_length=-1)
    des_variante1 = models.CharField(max_length=-1)
    des_atributo2 = models.CharField(max_length=-1)
    des_variante2 = models.CharField(max_length=-1)
    num_stock = models.IntegerField()
    num_area = models.SmallIntegerField()
    num_codigo = models.IntegerField()
    des_partnumber = models.CharField(max_length=-1)
    num_talla = models.IntegerField()
    num_depto = models.SmallIntegerField()
    num_clase = models.SmallIntegerField()
    num_familia = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_informacionmarketregistro2'
        unique_together = (('num_producto', 'des_skuerp'),)


class CtlInformacionpagosellermarketplace(models.Model):
    idu_seller = models.BigIntegerField()
    des_tipo = models.CharField(max_length=50)
    des_cuentabancaria = models.CharField(max_length=254)
    nom_ciudadbanco = models.CharField(max_length=254)
    nom_banco = models.CharField(max_length=254)
    des_direccionbanco = models.CharField(max_length=254)
    des_codigopostalbanco = models.CharField(max_length=254)
    des_clabe = models.CharField(max_length=254)
    nom_propietario = models.CharField(max_length=254)
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    opc_estatus = models.CharField(max_length=10)
    nom_actualiza = models.CharField(max_length=50)
    opc_procesado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_informacionpagosellermarketplace'


class CtlInformacionpagosellermarketplaceDetalle(models.Model):
    idu_seller = models.BigIntegerField()
    opc_pagobloqueado = models.BooleanField()
    imp_saldopagado = models.DecimalField(max_digits=10, decimal_places=2)
    des_suscripcionpago = models.BooleanField()
    imp_saldoporpagar = models.DecimalField(max_digits=10, decimal_places=2)
    imp_pagopendiente = models.DecimalField(max_digits=10, decimal_places=2)
    fec_iniciosuscripciongratis = models.DateTimeField()
    fec_finsuscripciongratis = models.DateTimeField()
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    opc_estatus = models.CharField(max_length=10)
    nom_actualiza = models.CharField(max_length=50)
    opc_procesado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_informacionpagosellermarketplace_detalle'


class CtlIntentosordenesdeventa(models.Model):
    folioorden = models.BigIntegerField(blank=True, null=True)
    numerointentos = models.IntegerField(blank=True, null=True)
    causa = models.TextField(blank=True, null=True)
    subcausa = models.TextField(blank=True, null=True)
    fecha_procesamiento = models.DateTimeField()
    facturado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_intentosordenesdeventa'


class CtlInventario(models.Model):
    numcodigo = models.IntegerField(primary_key=True)
    talla = models.IntegerField()
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_inventario'
        unique_together = (('numcodigo', 'talla'),)


class CtlInventarioTienda(models.Model):
    id_inventario = models.AutoField()
    fh_inventario = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_inventario_tienda'


class CtlInventariosoe(models.Model):
    id_serial = models.BigAutoField()
    num_area = models.SmallIntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.SmallIntegerField()
    num_cantidad = models.SmallIntegerField()
    num_precio = models.SmallIntegerField()
    fecha_entrada = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_inventariosoe'


class CtlInvespecial(models.Model):
    num_empleado = models.IntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.SmallIntegerField()
    num_area = models.SmallIntegerField()
    num_condicion = models.IntegerField()
    num_cantidad = models.IntegerField()
    num_preciocompra = models.IntegerField()
    num_precioetiqueta = models.IntegerField()
    num_resolucion = models.IntegerField()
    fec_registro = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_invespecial'


class CtlIovation(models.Model):
    idu_iovation = models.BigAutoField(primary_key=True)
    num_folio = models.IntegerField()
    nom_token = models.TextField()
    fec_creacion = models.DateField()

    class Meta:
        managed = False
        db_table = 'ctl_iovation'


class CtlIp(models.Model):
    keyx = models.AutoField()
    ip = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    flag_guest = models.BooleanField()
    ip_router = models.CharField(max_length=255, blank=True, null=True)
    orden = models.IntegerField()
    fecha = models.DateTimeField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_ip'


class CtlJabas(models.Model):
    nu_jabas_chicas = models.IntegerField(blank=True, null=True)
    nu_jabas_grandes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_jabas'


class CtlKeystrackingomnicanal(models.Model):
    appid = models.CharField(max_length=-1, blank=True, null=True)
    appkey = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_keystrackingomnicanal'


class CtlLandingpages(models.Model):
    idu_landingpage = models.AutoField()
    nom_landingpage = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_landingpages'


class CtlListadoemails(models.Model):
    idu_email = models.AutoField(blank=True, null=True)
    des_email = models.TextField(primary_key=True)
    opc_generadocorrecto = models.BooleanField()
    opc_generadoerror = models.BooleanField()
    opc_publicadocorrecto = models.BooleanField()
    opc_publicadoerror = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ctl_listadoemails'


class CtlListadoemailsMkp(models.Model):
    idu_email = models.AutoField(blank=True, null=True)
    des_email = models.TextField(primary_key=True)
    opc_generadocorrecto = models.BooleanField()
    opc_generadoerror = models.BooleanField()
    opc_publicadocorrecto = models.BooleanField()
    opc_publicadoerror = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ctl_listadoemails_mkp'


class CtlLogVentaempleado(models.Model):
    idu_log = models.AutoField()
    nom_archivo = models.CharField(max_length=100)
    desc_comentario = models.CharField(max_length=500)
    fec_movimiento = models.DateTimeField()
    num_folio = models.IntegerField()
    nom_mail = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'ctl_log_ventaempleado'


class CtlLogWsConvenio(models.Model):
    keyx = models.AutoField()
    idu_convenio = models.BigIntegerField(blank=True, null=True)
    idu_catalogo_ws = models.BigIntegerField(blank=True, null=True)
    respuesta_ws = models.TextField(blank=True, null=True)
    fec_fin = models.DateTimeField(blank=True, null=True)
    request_ws = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_log_ws_convenio'


class CtlLogactualizarestatus(models.Model):
    des_mensaje = models.CharField(max_length=100)
    idu_clave = models.IntegerField()
    idu_nivel = models.IntegerField()
    des_valoruno = models.CharField(max_length=30)
    des_valordos = models.CharField(max_length=30)
    fec_transaccion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_logactualizarestatus'


class CtlMarcadeltas(models.Model):
    idu_generaciondeltas = models.BigAutoField()
    opc_generaciondeltas = models.SmallIntegerField()
    fec_generaciondeltas = models.DateTimeField()
    opc_generacionfeed = models.SmallIntegerField()
    fec_generacionfeed = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_marcadeltas'


class CtlMarcasnovalidas(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    descmarca = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_marcasnovalidas'


class CtlMarcasoficiales(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    nummarca = models.IntegerField()
    descmarca = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'ctl_marcasoficiales'
        unique_together = (('numarea', 'nummarca'),)


class CtlMastercodigosoe(models.Model):
    num_codigo = models.IntegerField()
    num_talla = models.SmallIntegerField()
    num_cantidad = models.IntegerField()
    num_precioetiqueta = models.IntegerField()
    id_serial = models.BigIntegerField()
    clv_statusenvioropa = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_mastercodigosoe'


class CtlMayte(models.Model):
    idu_pedido = models.IntegerField(unique=True)
    fec_movimiento = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_mayte'


class CtlMedidas(models.Model):
    numcodigo = models.IntegerField(primary_key=True)
    peso = models.IntegerField()
    largo = models.IntegerField()
    ancho = models.IntegerField()
    alto = models.IntegerField()
    piescubicos = models.IntegerField()
    kilatajeorofino = models.IntegerField()
    peso_empaque = models.IntegerField()
    largo_empaque = models.IntegerField()
    ancho_empaque = models.IntegerField()
    alto_empaque = models.IntegerField()
    piescubicos_empaque = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_medidas'


class CtlMensajeriaresponse(models.Model):
    num_mensajeria = models.ForeignKey(CatMensajeriaactiva, models.DO_NOTHING, db_column='num_mensajeria', blank=True, null=True)
    num_guia = models.CharField(max_length=-1, blank=True, null=True)
    idu_estatus = models.CharField(max_length=-1, blank=True, null=True)
    nom_estatus = models.CharField(max_length=-1, blank=True, null=True)
    num_estatuscoppel = models.IntegerField(blank=True, null=True)
    nom_estatuscoppel = models.CharField(max_length=-1, blank=True, null=True)
    fecha_recibido = models.DateTimeField(blank=True, null=True)
    nom_quienrecibio = models.CharField(max_length=-1, blank=True, null=True)
    fecha_movto = models.DateTimeField(blank=True, null=True)
    flag_enviadomotor = models.IntegerField(blank=True, null=True)
    fecha_recoleccion = models.DateTimeField(blank=True, null=True)
    folio_manifiesto = models.IntegerField(blank=True, null=True)
    fecha_cerradomanifiesto = models.DateTimeField(blank=True, null=True)
    fecha_cartaporte = models.DateTimeField(blank=True, null=True)
    fecha_llegadanodo = models.DateTimeField(blank=True, null=True)
    nombre_nodo = models.CharField(max_length=-1, blank=True, null=True)
    intentos_entrega = models.IntegerField(blank=True, null=True)
    fecha_primerintento = models.DateTimeField(blank=True, null=True)
    fecha_entregaestimada = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_mensajeriaresponse'


class CtlMenuespeciales(models.Model):
    numarea = models.IntegerField(blank=True, null=True)
    nummenu = models.IntegerField(blank=True, null=True)
    numdepto = models.IntegerField(blank=True, null=True)
    numclase = models.IntegerField(blank=True, null=True)
    numfamilia = models.IntegerField(blank=True, null=True)
    fechaalta = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_menuespeciales'


class CtlModulosSistema(models.Model):
    idperfil = models.IntegerField(blank=True, null=True)
    idmodulo = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_modulos_sistema'


class CtlMonitoreoTiempoaire(models.Model):
    idu_monitoreo = models.AutoField()
    fec_movimiento = models.DateTimeField(unique=True, blank=True, null=True)
    des_respuesta_ws_soa = models.CharField(max_length=100)
    des_parametros_entrada = models.CharField(max_length=800)
    num_folio = models.IntegerField()
    num_cliente = models.IntegerField()
    num_empleado = models.IntegerField()
    num_importe = models.IntegerField()
    num_telefono = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_monitoreo_tiempoaire'


class CtlMovHistorial(models.Model):
    idu_mov_historial = models.BigAutoField()
    des_funcion = models.CharField(max_length=-1)
    num_registros = models.IntegerField()
    fec_inicia = models.DateTimeField()
    fec_termina = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_mov_historial'


class CtlMovtoTiempoAire(models.Model):
    idu_movto = models.AutoField(primary_key=True)
    idu_proceso = models.ForeignKey('CtlProcesosTiempoAire', models.DO_NOTHING, db_column='idu_proceso')
    idu_log = models.ForeignKey(CatLogTiempoAire, models.DO_NOTHING, db_column='idu_log')
    desc_respuesta = models.TextField()
    fec_movto = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_movto_tiempo_aire'


class CtlNewsletter(models.Model):
    email = models.CharField(primary_key=True, max_length=230)
    campaign = models.CharField(max_length=50)
    datereg = models.DateTimeField()
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_newsletter'


class CtlNotascompletas(models.Model):
    num_empleado = models.IntegerField()
    num_notafactura = models.IntegerField()
    idu_pedido = models.IntegerField()
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.SmallIntegerField(blank=True, null=True)
    num_area = models.SmallIntegerField()
    nom_articulo = models.CharField(max_length=120)
    id_serial = models.BigIntegerField(blank=True, null=True)
    num_cantidad = models.IntegerField()
    num_preciocompra = models.IntegerField()
    num_precioetiqueta = models.IntegerField()
    num_condicion = models.SmallIntegerField()
    nom_url = models.CharField(max_length=-1, blank=True, null=True)
    fec_registro = models.DateTimeField(blank=True, null=True)
    nom_posicion = models.CharField(max_length=-1, blank=True, null=True)
    flag_enviado = models.IntegerField()
    flag_foliomp = models.SmallIntegerField()
    flag_confirmado = models.SmallIntegerField()
    num_bodega = models.IntegerField()
    fec_confirmacion = models.DateTimeField()
    num_notaapartada = models.SmallIntegerField(blank=True, null=True)
    num_empleado_confirmacion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_notascompletas'


class CtlNotificacionesproactivas(models.Model):
    id_notificacion = models.AutoField(unique=True)
    num_tiponotificacion = models.IntegerField(blank=True, null=True)
    des_tiponotificacion = models.CharField(max_length=-1, blank=True, null=True)
    des_correo = models.TextField(blank=True, null=True)
    des_sms = models.CharField(max_length=-1, blank=True, null=True)
    des_pushnotification = models.CharField(max_length=-1, blank=True, null=True)
    des_whatsapp = models.CharField(max_length=-1, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    des_correopie1 = models.CharField(max_length=-1, blank=True, null=True)
    des_correopie2 = models.CharField(max_length=-1, blank=True, null=True)
    des_tituloh1 = models.CharField(max_length=-1, blank=True, null=True)
    des_tituloh2 = models.CharField(max_length=-1, blank=True, null=True)
    des_correo2 = models.TextField(blank=True, null=True)
    des_tituloproductos = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_notificacionesproactivas'


class CtlNotificacionesproactivasEnviosTmp(models.Model):
    id = models.BigAutoField()
    id_area = models.IntegerField()
    fecha_facturacion = models.DateField()
    id_tienda = models.IntegerField()
    id_cliente = models.IntegerField()
    depto_operacional = models.CharField(max_length=-1)
    num_caja = models.IntegerField()
    num_orden = models.IntegerField()
    num_empleado = models.IntegerField()
    num_factura = models.IntegerField(blank=True, null=True)
    num_nota = models.IntegerField()
    email_cliente = models.CharField(max_length=-1)
    trigger = models.CharField(max_length=-1, blank=True, null=True)
    id_trigger = models.CharField(max_length=-1, blank=True, null=True)
    fecha_envio_email = models.DateField(blank=True, null=True)
    status_email = models.SmallIntegerField()
    celular_cliente = models.CharField(max_length=-1, blank=True, null=True)
    proveedor_email = models.CharField(max_length=-1)
    id_notificacionproactiva = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_notificacionesproactivas_envios_tmp'


class CtlNotificacionesproactivasTipospagosMotivos(models.Model):
    id_notificacionproactiva_tipospago_motivo = models.AutoField(unique=True)
    id_notificacion = models.IntegerField()
    id_tipopago = models.IntegerField()
    id_motivo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_notificacionesproactivas_tipospagos_motivos'


class CtlNotificacionesproactivasfaltanteexcedentebitacora(models.Model):
    id_notificacionesproactivasrecordatorioecxeandfaltantepagobitac = models.BigAutoField()
    num_orden = models.IntegerField()
    fecha_envio = models.DateField()
    nom_correoelectronico = models.CharField(max_length=-1, blank=True, null=True)
    nom_cliente = models.CharField(max_length=-1, blank=True, null=True)
    nom_escenario = models.CharField(max_length=-1, blank=True, null=True)
    imp_escenario = models.IntegerField(blank=True, null=True)
    fecha_limite = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_notificacionesproactivasfaltanteexcedentebitacora'


class CtlNotificacionesproactivasfaltanteexcedentestatus(models.Model):
    id_notificacionesproactivasfaltanteexcedentestatus = models.AutoField(unique=True)
    clave_notificacion = models.CharField(max_length=-1, blank=True, null=True)
    num_diascontacto = models.SmallIntegerField()
    estatus = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_notificacionesproactivasfaltanteexcedentestatus'


class CtlNotificacionesproactivasincidenciasbitacora(models.Model):
    id_notificacionesproactivasincbitacora = models.BigAutoField()
    num_guia = models.CharField(max_length=-1)
    fecha_envio = models.DateField()
    idu_clave_mensajeriaestatus = models.CharField(max_length=2)
    fecha_respuesta_cliente = models.DateField(blank=True, null=True)
    num_tiponotificacion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_notificacionesproactivasincidenciasbitacora'


class CtlNotificacionesproactivasincidenciasstatus(models.Model):
    id_notificacionesproactivasincidenciasstatus = models.AutoField(unique=True)
    id_notificacionesproactivas = models.IntegerField()
    idu_clave_mensajeriastatus = models.CharField(max_length=2, blank=True, null=True)
    idu_paquetera = models.IntegerField()
    num_mensajeria = models.IntegerField()
    status = models.SmallIntegerField()
    nom_statusenvioclick = models.CharField(max_length=-1, blank=True, null=True)
    can_contactos = models.SmallIntegerField()
    num_diascontacto = models.SmallIntegerField()
    num_diasrespuesta = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_notificacionesproactivasincidenciasstatus'
        unique_together = (('id_notificacionesproactivas', 'idu_clave_mensajeriastatus', 'idu_paquetera', 'num_mensajeria', 'nom_statusenvioclick'),)


class CtlNotificacionesproactivasrecordatoriopagobitacora(models.Model):
    id_notificacionesproactivaspendientespagobitacora = models.BigAutoField()
    num_orden = models.IntegerField()
    fecha_envio = models.DateField()

    class Meta:
        managed = False
        db_table = 'ctl_notificacionesproactivasrecordatoriopagobitacora'


class CtlNotificacionesproactivasrecordatoriopagostatus(models.Model):
    id_notificacionesproactivasrecordatoriopagostatus = models.AutoField(unique=True)
    clave_notificacion = models.CharField(max_length=-1, blank=True, null=True)
    num_diascontacto = models.SmallIntegerField()
    estatus = models.SmallIntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_notificacionesproactivasrecordatoriopagostatus'


class CtlNuevosusuarioscommerce(models.Model):
    nom_correo = models.CharField(primary_key=True, max_length=100)
    nom_cliente = models.CharField(max_length=100)
    nom_apellidos = models.CharField(max_length=150)
    num_cliente = models.BigIntegerField()
    num_empleado = models.BigIntegerField()
    opc_procesado = models.IntegerField()
    fec_registro = models.DateField()
    hor_registro = models.TimeField()

    class Meta:
        managed = False
        db_table = 'ctl_nuevosusuarioscommerce'


class CtlOecapturainventario(models.Model):
    id_serial = models.AutoField()
    num_area = models.SmallIntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.SmallIntegerField()
    num_cantidad = models.SmallIntegerField()
    num_precio = models.SmallIntegerField()
    fecha_entrada = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_oecapturainventario'


class CtlOedireccionpedido(models.Model):
    id_direccionpedido = models.AutoField(primary_key=True)
    idu_pedido = models.IntegerField()
    nom_completo_cliente = models.CharField(max_length=100, blank=True, null=True)
    nom_completo_contacto = models.CharField(max_length=100, blank=True, null=True)
    nom_direccion = models.CharField(max_length=-1, blank=True, null=True)
    nom_colonia = models.CharField(max_length=100, blank=True, null=True)
    nom_referencia = models.CharField(max_length=-1, blank=True, null=True)
    nom_estado = models.CharField(max_length=20, blank=True, null=True)
    nom_ciudad = models.CharField(max_length=100, blank=True, null=True)
    num_codigopostal = models.CharField(max_length=-1, blank=True, null=True)
    num_telefono = models.CharField(max_length=20)
    nom_observaciones = models.CharField(max_length=-1, blank=True, null=True)
    num_empleadoregistro = models.IntegerField(blank=True, null=True)
    fecha_movimiento = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_oedireccionpedido'


class CtlOefechafactura(models.Model):
    num_area = models.SmallIntegerField()
    num_notafactura = models.IntegerField()
    fecha_facturacion = models.DateField()

    class Meta:
        managed = False
        db_table = 'ctl_oefechafactura'


class CtlOeliberaciondebloques(models.Model):
    idu_pedido = models.IntegerField()
    num_notafactura = models.IntegerField()
    num_area = models.SmallIntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.IntegerField()
    num_cantidad = models.SmallIntegerField()
    id_serial = models.IntegerField()
    num_codigo_confirmado = models.SmallIntegerField()
    flag_activo = models.IntegerField()
    num_empleado = models.IntegerField()
    fec_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_oeliberaciondebloques'


class CtlOepreclasificacion(models.Model):
    num_empleado = models.IntegerField()
    num_notafactura = models.IntegerField()
    idu_pedido = models.IntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.SmallIntegerField()
    num_area = models.SmallIntegerField()
    id_serial = models.BigIntegerField(blank=True, null=True)
    num_pasillo = models.IntegerField()
    nom_letra = models.CharField(max_length=20)
    num_bodega = models.IntegerField()
    flag_clasificado = models.SmallIntegerField()
    flag_foliomp = models.SmallIntegerField()
    fec_movimiento = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_oepreclasificacion'


class CtlOeracksocupados(models.Model):
    idu_rack = models.IntegerField(blank=True, null=True)
    num_nota = models.BigIntegerField(blank=True, null=True)
    num_orden = models.BigIntegerField(blank=True, null=True)
    num_codigo = models.BigIntegerField(blank=True, null=True)
    num_talla = models.CharField(max_length=-1, blank=True, null=True)
    fec_registro = models.DateTimeField(blank=True, null=True)
    num_flagocupado = models.SmallIntegerField(blank=True, null=True)
    keyx = models.BigAutoField()

    class Meta:
        managed = False
        db_table = 'ctl_oeracksocupados'


class CtlOrdenes(models.Model):
    idu_registro = models.IntegerField(blank=True, null=True)
    des_usuario = models.CharField(max_length=-1, blank=True, null=True)
    idu_orden = models.IntegerField(blank=True, null=True)
    num_tabla = models.IntegerField(blank=True, null=True)
    fec_bloqueo = models.DateTimeField(blank=True, null=True)
    opc_cita = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_ordenes'


class CtlOrdenesBanco(models.Model):
    id = models.AutoField()
    orden = models.IntegerField(blank=True, null=True)
    importe = models.IntegerField(blank=True, null=True)
    usado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_ordenes_banco'


class CtlOrdenesCanceladas(models.Model):
    idu_orden_cancelada = models.AutoField()
    num_folio = models.IntegerField()
    idu_motivos = models.ForeignKey(CatMotivosCancelacion, models.DO_NOTHING, db_column='idu_motivos')
    desc_cancelacion = models.TextField()
    fec_cancelada = models.DateTimeField()
    flag_reactivada = models.IntegerField(blank=True, null=True)
    num_empleado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_ordenes_canceladas'


class CtlOrdenesCanceladasAutomaticas(models.Model):
    idu_folio = models.IntegerField()
    fec_cancelada = models.DateField()
    fec_expira = models.DateField()

    class Meta:
        managed = False
        db_table = 'ctl_ordenes_canceladas_automaticas'


class CtlOrdenesUsoCat(models.Model):
    num_orden = models.IntegerField()
    num_empleado = models.IntegerField()
    fec_ingreso = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_ordenes_uso_cat'


class CtlOrdenesaenviarcorreo(models.Model):
    idu_envio = models.AutoField(primary_key=True)
    idu_carrito = models.BigIntegerField()
    id_orden = models.BigIntegerField()
    id_sesion = models.CharField(max_length=64)
    num_cliente = models.IntegerField(blank=True, null=True)
    id_tipocorreoenviar = models.SmallIntegerField()
    nom_email = models.CharField(max_length=250)
    nom_cliente = models.CharField(max_length=120)
    des_urlcarrito = models.CharField(max_length=100, blank=True, null=True)
    fec_alta = models.DateTimeField()
    fec_movimiento = models.DateTimeField()
    fec_envioemail = models.DateTimeField()
    id_proceso_envio = models.IntegerField()
    num_estatuscorreo = models.SmallIntegerField()
    num_estatuscompra = models.SmallIntegerField()
    num_tabla = models.SmallIntegerField()
    num_contenidoextra = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_ordenesaenviarcorreo'


class CtlOrdenesaenviarcorreoOchoDias(models.Model):
    idu_envio = models.IntegerField(blank=True, null=True)
    idu_carrito = models.BigIntegerField(blank=True, null=True)
    id_orden = models.BigIntegerField(blank=True, null=True)
    id_sesion = models.CharField(max_length=64, blank=True, null=True)
    num_cliente = models.IntegerField(blank=True, null=True)
    id_tipocorreoenviar = models.SmallIntegerField(blank=True, null=True)
    nom_email = models.CharField(max_length=250, blank=True, null=True)
    nom_cliente = models.CharField(max_length=120, blank=True, null=True)
    des_urlcarrito = models.CharField(max_length=100, blank=True, null=True)
    fec_alta = models.DateTimeField(blank=True, null=True)
    fec_movimiento = models.DateTimeField(blank=True, null=True)
    fec_envioemail = models.DateTimeField(blank=True, null=True)
    id_proceso_envio = models.IntegerField(blank=True, null=True)
    num_estatuscorreo = models.SmallIntegerField(blank=True, null=True)
    num_estatuscompra = models.SmallIntegerField(blank=True, null=True)
    num_tabla = models.SmallIntegerField(blank=True, null=True)
    num_contenidoextra = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_ordenesaenviarcorreo_ocho_dias'


class CtlOrdenesbloqueadas(models.Model):
    idu_bloqueo = models.BigIntegerField()
    id_orden = models.CharField(max_length=64)
    num_importe = models.IntegerField(blank=True, null=True)
    clv_bloqueo = models.IntegerField(blank=True, null=True)
    fec_orden = models.DateTimeField(blank=True, null=True)
    fec_registro = models.DateTimeField()
    num_estatus = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_ordenesbloqueadas'


class CtlOrdenesenviarcorreoProductos(models.Model):
    idu_envio = models.BigIntegerField()
    num_area = models.SmallIntegerField()
    num_codigo = models.IntegerField()
    num_depto = models.SmallIntegerField()
    num_clase = models.SmallIntegerField()
    num_familia = models.SmallIntegerField()
    num_cantidad = models.SmallIntegerField()
    nom_producto = models.CharField(max_length=116)
    des_urlimagen = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ctl_ordenesenviarcorreo_productos'


class CtlOrdenesenviarcorreoProductosOchoDias(models.Model):
    idu_envio = models.BigIntegerField(blank=True, null=True)
    num_area = models.SmallIntegerField(blank=True, null=True)
    num_codigo = models.IntegerField(blank=True, null=True)
    num_depto = models.SmallIntegerField(blank=True, null=True)
    num_clase = models.SmallIntegerField(blank=True, null=True)
    num_familia = models.SmallIntegerField(blank=True, null=True)
    num_cantidad = models.SmallIntegerField(blank=True, null=True)
    nom_producto = models.CharField(max_length=116, blank=True, null=True)
    des_urlimagen = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_ordenesenviarcorreo_productos_ocho_dias'


class CtlOrdenesmarketplace(models.Model):
    num_folio = models.BigIntegerField(primary_key=True)
    num_folioplataforma = models.BigIntegerField()
    num_foliopago = models.BigIntegerField()
    fec_registro = models.DateTimeField(blank=True, null=True)
    nom_plataforma = models.CharField(max_length=20, blank=True, null=True)
    des_observaciones = models.CharField(max_length=250, blank=True, null=True)
    num_empleado = models.IntegerField(blank=True, null=True)
    nom_empleado = models.CharField(max_length=50, blank=True, null=True)
    num_estatus = models.SmallIntegerField(blank=True, null=True)
    num_sku = models.IntegerField(blank=True, null=True)
    num_cantidadarticulos = models.SmallIntegerField(blank=True, null=True)
    num_guia = models.CharField(max_length=25, blank=True, null=True)
    des_talla = models.CharField(max_length=10, blank=True, null=True)
    des_tipoarticulo = models.CharField(max_length=1, blank=True, null=True)
    num_factura = models.IntegerField()
    num_nota = models.IntegerField()
    num_pagorequerido = models.IntegerField()
    fec_captura = models.DateTimeField(blank=True, null=True)
    fec_confirmacion = models.DateTimeField(blank=True, null=True)
    fec_cancelacion = models.DateTimeField(blank=True, null=True)
    fec_facturacion = models.DateTimeField(blank=True, null=True)
    fec_pendiente = models.DateTimeField(blank=True, null=True)
    num_validado = models.SmallIntegerField(blank=True, null=True)
    num_codigo_confirmado = models.SmallIntegerField()
    num_codigo_enviado = models.SmallIntegerField()
    id_serial = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_ordenesmarketplace'
        unique_together = (('num_folio', 'num_folioplataforma', 'num_foliopago'),)


class CtlOrdenesmotordetalle(models.Model):
    idu_ordendetalle = models.AutoField(primary_key=True)
    num_orden = models.IntegerField()
    estatus_orden = models.CharField(max_length=20)
    templateid = models.CharField(max_length=100, blank=True, null=True)
    origen = models.CharField(max_length=70)
    order_item_id = models.CharField(max_length=70, blank=True, null=True)
    order_status = models.CharField(max_length=20, blank=True, null=True)
    order_numguia = models.CharField(max_length=100, blank=True, null=True)
    estatus = models.IntegerField()
    fec_alta = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_ordenesmotordetalle'


class CtlOrdenesmotordetallehistorial(models.Model):
    idu_ordendetalle = models.AutoField(primary_key=True)
    num_orden = models.IntegerField()
    estatus_orden = models.CharField(max_length=20)
    templateid = models.CharField(max_length=100, blank=True, null=True)
    origen = models.CharField(max_length=70)
    order_item_id = models.CharField(max_length=70, blank=True, null=True)
    order_status = models.CharField(max_length=20, blank=True, null=True)
    order_numguia = models.CharField(max_length=100, blank=True, null=True)
    estatus = models.IntegerField()
    fec_alta = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_ordenesmotordetallehistorial'


class CtlOrdenesrecuperadas(models.Model):
    id_folio = models.BigIntegerField(primary_key=True)
    num_tipopago = models.SmallIntegerField()
    fec_movimiento = models.DateTimeField()
    num_importe = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_ordenesrecuperadas'


class CtlOrdenesvalidacioncontactabilidad(models.Model):
    num_folioorden = models.BigIntegerField()
    fec_movimiento = models.DateTimeField()
    num_cliente = models.BigIntegerField()
    num_empleado = models.BigIntegerField()
    num_telefono = models.CharField(max_length=12)
    idu_tipotelefono = models.SmallIntegerField()
    opc_registrada = models.SmallIntegerField()
    opc_rechazada = models.SmallIntegerField()
    desc_motivo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ctl_ordenesvalidacioncontactabilidad'


class CtlOrigenOrden(models.Model):
    folio = models.IntegerField(blank=True, null=True)
    registrado = models.CharField(max_length=-1, blank=True, null=True)
    id_tiempoaire = models.IntegerField(blank=True, null=True)
    fecha_realizada = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_origen_orden'


class CtlParametroscta(models.Model):
    idsesion = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_parametroscta'


class CtlPedidodetalle(models.Model):
    id_serial = models.AutoField()
    id_informacionpersonal = models.CharField(max_length=-1, blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    numarea = models.IntegerField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    talla = models.CharField(max_length=-1, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_pedidodetalle'


class CtlPedidoinformaciongeneral(models.Model):
    cc_vencido = models.CharField(max_length=-1, blank=True, null=True)
    sobreprecio12 = models.IntegerField(blank=True, null=True)
    sobreprecio18 = models.IntegerField(blank=True, null=True)
    folio = models.IntegerField(blank=True, null=True)
    puntajeparcelulares = models.IntegerField(blank=True, null=True)
    puntajeparaltoriesgo = models.IntegerField(blank=True, null=True)
    sobreprecioropa = models.IntegerField(blank=True, null=True)
    tasainteresropa = models.IntegerField(blank=True, null=True)
    cc_vencidoropa = models.CharField(max_length=-1, blank=True, null=True)
    nuevosaldoropa = models.IntegerField(blank=True, null=True)
    importeropa = models.IntegerField(blank=True, null=True)
    saldoropa = models.IntegerField(blank=True, null=True)
    importemuebles = models.IntegerField(blank=True, null=True)
    pagoinicialropa = models.IntegerField(blank=True, null=True)
    pagoinicialmuebles = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_pedidoinformaciongeneral'


class CtlPedidoinformacionpersonal(models.Model):
    nombre_de = models.CharField(max_length=-1, blank=True, null=True)
    apellidopaterno_de = models.CharField(max_length=-1, blank=True, null=True)
    apellidomaterno_de = models.CharField(max_length=-1, blank=True, null=True)
    telefono_de = models.CharField(max_length=-1, blank=True, null=True)
    celular_de = models.CharField(max_length=-1, blank=True, null=True)
    email_de = models.CharField(max_length=-1, blank=True, null=True)
    nombre_para = models.CharField(max_length=-1, blank=True, null=True)
    apellidopaterno_para = models.CharField(max_length=-1, blank=True, null=True)
    apellidomaterno_para = models.CharField(max_length=-1, blank=True, null=True)
    estado_para = models.CharField(max_length=-1, blank=True, null=True)
    ciudad_para = models.CharField(max_length=-1, blank=True, null=True)
    colonia_para = models.CharField(max_length=-1, blank=True, null=True)
    calle_para = models.CharField(max_length=-1, blank=True, null=True)
    entrecalles_para = models.CharField(max_length=-1, blank=True, null=True)
    codigopostal_para = models.CharField(max_length=-1, blank=True, null=True)
    numerocasa_para = models.IntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=-1, blank=True, null=True)
    id = models.AutoField(unique=True)
    idsession = models.CharField(max_length=64)
    flag_sesion = models.IntegerField(blank=True, null=True)
    nombreciudad_para = models.CharField(max_length=64, blank=True, null=True)
    nombreciudad_de = models.CharField(max_length=64, blank=True, null=True)
    dineroelectronico = models.IntegerField(blank=True, null=True)
    dineroelectronico_propuesto = models.IntegerField(blank=True, null=True)
    pagoinicial = models.IntegerField(blank=True, null=True)
    pagoinicial_propuesto = models.IntegerField(blank=True, null=True)
    clavecliente = models.IntegerField(blank=True, null=True)
    dineroelectronicoropa = models.IntegerField(blank=True, null=True)
    dineroelectronicomuebles = models.IntegerField(blank=True, null=True)
    pagoinicialropa = models.IntegerField(blank=True, null=True)
    pagoinicialmuebles = models.IntegerField(blank=True, null=True)
    importe = models.IntegerField(blank=True, null=True)
    importeropa = models.IntegerField(blank=True, null=True)
    importemuebles = models.IntegerField(blank=True, null=True)
    pagoinicialropa_propuesto = models.IntegerField(blank=True, null=True)
    pagoinicialmuebles_propuesto = models.IntegerField(blank=True, null=True)
    dineroelectronicoropa_propuesto = models.IntegerField(blank=True, null=True)
    dineroelectronicomuebles_propuesto = models.IntegerField(blank=True, null=True)
    validacioncreditoropa_propuesto = models.IntegerField(blank=True, null=True)
    coloniaref_para = models.IntegerField(blank=True, null=True)
    flagplazo18 = models.IntegerField(blank=True, null=True)
    flagplazo18_propuesto = models.IntegerField(blank=True, null=True)
    chk_facturacion = models.SmallIntegerField(blank=True, null=True)
    flag_dineroelectronico = models.IntegerField(blank=True, null=True)
    importemueblescredito = models.IntegerField(blank=True, null=True)
    importeropacredito = models.IntegerField(blank=True, null=True)
    validacioncreditomuebles_propuesto = models.IntegerField(blank=True, null=True)
    dineroelectronicomaximomuebles = models.IntegerField(blank=True, null=True)
    creditocoppel = models.IntegerField(blank=True, null=True)
    importemueblescredito18 = models.IntegerField(blank=True, null=True)
    sobreprecioropa = models.IntegerField(blank=True, null=True)
    gnfechatransaccion = models.DateField(blank=True, null=True)
    cuentabancaria = models.IntegerField(blank=True, null=True)
    fechagndominio = models.DateField(blank=True, null=True)
    tiempoactualizacion = models.DateTimeField(blank=True, null=True)
    referencia = models.CharField(max_length=16, blank=True, null=True)
    nsess = models.CharField(max_length=-1, blank=True, null=True)
    seq_abc = models.IntegerField(blank=True, null=True)
    seq_carrito = models.IntegerField(blank=True, null=True)
    seq_orden = models.IntegerField(blank=True, null=True)
    seq_credito = models.IntegerField(blank=True, null=True)
    tipopago = models.SmallIntegerField(blank=True, null=True)
    fechaultimaoperacion = models.DateTimeField(blank=True, null=True)
    tokenorden = models.CharField(max_length=-1, blank=True, null=True)
    pagoinicialropa_cliente = models.IntegerField(blank=True, null=True)
    pagoinicialmuebles_cliente = models.IntegerField(blank=True, null=True)
    pagoinicial_cliente = models.IntegerField(blank=True, null=True)
    dateultimaoperacion = models.DateTimeField(blank=True, null=True)
    flag_guest = models.SmallIntegerField(blank=True, null=True)
    forma_validacion = models.SmallIntegerField(blank=True, null=True)
    fechacreacion = models.DateTimeField(blank=True, null=True)
    nom_completousuario = models.CharField(max_length=100, blank=True, null=True)
    nom_completousuario_para = models.CharField(max_length=100, blank=True, null=True)
    num_extpara = models.CharField(max_length=6, blank=True, null=True)
    num_intpara = models.CharField(max_length=6, blank=True, null=True)
    num_opcionbloqueo = models.SmallIntegerField(blank=True, null=True)
    num_importetdcropa = models.IntegerField()
    num_importetdcmuebles = models.IntegerField()
    num_empleado = models.IntegerField()
    prc_saturacion = models.IntegerField()
    imp_nuevosaldo = models.IntegerField()
    num_puntajefinal = models.IntegerField()
    imp_pagoultimosdocemeses = models.IntegerField()
    prc_saturacion_ropa = models.IntegerField()
    imp_nuevosaldo_ropa = models.IntegerField()
    imp_pagoultimosdocemeses_ropa = models.IntegerField()
    prc_saturacion_muebles = models.IntegerField()
    num_puntajefinal_muebles = models.IntegerField()
    num_puntajefinal_ropa = models.IntegerField()
    imp_nuevosaldo_muebles = models.IntegerField()
    imp_pagoultimosdocemeses_muebles = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_pedidoinformacionpersonal'


class CtlPedidos(models.Model):
    idu_pedido = models.IntegerField(unique=True)
    nom_email = models.CharField(max_length=-1)
    num_clientecoppel = models.BigIntegerField()
    num_empleadocoppel = models.IntegerField()
    nom_cliente = models.CharField(max_length=-1)
    nom_apepaterno = models.CharField(max_length=100)
    nom_apematerno = models.CharField(max_length=100)
    num_importetotal = models.IntegerField()
    fec_orden = models.DateTimeField()
    num_telefono = models.CharField(max_length=20)
    opc_celular = models.BooleanField()
    num_folio = models.BigIntegerField(unique=True)
    num_estatus = models.IntegerField()
    num_totalarticulosmuebles = models.SmallIntegerField()
    num_totalarticulosropa = models.SmallIntegerField()
    num_importeropa = models.IntegerField()
    num_importemuebles = models.IntegerField()
    num_engancheropa = models.IntegerField()
    des_articulo = models.CharField(max_length=12)
    num_enganchemuebles = models.IntegerField()
    num_folioropa = models.IntegerField()
    num_foliomuebles = models.IntegerField()
    fec_movimiento = models.DateTimeField(blank=True, null=True)
    num_pagorecibido = models.IntegerField()
    desc_canalventa = models.CharField(max_length=20)
    desc_servicio = models.CharField(max_length=20)
    fec_facturanota = models.DateField()
    imp_marketplace = models.IntegerField(blank=True, null=True)
    fol_rastreounico = models.CharField(max_length=-1, blank=True, null=True)
    clv_ordenoms = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_pedidos'
        unique_together = (('num_folio', 'num_foliomuebles'),)


class CtlPedidosResplg(models.Model):
    idu_pedido = models.IntegerField(blank=True, null=True)
    nom_email = models.CharField(max_length=-1, blank=True, null=True)
    num_clientecoppel = models.BigIntegerField(blank=True, null=True)
    num_empleadocoppel = models.IntegerField(blank=True, null=True)
    nom_cliente = models.CharField(max_length=-1, blank=True, null=True)
    nom_apepaterno = models.CharField(max_length=100, blank=True, null=True)
    nom_apematerno = models.CharField(max_length=100, blank=True, null=True)
    num_importetotal = models.IntegerField(blank=True, null=True)
    fec_orden = models.DateTimeField(blank=True, null=True)
    num_telefono = models.CharField(max_length=20, blank=True, null=True)
    opc_celular = models.BooleanField(blank=True, null=True)
    num_folio = models.BigIntegerField(blank=True, null=True)
    num_estatus = models.IntegerField(blank=True, null=True)
    num_totalarticulosmuebles = models.SmallIntegerField(blank=True, null=True)
    num_totalarticulosropa = models.SmallIntegerField(blank=True, null=True)
    num_importeropa = models.IntegerField(blank=True, null=True)
    num_importemuebles = models.IntegerField(blank=True, null=True)
    num_engancheropa = models.IntegerField(blank=True, null=True)
    des_articulo = models.CharField(max_length=12, blank=True, null=True)
    num_enganchemuebles = models.IntegerField(blank=True, null=True)
    num_folioropa = models.IntegerField(blank=True, null=True)
    num_foliomuebles = models.IntegerField(blank=True, null=True)
    fec_movimiento = models.DateTimeField(blank=True, null=True)
    num_pagorecibido = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_pedidos_resplg'


class CtlPedidosmarketplace(models.Model):
    num_folio = models.BigIntegerField()
    idu_ordenlogistica = models.CharField(max_length=-1)
    num_cliente = models.IntegerField()
    idu_tiendaseller = models.IntegerField()
    des_statusorden = models.CharField(max_length=-1)
    des_razonstatusorden = models.CharField(max_length=-1)
    idu_razoncodigostatusorden = models.CharField(max_length=-1)
    num_tiempoembarque = models.SmallIntegerField()
    imp_precio = models.DecimalField(max_digits=10, decimal_places=2)
    imp_comisiontotal = models.DecimalField(max_digits=10, decimal_places=2)
    opc_errores = models.IntegerField(blank=True, null=True)
    idu_pedidosmkpl = models.BigAutoField(primary_key=True)
    fec_decisionaceptacion = models.DateTimeField()
    opc_cancelar = models.BooleanField()
    opc_evaluar = models.BooleanField()
    fec_creacion = models.DateTimeField()
    fec_debitocliente = models.DateTimeField()
    opc_clientemensaje = models.BooleanField()
    opc_incidente = models.BooleanField()
    opc_factura = models.BooleanField()
    fec_ultimaactualizacion = models.DateTimeField()
    clv_codigoenvio = models.CharField(max_length=15)
    des_companiaenvio = models.CharField(max_length=20)
    fec_plazoenvio = models.DateTimeField()
    num_precioenvio = models.DecimalField(max_digits=10, decimal_places=2)
    num_seguimientoenvio = models.CharField(max_length=50)
    des_urlseguimientoenvio = models.CharField(max_length=254)
    clv_codigotipoenvio = models.CharField(max_length=20)
    des_etiquetatipoenvio = models.CharField(max_length=254)
    num_preciototal = models.DecimalField(max_digits=10, decimal_places=2)
    fec_transaccion = models.DateTimeField()
    num_transaccion = models.CharField(max_length=50)
    num_precioconfirmar = models.DecimalField(max_digits=10, decimal_places=2)
    num_vendedortda = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_pedidosmarketplace'


class CtlPedidospbmasiva(models.Model):
    idu_pedido = models.IntegerField(blank=True, null=True)
    nom_email = models.CharField(max_length=-1, blank=True, null=True)
    num_clientecoppel = models.BigIntegerField(blank=True, null=True)
    num_empleadocoppel = models.IntegerField(blank=True, null=True)
    nom_cliente = models.CharField(max_length=-1, blank=True, null=True)
    nom_apepaterno = models.CharField(max_length=100, blank=True, null=True)
    nom_apematerno = models.CharField(max_length=100, blank=True, null=True)
    num_importetotal = models.IntegerField(blank=True, null=True)
    fec_orden = models.DateTimeField(blank=True, null=True)
    num_telefono = models.CharField(max_length=20, blank=True, null=True)
    opc_celular = models.BooleanField(blank=True, null=True)
    num_folio = models.BigIntegerField(blank=True, null=True)
    num_estatus = models.IntegerField(blank=True, null=True)
    num_totalarticulosmuebles = models.SmallIntegerField(blank=True, null=True)
    num_totalarticulosropa = models.SmallIntegerField(blank=True, null=True)
    num_importeropa = models.IntegerField(blank=True, null=True)
    num_importemuebles = models.IntegerField(blank=True, null=True)
    num_engancheropa = models.IntegerField(blank=True, null=True)
    des_articulo = models.CharField(max_length=12, blank=True, null=True)
    num_enganchemuebles = models.IntegerField(blank=True, null=True)
    num_folioropa = models.IntegerField(blank=True, null=True)
    num_foliomuebles = models.IntegerField(blank=True, null=True)
    fec_movimiento = models.DateTimeField(blank=True, null=True)
    num_pagorecibido = models.IntegerField(blank=True, null=True)
    desc_canalventa = models.CharField(max_length=20, blank=True, null=True)
    desc_servicio = models.CharField(max_length=20, blank=True, null=True)
    fec_facturanota = models.DateField(blank=True, null=True)
    imp_marketplace = models.IntegerField(blank=True, null=True)
    fol_rastreounico = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_pedidospbmasiva'


class CtlPedidosrealizados(models.Model):
    nombre_de = models.CharField(max_length=-1, blank=True, null=True)
    apellidopaterno_de = models.CharField(max_length=-1, blank=True, null=True)
    apellidomaterno_de = models.CharField(max_length=-1, blank=True, null=True)
    telefono_de = models.CharField(max_length=-1, blank=True, null=True)
    celular_de = models.CharField(max_length=-1, blank=True, null=True)
    email_de = models.CharField(max_length=-1, blank=True, null=True)
    nombre_para = models.CharField(max_length=-1, blank=True, null=True)
    apellidopaterno_para = models.CharField(max_length=-1, blank=True, null=True)
    apellidomaterno_para = models.CharField(max_length=-1, blank=True, null=True)
    estado_para = models.CharField(max_length=-1, blank=True, null=True)
    ciudad_para = models.CharField(max_length=-1, blank=True, null=True)
    colonia_para = models.CharField(max_length=-1, blank=True, null=True)
    calle_para = models.CharField(max_length=-1, blank=True, null=True)
    entrecalles_para = models.CharField(max_length=-1, blank=True, null=True)
    codigopostal_para = models.CharField(max_length=-1, blank=True, null=True)
    numerocasa_para = models.IntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=-1, blank=True, null=True)
    id = models.AutoField()
    idsession = models.CharField(max_length=64, blank=True, null=True)
    flag_sesion = models.IntegerField(blank=True, null=True)
    nombreciudad_para = models.CharField(max_length=64, blank=True, null=True)
    nombreciudad_de = models.CharField(max_length=64, blank=True, null=True)
    dineroelectronico = models.IntegerField(blank=True, null=True)
    dineroelectronico_propuesto = models.IntegerField(blank=True, null=True)
    pagoinicial = models.IntegerField(blank=True, null=True)
    pagoinicial_propuesto = models.IntegerField(blank=True, null=True)
    clavecliente = models.IntegerField(blank=True, null=True)
    pagado = models.IntegerField(blank=True, null=True)
    tipodecompra = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_pedidosrealizados'


class CtlPedidostienda(models.Model):
    num_folio = models.BigIntegerField(unique=True)
    num_empleado = models.IntegerField()
    num_caja = models.SmallIntegerField(blank=True, null=True)
    num_tienda_fisica = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_pedidostienda'


class CtlPendienteentregatda(models.Model):
    num_tienda = models.IntegerField()
    num_factura = models.IntegerField()
    idu_cliente = models.IntegerField()
    opc_recogecliente = models.SmallIntegerField()
    idu_tipoventa = models.SmallIntegerField()
    nom_nombrerecoge = models.CharField(max_length=50)
    nom_apellidopaternorecoge = models.CharField(max_length=50)
    nom_apellidomaternorecoge = models.CharField(max_length=50)
    fec_fechaventa = models.DateField()
    fec_fechamovto = models.DateTimeField()
    sec_keyx = models.AutoField()
    telefono_quien_recoge = models.BigIntegerField(blank=True, null=True)
    es_telefono_fijo = models.IntegerField(blank=True, null=True)
    idu_area = models.IntegerField(blank=True, null=True)
    idu_pedido = models.BigIntegerField()
    num_folio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_pendienteentregatda'


class CtlPendienteentregatdadetalle(models.Model):
    num_tienda = models.IntegerField()
    num_factura = models.IntegerField()
    num_codigo = models.IntegerField()
    num_cantidad = models.SmallIntegerField()
    num_cvesort = models.SmallIntegerField()
    num_estatus = models.SmallIntegerField()
    des_quienentrega = models.CharField(max_length=2)
    num_tiendaentrega = models.IntegerField()
    fec_fechaentregapropuesta = models.DateField()
    fec_fechaentregarealizada = models.DateField()
    des_serie = models.CharField(max_length=25)
    opc_flagcorreo = models.SmallIntegerField()
    fec_fechaentradatienda = models.DateField()
    fec_fechaactualizacion = models.DateField()
    num_referenciats = models.IntegerField()
    sec_keyx = models.IntegerField()
    bodegaentrega = models.IntegerField(blank=True, null=True)
    correoenviado_estatustres = models.SmallIntegerField(blank=True, null=True)
    correoenviado_estatuscuatro = models.SmallIntegerField(blank=True, null=True)
    correoenviado_faltandosdias = models.SmallIntegerField(blank=True, null=True)
    num_codigocelular = models.IntegerField()
    ismoto = models.IntegerField()
    correoenviado_moto = models.IntegerField(blank=True, null=True)
    num_estatusmoto = models.IntegerField()
    fec_fechaactivacion = models.DateField(blank=True, null=True)
    idu_area = models.IntegerField()
    idu_pedido = models.BigIntegerField()
    num_folio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_pendienteentregatdadetalle'


class CtlPendientesordenesde(models.Model):
    fol_orden = models.BigIntegerField(blank=True, null=True)
    clv_area = models.SmallIntegerField(blank=True, null=True)
    sku_producto = models.IntegerField(blank=True, null=True)
    num_talla = models.IntegerField(blank=True, null=True)
    num_cantidad = models.IntegerField(blank=True, null=True)
    num_campana = models.IntegerField(blank=True, null=True)
    imp_ganode = models.IntegerField(blank=True, null=True)
    clv_origen = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_pendientesordenesde'


class CtlPendientesordenesdecontado(models.Model):
    fol_orden = models.OneToOneField(CtlPedidos, models.DO_NOTHING, db_column='fol_orden', primary_key=True)
    clv_area = models.SmallIntegerField()
    sku_producto = models.IntegerField()
    num_talla = models.IntegerField()
    num_cantidad = models.IntegerField()
    num_campana = models.IntegerField()
    imp_ganode = models.IntegerField()
    clv_origen = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_pendientesordenesdecontado'
        unique_together = (('fol_orden', 'clv_area', 'sku_producto', 'num_talla'),)


class CtlPermisosadminmarketplace(models.Model):
    num_centro = models.IntegerField(unique=True)
    idu_permiso = models.ForeignKey(CatPermisosadminmarketplace, models.DO_NOTHING, db_column='idu_permiso')
    flag_activo = models.BooleanField()
    fec_alta = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_permisosadminmarketplace'


class CtlPermisosrolesoe(models.Model):
    idu_permiso = models.IntegerField(blank=True, null=True)
    idu_rol = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_permisosrolesoe'


class CtlPlantGuiasTallasParteCuerpoMedidasXsku(models.Model):
    idu_guia_parte_medida_xsku = models.BigAutoField(primary_key=True)
    id_guia_tallasku = models.BigIntegerField()
    id_guia_parte_cuerpo_sku = models.BigIntegerField()
    num_talla = models.SmallIntegerField()
    desc_medidas = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ctl_plant_guias_tallas_parte_cuerpo_medidas_xsku'


class CtlPlantGuiasTallasParteCuerpoXsku(models.Model):
    idu_guia_parte_xsku = models.BigAutoField(primary_key=True)
    id_guia_tallasku = models.BigIntegerField()
    id_parte_cuerpo = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_plant_guias_tallas_parte_cuerpo_xsku'


class CtlPlantillaGuiasTallasParteCuerpo(models.Model):
    idu_guia_parte = models.BigAutoField(primary_key=True)
    id_plantilla = models.BigIntegerField()
    id_parte_cuerpo = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_plantilla_guias_tallas_parte_cuerpo'


class CtlPlantillaGuiasTallasParteCuerpoMedidas(models.Model):
    idu_guia_parte_medida = models.BigAutoField(primary_key=True)
    id_plantilla = models.BigIntegerField()
    id_plantilla_parte_cuerpo = models.BigIntegerField()
    num_talla = models.SmallIntegerField()
    desc_medidas = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ctl_plantilla_guias_tallas_parte_cuerpo_medidas'


class CtlPlantillacaracteristica(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    numdepto = models.SmallIntegerField()
    numclase = models.SmallIntegerField()
    numfamilia = models.SmallIntegerField()
    numcaracteristica = models.ForeignKey(CatCaracteristicas, models.DO_NOTHING, db_column='numcaracteristica')
    numplantillacaracteristica = models.IntegerField()
    activo = models.BooleanField()
    num_ordendescripcion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_plantillacaracteristica'
        unique_together = (('numarea', 'numdepto', 'numclase', 'numfamilia', 'numcaracteristica'),)


class CtlPlantillasaccertify(models.Model):
    idu_plantilla = models.AutoField(primary_key=True)
    num_tipopago = models.IntegerField(blank=True, null=True)
    nom_tipocompra = models.CharField(max_length=15, blank=True, null=True)
    nom_formaprimaria = models.CharField(max_length=20, blank=True, null=True)
    nom_formasecundaria = models.CharField(max_length=20, blank=True, null=True)
    nom_opcion = models.CharField(max_length=60)
    nom_trigger = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'ctl_plantillasaccertify'


class CtlPlcypasswd(models.Model):
    idu_plcypasswd = models.BigIntegerField(primary_key=True)
    num_minpasswdlength = models.IntegerField()
    num_minalphabetic = models.IntegerField()
    num_minnumeric = models.IntegerField()
    num_maxinstances = models.IntegerField()
    num_maxconsecutivetype = models.IntegerField()
    num_maxlifetime = models.IntegerField()
    num_matchuserid = models.IntegerField()
    num_reusepassword = models.IntegerField()
    num_optcounter = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_plcypasswd'


class CtlPosicionesocupadas(models.Model):
    idu_posicion = models.IntegerField()
    num_empleado = models.IntegerField()
    num_notafactura = models.IntegerField()
    idu_pedido = models.IntegerField()
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.SmallIntegerField(blank=True, null=True)
    id_serial = models.BigIntegerField(blank=True, null=True)
    nom_posicion = models.CharField(max_length=-1, blank=True, null=True)
    opc_posicionllena = models.BooleanField(blank=True, null=True)
    flag_posicioncomplemento = models.IntegerField()
    idu_posicionpadre = models.IntegerField(blank=True, null=True)
    nom_posicionpadre = models.CharField(max_length=-1, blank=True, null=True)
    flag_articuloconfirmado = models.IntegerField(blank=True, null=True)
    flag_codigoleido = models.IntegerField()
    flag_foliomp = models.SmallIntegerField()
    fec_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_posicionesocupadas'


class CtlPreciocredito(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    numcodigo = models.IntegerField()
    numtalla = models.SmallIntegerField()
    numbodega = models.SmallIntegerField()
    preciocredito = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_preciocredito'
        unique_together = (('numarea', 'numbodega', 'numcodigo', 'numtalla'),)


class CtlPreconveniosdepago(models.Model):
    idu_convenio = models.AutoField()
    idu_status = models.SmallIntegerField()
    num_cliente = models.IntegerField()
    nom_cliente = models.CharField(max_length=100)
    nom_puntualidad = models.CharField(max_length=1)
    fec_ultimopago = models.DateField()
    imp_saldo = models.IntegerField()
    imp_vencido = models.IntegerField()
    imp_abonobase = models.IntegerField()
    imp_paseapagar = models.IntegerField()
    imp_mitadvencido = models.IntegerField()
    imp_montominimo = models.IntegerField()
    imp_montocliente = models.IntegerField()
    nom_situacionfinanciera = models.CharField(max_length=10)
    nom_estatusmontovencido = models.CharField(max_length=10)
    nom_mensajediagnostico = models.CharField(max_length=300)
    num_plazoconvenio = models.SmallIntegerField()
    fec_vigencia = models.DateField()
    fec_registro = models.DateTimeField()
    nom_correo = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_preconveniosdepago'


class CtlProcReclasificados(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    numcodigo = models.IntegerField()
    numdeptoant = models.SmallIntegerField()
    numclaseant = models.SmallIntegerField()
    numfamiliaant = models.SmallIntegerField()
    numdeptonuevo = models.SmallIntegerField()
    numclasenuevo = models.SmallIntegerField()
    numfamilianuevo = models.SmallIntegerField()
    atendido = models.BooleanField()
    usuarioatendio = models.CharField(max_length=-1)
    fechaatendido = models.DateTimeField()
    fechaactualizado = models.DateTimeField()
    vendible = models.SmallIntegerField()
    publicar = models.SmallIntegerField()
    status_view = models.SmallIntegerField()
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'ctl_proc_reclasificados'
        unique_together = (('numarea', 'numcodigo'),)


class CtlProcesarordenesdeventa(models.Model):
    folioorden = models.BigIntegerField(blank=True, null=True)
    num_cliente = models.BigIntegerField()
    num_empleado = models.BigIntegerField()
    ordenprocesada = models.IntegerField()
    correoenviado = models.IntegerField()
    fechaorden = models.DateField(blank=True, null=True)
    fec_factura = models.DateTimeField()
    fec_enviocorreo = models.DateTimeField()
    opc_procesandose = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_procesarordenesdeventa'


class CtlProcesarordenesdeventahistorial(models.Model):
    folioorden = models.BigIntegerField(blank=True, null=True)
    num_cliente = models.BigIntegerField(blank=True, null=True)
    num_empleado = models.BigIntegerField(blank=True, null=True)
    ordenprocesada = models.IntegerField(blank=True, null=True)
    correoenviado = models.IntegerField(blank=True, null=True)
    fechaorden = models.DateField(blank=True, null=True)
    fec_factura = models.DateTimeField(blank=True, null=True)
    fec_enviocorreo = models.DateTimeField(blank=True, null=True)
    opc_procesandose = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_procesarordenesdeventahistorial'


class CtlProcesoIndexacion(models.Model):
    flag_indexando = models.BooleanField(blank=True, null=True)
    fec_actualizacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_proceso_indexacion'


class CtlProcesosOficinadeenvios(models.Model):
    idu_oficinadeenvios = models.SmallIntegerField(blank=True, null=True)
    num_empleado = models.IntegerField(blank=True, null=True)
    idu_proceso = models.IntegerField(blank=True, null=True)
    nom_proceso = models.CharField(max_length=-1, blank=True, null=True)
    num_notafactura = models.IntegerField(blank=True, null=True)
    fec_movimiento = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_procesos_oficinadeenvios'


class CtlProcesosTdavirtual(models.Model):
    idu_transaccion = models.BigAutoField(primary_key=True)
    idu_proceso = models.ForeignKey(CatProcesosTdavirtual, models.DO_NOTHING, db_column='idu_proceso')
    idu_funcion = models.ForeignKey(CatFuncionesTdavirtual, models.DO_NOTHING, db_column='idu_funcion')
    num_ordenproceso = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_procesos_tdavirtual'


class CtlProcesosTiempoAire(models.Model):
    idu_proceso = models.AutoField(primary_key=True)
    num_cliente = models.IntegerField()
    num_empleado = models.IntegerField()
    desc_email = models.CharField(max_length=100)
    num_telefono = models.CharField(max_length=20)
    num_proveedor = models.SmallIntegerField()
    num_monto = models.SmallIntegerField()
    fec_proceso = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_procesos_tiempo_aire'


class CtlPromoMabe(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    factura = models.IntegerField()
    mensaje = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'ctl_promo_mabe'


class CtlPromocionesArgentina(models.Model):
    num_area = models.SmallIntegerField(primary_key=True)
    num_codigo = models.IntegerField()
    num_codigooferta = models.IntegerField()
    imp_preciopromocion = models.IntegerField()
    fec_inicialpromocion = models.DateTimeField()
    fec_finalpromocion = models.DateTimeField()
    opc_agotarexistencia = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ctl_promociones_argentina'
        unique_together = (('num_area', 'num_codigo', 'imp_preciopromocion', 'fec_inicialpromocion', 'fec_finalpromocion', 'opc_agotarexistencia'),)


class CtlPromocioneswebsphere(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    precio_o_dscto = models.IntegerField(blank=True, null=True)
    fechainicia = models.DateField(blank=True, null=True)
    fechafinal = models.DateField(blank=True, null=True)
    flagagotarexistencia = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_promocioneswebsphere'


class CtlRechazoscredito(models.Model):
    fol_orden = models.BigIntegerField(primary_key=True)
    num_area = models.IntegerField()
    idu_causa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_rechazoscredito'
        unique_together = (('fol_orden', 'num_area', 'idu_causa'),)


class CtlRedimirdineroelectronico(models.Model):
    folioorden = models.BigIntegerField(blank=True, null=True)
    gastoderopa = models.IntegerField(blank=True, null=True)
    gastodemuebles = models.IntegerField(blank=True, null=True)
    flagpagoinicial = models.SmallIntegerField(blank=True, null=True)
    flaggeneraventa = models.SmallIntegerField(blank=True, null=True)
    fechaorden = models.DateField(blank=True, null=True)
    saldodealafecha = models.IntegerField()
    cliente = models.IntegerField()
    opc_segenerodineroelectronico = models.IntegerField()
    opc_correodineroelectronico = models.IntegerField()
    imp_generoderopa = models.IntegerField()
    imp_generodemuebles = models.IntegerField()
    fec_generodineroelectronico = models.DateTimeField()
    fec_enviocorreodineroelectronico = models.DateTimeField()
    opc_seprocesoordenpendientepago = models.IntegerField(blank=True, null=True)
    opc_esnuevomonederoelectronico = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_redimirdineroelectronico'


class CtlRedimirdineroelectronicohistorial(models.Model):
    folioorden = models.BigIntegerField(blank=True, null=True)
    gastoderopa = models.IntegerField(blank=True, null=True)
    gastodemuebles = models.IntegerField(blank=True, null=True)
    flagpagoinicial = models.SmallIntegerField(blank=True, null=True)
    flaggeneraventa = models.SmallIntegerField(blank=True, null=True)
    fechaorden = models.DateField(blank=True, null=True)
    saldodealafecha = models.IntegerField()
    cliente = models.IntegerField()
    opc_segenerodineroelectronico = models.IntegerField()
    opc_correodineroelectronico = models.IntegerField()
    imp_generoderopa = models.IntegerField()
    imp_generodemuebles = models.IntegerField()
    fec_generodineroelectronico = models.DateTimeField()
    fec_enviocorreodineroelectronico = models.DateTimeField()
    opc_seprocesoordenpendientepago = models.IntegerField(blank=True, null=True)
    opc_esnuevomonederoelectronico = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_redimirdineroelectronicohistorial'


class CtlRedimirdineroelectronicopbmasiva(models.Model):
    folioorden = models.BigIntegerField(blank=True, null=True)
    gastoderopa = models.IntegerField(blank=True, null=True)
    gastodemuebles = models.IntegerField(blank=True, null=True)
    flagpagoinicial = models.SmallIntegerField(blank=True, null=True)
    flaggeneraventa = models.SmallIntegerField(blank=True, null=True)
    fechaorden = models.DateField(blank=True, null=True)
    saldodealafecha = models.IntegerField(blank=True, null=True)
    cliente = models.IntegerField(blank=True, null=True)
    opc_segenerodineroelectronico = models.IntegerField(blank=True, null=True)
    opc_correodineroelectronico = models.IntegerField(blank=True, null=True)
    imp_generoderopa = models.IntegerField(blank=True, null=True)
    imp_generodemuebles = models.IntegerField(blank=True, null=True)
    fec_generodineroelectronico = models.DateTimeField(blank=True, null=True)
    fec_enviocorreodineroelectronico = models.DateTimeField(blank=True, null=True)
    opc_seprocesoordenpendientepago = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_redimirdineroelectronicopbmasiva'


class CtlReembolsoitemmarketplace(models.Model):
    idu_rembolsoitem = models.BigAutoField(primary_key=True)
    idu_detallepedidomk = models.ForeignKey(CtlDetallepedidosmarketplace, models.DO_NOTHING, db_column='idu_detallepedidomk')
    num_monto = models.DecimalField(max_digits=10, decimal_places=2)
    fec_creacion = models.DateTimeField()
    idu_solicitud = models.CharField(max_length=-1)
    num_articulo = models.IntegerField(blank=True, null=True)
    clv_razoncodigo = models.CharField(max_length=3)
    des_status = models.CharField(max_length=50)
    fec_transaccion = models.DateTimeField()
    num_transaccion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ctl_reembolsoitemmarketplace'


class CtlRegistroCliente(models.Model):
    idu_cliente = models.AutoField()
    nom_cliente = models.CharField(max_length=200)
    desc_email = models.CharField(max_length=200)
    num_tel = models.CharField(max_length=20)
    num_cel = models.CharField(max_length=20)
    nom_estado = models.CharField(max_length=100)
    nom_ciudad = models.CharField(max_length=100)
    fec_registro = models.DateTimeField()
    fec_enviado = models.DateTimeField()
    num_status_envio = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_registro_cliente'


class CtlRegistroguiasmarketplace(models.Model):
    num_guia = models.CharField(primary_key=True, max_length=-1)
    fec_creacion = models.DateTimeField()
    tipo_guia = models.IntegerField()
    nom_carrier = models.CharField(max_length=-1)
    nom_cliente = models.CharField(max_length=-1)
    dir_cliente = models.CharField(max_length=-1)
    ciudad_cliente = models.CharField(max_length=-1)
    est_cliente = models.CharField(max_length=-1)
    cp_cliente = models.CharField(max_length=-1)
    email_cliente = models.CharField(max_length=-1)
    nom_seller = models.CharField(max_length=-1)
    dir_seller = models.CharField(max_length=-1)
    ciudad_seller = models.CharField(max_length=-1)
    est_seller = models.CharField(max_length=-1)
    cp_seller = models.CharField(max_length=-1)
    email_seller = models.CharField(max_length=-1)
    pickup_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_registroguiasmarketplace'


class CtlRegistromarket(models.Model):
    idu_registro = models.BigAutoField()
    des_registro = models.CharField(primary_key=True, max_length=-1)

    class Meta:
        managed = False
        db_table = 'ctl_registromarket'


class CtlRegistropreferencias(models.Model):
    email = models.CharField(unique=True, max_length=50)
    opc_recibirpromocion = models.SmallIntegerField()
    opc_recibirmensaje = models.SmallIntegerField()
    opc_preferenciascliente = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_registropreferencias'


class CtlReglascodificacionUrl(models.Model):
    idu_reglasurl = models.TextField(primary_key=True)
    nom_reglasdecoficiacion = models.TextField()

    class Meta:
        managed = False
        db_table = 'ctl_reglascodificacion_url'


class CtlRelacionMacrocategorias(models.Model):
    idu_macrocategoria = models.ForeignKey(CatMacrocategorias, models.DO_NOTHING, db_column='idu_macrocategoria')
    numareaweb = models.OneToOneField(CatAreasweb, models.DO_NOTHING, db_column='numareaweb')

    class Meta:
        managed = False
        db_table = 'ctl_relacion_macrocategorias'
        unique_together = (('idu_macrocategoria', 'numareaweb'),)


class CtlRelacionatributosecommercecoppel(models.Model):
    idu_atributoecommerce = models.BigIntegerField(primary_key=True)
    num_area = models.SmallIntegerField()
    num_depto = models.SmallIntegerField()
    num_caracteristica = models.IntegerField()
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    nom_actualiza = models.CharField(max_length=254)
    opc_activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ctl_relacionatributosecommercecoppel'
        unique_together = (('idu_atributoecommerce', 'num_caracteristica'),)


class CtlRelacionatributosecommercemarketplace(models.Model):
    idu_atributoecommerce = models.BigIntegerField(primary_key=True)
    idu_atributomarketplace = models.BigIntegerField()
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    nom_actualiza = models.CharField(max_length=254)
    opc_activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ctl_relacionatributosecommercemarketplace'
        unique_together = (('idu_atributoecommerce', 'idu_atributomarketplace'),)


class CtlRelacioncategoriasmarketplacecoppel(models.Model):
    idu_numareaweb = models.SmallIntegerField()
    idu_categoriamarketplace = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_relacioncategoriasmarketplacecoppel'


class CtlRelacionestatuscodigos(models.Model):
    idu_relacionestatuscodigo = models.AutoField(primary_key=True)
    idu_estatuscommerce = models.ForeignKey(CatEstatuscodigoscommerce, models.DO_NOTHING, db_column='idu_estatuscommerce')
    idu_estatuscoppel = models.ForeignKey(CatEstatuscodigoscoppel, models.DO_NOTHING, db_column='idu_estatuscoppel')

    class Meta:
        managed = False
        db_table = 'ctl_relacionestatuscodigos'


class CtlRelacionestatuscodigosmarketplace(models.Model):
    idu_relacionestatuscodigomarketplace = models.AutoField(primary_key=True)
    idu_estatusmarketplace = models.ForeignKey(CatEstatuscodigosmarketplace, models.DO_NOTHING, db_column='idu_estatusmarketplace')
    idu_estatuscoppel = models.ForeignKey(CatEstatuscodigoscoppel, models.DO_NOTHING, db_column='idu_estatuscoppel')
    idu_estatuscommerce = models.ForeignKey(CatEstatuscodigoscommerce, models.DO_NOTHING, db_column='idu_estatuscommerce')

    class Meta:
        managed = False
        db_table = 'ctl_relacionestatuscodigosmarketplace'


class CtlRelacionestatuspedido(models.Model):
    idu_relacionestatuspedido = models.AutoField(primary_key=True)
    idu_estatuspedidocommerce = models.ForeignKey(CatEstatuspedidocommerce, models.DO_NOTHING, db_column='idu_estatuspedidocommerce')
    idu_estatuspedidocoppel = models.ForeignKey(CatEstatuspedidocoppel, models.DO_NOTHING, db_column='idu_estatuspedidocoppel')

    class Meta:
        managed = False
        db_table = 'ctl_relacionestatuspedido'


class CtlRelacionofertadescuentosmarketplace(models.Model):
    idu_oferta = models.BigIntegerField()
    num_cantidad = models.SmallIntegerField()
    imp_precio = models.IntegerField()
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    opc_estatus = models.CharField(max_length=10)
    nom_actualiza = models.CharField(max_length=254)
    opc_procesado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_relacionofertadescuentosmarketplace'


class CtlRelacionofertapreciomarketplace(models.Model):
    idu_oferta = models.BigIntegerField()
    num_cantidad = models.SmallIntegerField()
    imp_precio = models.IntegerField()
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    opc_estatus = models.CharField(max_length=10)
    nom_actualiza = models.CharField(max_length=254)
    opc_procesado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_relacionofertapreciomarketplace'


class CtlRelacionordenfacturasmp(models.Model):
    num_folio = models.SmallIntegerField()
    num_factura = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_relacionordenfacturasmp'


class CtlRelacionproductoatributosmarketplace(models.Model):
    idu_producto = models.OneToOneField(CatProductosmarketplace, models.DO_NOTHING, db_column='idu_producto', primary_key=True)
    idu_atributo = models.BigIntegerField()
    des_valoratributo = models.CharField(max_length=2048)
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    opc_estatus = models.CharField(max_length=10)
    nom_actualiza = models.CharField(max_length=254)
    opc_procesado = models.SmallIntegerField()
    idu_valoratributo = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_relacionproductoatributosmarketplace'
        unique_together = (('idu_producto', 'idu_atributo', 'idu_valoratributo'),)


class CtlRelacionproductoimagenmarketplace(models.Model):
    num_codigomarketplace = models.BigIntegerField(primary_key=True)
    des_rutaimagen = models.CharField(max_length=254)
    nom_imagenes = models.CharField(max_length=1024)
    num_imagenes = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_relacionproductoimagenmarketplace'
        unique_together = (('num_codigomarketplace', 'des_rutaimagen'),)


class CtlRelacionproductoproveedormarketplace(models.Model):
    idu_producto = models.OneToOneField(CatProductosmarketplace, models.DO_NOTHING, db_column='idu_producto', primary_key=True)
    num_codigoproveedor = models.IntegerField()
    idu_skuproveedor = models.CharField(max_length=254)
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    opc_estatus = models.CharField(max_length=10)
    nom_actualiza = models.CharField(max_length=254)
    opc_procesado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_relacionproductoproveedormarketplace'
        unique_together = (('idu_producto', 'num_codigoproveedor'),)


class CtlRelacionpromocionesmarketplace(models.Model):
    idu_tienda = models.BigIntegerField()
    idu_triggerpromocion = models.CharField(max_length=254)
    idu_recompensapromocion = models.CharField(max_length=254)
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    opc_estatus = models.CharField(max_length=10)
    nom_actualiza = models.CharField(max_length=254)
    opc_procesado = models.SmallIntegerField()
    idu_ofertamirakl = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_relacionpromocionesmarketplace'


class CtlRelacionpromocionesmarketplaceDetalle(models.Model):
    idu_promocion = models.BigIntegerField()
    opc_activo = models.BooleanField()
    opc_cotizacion = models.BooleanField()
    num_codigocategoria = models.CharField(max_length=254)
    nom_canal = models.CharField(max_length=50)
    opc_codigoisomoneda = models.CharField(max_length=50)
    des_descripcion = models.CharField(max_length=2048)
    num_descuento = models.IntegerField()
    opc_recompensa = models.BooleanField()
    opc_trigger = models.BooleanField()
    num_alertacantidadminima = models.SmallIntegerField()
    imp_preciominimoenvio = models.IntegerField()
    imp_preciominimoenvioadicional = models.IntegerField()
    des_zonaenviominimo = models.CharField(max_length=254)
    des_tipoenviominimo = models.CharField(max_length=254)
    imp_precio = models.IntegerField()
    nom_partnumer = models.CharField(max_length=254)
    num_cantidad = models.SmallIntegerField()
    imp_preciototal = models.IntegerField()
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    opc_estatus = models.CharField(max_length=10)
    nom_actualiza = models.CharField(max_length=254)
    opc_procesado = models.SmallIntegerField()
    idu_oferta = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_relacionpromocionesmarketplace_detalle'


class CtlRelacionpromocionespreciosmarketplace(models.Model):
    idu_promocion = models.BigIntegerField()
    opc_codigocanal = models.CharField(max_length=50)
    fec_findescuento = models.DateTimeField()
    fec_iniciodescuento = models.DateTimeField()
    imp_precio = models.IntegerField()
    imp_preciodescuentounitario = models.IntegerField()
    imp_preciounitariooriginal = models.IntegerField()
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    opc_estatus = models.CharField(max_length=10)
    nom_actualiza = models.CharField(max_length=254)
    opc_procesado = models.SmallIntegerField()
    idu_oferta = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_relacionpromocionespreciosmarketplace'


class CtlRelacionpromocionesvolumenpreciosmarketplace(models.Model):
    idu_volumenprecio = models.BigAutoField(primary_key=True)
    idu_promocion = models.BigIntegerField()
    imp_precio = models.IntegerField()
    num_cantidadmaxima = models.SmallIntegerField()
    imp_preciodescuentounitario = models.IntegerField()
    imp_preciounitariooriginal = models.IntegerField()
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    opc_estatus = models.CharField(max_length=10)
    nom_actualiza = models.CharField(max_length=254)
    opc_procesado = models.SmallIntegerField()
    idu_oferta = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_relacionpromocionesvolumenpreciosmarketplace'


class CtlRelacionvaloratributomarketplacecoppel(models.Model):
    idu_valoratributo = models.BigIntegerField(primary_key=True)
    num_area = models.SmallIntegerField()
    num_depto = models.SmallIntegerField()
    num_detallecaracteristica = models.IntegerField()
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    nom_actualiza = models.CharField(max_length=254)
    opc_activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ctl_relacionvaloratributomarketplacecoppel'
        unique_together = (('idu_valoratributo', 'num_detallecaracteristica'),)


class CtlRelacionvaloresatributosmarketplace(models.Model):
    idu_listavalores = models.ForeignKey(CatValoresatributosmarketplace, models.DO_NOTHING, db_column='idu_listavalores')
    nom_listavalor = models.CharField(max_length=254)
    idu_valoratributo = models.BigAutoField(primary_key=True)
    des_valoratributoen = models.CharField(max_length=254)
    des_valoratributomx = models.CharField(max_length=254)
    opc_activo = models.BooleanField()
    fec_creacion = models.DateTimeField()
    fec_actualizacion = models.DateTimeField()
    opc_estatus = models.CharField(max_length=10)
    nom_actualiza = models.CharField(max_length=254)
    opc_procesado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_relacionvaloresatributosmarketplace'
        unique_together = (('idu_valoratributo', 'idu_listavalores'),)


class CtlRespuestasComentarios(models.Model):
    idrespuesta = models.AutoField()
    respuesta = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    idcomentario = models.IntegerField(blank=True, null=True)
    publicar = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_respuestas_comentarios'


class CtlRespuestasclientesconvenios(models.Model):
    idu_cliente = models.IntegerField()
    idu_pregunta = models.IntegerField()
    idu_respuesta = models.CharField(max_length=-1, blank=True, null=True)
    puntaje = models.FloatField(blank=True, null=True)
    idu_convenio = models.IntegerField(blank=True, null=True)
    nom_pregunta = models.CharField(max_length=-1, blank=True, null=True)
    nom_respuesta = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_respuestasclientesconvenios'


class CtlResurtidooe(models.Model):
    num_empleado = models.IntegerField()
    idu_pedido = models.IntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.SmallIntegerField()
    num_cantidad = models.SmallIntegerField()
    id_serial = models.IntegerField()
    fec_registro = models.DateTimeField(blank=True, null=True)
    fec_movimiento = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_resurtidooe'


class CtlRolesdeusuario(models.Model):
    rolesdeusuario_id = models.AutoField(primary_key=True)
    numero_empleado = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250, blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    field1 = models.CharField(max_length=250, blank=True, null=True)
    creacion = models.DateTimeField()
    modicicacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_rolesdeusuario'


class CtlRolesdeusuarioProyecto(models.Model):
    ctl_rolesdeusuario_proyecto_id = models.AutoField(primary_key=True)
    rolesdeusuario = models.ForeignKey(CtlRolesdeusuario, models.DO_NOTHING)
    proyecto_vista = models.ForeignKey('CtlRolesdeusuarioProyectoVentana', models.DO_NOTHING)
    proyecto = models.CharField(max_length=50)
    lectura = models.BooleanField()
    escritura = models.BooleanField()
    lectura_escritura = models.BooleanField()
    field1 = models.CharField(max_length=250, blank=True, null=True)
    creacion = models.DateTimeField(blank=True, null=True)
    modicicacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_rolesdeusuario_proyecto'


class CtlRolesdeusuarioProyectoVentana(models.Model):
    proyecto_vista_id = models.AutoField(primary_key=True)
    proyecto = models.CharField(max_length=50)
    vista = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_rolesdeusuario_proyecto_ventana'
# Unable to inspect table 'ctl_schedule_feedmarketplace'
# The error was: permission denied for table ctl_schedule_feedmarketplace


class CtlServicio(models.Model):
    idu_servicio = models.AutoField()
    desc_servicio = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_servicio'


class CtlServidoresSolr(models.Model):
    keyx = models.AutoField()
    ip_servidor = models.CharField(max_length=-1, blank=True, null=True)
    nom_tipo_red = models.CharField(max_length=-1, blank=True, null=True)
    peso = models.IntegerField(blank=True, null=True)
    flag_servidorprimario = models.BooleanField(blank=True, null=True)
    flag_activo = models.BooleanField(blank=True, null=True)
    flag_indexar = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_servidores_solr'


class CtlSkusexcluidos(models.Model):
    num_id = models.AutoField(blank=True, null=True)
    num_area = models.SmallIntegerField(primary_key=True)
    num_sku = models.IntegerField()
    nom_articuloweb = models.TextField()
    fec_inicioexclusion = models.DateField()
    fec_finexclusion = models.DateField()
    nom_tipoexclusion = models.TextField()
    nom_departamento = models.TextField()
    nom_clase = models.TextField()
    nom_familia = models.TextField()
    num_departamento = models.SmallIntegerField()
    num_clase = models.SmallIntegerField()
    num_familia = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_skusexcluidos'
        unique_together = (('num_area', 'num_sku', 'nom_tipoexclusion'),)


class CtlSkusexcluidosMkp(models.Model):
    num_id = models.AutoField(blank=True, null=True)
    num_sku = models.TextField(primary_key=True)
    nom_descripcion = models.TextField()
    nom_categoria_mkp = models.TextField()
    fec_inicioexclusion = models.DateField()
    fec_finexclusion = models.DateField()

    class Meta:
        managed = False
        db_table = 'ctl_skusexcluidos_mkp'


class CtlSmsEnviadosProveedor(models.Model):
    fecha = models.DateField(blank=True, null=True)
    sms_enviados = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_sms_enviados_proveedor'


class CtlSolicitudescorreo(models.Model):
    num_solicitud = models.IntegerField(blank=True, null=True)
    tipo_correo = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=50)
    fecha = models.DateTimeField(blank=True, null=True)
    num_tienda = models.IntegerField()
    id = models.AutoField()

    class Meta:
        managed = False
        db_table = 'ctl_solicitudescorreo'
        unique_together = (('id', 'num_solicitud', 'num_tienda', 'fecha'),)


class CtlStoresbodegas(models.Model):
    idu_store = models.IntegerField(primary_key=True)
    num_ciudad = models.IntegerField()
    num_bodega = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_storesbodegas'
        unique_together = (('idu_store', 'num_ciudad', 'num_bodega'),)


class CtlStoresbodegasEtl(models.Model):
    num_ciudad = models.IntegerField(blank=True, null=True)
    idu_store = models.IntegerField(blank=True, null=True)
    num_bodega = models.IntegerField(blank=True, null=True)
    opc_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_storesbodegas_etl'


class CtlSubcategoriasCatalogo(models.Model):
    id = models.AutoField()
    num_padre = models.IntegerField(blank=True, null=True)
    num_subcategorias = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_subcategorias_catalogo'


class CtlSubcomponentes(models.Model):
    id_subcomponente = models.IntegerField(primary_key=True)
    id_tipo = models.IntegerField()
    nom_contenido = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'ctl_subcomponentes'
        unique_together = (('id_subcomponente', 'id_tipo'),)


class CtlSurtidoGuia(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    cantidad = models.SmallIntegerField(blank=True, null=True)
    talla = models.CharField(max_length=-1, blank=True, null=True)
    fechaventa = models.DateField(blank=True, null=True)
    numbodega = models.SmallIntegerField(blank=True, null=True)
    marca = models.CharField(max_length=100, blank=True, null=True)
    serial = models.AutoField()

    class Meta:
        managed = False
        db_table = 'ctl_surtido_guia'


class CtlSurtidoRopa(models.Model):
    numarea = models.SmallIntegerField()
    numcodigo = models.IntegerField()
    cantidad = models.SmallIntegerField()
    talla = models.SmallIntegerField()
    folio = models.IntegerField()
    fechaventa = models.DateField(blank=True, null=True)
    numbodega = models.SmallIntegerField()
    tipoventa = models.CharField(max_length=1)
    flagsurtido = models.CharField(max_length=1)
    fechaactualiza = models.DateTimeField()
    num_empleado = models.IntegerField()
    num_folioorden = models.BigIntegerField()
    flag_ordensingle = models.IntegerField(blank=True, null=True)
    fec_nota = models.DateTimeField()
    fec_surtiroficina = models.DateField()
    fec_notatienda = models.DateField()
    fec_concentrado = models.DateTimeField(blank=True, null=True)
    fec_procesado = models.DateTimeField(blank=True, null=True)
    cedis_traspaso = models.SmallIntegerField()
    id_serial = models.IntegerField(blank=True, null=True)
    id_carrier = models.IntegerField(blank=True, null=True)
    carrier = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_surtido_ropa'


class CtlSurtidoRopaAnt(models.Model):
    numarea = models.SmallIntegerField()
    numcodigo = models.IntegerField()
    cantidad = models.SmallIntegerField()
    talla = models.SmallIntegerField()
    folio = models.IntegerField()
    fechaventa = models.DateField(blank=True, null=True)
    numbodega = models.SmallIntegerField()
    tipoventa = models.CharField(max_length=1)
    flagsurtido = models.CharField(max_length=1)
    fechaactualiza = models.DateTimeField()
    num_empleado = models.IntegerField()
    num_folioorden = models.BigIntegerField()
    flag_ordensingle = models.IntegerField(blank=True, null=True)
    fec_nota = models.DateTimeField()
    fec_surtiroficina = models.DateField()
    fec_notatienda = models.DateField()
    fec_concentrado = models.DateTimeField(blank=True, null=True)
    fec_procesado = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_surtido_ropa_ant'


class CtlSurtidoRopaCodigosservicio(models.Model):
    numarea = models.SmallIntegerField()
    numcodigo = models.IntegerField()
    cantidad = models.SmallIntegerField()
    talla = models.SmallIntegerField()
    folio = models.IntegerField()
    fechaventa = models.DateField(blank=True, null=True)
    numbodega = models.SmallIntegerField()
    tipoventa = models.CharField(max_length=1)
    fechaactualiza = models.DateTimeField()
    num_empleado = models.IntegerField()
    num_folioorden = models.BigIntegerField()
    flag_ordensingle = models.IntegerField(blank=True, null=True)
    fec_nota = models.DateTimeField()
    fec_surtiroficina = models.DateField()
    fec_notatienda = models.DateField()
    fec_concentrado = models.DateTimeField(blank=True, null=True)
    fec_procesado = models.DateTimeField(blank=True, null=True)
    flag_devolucion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_surtido_ropa_codigosservicio'


class CtlSurtidoRopaHist(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    cantidad = models.SmallIntegerField(blank=True, null=True)
    talla = models.SmallIntegerField(blank=True, null=True)
    folio = models.IntegerField(blank=True, null=True)
    fechaventa = models.DateField(blank=True, null=True)
    numbodega = models.SmallIntegerField(blank=True, null=True)
    tipoventa = models.CharField(max_length=1, blank=True, null=True)
    flagsurtido = models.CharField(max_length=1, blank=True, null=True)
    fechaactualiza = models.DateTimeField(blank=True, null=True)
    num_empleado = models.IntegerField(blank=True, null=True)
    num_folioorden = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_surtido_ropa_hist'


class CtlSurtidoRopaTemp(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    cantidad = models.SmallIntegerField(blank=True, null=True)
    talla = models.SmallIntegerField(blank=True, null=True)
    folio = models.IntegerField(blank=True, null=True)
    fechaventa = models.DateField(blank=True, null=True)
    numbodega = models.SmallIntegerField(blank=True, null=True)
    tipoventa = models.CharField(max_length=1, blank=True, null=True)
    flagsurtido = models.CharField(max_length=1, blank=True, null=True)
    fechaactualiza = models.DateTimeField(blank=True, null=True)
    num_empleado = models.IntegerField(blank=True, null=True)
    num_folioorden = models.BigIntegerField(blank=True, null=True)
    flag_ordensingle = models.IntegerField(blank=True, null=True)
    fec_nota = models.DateTimeField(blank=True, null=True)
    fec_surtiroficina = models.DateField(blank=True, null=True)
    fec_notatienda = models.DateField(blank=True, null=True)
    fec_concentrado = models.DateTimeField(blank=True, null=True)
    fec_procesado = models.DateTimeField(blank=True, null=True)
    cedis_traspaso = models.SmallIntegerField(blank=True, null=True)
    id_serial = models.IntegerField(blank=True, null=True)
    id_carrier = models.IntegerField(blank=True, null=True)
    carrier = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_surtido_ropa_temp'


class CtlTdacartera(models.Model):
    id = models.AutoField()
    stipomensaje = models.SmallIntegerField()
    ivalorseguridad = models.IntegerField()
    itipoopcion = models.IntegerField()
    cipcartera = models.CharField(max_length=20)
    cclave = models.CharField(max_length=1)
    ctipomovimiento = models.CharField(max_length=1)
    icliente = models.IntegerField()
    ifolio = models.IntegerField()
    iimporte = models.IntegerField()
    ienganche = models.IntegerField()
    iinteres = models.IntegerField()
    tfechadia = models.IntegerField()
    tfechames = models.IntegerField()
    tfechaanio = models.IntegerField()
    idevolucionfactura = models.IntegerField()
    ifactura = models.IntegerField()
    itienda = models.IntegerField()
    iciudadtiendamov = models.IntegerField()
    iplazo = models.IntegerField()
    iabono = models.IntegerField()
    cdescripcionarticulo = models.CharField(max_length=10)
    inumeroarticulos = models.IntegerField()
    idiapago = models.IntegerField()
    isaldocuenta = models.IntegerField()
    iplazoconvenio = models.IntegerField()
    iefectuo = models.IntegerField()
    cclaveajuste = models.CharField(max_length=2)
    tfechasaldacondia = models.IntegerField()
    tfechasaldaconmes = models.IntegerField()
    tfechasaldaconanio = models.IntegerField()
    ivencidoinicial = models.IntegerField()
    isaldoinicial = models.IntegerField()
    ctipoconvenio = models.CharField(max_length=1)
    csubtipoconvenio = models.CharField(max_length=1)
    iimportesaldacon = models.IntegerField()
    tfechanacimientodia = models.IntegerField()
    tfechanacimientomes = models.IntegerField()
    tfechanacimientoanio = models.IntegerField()
    tfechavencimientodia = models.IntegerField()
    tfechavencimientomes = models.IntegerField()
    tfechavencimientoanio = models.IntegerField()
    cflagseguroconyugal = models.CharField(max_length=1)
    icantidadseguros = models.IntegerField()
    cmovtoseguro = models.CharField(max_length=1)
    icaja = models.IntegerField()
    icajaoriginal = models.IntegerField()
    carea = models.CharField(max_length=1)
    ctipograbado = models.CharField(max_length=1)
    ipuerto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_tdacartera'


class CtlTempduplicidad(models.Model):
    num_orden = models.IntegerField(blank=True, null=True)
    num_guia = models.CharField(max_length=-1, blank=True, null=True)
    nom_cliente = models.CharField(max_length=-1, blank=True, null=True)
    fecha_entrega = models.CharField(max_length=-1, blank=True, null=True)
    paquetera = models.CharField(max_length=-1, blank=True, null=True)
    fecha_procesamiento = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_tempduplicidad'


class CtlTemplates(models.Model):
    id_template = models.IntegerField(primary_key=True)
    id_componente = models.IntegerField()
    nom_ruta = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ctl_templates'


class CtlTiempoairebloqueo(models.Model):
    idu_bloqueo = models.AutoField(primary_key=True)
    num_cliente = models.IntegerField()
    num_telefono = models.CharField(max_length=20)
    nom_email = models.CharField(max_length=100)
    des_observaciones = models.CharField(max_length=255)
    fec_alta = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_tiempoairebloqueo'


class CtlTiendaListaRel(models.Model):
    lista = models.CharField(max_length=2, blank=True, null=True)
    idu_ciudad = models.SmallIntegerField(blank=True, null=True)
    tipo_ciudad = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_tienda_lista_rel'


class CtlTiendasPilotoEspejo(models.Model):
    numespejo = models.IntegerField(primary_key=True)
    numpiloto = models.IntegerField()
    tipotiendaespejo = models.CharField(max_length=-1, blank=True, null=True)
    tipotiendapiloto = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_tiendas_piloto_espejo'
        unique_together = (('numespejo', 'numpiloto'),)


class CtlTiendasregioncelulares(models.Model):
    num_tienda = models.SmallIntegerField(primary_key=True)
    num_bodega = models.SmallIntegerField()
    num_ciudadpertenece = models.SmallIntegerField()
    num_ciudad = models.SmallIntegerField()
    num_ciudaddistribucion = models.SmallIntegerField()
    des_ciudadcelular = models.CharField(max_length=4)
    num_regioncelular = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ctl_tiendasregioncelulares'


class CtlTipoBanerCoppelCom(models.Model):
    idu_tipo_banner = models.AutoField(primary_key=True)
    desc_tipo_banner = models.CharField(max_length=90)

    class Meta:
        managed = False
        db_table = 'ctl_tipo_baner_coppel_com'


class CtlTokensession(models.Model):
    id_session = models.CharField(max_length=60)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_tokensession'


class CtlTokentrackingomnicanal(models.Model):
    token_omnicanal = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_tokentrackingomnicanal'


class CtlTotalSurtido(models.Model):
    tienda = models.SmallIntegerField(blank=True, null=True)
    cantidad = models.SmallIntegerField(blank=True, null=True)
    total_pesos = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    fechaventa = models.DateTimeField(blank=True, null=True)
    numbodega = models.SmallIntegerField(blank=True, null=True)
    area = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_total_surtido'


class CtlTransferenciasoe(models.Model):
    tipo_transferencia = models.SmallIntegerField()
    num_lote = models.SmallIntegerField()
    num_cantidad_lote = models.SmallIntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.SmallIntegerField()
    num_precio = models.IntegerField()
    num_cantidad = models.SmallIntegerField()
    num_caja = models.SmallIntegerField()
    num_bodega = models.SmallIntegerField()
    num_jaba = models.IntegerField()
    fec_creacion = models.DateTimeField(blank=True, null=True)
    fec_modificacion = models.DateTimeField(blank=True, null=True)
    fec_mov_tranferencia = models.DateTimeField(blank=True, null=True)
    id_oficinaenvios = models.BigIntegerField()
    flag_transferencia = models.IntegerField()
    num_area = models.SmallIntegerField(blank=True, null=True)
    num_empleado = models.IntegerField(blank=True, null=True)
    num_guia = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_transferenciasoe'


class CtlTsearcharticulo(models.Model):
    numarea = models.OneToOneField(CatArticulos, models.DO_NOTHING, db_column='numarea', primary_key=True)
    numcodigo = models.IntegerField()
    descarticulo = models.TextField(blank=True, null=True)  # This field type is a guess.
    nomarticulo = models.TextField(blank=True, null=True)  # This field type is a guess.
    nomareaweb = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ctl_tsearcharticulo'
        unique_together = (('numarea', 'numcodigo'),)


class CtlUnidadesropaVendidas(models.Model):
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.IntegerField(blank=True, null=True)
    num_bodega = models.SmallIntegerField(blank=True, null=True)
    num_uni_iniciales = models.SmallIntegerField(blank=True, null=True)
    num_uni_vendidas = models.SmallIntegerField(blank=True, null=True)
    num_uni_actuales = models.SmallIntegerField(blank=True, null=True)
    fec_respaldo = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_unidadesropa_vendidas'


class CtlUrlamigablesmodificadas(models.Model):
    idu_registro = models.AutoField()
    nom_menuweb = models.CharField(max_length=-1)
    nom_urlamigable = models.TextField(blank=True, null=True)
    nom_urldinamica = models.TextField(blank=True, null=True)
    num_tipomovimiento = models.SmallIntegerField(blank=True, null=True)
    fec_movimiento = models.DateField(blank=True, null=True)
    num_procesada = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_urlamigablesmodificadas'


class CtlUrlestaticas(models.Model):
    idu_registro = models.AutoField()
    nom_categoria = models.CharField(max_length=200)
    nom_seccion = models.CharField(max_length=200)
    nom_metatitle = models.CharField(max_length=200)
    nom_metadescripcion = models.CharField(max_length=200)
    nom_urlamigable = models.TextField()
    nom_urldinamica = models.TextField()
    keywords = models.CharField(max_length=200)
    fec_movimiento = models.DateField()

    class Meta:
        managed = False
        db_table = 'ctl_urlestaticas'


class CtlUsuariosTokens(models.Model):
    email = models.CharField(primary_key=True, max_length=255)
    token = models.CharField(max_length=32)
    cod_sesion = models.CharField(max_length=50)
    logueado = models.CharField(max_length=1)
    es_cliente = models.CharField(max_length=1)
    fechacreacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_usuarios_tokens'
        unique_together = (('email', 'token'),)


class CtlUtmreferidos(models.Model):
    num_orden = models.BigIntegerField(primary_key=True)
    utm_campania = models.CharField(max_length=-1, blank=True, null=True)
    utm_medio = models.CharField(max_length=-1, blank=True, null=True)
    utm_origen = models.CharField(max_length=-1, blank=True, null=True)
    utm_contenido = models.CharField(max_length=-1, blank=True, null=True)
    fec_movimiento = models.DateTimeField()
    desc_canalventa = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctl_utmreferidos'


class CtlValidacionTokens(models.Model):
    idu_token = models.BigAutoField(primary_key=True)
    val_token = models.CharField(max_length=-1, blank=True, null=True)
    ban_expiro = models.BooleanField()
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_validacion_tokens'


class CtlVentatiempoaire(models.Model):
    id_tiempoaire = models.BigIntegerField()
    num_codigo = models.BigIntegerField()
    num_cliente = models.BigIntegerField()
    num_empleado = models.BigIntegerField()
    num_telefono = models.BigIntegerField()
    id_carrier = models.BigIntegerField()
    num_importe = models.BigIntegerField()
    num_foliotda800 = models.BigIntegerField()
    num_foliorecarga = models.BigIntegerField()
    num_estatustda800 = models.SmallIntegerField()
    num_estatusclinea = models.SmallIntegerField()
    num_estatusrecarga = models.SmallIntegerField()
    num_respuestaproveedor = models.CharField(max_length=10)
    fec_movimiento = models.DateField()
    fec_alta = models.DateField()

    class Meta:
        managed = False
        db_table = 'ctl_ventatiempoaire'


class CtlVigenciaLigueClientesDig(models.Model):
    id_process = models.SmallIntegerField(primary_key=True)
    valid_days = models.IntegerField()
    flag_valida_vigencia = models.BooleanField()
    flag_valida_venta = models.BooleanField()
    flag_encendido = models.BooleanField()
    centro_muebles = models.CharField(max_length=-1, blank=True, null=True)
    centro_ropa = models.CharField(max_length=-1, blank=True, null=True)
    flag_ventaportiendas = models.BooleanField()
    tiendas = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ctl_vigencia_ligue_clientes_dig'


class CtlZonasrelacionado(models.Model):
    numciudad = models.IntegerField(primary_key=True)
    numcolonia = models.IntegerField()
    nomzona = models.CharField(max_length=100)
    poblacionzona = models.CharField(max_length=50)
    municipiozona = models.CharField(max_length=50)
    codigopostalzona = models.IntegerField()
    numciudadcoppel = models.IntegerField()
    numcoloniacoppel = models.IntegerField()
    nomzonacoppel = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ctl_zonasrelacionado'
        unique_together = (('numciudad', 'numcolonia'),)


class CtrlFamiliacomplementaria(models.Model):
    idu_familiacomplementaria = models.AutoField(primary_key=True)
    idu_familiapivote = models.ForeignKey('CtrlFamiliapivote', models.DO_NOTHING, db_column='idu_familiapivote')
    idu_area = models.ForeignKey(CatFamilias, models.DO_NOTHING, db_column='idu_area')
    idu_departamento = models.IntegerField()
    idu_clase = models.IntegerField()
    idu_familia = models.IntegerField()
    opc_estatus = models.SmallIntegerField()
    num_prioridad = models.SmallIntegerField()
    fec_registro = models.DateTimeField()
    fec_modifico = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctrl_familiacomplementaria'


class CtrlFamiliapivote(models.Model):
    idu_familiapivote = models.AutoField(primary_key=True)
    idu_area = models.ForeignKey(CatDepartamentos, models.DO_NOTHING, db_column='idu_area')
    idu_departamento = models.IntegerField()
    idu_clase = models.IntegerField()
    idu_familia = models.IntegerField()
    opc_norelacion = models.SmallIntegerField()
    opc_estatus = models.SmallIntegerField()
    fec_registro = models.DateTimeField()
    fec_modifico = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctrl_familiapivote'


class CtrlRelacioncaracteristicadetalle(models.Model):
    idu_relacioncaracteristicadetalle = models.AutoField(primary_key=True)
    idu_familiacomplementaria = models.ForeignKey(CtrlFamiliacomplementaria, models.DO_NOTHING, db_column='idu_familiacomplementaria')
    idu_caracteristicapivote = models.ForeignKey(CatDetallescaracteristicas, models.DO_NOTHING, db_column='idu_caracteristicapivote')
    idu_detallepivote = models.IntegerField()
    idu_caracteristicacomplementaria = models.ForeignKey(CatCaracteristicas, models.DO_NOTHING, db_column='idu_caracteristicacomplementaria')
    idu_detallecomplementaria = models.IntegerField()
    opc_estatus = models.SmallIntegerField()
    fec_registro = models.DateTimeField()
    fec_modifico = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctrl_relacioncaracteristicadetalle'


class Cultimaletra(models.Model):
    nom_letra = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cultimaletra'


class Cultimaletraasignar(models.Model):
    nom_letra = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cultimaletraasignar'


class DatosSku(models.Model):
    idu_pedido = models.IntegerField(blank=True, null=True)
    nom_email = models.CharField(max_length=-1, blank=True, null=True)
    num_clientecoppel = models.BigIntegerField(blank=True, null=True)
    num_empleadocoppel = models.IntegerField(blank=True, null=True)
    nom_cliente = models.CharField(max_length=-1, blank=True, null=True)
    nom_apepaterno = models.CharField(max_length=100, blank=True, null=True)
    nom_apematerno = models.CharField(max_length=100, blank=True, null=True)
    num_importetotal = models.IntegerField(blank=True, null=True)
    fec_orden = models.DateTimeField(blank=True, null=True)
    num_telefono = models.CharField(max_length=20, blank=True, null=True)
    opc_celular = models.BooleanField(blank=True, null=True)
    num_folio = models.BigIntegerField(blank=True, null=True)
    num_estatus = models.IntegerField(blank=True, null=True)
    num_totalarticulosmuebles = models.SmallIntegerField(blank=True, null=True)
    num_totalarticulosropa = models.SmallIntegerField(blank=True, null=True)
    num_importeropa = models.IntegerField(blank=True, null=True)
    num_importemuebles = models.IntegerField(blank=True, null=True)
    num_engancheropa = models.IntegerField(blank=True, null=True)
    des_articulo = models.CharField(max_length=12, blank=True, null=True)
    num_enganchemuebles = models.IntegerField(blank=True, null=True)
    num_folioropa = models.IntegerField(blank=True, null=True)
    num_foliomuebles = models.IntegerField(blank=True, null=True)
    fec_movimiento = models.DateTimeField(blank=True, null=True)
    num_pagorecibido = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datos_sku'


class Dfecha(models.Model):
    fechaentrega = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dfecha'


class DfechaAtiempo(models.Model):
    fun_obtener_oedialaboralsiguiente = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dfecha_atiempo'


class DfechaRetraso1Dia(models.Model):
    fun_obtener_oedialaboralsiguiente = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dfecha_retraso_1dia'


class Dfechafin(models.Model):
    dd = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dfechafin'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Drespuesta(models.Model):
    fun_sumardiashabiles = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drespuesta'


class Estados(models.Model):
    numero = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=-1, blank=True, null=True)
    inicial = models.CharField(max_length=5, blank=True, null=True)
    des_abreviacion_dos = models.CharField(max_length=2)
    flag_contingencia = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados'


class Estadospeticion(models.Model):
    numero = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=-1, blank=True, null=True)
    inicial = models.CharField(max_length=5, blank=True, null=True)
    des_abreviacion_dos = models.CharField(max_length=2, blank=True, null=True)
    flag_contingencia = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadospeticion'


class EstatusArticulo(models.Model):
    nom_estatus = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estatus_articulo'
# Unable to inspect table 'factura'
# The error was: permission denied for table factura
# Unable to inspect table 'factura_detalle'
# The error was: permission denied for table factura_detalle


class GanadoresSorteo(models.Model):
    apellido = models.CharField(max_length=-1, blank=True, null=True)
    nombre = models.CharField(max_length=-1, blank=True, null=True)
    numboleto = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=-1, blank=True, null=True)
    premio = models.CharField(max_length=-1, blank=True, null=True)
    numeracion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ganadores_sorteo'


class GndominioCat(models.Model):
    fecha = models.DateField(blank=True, null=True)
    preciomaximo = models.IntegerField(blank=True, null=True)
    preciomaximocredito = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gndominio_cat'


class HisArticulos(models.Model):
    numarea = models.SmallIntegerField()
    numdepto = models.SmallIntegerField()
    numclase = models.SmallIntegerField()
    numfamilia = models.SmallIntegerField()
    numcodigo = models.IntegerField()
    modelo = models.CharField(max_length=35)
    nummarca = models.SmallIntegerField()
    nomarticulo = models.CharField(max_length=120)
    descarticulo = models.TextField()
    fechaalta = models.DateTimeField()
    preciovntaint = models.IntegerField()
    preciovntafrontera = models.IntegerField()
    exclusivo = models.SmallIntegerField()
    publicar = models.SmallIntegerField()
    nuevo = models.SmallIntegerField()
    numestatus = models.SmallIntegerField()
    meta_keyword = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    numdisponibilidad = models.SmallIntegerField()
    comprar = models.SmallIntegerField()
    fechaactualiza = models.DateTimeField()
    nomarticuloweb = models.CharField(max_length=120)
    meta_title = models.CharField(max_length=255)
    num_garantiaenmeses = models.SmallIntegerField()
    num_seccion = models.SmallIntegerField()
    flag_manejaiva = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'his_articulos'


class HisArticuloscolorespim(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    numcodigo = models.IntegerField()
    numcolor = models.ForeignKey(CatColores, models.DO_NOTHING, db_column='numcolor')
    numtipocolor = models.ForeignKey(CatTipocolores, models.DO_NOTHING, db_column='numtipocolor')

    class Meta:
        managed = False
        db_table = 'his_articuloscolorespim'
        unique_together = (('numarea', 'numcodigo', 'numcolor', 'numtipocolor'),)


class HisArticulosconfirmados(models.Model):
    num_empleado = models.IntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.SmallIntegerField()
    num_area = models.SmallIntegerField()
    num_cantidad = models.IntegerField()
    num_preciocompra = models.IntegerField()
    num_precioetiqueta = models.IntegerField()
    num_condicion = models.IntegerField()
    fec_registro = models.DateTimeField()
    fec_confirmacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'his_articulosconfirmados'


class HisArticulosdetcaracteristicaspim(models.Model):
    numarea = models.SmallIntegerField()
    numcodigo = models.IntegerField()
    numcaracteristica = models.IntegerField()
    numdetallecaracteristica = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'his_articulosdetcaracteristicaspim'


class HisArticulospim(models.Model):
    numarea = models.SmallIntegerField()
    numcodigo = models.IntegerField()
    modelo = models.CharField(max_length=35)
    nummarca = models.SmallIntegerField()
    nomarticulo = models.CharField(max_length=120)
    descarticulo = models.TextField()
    meta_keyword = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    nomarticuloweb = models.CharField(max_length=120)
    fechaalta = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'his_articulospim'


class HisBalanceoe(models.Model):
    num_folioropa = models.IntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.IntegerField()
    num_necesidad = models.IntegerField()
    num_cedisorigen = models.IntegerField()
    num_cedisdestino = models.IntegerField()
    fec_procesado = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'his_balanceoe'


class HisBpguiasurtido(models.Model):
    numbodega = models.SmallIntegerField()
    clavemov = models.CharField(max_length=2)
    numlote = models.SmallIntegerField()
    numlector = models.SmallIntegerField()
    numsurtidor = models.SmallIntegerField()
    numtienda = models.SmallIntegerField()
    fechacreacion = models.DateField()
    numcodigo = models.IntegerField()
    numtalla = models.SmallIntegerField()
    mesetiqueta = models.SmallIntegerField()
    cantidad = models.SmallIntegerField()
    numseccion = models.SmallIntegerField()
    nomguia = models.CharField(max_length=20)
    fechaactualiza = models.DateField()
    consecutivo = models.SmallIntegerField()
    precio = models.SmallIntegerField()
    numdepto = models.SmallIntegerField()
    numclase = models.SmallIntegerField()
    numfamilia = models.SmallIntegerField()
    numcentro = models.IntegerField()
    preciomaximo = models.SmallIntegerField()
    marca = models.CharField(max_length=50)
    esimportacion = models.CharField(max_length=1)
    areacodigo = models.CharField(max_length=1)
    esdescontinuado = models.SmallIntegerField()
    numcodigodes = models.IntegerField()
    keyx = models.AutoField()
    numtipoiva = models.SmallIntegerField()
    rebajado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'his_bpguiasurtido'


class HisBpguiasurtidoresp(models.Model):
    numbodega = models.SmallIntegerField(blank=True, null=True)
    clavemov = models.CharField(max_length=2, blank=True, null=True)
    numlote = models.SmallIntegerField(blank=True, null=True)
    numlector = models.SmallIntegerField(blank=True, null=True)
    numsurtidor = models.SmallIntegerField(blank=True, null=True)
    numtienda = models.SmallIntegerField(blank=True, null=True)
    fechacreacion = models.DateField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    numtalla = models.SmallIntegerField(blank=True, null=True)
    mesetiqueta = models.SmallIntegerField(blank=True, null=True)
    cantidad = models.SmallIntegerField(blank=True, null=True)
    numseccion = models.SmallIntegerField(blank=True, null=True)
    nomguia = models.CharField(max_length=20, blank=True, null=True)
    fechaactualiza = models.DateField(blank=True, null=True)
    consecutivo = models.SmallIntegerField(blank=True, null=True)
    precio = models.SmallIntegerField(blank=True, null=True)
    numdepto = models.SmallIntegerField(blank=True, null=True)
    numclase = models.SmallIntegerField(blank=True, null=True)
    numfamilia = models.SmallIntegerField(blank=True, null=True)
    numcentro = models.IntegerField(blank=True, null=True)
    preciomaximo = models.SmallIntegerField(blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    esimportacion = models.CharField(max_length=1, blank=True, null=True)
    areacodigo = models.CharField(max_length=1, blank=True, null=True)
    esdescontinuado = models.SmallIntegerField(blank=True, null=True)
    numcodigodes = models.IntegerField(blank=True, null=True)
    keyx = models.IntegerField(blank=True, null=True)
    numtipoiva = models.SmallIntegerField(blank=True, null=True)
    rebajado = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_bpguiasurtidoresp'
# Unable to inspect table 'his_cambiostockenmeli'
# The error was: permission denied for table his_cambiostockenmeli


class HisCancelacionDevoluciones(models.Model):
    id_serial = models.IntegerField()
    num_folio_devolucion = models.IntegerField()
    num_folioropa = models.IntegerField()
    estatus_anterior = models.CharField(max_length=250)
    motivo = models.CharField(max_length=50)
    fec_devolucion = models.DateTimeField(blank=True, null=True)
    num_empleado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'his_cancelacion_devoluciones'


class HisCargasArg(models.Model):
    carga_id = models.BigIntegerField(primary_key=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_cargas_arg'


class HisCatArticulosReclasificados(models.Model):
    numarea = models.SmallIntegerField()
    numcodigo = models.IntegerField()
    numdeptoant = models.SmallIntegerField()
    numclaseant = models.SmallIntegerField()
    numfamiliaant = models.SmallIntegerField()
    numdeptonuevo = models.SmallIntegerField()
    numclasenuevo = models.SmallIntegerField()
    numfamilianuevo = models.SmallIntegerField()
    usuarioatendio = models.CharField(max_length=50, blank=True, null=True)
    fechaatendido = models.DateTimeField()
    fechamov = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'his_cat_articulos_reclasificados'


class HisCatCategoriasArg(models.Model):
    groupidentifier = models.CharField(primary_key=True, max_length=64)
    topgroup = models.CharField(max_length=5, blank=True, null=True)
    parentgroupidentifier = models.CharField(max_length=64, blank=True, null=True)
    sequence = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    shortdescription = models.CharField(max_length=254, blank=True, null=True)
    longdescription = models.CharField(max_length=4000, blank=True, null=True)
    thumbnail = models.CharField(max_length=254, blank=True, null=True)
    fullimage = models.CharField(max_length=254, blank=True, null=True)
    published = models.SmallIntegerField(blank=True, null=True)
    keyword = models.CharField(max_length=254, blank=True, null=True)
    urlkeyword = models.CharField(max_length=254, blank=True, null=True)
    pagetitle = models.CharField(max_length=254, blank=True, null=True)
    metadescription = models.CharField(max_length=1024, blank=True, null=True)
    delete = models.SmallIntegerField()
    field1 = models.CharField(max_length=254, blank=True, null=True)
    field2 = models.CharField(max_length=254, blank=True, null=True)
    hash = models.BigIntegerField(blank=True, null=True)
    carga_id = models.BigIntegerField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_cat_categorias_arg'


class HisCatCategoriasDeltaArg(models.Model):
    carga_id = models.BigIntegerField(primary_key=True)
    groupidentifier = models.CharField(max_length=64)
    topgroup = models.CharField(max_length=5, blank=True, null=True)
    parentgroupidentifier = models.CharField(max_length=64, blank=True, null=True)
    sequence = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    shortdescription = models.CharField(max_length=254, blank=True, null=True)
    longdescription = models.CharField(max_length=4000, blank=True, null=True)
    thumbnail = models.CharField(max_length=254, blank=True, null=True)
    fullimage = models.CharField(max_length=254, blank=True, null=True)
    published = models.SmallIntegerField(blank=True, null=True)
    keyword = models.CharField(max_length=254, blank=True, null=True)
    urlkeyword = models.CharField(max_length=254, blank=True, null=True)
    pagetitle = models.CharField(max_length=254, blank=True, null=True)
    metadescription = models.CharField(max_length=1024, blank=True, null=True)
    delete = models.SmallIntegerField()
    field1 = models.CharField(max_length=254, blank=True, null=True)
    field2 = models.CharField(max_length=254, blank=True, null=True)
    hash = models.BigIntegerField(blank=True, null=True)
    order = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_cat_categorias_delta_arg'
        unique_together = (('carga_id', 'groupidentifier', 'delete'),)


class HisCatClientes(models.Model):
    numusuario = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellidopaterno = models.CharField(max_length=30)
    apellidomaterno = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=-1)
    ciudad = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    calle = models.CharField(max_length=40)
    colonia = models.CharField(max_length=30)
    numcasa = models.CharField(max_length=12)
    clientecoppel = models.CharField(max_length=2)
    numclientecoppel = models.IntegerField()
    telefono = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    ext = models.CharField(max_length=20)
    cp = models.CharField(max_length=5)
    saldo = models.DecimalField(max_digits=65535, decimal_places=65535)
    otra = models.CharField(max_length=5)
    registro = models.CharField(max_length=1)
    correovalido = models.IntegerField()
    confirmado = models.CharField(max_length=1)
    interior = models.CharField(max_length=12)
    numciudad = models.IntegerField()
    numcolonia = models.IntegerField()
    numcalle = models.IntegerField()
    fechanacimiento = models.DateField()
    sexo = models.BooleanField()
    fecharegistro = models.DateField()
    celular = models.CharField(max_length=128, blank=True, null=True)
    entrecalles = models.CharField(max_length=-1, blank=True, null=True)
    domicilioobservaciones = models.CharField(max_length=-1, blank=True, null=True)
    id = models.AutoField()
    fechacreacion = models.DateTimeField(blank=True, null=True)
    fec_actualizacion = models.DateTimeField(blank=True, null=True)
    tipo_registro = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'his_cat_clientes'


class HisCatPrecioArg(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=20)
    price = models.FloatField(blank=True, null=True)
    carga_id = models.BigIntegerField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_cat_precio_arg'


class HisCatPrecioDeltaArg(models.Model):
    carga_id = models.BigIntegerField(primary_key=True)
    partnumber = models.CharField(max_length=20)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_cat_precio_delta_arg'
        unique_together = (('carga_id', 'partnumber'),)


class HisCatProductoCategoriaRelArg(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=64)
    parentgroupidentifier = models.CharField(max_length=64)
    sequence = models.FloatField(blank=True, null=True)
    delete = models.SmallIntegerField()
    carga_id = models.BigIntegerField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_cat_producto_categoria_rel_arg'
        unique_together = (('partnumber', 'parentgroupidentifier'),)


class HisCatProductoCategoriaRelDeltaArg(models.Model):
    carga_id = models.BigIntegerField(primary_key=True)
    partnumber = models.CharField(max_length=64)
    parentgroupidentifier = models.CharField(max_length=64)
    sequence = models.FloatField(blank=True, null=True)
    delete = models.SmallIntegerField()
    order = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_cat_producto_categoria_rel_delta_arg'
        unique_together = (('carga_id', 'partnumber', 'parentgroupidentifier', 'delete'),)


class HisCatProductosArg(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=20)
    type = models.CharField(max_length=15, blank=True, null=True)
    parentpartnumber = models.CharField(max_length=20, blank=True, null=True)
    parentgroupidentifier = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    shortdescription = models.CharField(max_length=254, blank=True, null=True)
    longdescription = models.TextField(blank=True, null=True)
    thumbnail = models.CharField(max_length=254, blank=True, null=True)
    fullimage = models.CharField(max_length=254, blank=True, null=True)
    available = models.SmallIntegerField(blank=True, null=True)
    published = models.SmallIntegerField(blank=True, null=True)
    buyable = models.SmallIntegerField(blank=True, null=True)
    manufacturer = models.CharField(max_length=64, blank=True, null=True)
    keyword = models.CharField(max_length=254, blank=True, null=True)
    delete = models.SmallIntegerField()
    urlkeyword = models.CharField(max_length=254, blank=True, null=True)
    metadescription = models.CharField(max_length=1024, blank=True, null=True)
    pagetitle = models.CharField(max_length=254, blank=True, null=True)
    hash = models.BigIntegerField(blank=True, null=True)
    num_area = models.SmallIntegerField(blank=True, null=True)
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.SmallIntegerField(blank=True, null=True)
    carga_id = models.SmallIntegerField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_cat_productos_arg'


class HisCatProductosDeltaArg(models.Model):
    carga_id = models.BigIntegerField(primary_key=True)
    partnumber = models.CharField(max_length=20)
    type = models.CharField(max_length=15, blank=True, null=True)
    parentpartnumber = models.CharField(max_length=20, blank=True, null=True)
    parentgroupidentifier = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    shortdescription = models.CharField(max_length=254, blank=True, null=True)
    longdescription = models.TextField(blank=True, null=True)
    thumbnail = models.CharField(max_length=254, blank=True, null=True)
    fullimage = models.CharField(max_length=254, blank=True, null=True)
    available = models.SmallIntegerField(blank=True, null=True)
    published = models.SmallIntegerField(blank=True, null=True)
    buyable = models.SmallIntegerField(blank=True, null=True)
    manufacturer = models.CharField(max_length=64, blank=True, null=True)
    keyword = models.CharField(max_length=254, blank=True, null=True)
    delete = models.SmallIntegerField()
    urlkeyword = models.CharField(max_length=254, blank=True, null=True)
    metadescription = models.CharField(max_length=1024, blank=True, null=True)
    pagetitle = models.CharField(max_length=254, blank=True, null=True)
    hash = models.BigIntegerField(blank=True, null=True)
    num_area = models.SmallIntegerField(blank=True, null=True)
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.SmallIntegerField(blank=True, null=True)
    order = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_cat_productos_delta_arg'
        unique_together = (('carga_id', 'partnumber', 'delete'),)


class HisConfirmacionarticulos(models.Model):
    num_empleado = models.IntegerField()
    num_notafactura = models.IntegerField()
    idu_pedido = models.IntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.SmallIntegerField()
    num_area = models.SmallIntegerField()
    nom_articulo = models.CharField(max_length=120)
    id_serial = models.IntegerField(blank=True, null=True)
    num_cantidad = models.IntegerField()
    num_preciocompra = models.IntegerField()
    num_precioetiqueta = models.IntegerField()
    num_condicion = models.SmallIntegerField()
    nom_url = models.CharField(max_length=-1, blank=True, null=True)
    flag_confirmado = models.SmallIntegerField(blank=True, null=True)
    flag_clasificado = models.SmallIntegerField()
    num_bodega = models.IntegerField()
    fec_registro = models.DateTimeField(blank=True, null=True)
    fec_confirmacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_confirmacionarticulos'


class HisCtlBitacoraProcesoCompra(models.Model):
    id_proceso_compra = models.BigIntegerField(primary_key=True)
    orden_id = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    num_cliente = models.CharField(max_length=15, blank=True, null=True)
    exitoso = models.BooleanField(blank=True, null=True)
    descripcion_error = models.TextField(blank=True, null=True)
    id_tipo_cliente = models.IntegerField()
    fecha_llamado = models.DateTimeField(blank=True, null=True)
    is_market_place = models.BooleanField(blank=True, null=True)
    field3 = models.TextField(blank=True, null=True)
    num_server = models.CharField(max_length=250, blank=True, null=True)
    nom_correo = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_ctl_bitacora_proceso_compra'


class HisCtlBitacoraProcesoCompraDetalle(models.Model):
    id_detalle_compra = models.BigIntegerField(primary_key=True)
    id_proceso_compra = models.IntegerField()
    id_tipo_proceso = models.IntegerField()
    fecha_llamado = models.DateTimeField(blank=True, null=True)
    exitoso = models.BooleanField(blank=True, null=True)
    descripcion_error = models.TextField(blank=True, null=True)
    folio_apartado = models.CharField(max_length=15, blank=True, null=True)
    desacople = models.BooleanField(blank=True, null=True)
    metodo_pago = models.CharField(max_length=150, blank=True, null=True)
    tiempo_respuesta = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    request_load = models.TextField(blank=True, null=True)
    response_load = models.TextField(blank=True, null=True)
    info_load = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_ctl_bitacora_proceso_compra_detalle'
# Unable to inspect table 'his_ctl_conf_fecha_promesa'
# The error was: permission denied for table his_ctl_conf_fecha_promesa


class HisCtlEntregaArticulosBodega(models.Model):
    num_folio = models.BigIntegerField()
    idu_pedido = models.IntegerField()
    num_area = models.SmallIntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.SmallIntegerField()
    num_bodegaentrega = models.IntegerField()
    fec_entrega = models.DateField()
    fec_movto = models.DateField()
    fec_entregafuturo = models.DateField()
    num_cantidadventafuturo = models.IntegerField()
    num_estatusbodegaropa = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_ctl_entrega_articulos_bodega'


class HisCtlInformacionmarketregistro1(models.Model):
    idu_registro = models.BigIntegerField(primary_key=True)
    num_producto = models.BigIntegerField()
    num_tiporegistro = models.IntegerField()
    des_titulo = models.CharField(max_length=-1)
    num_precio = models.IntegerField()
    num_precio_especial = models.CharField(max_length=-1)
    des_codigo = models.CharField(max_length=-1)
    num_impuesto = models.IntegerField()
    des_tags = models.CharField(max_length=254)
    des_activo = models.CharField(max_length=-1)
    des_url = models.CharField(max_length=-1)
    des_html = models.CharField(max_length=-1)
    des_videoid = models.CharField(max_length=-1)
    des_caracteristicas = models.CharField(max_length=-1)
    num_garantia = models.IntegerField()
    num_area = models.SmallIntegerField()
    num_codigo = models.IntegerField()
    fec_registro = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'his_ctl_informacionmarketregistro1'
        unique_together = (('idu_registro', 'num_producto'),)


class HisCtlInformacionmarketregistro2(models.Model):
    idu_registro = models.BigIntegerField(primary_key=True)
    num_producto = models.BigIntegerField()
    num_tiporegistro = models.IntegerField()
    des_skuerp = models.CharField(max_length=-1)
    des_atributo1 = models.CharField(max_length=-1)
    des_variante1 = models.CharField(max_length=-1)
    des_atributo2 = models.CharField(max_length=-1)
    des_variante2 = models.CharField(max_length=-1)
    num_stock = models.IntegerField()
    num_area = models.SmallIntegerField()
    num_codigo = models.IntegerField()
    des_partnumber = models.CharField(max_length=-1)
    num_talla = models.IntegerField()
    fec_registro = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'his_ctl_informacionmarketregistro2'
        unique_together = (('idu_registro', 'num_producto', 'des_skuerp'),)


class HisCtlRegistromarket(models.Model):
    idu_registro = models.BigAutoField()
    des_registro = models.CharField(max_length=-1)
    fec_registro = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'his_ctl_registromarket'


class HisCtlSurtidoRopa(models.Model):
    numarea = models.SmallIntegerField()
    numcodigo = models.IntegerField()
    cantidad = models.SmallIntegerField()
    talla = models.SmallIntegerField()
    folio = models.IntegerField()
    fechaventa = models.DateField(blank=True, null=True)
    numbodega = models.SmallIntegerField()
    tipoventa = models.CharField(max_length=1)
    flagsurtido = models.CharField(max_length=1)
    fechaactualiza = models.DateTimeField()
    num_empleado = models.IntegerField()
    num_folioorden = models.BigIntegerField()
    flag_ordensingle = models.IntegerField(blank=True, null=True)
    fec_nota = models.DateTimeField()
    fec_surtiroficina = models.DateField()
    fec_notatienda = models.DateField()
    fec_concentrado = models.DateTimeField(blank=True, null=True)
    fec_procesado = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_ctl_surtido_ropa'


class HisDetalleimportarrelaciones(models.Model):
    idu_registrodetalleimportarrelaciones = models.AutoField(primary_key=True)
    idu_importarrelacion = models.IntegerField()
    opc_norelacion = models.SmallIntegerField()
    idu_areapivote = models.ForeignKey(CatFamilias, models.DO_NOTHING, db_column='idu_areapivote')
    idu_departamentopivote = models.IntegerField()
    idu_clasepivote = models.IntegerField()
    idu_familiapivote = models.ForeignKey(CtrlFamiliapivote, models.DO_NOTHING, db_column='idu_familiapivote')
    idu_caracteristicapivote = models.ForeignKey(CatDetallescaracteristicas, models.DO_NOTHING, db_column='idu_caracteristicapivote')
    idu_detallepivote = models.IntegerField()
    num_prioridad = models.IntegerField()
    idu_areacomplementaria = models.ForeignKey(CatDepartamentos, models.DO_NOTHING, db_column='idu_areacomplementaria')
    idu_departamentocomplementaria = models.IntegerField()
    idu_clasecomplementaria = models.IntegerField()
    idu_familiacomplementaria = models.ForeignKey(CtrlFamiliacomplementaria, models.DO_NOTHING, db_column='idu_familiacomplementaria')
    idu_caracteristicacomplementaria = models.ForeignKey(CatCaracteristicas, models.DO_NOTHING, db_column='idu_caracteristicacomplementaria')
    idu_detallecomplementaria = models.IntegerField()
    opc_estatus = models.SmallIntegerField()
    fec_registro = models.DateTimeField()
    fec_modifico = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'his_detalleimportarrelaciones'


class HisDetallepedidos(models.Model):
    idu_pedido = models.IntegerField(blank=True, null=True)
    nom_sitem = models.CharField(max_length=50, blank=True, null=True)
    num_area = models.SmallIntegerField(blank=True, null=True)
    num_talla = models.IntegerField(blank=True, null=True)
    num_codigo = models.IntegerField(blank=True, null=True)
    num_cantidad = models.IntegerField(blank=True, null=True)
    num_ganodineroe = models.IntegerField(blank=True, null=True)
    num_gastodineroe = models.IntegerField(blank=True, null=True)
    num_preciooriginal = models.IntegerField(blank=True, null=True)
    num_preciocreditounitario = models.IntegerField(blank=True, null=True)
    num_preciopromocion = models.IntegerField(blank=True, null=True)
    num_foliotelcel = models.BigIntegerField()
    des_articulo = models.CharField(max_length=12)
    num_tipoprecio = models.SmallIntegerField()
    num_tipodescuento = models.SmallIntegerField()
    num_preciodescuentoempleado = models.IntegerField()
    num_orderitem = models.BigIntegerField()
    nom_articuloweb = models.CharField(max_length=120, blank=True, null=True)
    num_codigochip = models.IntegerField()
    num_codigoanterior = models.IntegerField()
    num_preciocreditocoppel = models.IntegerField()
    fec_respaldo = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'his_detallepedidos'


class HisDireccionentrega(models.Model):
    idu_pedido = models.IntegerField(primary_key=True)
    nom_completo = models.CharField(max_length=100, blank=True, null=True)
    num_estado = models.IntegerField(blank=True, null=True)
    num_ciudad = models.IntegerField(blank=True, null=True)
    num_colonia = models.IntegerField(blank=True, null=True)
    nom_calle = models.CharField(max_length=-1, blank=True, null=True)
    nom_entrecalles = models.CharField(max_length=-1, blank=True, null=True)
    num_casa = models.IntegerField(blank=True, null=True)
    num_codigopostal = models.CharField(max_length=-1, blank=True, null=True)
    num_coloniareferencia = models.IntegerField(blank=True, null=True)
    des_observaciones = models.CharField(max_length=-1, blank=True, null=True)
    num_interior = models.CharField(max_length=7)
    num_telefono = models.CharField(max_length=20)
    opc_celular = models.BooleanField()
    des_coloniacommerce = models.CharField(max_length=200)
    fec_respaldo = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'his_direccionentrega'


class HisDistcoppelresponse(models.Model):
    num_guia = models.CharField(max_length=-1, blank=True, null=True)
    idu_estatus = models.CharField(max_length=-1, blank=True, null=True)
    fecha_recibido = models.DateTimeField(blank=True, null=True)
    nom_quienrecibio = models.CharField(max_length=-1, blank=True, null=True)
    fec_procesado = models.DateTimeField(blank=True, null=True)
    des_estatus = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_distcoppelresponse'


class HisEntregaArticulosBodega(models.Model):
    num_folio = models.BigIntegerField()
    idu_pedido = models.IntegerField()
    num_area = models.SmallIntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.SmallIntegerField()
    num_bodegaentrega = models.IntegerField()
    fec_entrega = models.DateField()
    fec_movto = models.DateField()
    fec_entregafuturo = models.DateField()
    num_cantidadventafuturo = models.IntegerField()
    num_estatusbodegaropa = models.SmallIntegerField()
    fec_respaldo = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'his_entrega_articulos_bodega'


class HisEstatuscodigos(models.Model):
    idu_registro = models.BigIntegerField(primary_key=True)
    num_folio = models.BigIntegerField()
    idu_estatuscodigo = models.IntegerField()
    num_area = models.IntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.IntegerField()
    num_cantidad = models.IntegerField()
    num_orderitem = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'his_estatuscodigos'


class HisEstatuspedido(models.Model):
    num_folio = models.BigIntegerField(primary_key=True)
    num_cliente = models.BigIntegerField()
    idu_estatuspedido = models.IntegerField()
    fec_estimadaropa = models.DateTimeField()
    fec_promesamuebles = models.DateTimeField()
    fec_promesaropa = models.DateTimeField()
    fec_entregaropa = models.DateTimeField()
    fec_entregamuebles = models.DateTimeField()
    fec_respaldo = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'his_estatuspedido'


class HisExportaarchivoderelaciones(models.Model):
    idu_registroexportararchivo = models.AutoField(primary_key=True)
    num_empleado = models.IntegerField()
    nom_empleado = models.CharField(max_length=150)
    idu_area = models.ForeignKey(CatDepartamentos, models.DO_NOTHING, db_column='idu_area')
    idu_departamento = models.IntegerField()
    idu_clase = models.IntegerField()
    idu_familia = models.IntegerField()
    opc_estatus = models.SmallIntegerField()
    fec_modifica = models.DateTimeField()
    fec_registro = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'his_exportaarchivoderelaciones'


class HisFeedproductoLogs(models.Model):
    idu_folio = models.AutoField(primary_key=True)
    opc_operacionhecha = models.TextField()
    fec_iniciooperacion = models.TextField()
    num_duracion = models.IntegerField()
    opc_estatus = models.TextField()
    nom_usuario = models.TextField()

    class Meta:
        managed = False
        db_table = 'his_feedproducto_logs'


class HisFeedproductoLogsMkp(models.Model):
    idu_folio = models.AutoField(primary_key=True)
    opc_operacionhecha = models.TextField()
    fec_iniciooperacion = models.TextField()
    num_duracion = models.IntegerField()
    opc_estatus = models.TextField()
    nom_usuario = models.TextField()

    class Meta:
        managed = False
        db_table = 'his_feedproducto_logs_mkp'


class HisFoliosatendidosporcat(models.Model):
    folio = models.IntegerField(primary_key=True)
    numempleado = models.IntegerField()
    fecha = models.DateTimeField()
    gnfechatransaccion = models.DateField()
    llamadas = models.IntegerField()
    finalizada = models.CharField(max_length=1, blank=True, null=True)
    observaciones_cat = models.TextField()
    fec_ultimointento = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_foliosatendidosporcat'


class HisFormadepago(models.Model):
    idu_pedido = models.OneToOneField('HisPedidos', models.DO_NOTHING, db_column='idu_pedido', primary_key=True)
    num_tipopago = models.SmallIntegerField()
    num_pagoinicialropa = models.IntegerField()
    num_pagoinicialmuebles = models.IntegerField()
    flag_dineroelectronico = models.IntegerField()
    num_dineroelectronicoropa = models.IntegerField()
    num_dineroelectronicomuebles = models.IntegerField()
    num_importetdcropa = models.IntegerField()
    num_importetdcmuebles = models.IntegerField()
    num_porcentajedescuento = models.SmallIntegerField()
    num_margencompra = models.IntegerField()
    num_margencredito = models.IntegerField()
    num_sobrepreciomuebles = models.IntegerField()
    num_tarjeta = models.IntegerField()
    num_referencia = models.CharField(max_length=50)
    cve_banco = models.CharField(max_length=5, blank=True, null=True)
    fec_respaldo = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'his_formadepago'


class HisGaleriaarticulopim(models.Model):
    numarea = models.SmallIntegerField()
    numcodigo = models.IntegerField()
    nomimagen = models.CharField(max_length=30)
    numgaleria = models.BigAutoField()
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_galeriaarticulopim'


class HisGuiareenviooe(models.Model):
    idu_pedido = models.IntegerField()
    num_notafactura = models.IntegerField(blank=True, null=True)
    num_guiaoriginal = models.CharField(max_length=-1, blank=True, null=True)
    num_guiadevolucion = models.CharField(max_length=-1, blank=True, null=True)
    num_guiareenvio = models.CharField(max_length=-1, blank=True, null=True)
    flag_cancelacion = models.SmallIntegerField(blank=True, null=True)
    num_empleado = models.IntegerField(blank=True, null=True)
    fec_registro = models.DateTimeField(blank=True, null=True)
    fec_historial = models.DateTimeField(blank=True, null=True)
    num_empleadohistorial = models.IntegerField(blank=True, null=True)
    idu_oficinadeenvios = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_guiareenviooe'


class HisHistorialventasoe(models.Model):
    idu_pedido = models.IntegerField()
    num_notafactura = models.IntegerField()
    num_foliomp = models.BigIntegerField()
    num_area = models.SmallIntegerField()
    num_codigo = models.IntegerField()
    num_cantidad = models.SmallIntegerField()
    num_talla = models.SmallIntegerField()
    num_precio = models.SmallIntegerField()
    fec_venta = models.DateField()
    num_bodega = models.SmallIntegerField()
    id_serial = models.IntegerField()
    num_guia = models.CharField(max_length=25, blank=True, null=True)
    flag_ordensingle = models.IntegerField()
    flag_estatuscodigo = models.IntegerField()
    num_tipoembalaje = models.SmallIntegerField()
    num_codigo_confirmado = models.SmallIntegerField()
    num_codigo_enviado = models.SmallIntegerField()
    num_folioplataforma = models.BigIntegerField()
    fecha_movimiento = models.DateTimeField(blank=True, null=True)
    flag_etiquetamaster_confirmado = models.IntegerField(blank=True, null=True)
    idu_paquetera = models.IntegerField(blank=True, null=True)
    idu_multicarrier = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_historialventasoe'


class HisImportarrelaciones(models.Model):
    idu_registroimportarrelaciones = models.AutoField(primary_key=True)
    num_empleado = models.IntegerField()
    nom_empleado = models.CharField(max_length=150)
    nom_archivo = models.CharField(max_length=150)
    opc_estatus = models.SmallIntegerField()
    fec_registro = models.DateTimeField()
    fec_modifica = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'his_importarrelaciones'


class HisIndexaciones(models.Model):
    keyx = models.AutoField()
    ip_servidor = models.CharField(max_length=-1, blank=True, null=True)
    flag_exito = models.BooleanField(blank=True, null=True)
    fec_actualizacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_indexaciones'


class HisInventariosoe(models.Model):
    num_area = models.SmallIntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.SmallIntegerField()
    num_cantidad = models.SmallIntegerField()
    num_precio = models.SmallIntegerField()
    fecha_entrada = models.DateTimeField(blank=True, null=True)
    fecha_salida = models.DateTimeField(blank=True, null=True)
    id_serial = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'his_inventariosoe'


class HisInvespecial(models.Model):
    num_empleado = models.IntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.SmallIntegerField()
    num_area = models.SmallIntegerField()
    num_condicion = models.IntegerField()
    num_cantidad = models.IntegerField()
    num_preciocompra = models.IntegerField()
    num_precioetiqueta = models.IntegerField()
    num_resolucion = models.IntegerField()
    fec_registro = models.DateTimeField()
    keyx = models.BigIntegerField(blank=True, null=True)
    num_empleado_resolucion = models.IntegerField(blank=True, null=True)
    fec_resolucion = models.DateTimeField(blank=True, null=True)
    id_serial = models.BigIntegerField(blank=True, null=True)
    num_devolucion_muebles = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_invespecial'


class HisMovDeltasmarketplaceAttrdictionary(models.Model):
    idu_atributomarketplace = models.BigIntegerField(primary_key=True)
    identifier = models.CharField(max_length=120)
    type = models.CharField(max_length=120)
    attributetype = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    description = models.TextField()
    sequence = models.IntegerField()
    displayable = models.BooleanField()
    searchable = models.BooleanField()
    comparable = models.BooleanField()
    storedisplay = models.SmallIntegerField()
    merchandisable = models.BooleanField()
    facetable = models.BooleanField()
    allowmultiplefacetvalueselection = models.BooleanField(blank=True, null=True)
    facetvalueordering = models.BooleanField()
    includeinsearchresults = models.BooleanField()
    showemptyfacetvalues = models.BooleanField()
    maximumvaluestodisplay = models.SmallIntegerField()
    delete = models.SmallIntegerField()
    opc_nuevo = models.BooleanField()
    idu_carga = models.ForeignKey(CtlCargasMarketplace, models.DO_NOTHING, db_column='idu_carga')

    class Meta:
        managed = False
        db_table = 'his_mov_deltasmarketplace_attrdictionary'
        unique_together = (('idu_atributomarketplace', 'identifier', 'delete', 'idu_carga'),)


class HisMovDeltasmarketplaceAttrdictionaryAllowedData(models.Model):
    idu_valoratributo = models.BigIntegerField()
    identifier = models.CharField(primary_key=True, max_length=120)
    valueidentifier = models.TextField()
    value = models.TextField(blank=True, null=True)
    sequence = models.IntegerField()
    languageid = models.SmallIntegerField()
    delete = models.SmallIntegerField()
    idu_carga = models.ForeignKey(CtlCargasMarketplace, models.DO_NOTHING, db_column='idu_carga')

    class Meta:
        managed = False
        db_table = 'his_mov_deltasmarketplace_attrdictionary_allowed_data'
        unique_together = (('identifier', 'valueidentifier', 'idu_carga'),)


class HisMovDeltasmarketplaceAttrmap(models.Model):
    idu_atributomarketplace = models.BigIntegerField()
    partnumber = models.CharField(primary_key=True, max_length=64)
    attributeidentifier = models.CharField(max_length=254)
    valueidentifier = models.CharField(max_length=254)
    value = models.CharField(max_length=254)
    usage = models.CharField(max_length=64)
    sequence = models.IntegerField()
    delete = models.IntegerField()
    idu_carga = models.ForeignKey(CtlCargasMarketplace, models.DO_NOTHING, db_column='idu_carga')

    class Meta:
        managed = False
        db_table = 'his_mov_deltasmarketplace_attrmap'
        unique_together = (('partnumber', 'attributeidentifier', 'valueidentifier', 'value', 'delete', 'idu_carga'),)


class HisMovDeltasmarketplaceCategorias(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    numareaweb = models.SmallIntegerField()
    opc_nivel = models.SmallIntegerField()
    groupidentifier = models.CharField(max_length=254)
    topgroup = models.BooleanField()
    parentgroupidentifier = models.CharField(max_length=254)
    sequence = models.IntegerField()
    name = models.CharField(max_length=254)
    shortdescription = models.CharField(max_length=254)
    longdescription = models.CharField(max_length=2048)
    thumbnail = models.CharField(max_length=120)
    fullimage = models.CharField(max_length=120)
    published = models.IntegerField()
    urlkeyword = models.CharField(max_length=254)
    pagetitle = models.CharField(max_length=254)
    keyword = models.CharField(max_length=254)
    metadescription = models.CharField(max_length=254)
    delete = models.CharField(max_length=1)
    field1 = models.CharField(max_length=254)
    field2 = models.CharField(max_length=254)
    idu_carga = models.ForeignKey(CtlCargasMarketplace, models.DO_NOTHING, db_column='idu_carga')

    class Meta:
        managed = False
        db_table = 'his_mov_deltasmarketplace_categorias'
        unique_together = (('numarea', 'numareaweb', 'idu_carga'),)


class HisMovDeltasmarketplaceCategoriasventa(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    numareaweb = models.SmallIntegerField()
    opc_nivel = models.SmallIntegerField()
    groupidentifier = models.CharField(max_length=254)
    topgroup = models.BooleanField()
    parentgroupidentifier = models.CharField(max_length=254)
    sequence = models.IntegerField()
    name = models.CharField(max_length=254)
    shortdescription = models.CharField(max_length=254)
    longdescription = models.CharField(max_length=2048)
    thumbnail = models.CharField(max_length=120)
    fullimage = models.CharField(max_length=120)
    published = models.IntegerField()
    urlkeyword = models.CharField(max_length=254)
    pagetitle = models.CharField(max_length=254)
    keyword = models.CharField(max_length=254)
    metadescription = models.CharField(max_length=254)
    delete = models.CharField(max_length=1)
    field1 = models.CharField(max_length=254)
    field2 = models.CharField(max_length=254)
    idu_carga = models.ForeignKey(CtlCargasMarketplace, models.DO_NOTHING, db_column='idu_carga')

    class Meta:
        managed = False
        db_table = 'his_mov_deltasmarketplace_categoriasventa'
        unique_together = (('numarea', 'numareaweb'),)


class HisMovDeltasmarketplaceInventory(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=64)
    fullfillmentcentername = models.CharField(max_length=50)
    quantity = models.IntegerField()
    delete = models.IntegerField()
    idu_carga = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'his_mov_deltasmarketplace_inventory'
        unique_together = (('partnumber', 'fullfillmentcentername', 'idu_carga'),)


class HisMovDeltasmarketplaceItems(models.Model):
    idu_producto = models.BigIntegerField()
    partnumber = models.CharField(max_length=64)
    type = models.CharField(max_length=16)
    name = models.CharField(max_length=264)
    shortdescription = models.CharField(max_length=264)
    longdescription = models.CharField(max_length=4000)
    published = models.SmallIntegerField()
    keyword = models.CharField(max_length=264)
    delete = models.SmallIntegerField()
    manufacturer = models.CharField(max_length=64)
    buyable = models.IntegerField()
    mpn_vendedor = models.CharField(primary_key=True, max_length=64)
    idu_carga = models.ForeignKey(CtlCargasMarketplace, models.DO_NOTHING, db_column='idu_carga')

    class Meta:
        managed = False
        db_table = 'his_mov_deltasmarketplace_items'
        unique_together = (('mpn_vendedor', 'idu_carga'),)


class HisMovDeltasmarketplaceOfferPrice(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=64)
    price = models.IntegerField()
    currencycode = models.CharField(max_length=16)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    field1 = models.CharField(max_length=20)
    sellerid = models.BigIntegerField()
    mpofferid = models.BigIntegerField()
    identifier = models.BigIntegerField()
    buyboxweight = models.FloatField()
    selleritemid = models.CharField(max_length=30)
    condition = models.CharField(max_length=10)
    conditiondesc = models.CharField(max_length=254)
    precedence = models.FloatField()
    delete = models.IntegerField()
    idu_carga = models.BigIntegerField()
    idu_producto = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'his_mov_deltasmarketplace_offer_price'
        unique_together = (('partnumber', 'identifier', 'delete', 'idu_carga'),)


class HisMovDeltasmarketplacePriceList(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=64)
    listprice = models.IntegerField()
    currencycode = models.CharField(max_length=16)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    identifier = models.BigIntegerField()
    delete = models.IntegerField()
    idu_carga = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'his_mov_deltasmarketplace_price_list'
        unique_together = (('partnumber', 'identifier', 'delete', 'idu_carga'),)


class HisMovDeltasmarketplaceProductos(models.Model):
    idu_producto = models.BigIntegerField(primary_key=True)
    partnumber = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    name = models.CharField(max_length=128)
    shortdescription = models.CharField(max_length=254)
    longdescription = models.CharField(max_length=4000)
    thumbnail = models.CharField(max_length=254)
    fullimage = models.CharField(max_length=254)
    published = models.SmallIntegerField()
    keyword = models.CharField(max_length=254)
    delete = models.SmallIntegerField()
    manufacturerpartnumber = models.CharField(max_length=64)
    manufacturer = models.CharField(max_length=64)
    url = models.CharField(max_length=254)
    field1 = models.IntegerField()
    field2 = models.IntegerField()
    field3 = models.FloatField()
    field4 = models.CharField(max_length=254)
    field5 = models.CharField(max_length=254)
    buyable = models.IntegerField()
    parentpartnumber = models.CharField(max_length=64)
    urlkeyword = models.CharField(max_length=254)
    metadescription = models.CharField(max_length=1024)
    pagetitle = models.CharField(max_length=254)
    idu_carga = models.ForeignKey(CtlCargasMarketplace, models.DO_NOTHING, db_column='idu_carga')

    class Meta:
        managed = False
        db_table = 'his_mov_deltasmarketplace_productos'
        unique_together = (('idu_producto', 'partnumber', 'idu_carga'),)


class HisMovDeltasmarketplacePromotions(models.Model):
    administrativename = models.CharField(primary_key=True, max_length=254)
    endtime = models.DateTimeField()
    admindescription = models.CharField(max_length=2048)
    percentage = models.SmallIntegerField()
    stardate = models.DateTimeField()
    opc_tipo = models.CharField(max_length=50)
    subtype = models.CharField(max_length=100)
    identifier = models.CharField(max_length=254)
    currency = models.CharField(max_length=50)
    shortdescription = models.CharField(max_length=2048)
    longdescription = models.CharField(max_length=2048)
    amountoff = models.SmallIntegerField()
    opc_estado = models.CharField(max_length=50)
    delete = models.SmallIntegerField()
    idu_carga = models.ForeignKey(CtlCargasMarketplace, models.DO_NOTHING, db_column='idu_carga')

    class Meta:
        managed = False
        db_table = 'his_mov_deltasmarketplace_promotions'
        unique_together = (('administrativename', 'idu_carga'),)


class HisMovDeltasmarketplaceRelacionproductocategoria(models.Model):
    idu_numareaweb = models.IntegerField()
    partnumber = models.CharField(primary_key=True, max_length=64)
    parentgroupidentifier = models.CharField(max_length=254)
    sequence = models.IntegerField()
    delete = models.SmallIntegerField()
    idu_carga = models.ForeignKey(CtlCargasMarketplace, models.DO_NOTHING, db_column='idu_carga')

    class Meta:
        managed = False
        db_table = 'his_mov_deltasmarketplace_relacionproductocategoria'
        unique_together = (('partnumber', 'parentgroupidentifier', 'delete', 'idu_carga'),)


class HisMovDeltasmarketplaceRelacionproductoitem(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=64)
    parentpartnumber = models.CharField(max_length=254)
    idu_producto = models.BigIntegerField()
    des_valoratributomx = models.CharField(max_length=64)
    des_valoratributo = models.CharField(max_length=254)
    sequence = models.SmallIntegerField()
    delete = models.SmallIntegerField()
    idu_carga = models.ForeignKey(CtlCargasMarketplace, models.DO_NOTHING, db_column='idu_carga')

    class Meta:
        managed = False
        db_table = 'his_mov_deltasmarketplace_relacionproductoitem'
        unique_together = (('partnumber', 'parentpartnumber', 'sequence', 'delete', 'idu_carga'),)


class HisMovDeltasmarketplaceVendedores(models.Model):
    idu_seller = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=254)
    logo = models.CharField(max_length=254)
    registrydate = models.DateTimeField()
    description = models.CharField(max_length=2048)
    warrantypolicies = models.TextField()
    shippingpolicies = models.TextField()
    returnpolicies = models.TextField()
    premium = models.SmallIntegerField()
    status = models.CharField(max_length=1)
    field1 = models.CharField(max_length=254)
    field2 = models.CharField(max_length=254)
    field3 = models.CharField(max_length=254)
    delete = models.SmallIntegerField()
    idu_carga = models.ForeignKey(CtlCargasMarketplace, models.DO_NOTHING, db_column='idu_carga')

    class Meta:
        managed = False
        db_table = 'his_mov_deltasmarketplace_vendedores'
        unique_together = (('idu_seller', 'idu_carga'),)


class HisMovEstatuscodigos(models.Model):
    idu_registro = models.AutoField(primary_key=True)
    num_folio = models.BigIntegerField()
    idu_estatuscodigo = models.IntegerField()
    num_area = models.IntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.IntegerField()
    num_cantidad = models.IntegerField()
    fec_movimiento = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'his_mov_estatuscodigos'


class HisMovEstatuspedido(models.Model):
    idu_registroventa = models.AutoField(primary_key=True)
    num_folio = models.BigIntegerField()
    idu_estatuspedido = models.IntegerField()
    fec_movimiento = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'his_mov_estatuspedido'


class HisMovVentaRopa(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    cantidad = models.SmallIntegerField(blank=True, null=True)
    talla = models.CharField(max_length=-1, blank=True, null=True)
    folio = models.IntegerField(blank=True, null=True)
    fechaventa = models.DateField(blank=True, null=True)
    numbodega = models.SmallIntegerField(blank=True, null=True)
    tipoventa = models.CharField(max_length=1, blank=True, null=True)
    flagsurtido = models.CharField(max_length=1)
    flagenviado = models.CharField(max_length=1)
    flagapartado = models.CharField(max_length=1)
    precio = models.IntegerField()
    id_serial = models.AutoField(primary_key=True)
    nu_guia = models.CharField(max_length=25, blank=True, null=True)
    flagvendido = models.CharField(max_length=1, blank=True, null=True)
    sn_codigo_confirmado = models.IntegerField(blank=True, null=True)
    sn_impreso = models.IntegerField(blank=True, null=True)
    precio_surtido = models.IntegerField(blank=True, null=True)
    fh_surtido = models.DateTimeField(blank=True, null=True)
    flag_ordensingle = models.IntegerField(blank=True, null=True)
    flag_statuscodigo = models.IntegerField()
    num_foliomp = models.BigIntegerField()
    num_tipoembalaje = models.SmallIntegerField()
    idu_paquetera = models.IntegerField(blank=True, null=True)
    idu_multicarrier = models.IntegerField(blank=True, null=True)
    flag_contingencia = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_mov_venta_ropa'


class HisMovVentasCatalogoManual(models.Model):
    num_orden = models.BigIntegerField()
    num_empleado = models.IntegerField()
    dfecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_mov_ventas_catalogo_manual'


class HisMovimientosordenes(models.Model):
    idu_movimiento = models.AutoField(primary_key=True)
    fec_movimiento = models.CharField(max_length=-1, blank=True, null=True)
    des_empleado = models.CharField(max_length=-1, blank=True, null=True)
    idu_orden = models.IntegerField(blank=True, null=True)
    des_movimiento = models.CharField(max_length=-1, blank=True, null=True)
    des_valoranterior = models.CharField(max_length=-1, blank=True, null=True)
    des_valoractual = models.CharField(max_length=-1, blank=True, null=True)
    opc_estadoorden = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_movimientosordenes'


class HisNotascompletas(models.Model):
    num_empleado = models.IntegerField()
    num_notafactura = models.IntegerField()
    idu_pedido = models.IntegerField()
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.SmallIntegerField(blank=True, null=True)
    num_area = models.SmallIntegerField()
    nom_articulo = models.CharField(max_length=120)
    id_serial = models.BigIntegerField(blank=True, null=True)
    num_cantidad = models.IntegerField()
    num_preciocompra = models.IntegerField()
    num_precioetiqueta = models.IntegerField()
    num_condicion = models.SmallIntegerField()
    nom_url = models.CharField(max_length=-1, blank=True, null=True)
    fec_registro = models.DateTimeField(blank=True, null=True)
    nom_posicion = models.CharField(max_length=-1, blank=True, null=True)
    flag_enviado = models.IntegerField()
    flag_foliomp = models.SmallIntegerField()
    flag_confirmado = models.SmallIntegerField()
    num_bodega = models.IntegerField()
    fec_confirmacion = models.DateTimeField()
    num_empleado_confirmacion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_notascompletas'


class HisOeliberaciondebloques(models.Model):
    idu_pedido = models.IntegerField()
    num_notafactura = models.IntegerField()
    num_area = models.SmallIntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.IntegerField()
    num_cantidad = models.SmallIntegerField()
    id_serial = models.IntegerField()
    num_codigo_confirmado = models.SmallIntegerField()
    flag_activo = models.IntegerField()
    num_empleado = models.IntegerField()
    fec_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_oeliberaciondebloques'


class HisOepreclasificacion(models.Model):
    num_empleado = models.IntegerField()
    num_notafactura = models.IntegerField()
    idu_pedido = models.IntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.SmallIntegerField()
    num_area = models.SmallIntegerField()
    id_serial = models.BigIntegerField(blank=True, null=True)
    num_pasillo = models.IntegerField()
    nom_letra = models.CharField(max_length=20)
    num_bodega = models.IntegerField()
    flag_clasificado = models.SmallIntegerField()
    flag_foliomp = models.SmallIntegerField()
    fec_movimiento = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'his_oepreclasificacion'


class HisOrdenesaenviarcorreo(models.Model):
    idu_envio = models.AutoField(primary_key=True)
    idu_carrito = models.BigIntegerField()
    id_orden = models.BigIntegerField()
    id_sesion = models.CharField(max_length=64)
    num_cliente = models.IntegerField(blank=True, null=True)
    id_tipocorreoenviar = models.SmallIntegerField()
    nom_email = models.CharField(max_length=250)
    nom_cliente = models.CharField(max_length=120)
    des_urlcarrito = models.CharField(max_length=100, blank=True, null=True)
    fec_alta = models.DateTimeField()
    fec_movimiento = models.DateTimeField()
    fec_envioemail = models.DateTimeField()
    id_proceso_envio = models.IntegerField()
    num_estatuscorreo = models.SmallIntegerField()
    num_estatuscompra = models.SmallIntegerField()
    num_tabla = models.SmallIntegerField()
    num_contenidoextra = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_ordenesaenviarcorreo'


class HisPedidos(models.Model):
    idu_pedido = models.IntegerField(unique=True)
    nom_email = models.CharField(max_length=-1)
    num_clientecoppel = models.BigIntegerField()
    num_empleadocoppel = models.IntegerField()
    nom_cliente = models.CharField(max_length=-1)
    nom_apepaterno = models.CharField(max_length=100)
    nom_apematerno = models.CharField(max_length=100)
    num_importetotal = models.IntegerField()
    fec_orden = models.DateTimeField()
    num_telefono = models.CharField(max_length=20)
    opc_celular = models.BooleanField()
    num_folio = models.BigIntegerField(unique=True)
    num_estatus = models.IntegerField()
    num_totalarticulosmuebles = models.SmallIntegerField()
    num_totalarticulosropa = models.SmallIntegerField()
    num_importeropa = models.IntegerField()
    num_importemuebles = models.IntegerField()
    num_engancheropa = models.IntegerField()
    des_articulo = models.CharField(max_length=12)
    num_enganchemuebles = models.IntegerField()
    num_folioropa = models.IntegerField()
    num_foliomuebles = models.IntegerField()
    fec_movimiento = models.DateTimeField(blank=True, null=True)
    num_pagorecibido = models.IntegerField()
    desc_canalventa = models.CharField(max_length=20)
    desc_servicio = models.CharField(max_length=20)
    fec_facturanota = models.DateField()
    fec_respaldo = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'his_pedidos'
        unique_together = (('num_folio', 'num_foliomuebles'),)


class HisPendienteentregatda(models.Model):
    num_tienda = models.IntegerField()
    num_factura = models.IntegerField()
    idu_cliente = models.IntegerField()
    opc_recogecliente = models.SmallIntegerField()
    idu_tipoventa = models.SmallIntegerField()
    nom_nombrerecoge = models.CharField(max_length=50)
    nom_apellidopaternorecoge = models.CharField(max_length=50)
    nom_apellidomaternorecoge = models.CharField(max_length=50)
    fec_fechaventa = models.DateField()
    fec_fechamovto = models.DateTimeField()
    sec_keyx = models.AutoField()
    telefono_quien_recoge = models.BigIntegerField(blank=True, null=True)
    es_telefono_fijo = models.IntegerField(blank=True, null=True)
    idu_area = models.IntegerField(blank=True, null=True)
    fec_procesamiento = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'his_pendienteentregatda'


class HisPendienteentregatdadetalle(models.Model):
    num_tienda = models.IntegerField()
    num_factura = models.IntegerField()
    num_codigo = models.IntegerField()
    num_cantidad = models.SmallIntegerField()
    num_cvesort = models.SmallIntegerField()
    num_estatus = models.SmallIntegerField()
    des_quienentrega = models.CharField(max_length=2)
    num_tiendaentrega = models.IntegerField()
    fec_fechaentregapropuesta = models.DateField()
    fec_fechaentregarealizada = models.DateField()
    des_serie = models.CharField(max_length=25)
    opc_flagcorreo = models.SmallIntegerField()
    fec_fechaentradatienda = models.DateField()
    fec_fechaactualizacion = models.DateField()
    num_referenciats = models.IntegerField()
    sec_keyx = models.IntegerField()
    bodegaentrega = models.IntegerField(blank=True, null=True)
    correoenviado_estatustres = models.SmallIntegerField(blank=True, null=True)
    correoenviado_estatuscuatro = models.SmallIntegerField(blank=True, null=True)
    correoenviado_faltandosdias = models.SmallIntegerField(blank=True, null=True)
    num_codigocelular = models.IntegerField()
    ismoto = models.IntegerField()
    correoenviado_moto = models.IntegerField(blank=True, null=True)
    num_estatusmoto = models.IntegerField()
    fec_fechaactivacion = models.DateField(blank=True, null=True)
    fec_procesamiento = models.DateTimeField()
    idu_area = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'his_pendienteentregatdadetalle'


class HisPendingDeliverBatch(models.Model):
    pending_id = models.CharField(primary_key=True, max_length=255)
    folio_orden = models.BigIntegerField(blank=True, null=True)
    motorcycle = models.IntegerField(blank=True, null=True)
    number_area = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    store = models.IntegerField(blank=True, null=True)
    invoice = models.IntegerField(blank=True, null=True)
    status_email_motorcycle = models.IntegerField(blank=True, null=True)
    status_motorcycle = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_pending_deliver_batch'


class HisPosicionesocupadas(models.Model):
    idu_posicion = models.IntegerField()
    num_empleado = models.IntegerField()
    num_notafactura = models.IntegerField()
    idu_pedido = models.IntegerField()
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.SmallIntegerField(blank=True, null=True)
    id_serial = models.BigIntegerField(blank=True, null=True)
    nom_posicion = models.CharField(max_length=-1, blank=True, null=True)
    opc_posicionllena = models.BooleanField(blank=True, null=True)
    flag_posicioncomplemento = models.IntegerField()
    idu_posicionpadre = models.IntegerField(blank=True, null=True)
    nom_posicionpadre = models.CharField(max_length=-1, blank=True, null=True)
    flag_articuloconfirmado = models.IntegerField(blank=True, null=True)
    flag_codigoleido = models.IntegerField()
    flag_foliomp = models.SmallIntegerField()
    fec_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_posicionesocupadas'


class HisProcesoventas(models.Model):
    sec_serial = models.IntegerField()
    des_session = models.CharField(max_length=50)
    num_cliente = models.IntegerField()
    clv_tipoprocesoventa = models.SmallIntegerField(blank=True, null=True)
    clv_tipoopcionventa = models.SmallIntegerField(blank=True, null=True)
    fol_procesoventa = models.IntegerField(blank=True, null=True)
    fec_procesoventa = models.DateTimeField(blank=True, null=True)
    clv_respuestaventas = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_procesoventas'


class HisSeguimientopedido(models.Model):
    factura = models.IntegerField()
    tienda = models.SmallIntegerField()
    codigo = models.IntegerField()
    cantidad = models.IntegerField()
    clavemovto = models.SmallIntegerField()
    causa = models.SmallIntegerField()
    fechamovto = models.DateTimeField()
    cvesort = models.SmallIntegerField()
    keyx = models.AutoField()
    borrarestatus = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_seguimientopedido'


class HisSurtidoRopa(models.Model):
    numarea = models.SmallIntegerField()
    numcodigo = models.IntegerField()
    cantidad = models.SmallIntegerField()
    talla = models.SmallIntegerField()
    folio = models.IntegerField()
    fechaventa = models.DateField(blank=True, null=True)
    numbodega = models.SmallIntegerField()
    tipoventa = models.CharField(max_length=1)
    flagsurtido = models.CharField(max_length=1)
    fechaactualiza = models.DateTimeField()
    num_empleado = models.IntegerField()
    num_folioorden = models.BigIntegerField()
    flag_ordensingle = models.IntegerField(blank=True, null=True)
    fec_respaldo = models.DateTimeField()
    fec_nota = models.DateTimeField()
    fec_surtiroficina = models.DateField()
    fec_notatienda = models.DateField()
    fec_concentrado = models.DateTimeField(blank=True, null=True)
    fec_procesado = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_surtido_ropa'


class HisTransferenciasoe(models.Model):
    tipo_transferencia = models.SmallIntegerField(blank=True, null=True)
    num_lote = models.SmallIntegerField(blank=True, null=True)
    num_cantidad_lote = models.SmallIntegerField(blank=True, null=True)
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.SmallIntegerField(blank=True, null=True)
    num_precio = models.IntegerField(blank=True, null=True)
    num_cantidad = models.SmallIntegerField(blank=True, null=True)
    num_caja = models.SmallIntegerField(blank=True, null=True)
    num_bodega = models.SmallIntegerField(blank=True, null=True)
    num_jaba = models.IntegerField(blank=True, null=True)
    fec_creacion = models.DateTimeField(blank=True, null=True)
    fec_modificacion = models.DateTimeField(blank=True, null=True)
    fec_mov_transferencia = models.DateTimeField(blank=True, null=True)
    id_oficinaenvios = models.BigIntegerField(blank=True, null=True)
    flag_transferencia = models.IntegerField(blank=True, null=True)
    num_area = models.SmallIntegerField(blank=True, null=True)
    num_empleado = models.IntegerField(blank=True, null=True)
    num_guia = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_transferenciasoe'


class HisVentaRopa(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    cantidad = models.SmallIntegerField(blank=True, null=True)
    talla = models.CharField(max_length=-1, blank=True, null=True)
    folio = models.IntegerField(blank=True, null=True)
    fechaventa = models.DateField(blank=True, null=True)
    numbodega = models.SmallIntegerField(blank=True, null=True)
    tipoventa = models.CharField(max_length=1, blank=True, null=True)
    flagsurtido = models.CharField(max_length=1)
    flagenviado = models.CharField(max_length=1)
    flagapartado = models.CharField(max_length=1)
    precio = models.IntegerField()
    id_serial = models.AutoField()
    nu_guia = models.CharField(max_length=25, blank=True, null=True)
    flagvendido = models.CharField(max_length=1, blank=True, null=True)
    sn_codigo_confirmado = models.IntegerField(blank=True, null=True)
    sn_impreso = models.IntegerField(blank=True, null=True)
    precio_surtido = models.IntegerField(blank=True, null=True)
    fh_surtido = models.DateTimeField(blank=True, null=True)
    flag_ordensingle = models.IntegerField(blank=True, null=True)
    fec_respaldo = models.DateTimeField()
    flag_statuscodigo = models.IntegerField()
    num_tipoembalaje = models.SmallIntegerField()
    idu_paquetera = models.IntegerField(blank=True, null=True)
    idu_multicarrier = models.IntegerField(blank=True, null=True)
    flag_contingencia = models.SmallIntegerField(blank=True, null=True)
    num_foliomp = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'his_venta_ropa'


class HisVentasoe(models.Model):
    idu_pedido = models.IntegerField()
    num_notafactura = models.IntegerField()
    num_foliomp = models.BigIntegerField()
    num_area = models.SmallIntegerField()
    num_codigo = models.IntegerField()
    num_cantidad = models.SmallIntegerField()
    num_talla = models.SmallIntegerField()
    num_precio = models.SmallIntegerField()
    fec_venta = models.DateField()
    num_bodega = models.SmallIntegerField()
    id_serial = models.IntegerField()
    num_guia = models.CharField(max_length=25, blank=True, null=True)
    flag_ordensingle = models.IntegerField()
    flag_estatuscodigo = models.IntegerField()
    num_tipoembalaje = models.SmallIntegerField()
    num_codigo_confirmado = models.SmallIntegerField()
    num_codigo_enviado = models.SmallIntegerField()
    num_folioplataforma = models.BigIntegerField()
    fecha_movimiento = models.DateTimeField(blank=True, null=True)
    flag_etiquetamaster_confirmado = models.IntegerField(blank=True, null=True)
    idu_paquetera = models.IntegerField(blank=True, null=True)
    idu_multicarrier = models.IntegerField(blank=True, null=True)
    opc_movimientoaoficinadeenvios = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_ventasoe'


class HisVentastarjetas(models.Model):
    clv_tarjetacredito = models.CharField(max_length=128)
    nom_email = models.CharField(max_length=100)
    fol_ventastarjeta = models.IntegerField()
    opc_aceptado = models.SmallIntegerField()
    num_referencia = models.IntegerField()
    imp_compra = models.IntegerField()
    fec_actualiza = models.DateTimeField(blank=True, null=True)
    sec_serial = models.AutoField()
    causa = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_ventastarjetas'


class HisZonasdistribucioncedis(models.Model):
    num_bodega = models.SmallIntegerField(blank=True, null=True)
    num_ciudad = models.SmallIntegerField(blank=True, null=True)
    num_zona = models.IntegerField(blank=True, null=True)
    nom_zona = models.CharField(max_length=30, blank=True, null=True)
    num_codigopostal = models.IntegerField(blank=True, null=True)
    mvto = models.IntegerField(blank=True, null=True)
    num_empleado_mvto = models.BigIntegerField(blank=True, null=True)
    fecha_mvto = models.DateTimeField(blank=True, null=True)
    num_bodega_destino = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_zonasdistribucioncedis'


class HistDomiciliosbodega(models.Model):
    nombre_para = models.CharField(max_length=-1, blank=True, null=True)
    apellidopaterno_para = models.CharField(max_length=-1, blank=True, null=True)
    apellidomaterno_para = models.CharField(max_length=-1, blank=True, null=True)
    estado_para = models.CharField(max_length=-1, blank=True, null=True)
    ciudad_para = models.CharField(max_length=-1, blank=True, null=True)
    colonia_para = models.CharField(max_length=-1, blank=True, null=True)
    calle_para = models.CharField(max_length=-1, blank=True, null=True)
    entrecalles_para = models.CharField(max_length=-1, blank=True, null=True)
    codigopostal_para = models.CharField(max_length=-1, blank=True, null=True)
    numerocasa_para = models.IntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=-1, blank=True, null=True)
    id = models.AutoField()
    idsession = models.CharField(max_length=64)
    nombreciudad_para = models.CharField(max_length=64, blank=True, null=True)
    coloniaref_para = models.IntegerField(blank=True, null=True)
    tiempoactualizacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hist_domiciliosbodega'


class HistFacturasgeneradas(models.Model):
    id = models.AutoField()
    folio = models.IntegerField(blank=True, null=True)
    flagexito = models.IntegerField(blank=True, null=True)
    respuesta = models.TextField(blank=True, null=True)
    xml = models.TextField(blank=True, null=True)
    sql = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    tipofactura = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hist_facturasgeneradas'
# Unable to inspect table 'historicalperformancebuybox'
# The error was: permission denied for table historicalperformancebuybox


class HistoricoPrecios(models.Model):
    numcodigo = models.IntegerField()
    numarea = models.IntegerField()
    precio_anterior = models.IntegerField()
    precio_nuevo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historico_precios'


class Iactivas(models.Model):
    idu_posicion = models.IntegerField(blank=True, null=True)
    num_pasillo = models.IntegerField(blank=True, null=True)
    nom_posicion = models.CharField(max_length=20, blank=True, null=True)
    nom_letra = models.CharField(max_length=20, blank=True, null=True)
    num_nivel = models.IntegerField(blank=True, null=True)
    num_columna = models.IntegerField(blank=True, null=True)
    opc_activo = models.BooleanField(blank=True, null=True)
    num_letraspasillo = models.IntegerField(blank=True, null=True)
    num_codigobarra = models.BigIntegerField(blank=True, null=True)
    num_bodega = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iactivas'


class Iarticulosclasificados(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iarticulosclasificados'


class Iarticulosrecibidossingle(models.Model):
    field_column_field = models.BigIntegerField(db_column='?column?', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'iarticulosrecibidossingle'


class Iattributevariant(models.Model):
    idu_atributo = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iattributevariant'


class Ibrand(models.Model):
    idu_atributo = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ibrand'


class Icapacidad(models.Model):
    num_valor = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icapacidad'


class Iciudadcoppel(models.Model):
    num_ciudadcoppel = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iciudadcoppel'


class Icontador(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icontador'


class Icontadortotalfilas(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icontadortotalfilas'


class Idatributo(models.Model):
    idu_atributo = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idatributo'


class Idias(models.Model):
    num_valor = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idias'


class Idpedido(models.Model):
    idu_pedido = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idpedido'


class Idsesion(models.Model):
    pg_backend_pid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idsesion'


class IduFampivote(models.Model):
    idu_familiapivote = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idu_fampivote'


class IduPed(models.Model):
    idu_pedido = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idu_ped'


class IduPedido(models.Model):
    idu_pedido = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idu_pedido'


class IduPedidos(models.Model):
    idu_pedido = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idu_pedidos'


class Idupedido(models.Model):
    folio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idupedido'


class Idvaloratributo(models.Model):
    nom_listavalor = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idvaloratributo'


class Iexistenciabodega(models.Model):
    num_existencia = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iexistenciabodega'


class Iexistenciaminima(models.Model):
    num_existenciaminima = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iexistenciaminima'


class Iexistenciaminimaexclusivoscoppel(models.Model):
    num_existenciaminima = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iexistenciaminimaexclusivoscoppel'


class Iexistenciaminimaropa(models.Model):
    num_existenciaminimacommerce = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iexistenciaminimaropa'


class Ifactura(models.Model):
    num_foliomuebles = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifactura'


class Ifacturado(models.Model):
    case = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifacturado'
# Unable to inspect table 'iflagredimir'
# The error was: permission denied for table iflagredimir


class Ifoliomp(models.Model):
    num_foliomp = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifoliomp'


class Igtin(models.Model):
    idu_atributo = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'igtin'


class IiduCategoria(models.Model):
    idu_categoria = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iidu_categoria'


class Iidupedido(models.Model):
    idu_pedido = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iidupedido'


class Iiduproducto(models.Model):
    idu_producto = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iiduproducto'


class Iimage1(models.Model):
    idu_atributo = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iimage1'


class Iiscreditocoppel(models.Model):
    escreditocoppel = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iiscreditocoppel'
# Unable to inspect table 'index_bload_dbmantto'
# The error was: permission denied for table index_bload_dbmantto
# Unable to inspect table 'index_bload_dbmantto_reindex'
# The error was: permission denied for table index_bload_dbmantto_reindex


class Inotascompletas(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inotascompletas'


class Inotasconatraso(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inotasconatraso'


class Inotaspreparadasdia(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inotaspreparadasdia'


class Inotaspreparadashistorial(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inotaspreparadashistorial'


class Intentoscorreo(models.Model):
    numerointentos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intentoscorreo'


class Inumbodega(models.Model):
    idu_bodega = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inumbodega'


class Inumexistenciaminima(models.Model):
    num_existenciaminima = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inumexistenciaminima'


class Inumorden(models.Model):
    num_folio = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inumorden'


class Inumtienda(models.Model):
    idu_tienda = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inumtienda'


class Ipedido(models.Model):
    idu_pedido = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ipedido'


class Iproductname(models.Model):
    idu_atributo = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iproductname'


class Isaldode(models.Model):
    saldo_dineroe = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'isaldode'


class Ishortdescription(models.Model):
    idu_atributo = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ishortdescription'


class Itasainteres(models.Model):
    tasainteres = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itasainteres'


class Itasainteresropa(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    tasainteres = models.SmallIntegerField(blank=True, null=True)
    tasainteresriesgo = models.SmallIntegerField(blank=True, null=True)
    num_tasainteres18riesgo = models.SmallIntegerField(blank=True, null=True)
    num_tasainteres24 = models.SmallIntegerField(blank=True, null=True)
    num_tasainteres24riesgo = models.SmallIntegerField(blank=True, null=True)
    num_tasainteres18 = models.SmallIntegerField(blank=True, null=True)
    num_tasainteresmarketplace = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itasainteresropa'


class Itotal(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itotal'


class Itotalareamuebles(models.Model):
    sum = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itotalareamuebles'


class Itotalarearopa(models.Model):
    sum = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itotalarearopa'


class Itotalarticulossingle(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itotalarticulossingle'


class Itotaldescuentoropa(models.Model):
    sum = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itotaldescuentoropa'


class Itotaldiaatraso3(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itotaldiaatraso3'


class Itotalletrasllenas(models.Model):
    sum = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itotalletrasllenas'


class Itotalmov(models.Model):
    sum = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itotalmov'


class Itotalnotas(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itotalnotas'


class Itotalnotasdiasingle(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itotalnotasdiasingle'


class Itotalnotasentregadas(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itotalnotasentregadas'


class Itotalnotaspendientesenvio(models.Model):
    num_guia = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itotalnotaspendientesenvio'


class Itotalnotaspendientesrecoleccion(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itotalnotaspendientesrecoleccion'


class Itotalpedidos(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itotalpedidos'


class Itotalregistros(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itotalregistros'


class Iultimaletrallena(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iultimaletrallena'


class Izona(models.Model):
    num_zona = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'izona'


class Lcompras(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lcompras'


class Lctarjetas(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lctarjetas'


class Lnodoemail(models.Model):
    num_nodo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lnodoemail'


class LogProcapartado(models.Model):
    id = models.AutoField()
    operacion = models.TextField(blank=True, null=True)
    folio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_procapartado'


class LogVenta(models.Model):
    id = models.AutoField()
    tipo_operacion = models.IntegerField(blank=True, null=True)
    flag_exito = models.IntegerField(blank=True, null=True)
    comentarios = models.CharField(max_length=-1, blank=True, null=True)
    folio = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_venta'


class MaeArticulosconfirmados(models.Model):
    num_empleado = models.IntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.SmallIntegerField()
    num_area = models.SmallIntegerField()
    nom_articulo = models.CharField(max_length=120)
    num_cantidad = models.IntegerField()
    num_preciocompra = models.IntegerField()
    num_precioetiqueta = models.IntegerField()
    num_condicion = models.SmallIntegerField()
    fec_registro = models.DateTimeField()
    fec_confirmacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mae_articulosconfirmados'


class MaeClientescarterasecommerce(models.Model):
    num_cliente = models.BigIntegerField(blank=True, null=True)
    num_telefonocasa = models.BigIntegerField(blank=True, null=True)
    num_telefonocelular = models.BigIntegerField(blank=True, null=True)
    des_estatustelefonocasa = models.CharField(max_length=2, blank=True, null=True)
    des_estatustelefonocelular = models.CharField(max_length=2, blank=True, null=True)
    flg_flagclienteactivo = models.SmallIntegerField(blank=True, null=True)
    fec_fechaultimoabono = models.DateField(blank=True, null=True)
    fec_fechaaltacartera = models.DateField(blank=True, null=True)
    des_sexo = models.CharField(max_length=1, blank=True, null=True)
    des_complemento = models.CharField(max_length=30, blank=True, null=True)
    num_altatienda = models.IntegerField(blank=True, null=True)
    fec_fecha = models.DateField(blank=True, null=True)
    fec_nacimiento = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mae_clientescarterasecommerce'


class MaeConfiguracion(models.Model):
    idu_configuracion = models.IntegerField(primary_key=True)
    imp_minimoempleado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mae_configuracion'


class MaeCorreos(models.Model):
    numerocliente = models.IntegerField(blank=True, null=True)
    correoelectronico = models.CharField(max_length=50, blank=True, null=True)
    fechaaltamail = models.DateTimeField(blank=True, null=True)
    valido = models.SmallIntegerField(blank=True, null=True)
    fechadeconfirmacion = models.DateTimeField(blank=True, null=True)
    fechadecancelacion = models.DateTimeField(blank=True, null=True)
    tienda = models.SmallIntegerField(blank=True, null=True)
    claveorigen = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mae_correos'


class MaeEtiquetasmasterconfirmadas(models.Model):
    idu_etiquetamaster = models.BigAutoField()
    num_etiquetamaster = models.CharField(max_length=21, blank=True, null=True)
    num_empleado = models.IntegerField(blank=True, null=True)
    fec_confirmacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mae_etiquetasmasterconfirmadas'


class MaeExistencias(models.Model):
    numarea = models.OneToOneField(CatTallasarticulos, models.DO_NOTHING, db_column='numarea', primary_key=True)
    numbodega = models.SmallIntegerField()
    numcodigo = models.IntegerField()
    numtalla = models.SmallIntegerField()
    precioventa = models.IntegerField()
    disponible = models.IntegerField()
    tipoarticulo = models.SmallIntegerField()
    preciocredito = models.IntegerField()
    preciofrontera = models.IntegerField()
    num_existencia = models.SmallIntegerField()
    agotado = models.CharField(max_length=1)
    opc_disponiblenacionalecommerce = models.SmallIntegerField()
    opc_modificado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mae_existencias'
        unique_together = (('numarea', 'numbodega', 'numcodigo', 'numtalla'),)


class MaeExistenciasBodegaArg(models.Model):
    num_area = models.SmallIntegerField(primary_key=True)
    num_codigo = models.IntegerField()
    num_talla = models.SmallIntegerField()
    num_bodega = models.IntegerField()
    imp_precioventa = models.IntegerField()
    num_disponible = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mae_existencias_bodega_arg'
        unique_together = (('num_area', 'num_codigo', 'num_talla', 'num_bodega'),)


class MaeExistenciasTiendaArg(models.Model):
    num_area = models.SmallIntegerField(primary_key=True)
    num_codigo = models.IntegerField()
    num_talla = models.SmallIntegerField()
    num_tienda = models.SmallIntegerField()
    num_existencia = models.SmallIntegerField()
    num_stock = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mae_existencias_tienda_arg'
        unique_together = (('num_area', 'num_codigo', 'num_talla', 'num_tienda'),)


class MaeExistenciastienda(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    numtienda = models.SmallIntegerField()
    numcodigo = models.IntegerField()
    numtalla = models.SmallIntegerField()
    disponible = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mae_existenciastienda'
        unique_together = (('numarea', 'numcodigo', 'numtalla', 'numtienda'),)


class MaeInventariosoe(models.Model):
    id_serial = models.BigAutoField()
    num_area = models.SmallIntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.SmallIntegerField()
    num_cantidad = models.SmallIntegerField()
    num_precio = models.SmallIntegerField()
    fecha_entrada = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mae_inventariosoe'


class MaeInvespecial(models.Model):
    num_empleado = models.IntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.SmallIntegerField()
    num_area = models.SmallIntegerField()
    nom_articulo = models.CharField(max_length=120)
    num_cantidad = models.IntegerField()
    num_preciocompra = models.IntegerField()
    num_precioetiqueta = models.IntegerField()
    num_condicion = models.IntegerField()
    num_resolucion = models.IntegerField()
    fec_registro = models.DateTimeField()
    nom_url = models.CharField(max_length=-1, blank=True, null=True)
    num_bodega = models.IntegerField(blank=True, null=True)
    flag_confirmado = models.SmallIntegerField(blank=True, null=True)
    id_serial = models.BigIntegerField(blank=True, null=True)
    idu_proceso = models.SmallIntegerField()
    keyx = models.BigAutoField()
    num_notafactura = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mae_invespecial'


class MaePlanestarifariosdetalle(models.Model):
    num_area = models.IntegerField()
    num_depto = models.IntegerField()
    num_clase = models.IntegerField()
    num_familia = models.IntegerField()
    num_telefonica = models.IntegerField()
    num_skuplan = models.IntegerField()
    num_skutelefono = models.IntegerField()
    imp_preciointerior = models.IntegerField()
    imp_preciofrontera = models.IntegerField()
    imp_pagomensual = models.IntegerField()
    imp_rentainterior = models.IntegerField()
    imp_rentafrontera = models.IntegerField()
    fec_vigenciainicial = models.DateField()
    fec_vigenciafinal = models.DateField()
    imp_deposito = models.IntegerField()
    imp_diferenciaporequipo = models.IntegerField()
    nom_marcasku = models.CharField(max_length=40)
    nom_modelobase = models.CharField(max_length=40)
    imp_comision = models.IntegerField()
    opc_flagagotarexistencia = models.IntegerField()
    idu_claveplan = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'mae_planestarifariosdetalle'


class MaePlanestarifariosgeneral(models.Model):
    num_area = models.IntegerField()
    num_depto = models.IntegerField()
    num_clase = models.IntegerField()
    num_familia = models.IntegerField()
    num_telefonica = models.IntegerField()
    num_skuplan = models.IntegerField()
    nom_articulo = models.CharField(max_length=10)
    nom_marca = models.CharField(max_length=10)
    nom_modelo = models.CharField(max_length=20)
    num_plazos = models.SmallIntegerField()
    idu_claveplan = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'mae_planestarifariosgeneral'
# Unable to inspect table 'mae_productospublicados_feedmkp'
# The error was: permission denied for table mae_productospublicados_feedmkp


class MaetelefonosRes(models.Model):
    numerocliente = models.IntegerField(blank=True, null=True)
    tipotelefono = models.SmallIntegerField(blank=True, null=True)
    numerotelefono = models.BigIntegerField(blank=True, null=True)
    numeroextension = models.IntegerField(blank=True, null=True)
    contacto = models.CharField(max_length=1, blank=True, null=True)
    tipored = models.CharField(max_length=1, blank=True, null=True)
    carrier = models.SmallIntegerField(blank=True, null=True)
    fecharegistrotelefonoorigen = models.DateTimeField(blank=True, null=True)
    areacapturatelefonoorigen = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maetelefonos_res'


class MonitorBitacora(models.Model):
    log_id = models.AutoField(primary_key=True)
    server_id = models.IntegerField()
    type = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    user_id = models.CharField(max_length=255)
    tipo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monitor_bitacora'


class MonitorConfig(models.Model):
    llave = models.CharField(primary_key=True, max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'monitor_config'


class MonitorServidores(models.Model):
    server_id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50)
    estatus = models.CharField(max_length=3)
    ultima_online = models.DateTimeField(blank=True, null=True)
    ultima_revision = models.DateTimeField(blank=True, null=True)
    activo = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    sms = models.CharField(max_length=50)
    error = models.IntegerField()
    ambiente = models.IntegerField()
    xml = models.TextField(blank=True, null=True)
    nombre_funcion = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monitor_servidores'


class MonitorTrazabilidad(models.Model):
    trazabilidad_id = models.AutoField(primary_key=True)
    server_id = models.IntegerField()
    key = models.IntegerField()
    boss = models.IntegerField()
    nombre = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    objeto = models.CharField(max_length=255)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monitor_trazabilidad'


class MovApalineaapartadociudad(models.Model):
    ciudadnum = models.SmallIntegerField(blank=True, null=True)
    local = models.SmallIntegerField(blank=True, null=True)
    orden = models.SmallIntegerField(blank=True, null=True)
    dias = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_apalineaapartadociudad'


class MovArticulos(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    numdepto = models.SmallIntegerField()
    numclase = models.SmallIntegerField()
    numfamilia = models.SmallIntegerField()
    numcodigo = models.IntegerField()
    modelo = models.CharField(max_length=35)
    nummarca = models.SmallIntegerField()
    nomarticulo = models.CharField(max_length=120)
    descarticulo = models.TextField()
    fechaalta = models.DateTimeField()
    preciovntaint = models.IntegerField()
    preciovntafrontera = models.IntegerField()
    exclusivo = models.SmallIntegerField()
    publicar = models.SmallIntegerField()
    nuevo = models.SmallIntegerField()
    descmarca = models.CharField(max_length=30, blank=True, null=True)
    disponibilidad = models.CharField(max_length=1)
    comprar = models.SmallIntegerField()
    entrada = models.SmallIntegerField()
    tipoarticulo = models.SmallIntegerField()
    nomarticuloweb = models.CharField(max_length=120)
    region = models.CharField(max_length=-1, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    colordetalle = models.IntegerField(blank=True, null=True)
    opc_descontinuado = models.SmallIntegerField()
    modoentrega = models.CharField(max_length=1)
    nacoimp = models.CharField(max_length=1)
    clv_novtaporr = models.SmallIntegerField()
    num_diasespera = models.IntegerField()
    reutilizado = models.SmallIntegerField()
    num_garantiaenmeses = models.SmallIntegerField()
    num_seccion = models.SmallIntegerField()
    flag_manejaiva = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mov_articulos'
        unique_together = (('numarea', 'numcodigo'),)


class MovBajagaleriaarticulo(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    nomimagen = models.CharField(max_length=30, blank=True, null=True)
    numgaleria = models.BigIntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    fechaactualiza = models.DateField()

    class Meta:
        managed = False
        db_table = 'mov_bajagaleriaarticulo'


class MovBalanceoe(models.Model):
    num_folioropa = models.IntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.IntegerField()
    num_necesidad = models.IntegerField()
    num_cedisorigen = models.IntegerField()
    num_cedisdestino = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mov_balanceoe'


class MovBpguiasurtido(models.Model):
    numbodega = models.SmallIntegerField()
    clavemov = models.CharField(max_length=2)
    numlote = models.SmallIntegerField()
    numlector = models.SmallIntegerField()
    numsurtidor = models.SmallIntegerField()
    numtienda = models.SmallIntegerField()
    fechacreacion = models.DateField()
    numcodigo = models.IntegerField()
    numtalla = models.SmallIntegerField()
    mesetiqueta = models.SmallIntegerField()
    cantidad = models.SmallIntegerField()
    numseccion = models.SmallIntegerField()
    nomguia = models.CharField(max_length=20)
    fechaactualiza = models.DateField()
    consecutivo = models.SmallIntegerField()
    precio = models.SmallIntegerField()
    numdepto = models.SmallIntegerField()
    numclase = models.SmallIntegerField()
    numfamilia = models.SmallIntegerField()
    numcentro = models.IntegerField()
    preciomaximo = models.SmallIntegerField()
    marca = models.CharField(max_length=50)
    esimportacion = models.CharField(max_length=1)
    areacodigo = models.CharField(max_length=1)
    esdescontinuado = models.SmallIntegerField()
    numcodigodes = models.IntegerField()
    keyx = models.AutoField()
    numtipoiva = models.SmallIntegerField()
    rebajado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mov_bpguiasurtido'


class MovCarrito(models.Model):
    idsession = models.CharField(max_length=50, blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    numarea = models.SmallIntegerField(blank=True, null=True)
    cantidad = models.SmallIntegerField(blank=True, null=True)
    talla = models.CharField(max_length=10, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    id = models.AutoField()
    flag_sesion = models.CharField(max_length=64, blank=True, null=True)
    disponibilidadarticulo = models.IntegerField(blank=True, null=True)
    fechaentregaarticulo = models.DateField(blank=True, null=True)
    armararticulo = models.IntegerField(blank=True, null=True)
    preciocontadounitario = models.IntegerField(blank=True, null=True)
    articulonuevo = models.IntegerField(blank=True, null=True)
    preciopromocion = models.IntegerField(blank=True, null=True)
    disponibilidadmuebles = models.IntegerField(blank=True, null=True)
    fechaentregamuebles = models.DateField(blank=True, null=True)
    preciocreditounitario = models.IntegerField(blank=True, null=True)
    flag_armado = models.IntegerField(blank=True, null=True)
    preciooriginal = models.IntegerField(blank=True, null=True)
    folio = models.IntegerField(blank=True, null=True)
    idu_carrito = models.BigIntegerField(blank=True, null=True)
    num_foliotelcel = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mov_carrito'
        unique_together = (('folio', 'numcodigo', 'numarea', 'talla'),)


class MovCarritoentregadetalle(models.Model):
    folio = models.IntegerField()
    numcodigo = models.IntegerField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    bodega = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_carritoentregadetalle'


class MovCedisenvios(models.Model):
    num_cedisregional = models.SmallIntegerField(primary_key=True)
    nom_cedisregional = models.CharField(max_length=25)
    nom_ipregional = models.CharField(max_length=20)
    clv_tipocedis = models.SmallIntegerField()
    nom_tipocedis = models.CharField(max_length=20)
    num_cedissoporte = models.SmallIntegerField()
    nom_cedissoporte = models.CharField(max_length=25)
    nom_ipsoporte = models.CharField(max_length=20)
    clv_predeterminado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mov_cedisenvios'


class MovCenciudades(models.Model):
    idu_ciudad = models.SmallIntegerField()
    nom_abreviatura = models.CharField(max_length=4)
    nom_largociudad = models.CharField(max_length=30)
    num_bodega = models.IntegerField()
    des_regioncelular = models.CharField(max_length=3)
    imp_tasainteres = models.SmallIntegerField()
    imp_tasaiva = models.SmallIntegerField()
    des_servidor = models.CharField(max_length=15)
    cvl_local = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'mov_cenciudades'


class MovClases(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    numdepto = models.SmallIntegerField()
    numclase = models.SmallIntegerField()
    descclase = models.CharField(max_length=50)
    activo = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mov_clases'
        unique_together = (('numarea', 'numdepto', 'numclase'),)


class MovClientes(models.Model):
    numusuario = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    apellidopaterno = models.CharField(max_length=50, blank=True, null=True)
    apellidomaterno = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=10, blank=True, null=True)
    ciudad = models.CharField(max_length=20, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    pais = models.CharField(max_length=20, blank=True, null=True)
    calle = models.CharField(max_length=50, blank=True, null=True)
    colonia = models.CharField(max_length=50, blank=True, null=True)
    numcasa = models.CharField(max_length=12, blank=True, null=True)
    clientecoppel = models.CharField(max_length=2, blank=True, null=True)
    numclientecoppel = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    ext = models.CharField(max_length=20, blank=True, null=True)
    cp = models.CharField(max_length=5, blank=True, null=True)
    saldo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    otra = models.CharField(max_length=5, blank=True, null=True)
    registro = models.CharField(max_length=1, blank=True, null=True)
    correovalido = models.IntegerField(blank=True, null=True)
    confirmado = models.CharField(max_length=1, blank=True, null=True)
    interior = models.CharField(max_length=12, blank=True, null=True)
    numciudad = models.IntegerField(blank=True, null=True)
    numcolonia = models.IntegerField(blank=True, null=True)
    numcalle = models.IntegerField(blank=True, null=True)
    fechanacimiento = models.CharField(max_length=50, blank=True, null=True)
    fecharegistro = models.CharField(max_length=50, blank=True, null=True)
    celular = models.CharField(max_length=128, blank=True, null=True)
    entrecalles = models.CharField(max_length=-1, blank=True, null=True)
    domicilioobservaciones = models.CharField(max_length=-1, blank=True, null=True)
    idserial = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_clientes'


class MovClientesMigrados(models.Model):
    email = models.TextField(blank=True, null=True)
    numcliente = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_clientes_migrados'


class MovCodigoscelularesregion(models.Model):
    num_area = models.SmallIntegerField()
    num_codigo = models.IntegerField()
    des_region = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'mov_codigoscelularesregion'


class MovCodigosregionestelcel(models.Model):
    num_codigogeneral = models.CharField(max_length=-1)
    num_codigoregion = models.IntegerField()
    num_regiontelcel = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'mov_codigosregionestelcel'


class MovColores(models.Model):
    numcolor = models.SmallIntegerField(primary_key=True)
    desccolor = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'mov_colores'


class MovComentariosarticulos(models.Model):
    numarea = models.SmallIntegerField()
    numcodigo = models.IntegerField()
    nomcomentario = models.CharField(max_length=30)
    desccomentario = models.TextField()
    numcliente = models.IntegerField()
    correo = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    activo = models.BooleanField()
    idcomentario = models.AutoField()

    class Meta:
        managed = False
        db_table = 'mov_comentariosarticulos'


class MovConfigCedisropa(models.Model):
    num_cedis = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_config_cedisropa'


class MovConfiguracionesCobroenvio(models.Model):
    id_configuracion = models.ForeignKey(CatAccionesCobroenvio, models.DO_NOTHING, db_column='id_configuracion')
    entrada = models.TextField()
    salida = models.TextField()
    usuario = models.CharField(max_length=20)
    fecha_modificacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mov_configuraciones_cobroenvio'


class MovConfiguracionpasillos(models.Model):
    idu_configuracion = models.AutoField()
    num_pasillo = models.SmallIntegerField()
    num_letras = models.SmallIntegerField()
    num_bodega = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mov_configuracionpasillos'


class MovDeltasAttrdictionary(models.Model):
    identifier = models.CharField(primary_key=True, max_length=120)
    type = models.CharField(max_length=120)
    attributetype = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    description = models.TextField()
    sequence = models.IntegerField()
    displayable = models.CharField(max_length=120)
    searchable = models.BooleanField()
    comparable = models.BooleanField()
    storedisplay = models.SmallIntegerField()
    merchandisable = models.BooleanField()
    facetable = models.BooleanField()
    allowmultiplefacetvalueselection = models.BooleanField(blank=True, null=True)
    facetvalueordering = models.BooleanField(blank=True, null=True)
    includeinsearchresults = models.BooleanField(blank=True, null=True)
    showemptyfacetvalues = models.BooleanField(blank=True, null=True)
    maximumvaluestodisplay = models.SmallIntegerField()
    allowedvalues = models.TextField()
    allowedvalue1 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue2 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue3 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue4 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue5 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue6 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue7 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue8 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue9 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue10 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue11 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue12 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue13 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue14 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue15 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue16 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue17 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue18 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue19 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue20 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue21 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue22 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue23 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue24 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue25 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue26 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue27 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue28 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue29 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue30 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue31 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue32 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue33 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue34 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue35 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue36 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue37 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue38 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue39 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue40 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue41 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue42 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue43 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue44 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue45 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue46 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue47 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue48 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue49 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue50 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue51 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue52 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue53 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue54 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue55 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue56 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue57 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue58 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue59 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue60 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue61 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue62 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue63 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue64 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue65 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue66 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue67 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue68 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue69 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue70 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue71 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue72 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue73 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue74 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue75 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue76 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue77 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue78 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue79 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue80 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue81 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue82 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue83 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue84 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue85 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue86 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue87 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue88 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue89 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue90 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue91 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue92 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue93 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue94 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue95 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue96 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue97 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue98 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue99 = models.CharField(max_length=255, blank=True, null=True)
    allowedvalue100 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier1 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier2 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier3 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier4 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier5 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier6 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier7 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier8 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier9 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier10 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier11 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier12 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier13 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier14 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier15 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier16 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier17 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier18 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier19 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier20 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier21 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier22 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier23 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier24 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier25 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier26 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier27 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier28 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier29 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier30 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier31 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier32 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier33 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier34 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier35 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier36 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier37 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier38 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier39 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier40 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier41 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier42 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier43 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier44 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier45 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier46 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier47 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier48 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier49 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier50 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier51 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier52 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier53 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier54 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier55 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier56 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier57 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier58 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier59 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier60 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier61 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier62 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier63 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier64 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier65 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier66 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier67 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier68 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier69 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier70 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier71 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier72 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier73 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier74 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier75 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier76 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier77 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier78 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier79 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier80 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier81 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier82 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier83 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier84 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier85 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier86 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier87 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier88 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier89 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier90 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier91 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier92 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier93 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier94 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier95 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier96 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier97 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier98 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier99 = models.CharField(max_length=255, blank=True, null=True)
    allowedidentifier100 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_deltas_attrdictionary'


class MovDeltasAttrmap(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=64)
    attributeidentifier = models.CharField(max_length=254)
    valueidentifier = models.CharField(max_length=254)
    value = models.CharField(max_length=254)
    usage = models.CharField(max_length=64)
    sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mov_deltas_attrmap'
        unique_together = (('partnumber', 'attributeidentifier', 'valueidentifier', 'value'),)


class MovDeltasCategory(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    numareaweb = models.SmallIntegerField()
    groupidentifier = models.CharField(max_length=254)
    topgroup = models.BooleanField(blank=True, null=True)
    nivel = models.IntegerField()
    parentgroupidentifier = models.CharField(max_length=254, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=254)
    shortdescription = models.CharField(max_length=255, blank=True, null=True)
    longdescription = models.CharField(max_length=2048, blank=True, null=True)
    thumbnail = models.CharField(max_length=120, blank=True, null=True)
    fullimage = models.CharField(max_length=120, blank=True, null=True)
    published = models.IntegerField(blank=True, null=True)
    urlkeyword = models.CharField(max_length=254, blank=True, null=True)
    pagetitle = models.CharField(max_length=254, blank=True, null=True)
    keyword = models.CharField(max_length=254, blank=True, null=True)
    metadescription = models.CharField(max_length=254, blank=True, null=True)
    field1 = models.CharField(max_length=254, blank=True, null=True)
    field2 = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_deltas_category'
        unique_together = (('numarea', 'numareaweb'),)


class MovDeltasClassFamily(models.Model):
    numarea = models.SmallIntegerField()
    numareaweb = models.SmallIntegerField()
    code = models.CharField(max_length=264)
    nivel = models.SmallIntegerField()
    department = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    type = models.CharField(max_length=254)
    titulo = models.CharField(max_length=254, blank=True, null=True)
    metakeyword = models.CharField(max_length=254, blank=True, null=True)
    metadescription = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_deltas_class_family'


class MovDeltasCpStore(models.Model):
    store_code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'mov_deltas_cp_store'


class MovDeltasExclusivosCoppel(models.Model):
    numcodigo = models.IntegerField()
    numarea = models.SmallIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'mov_deltas_exclusivos_coppel'
        unique_together = (('numarea', 'numcodigo'),)


class MovDeltasFilter(models.Model):
    catalogfiltername = models.CharField(primary_key=True, max_length=100)
    storeidentifier = models.CharField(max_length=50)
    catalogidentifier = models.CharField(max_length=100)
    usage = models.CharField(max_length=15)
    spanishdescription = models.CharField(max_length=500)
    filtertype = models.IntegerField()
    storecode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mov_deltas_filter'


class MovDeltasInventory(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=64)
    fullfillmentcentername = models.CharField(max_length=50)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mov_deltas_inventory'
        unique_together = (('partnumber', 'fullfillmentcentername'),)


class MovDeltasMercadoLibre(models.Model):
    sku = models.CharField(max_length=64)
    titulo = models.CharField(max_length=128, blank=True, null=True)
    garantia = models.SmallIntegerField(blank=True, null=True)
    precios = models.CharField(max_length=254, blank=True, null=True)
    stock = models.TextField(blank=True, null=True)
    descripcion_html = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.TextField(blank=True, null=True)
    atributo = models.TextField(blank=True, null=True)
    imagen = models.TextField(blank=True, null=True)
    variantes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_deltas_mercado_libre'


class MovDeltasMercadoLibreCambiosetl(models.Model):
    sku = models.CharField(max_length=64, blank=True, null=True)
    titulo = models.CharField(max_length=128, blank=True, null=True)
    garantia = models.SmallIntegerField(blank=True, null=True)
    precios = models.CharField(max_length=254, blank=True, null=True)
    stock = models.TextField(blank=True, null=True)
    descripcion_html = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.TextField(blank=True, null=True)
    atributo = models.TextField(blank=True, null=True)
    imagen = models.TextField(blank=True, null=True)
    variantes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_deltas_mercado_libre_cambiosetl'


class MovDeltasMercadoLibreEtl(models.Model):
    sku = models.CharField(max_length=64, blank=True, null=True)
    titulo = models.CharField(max_length=128, blank=True, null=True)
    garantia = models.SmallIntegerField(blank=True, null=True)
    precios = models.CharField(max_length=254, blank=True, null=True)
    stock = models.TextField(blank=True, null=True)
    descripcion_html = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.TextField(blank=True, null=True)
    atributo = models.TextField(blank=True, null=True)
    imagen = models.TextField(blank=True, null=True)
    variantes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_deltas_mercado_libre_etl'


class MovDeltasOfferPrice(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=64)
    price = models.IntegerField()
    currencycode = models.CharField(max_length=16)
    startdate = models.DateField()
    enddate = models.DateField()
    field1 = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'mov_deltas_offer_price'


class MovDeltasPriceList(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=64)
    listprice = models.IntegerField()
    currencycode = models.CharField(max_length=16)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mov_deltas_price_list'


class MovDeltasProdCat(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=64)
    parentgroupidentifier = models.CharField(max_length=64, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_deltas_prod_cat'


class MovDeltasProductfilter(models.Model):
    catalogfilterid = models.CharField(max_length=100)
    catalogfiltername = models.CharField(primary_key=True, max_length=100)
    storeidentifier = models.CharField(max_length=30)
    catalogidentifier = models.CharField(max_length=100)
    selectiontype = models.CharField(max_length=10)
    partnumber = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'mov_deltas_productfilter'
        unique_together = (('catalogfiltername', 'storeidentifier', 'partnumber'),)


class MovDeltasProductfilterRespa(models.Model):
    catalogfilterid = models.CharField(max_length=100, blank=True, null=True)
    catalogfiltername = models.CharField(max_length=100, blank=True, null=True)
    storeidentifier = models.CharField(max_length=30, blank=True, null=True)
    catalogidentifier = models.CharField(max_length=100, blank=True, null=True)
    selectiontype = models.CharField(max_length=10, blank=True, null=True)
    partnumber = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_deltas_productfilter_respa'


class MovDeltasProducts(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=64)
    numarea = models.SmallIntegerField()
    numdepto = models.SmallIntegerField(blank=True, null=True)
    numclase = models.SmallIntegerField(blank=True, null=True)
    numfamilia = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField()
    numtalla = models.SmallIntegerField(blank=True, null=True)
    type = models.CharField(max_length=16, blank=True, null=True)
    isproduct = models.BooleanField(blank=True, null=True)
    parentpartnumber = models.CharField(max_length=64, blank=True, null=True)
    category = models.CharField(max_length=264, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    shortdescription = models.CharField(max_length=255, blank=True, null=True)
    longdescription = models.TextField(blank=True, null=True)
    keyword = models.CharField(max_length=254, blank=True, null=True)
    marca = models.CharField(max_length=120, blank=True, null=True)
    thumbnail = models.CharField(max_length=120, blank=True, null=True)
    fullimage = models.CharField(max_length=120, blank=True, null=True)
    sequence = models.CharField(max_length=5, blank=True, null=True)
    language_id = models.CharField(max_length=5, blank=True, null=True)
    available = models.IntegerField(blank=True, null=True)
    published = models.IntegerField(blank=True, null=True)
    buyable = models.IntegerField(blank=True, null=True)
    availabilitydate_localspecific = models.DateTimeField(blank=True, null=True)
    promotion_price_currency = models.CharField(max_length=25, blank=True, null=True)
    contado_price = models.IntegerField(blank=True, null=True)
    credito_price = models.IntegerField(blank=True, null=True)
    promotion_price = models.CharField(max_length=10, blank=True, null=True)
    flag_price = models.CharField(max_length=10, blank=True, null=True)
    fechainicialpromo = models.DateField(blank=True, null=True)
    fechafinalpromo = models.DateField(blank=True, null=True)
    field1 = models.CharField(max_length=264, blank=True, null=True)
    field2 = models.CharField(max_length=264, blank=True, null=True)
    manufacturer = models.CharField(max_length=254, blank=True, null=True)
    region_telcel = models.CharField(max_length=264, blank=True, null=True)
    dcf = models.CharField(max_length=25, blank=True, null=True)
    nivel = models.SmallIntegerField(blank=True, null=True)
    flag_cambio_category = models.BooleanField(blank=True, null=True)
    delete_value = models.CharField(max_length=25, blank=True, null=True)
    urlkeyword = models.CharField(max_length=250)
    pagetitle = models.CharField(max_length=150)
    metadescription = models.CharField(max_length=250, blank=True, null=True)
    gtin = models.CharField(max_length=14, blank=True, null=True)
    modelo = models.CharField(max_length=35)
    color = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'mov_deltas_products'
        unique_together = (('partnumber', 'numarea', 'numcodigo'),)


class MovDeltasmarketplaceAttrdictionary(models.Model):
    idu_atributomarketplace = models.BigIntegerField(primary_key=True)
    identifier = models.CharField(max_length=120)
    type = models.CharField(max_length=120)
    attributetype = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    description = models.TextField()
    sequence = models.IntegerField()
    displayable = models.BooleanField()
    searchable = models.BooleanField()
    comparable = models.BooleanField()
    storedisplay = models.SmallIntegerField()
    merchandisable = models.BooleanField()
    facetable = models.BooleanField()
    allowmultiplefacetvalueselection = models.BooleanField(blank=True, null=True)
    facetvalueordering = models.BooleanField()
    includeinsearchresults = models.BooleanField()
    showemptyfacetvalues = models.BooleanField()
    maximumvaluestodisplay = models.SmallIntegerField()
    delete = models.SmallIntegerField()
    opc_nuevo = models.BooleanField()
    idu_carga = models.ForeignKey(CtlCargasMarketplace, models.DO_NOTHING, db_column='idu_carga')

    class Meta:
        managed = False
        db_table = 'mov_deltasmarketplace_attrdictionary'
        unique_together = (('idu_atributomarketplace', 'identifier', 'delete'), ('idu_atributomarketplace', 'delete'),)


class MovDeltasmarketplaceAttrdictionaryAllowedData(models.Model):
    idu_valoratributo = models.BigIntegerField()
    identifier = models.CharField(primary_key=True, max_length=120)
    valueidentifier = models.TextField()
    value = models.TextField(blank=True, null=True)
    sequence = models.IntegerField()
    languageid = models.SmallIntegerField()
    delete = models.SmallIntegerField()
    idu_carga = models.ForeignKey(CtlCargasMarketplace, models.DO_NOTHING, db_column='idu_carga')

    class Meta:
        managed = False
        db_table = 'mov_deltasmarketplace_attrdictionary_allowed_data'
        unique_together = (('identifier', 'valueidentifier'),)


class MovDeltasmarketplaceAttrmap(models.Model):
    idu_atributomarketplace = models.BigIntegerField()
    partnumber = models.CharField(primary_key=True, max_length=64)
    attributeidentifier = models.CharField(max_length=254)
    valueidentifier = models.CharField(max_length=254)
    value = models.CharField(max_length=254)
    usage = models.CharField(max_length=64)
    sequence = models.IntegerField()
    delete = models.IntegerField()
    idu_carga = models.ForeignKey(CtlCargasMarketplace, models.DO_NOTHING, db_column='idu_carga')

    class Meta:
        managed = False
        db_table = 'mov_deltasmarketplace_attrmap'
        unique_together = (('partnumber', 'attributeidentifier', 'valueidentifier', 'value', 'delete'),)


class MovDeltasmarketplaceCategorias(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    numareaweb = models.SmallIntegerField()
    opc_nivel = models.SmallIntegerField()
    groupidentifier = models.CharField(max_length=254)
    topgroup = models.BooleanField()
    parentgroupidentifier = models.CharField(max_length=254)
    sequence = models.IntegerField()
    name = models.CharField(max_length=254)
    shortdescription = models.CharField(max_length=254)
    longdescription = models.CharField(max_length=2048)
    thumbnail = models.CharField(max_length=120)
    fullimage = models.CharField(max_length=120)
    published = models.IntegerField()
    urlkeyword = models.CharField(max_length=254)
    pagetitle = models.CharField(max_length=254)
    keyword = models.CharField(max_length=254)
    metadescription = models.CharField(max_length=254)
    delete = models.CharField(max_length=1)
    field1 = models.CharField(max_length=254)
    field2 = models.CharField(max_length=254)
    idu_carga = models.ForeignKey(CtlCargasMarketplace, models.DO_NOTHING, db_column='idu_carga')

    class Meta:
        managed = False
        db_table = 'mov_deltasmarketplace_categorias'
        unique_together = (('numarea', 'numareaweb'),)


class MovDeltasmarketplaceCategoriasventa(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    numareaweb = models.SmallIntegerField()
    opc_nivel = models.SmallIntegerField()
    groupidentifier = models.CharField(max_length=254)
    topgroup = models.BooleanField()
    parentgroupidentifier = models.CharField(max_length=254)
    sequence = models.IntegerField()
    name = models.CharField(max_length=254)
    shortdescription = models.CharField(max_length=254)
    longdescription = models.CharField(max_length=2048)
    thumbnail = models.CharField(max_length=120)
    fullimage = models.CharField(max_length=120)
    published = models.IntegerField()
    urlkeyword = models.CharField(max_length=254)
    pagetitle = models.CharField(max_length=254)
    keyword = models.CharField(max_length=254)
    metadescription = models.CharField(max_length=254)
    delete = models.CharField(max_length=1)
    field1 = models.CharField(max_length=254)
    field2 = models.CharField(max_length=254)
    idu_carga = models.ForeignKey(CtlCargasMarketplace, models.DO_NOTHING, db_column='idu_carga')

    class Meta:
        managed = False
        db_table = 'mov_deltasmarketplace_categoriasventa'
        unique_together = (('numarea', 'numareaweb'),)


class MovDeltasmarketplaceInventory(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=64)
    fullfillmentcentername = models.CharField(max_length=50)
    quantity = models.IntegerField()
    delete = models.IntegerField()
    idu_carga = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mov_deltasmarketplace_inventory'
        unique_together = (('partnumber', 'fullfillmentcentername'),)


class MovDeltasmarketplaceItems(models.Model):
    idu_producto = models.BigIntegerField()
    partnumber = models.CharField(max_length=64)
    type = models.CharField(max_length=16)
    name = models.CharField(max_length=264)
    shortdescription = models.CharField(max_length=264)
    longdescription = models.CharField(max_length=4000)
    published = models.SmallIntegerField()
    keyword = models.CharField(max_length=264)
    delete = models.SmallIntegerField()
    manufacturer = models.CharField(max_length=64)
    buyable = models.IntegerField()
    mpn_vendedor = models.CharField(primary_key=True, max_length=64)
    idu_carga = models.ForeignKey(CtlCargasMarketplace, models.DO_NOTHING, db_column='idu_carga')

    class Meta:
        managed = False
        db_table = 'mov_deltasmarketplace_items'
# Unable to inspect table 'mov_deltasmarketplace_items_oferta_invalida'
# The error was: permission denied for table mov_deltasmarketplace_items_oferta_invalida


class MovDeltasmarketplaceOfferPrice(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=64)
    price = models.IntegerField()
    currencycode = models.CharField(max_length=16)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    field1 = models.CharField(max_length=20)
    sellerid = models.BigIntegerField()
    mpofferid = models.BigIntegerField()
    identifier = models.BigIntegerField()
    buyboxweight = models.FloatField()
    selleritemid = models.CharField(max_length=30)
    condition = models.CharField(max_length=10)
    conditiondesc = models.CharField(max_length=254)
    precedence = models.FloatField()
    delete = models.IntegerField()
    idu_carga = models.BigIntegerField()
    idu_producto = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mov_deltasmarketplace_offer_price'
        unique_together = (('partnumber', 'identifier', 'delete'),)


class MovDeltasmarketplacePriceList(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=64)
    listprice = models.IntegerField()
    currencycode = models.CharField(max_length=16)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    identifier = models.BigIntegerField()
    delete = models.IntegerField()
    idu_carga = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mov_deltasmarketplace_price_list'
        unique_together = (('partnumber', 'identifier', 'delete'),)


class MovDeltasmarketplaceProductos(models.Model):
    idu_producto = models.BigIntegerField(primary_key=True)
    partnumber = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    name = models.CharField(max_length=512)
    shortdescription = models.CharField(max_length=254)
    longdescription = models.CharField(max_length=4000)
    thumbnail = models.CharField(max_length=254)
    fullimage = models.CharField(max_length=254)
    published = models.SmallIntegerField()
    keyword = models.CharField(max_length=254)
    delete = models.SmallIntegerField()
    manufacturerpartnumber = models.CharField(max_length=64)
    manufacturer = models.CharField(max_length=64)
    url = models.CharField(max_length=254)
    field1 = models.IntegerField()
    field2 = models.IntegerField()
    field3 = models.FloatField()
    field4 = models.CharField(max_length=254)
    field5 = models.CharField(max_length=254)
    buyable = models.IntegerField()
    parentpartnumber = models.CharField(max_length=64)
    urlkeyword = models.CharField(max_length=254)
    metadescription = models.CharField(max_length=1024)
    pagetitle = models.CharField(max_length=254)
    idu_carga = models.ForeignKey(CtlCargasMarketplace, models.DO_NOTHING, db_column='idu_carga')

    class Meta:
        managed = False
        db_table = 'mov_deltasmarketplace_productos'
        unique_together = (('idu_producto', 'partnumber'),)


class MovDeltasmarketplacePromotions(models.Model):
    administrativename = models.CharField(primary_key=True, max_length=254)
    endtime = models.DateTimeField()
    admindescription = models.CharField(max_length=2048)
    percentage = models.SmallIntegerField()
    stardate = models.DateTimeField()
    opc_tipo = models.CharField(max_length=50)
    subtype = models.CharField(max_length=100)
    identifier = models.CharField(max_length=254)
    currency = models.CharField(max_length=50)
    shortdescription = models.CharField(max_length=2048)
    longdescription = models.CharField(max_length=2048)
    amountoff = models.SmallIntegerField()
    opc_estado = models.CharField(max_length=50)
    delete = models.SmallIntegerField()
    idu_carga = models.ForeignKey(CtlCargasMarketplace, models.DO_NOTHING, db_column='idu_carga')

    class Meta:
        managed = False
        db_table = 'mov_deltasmarketplace_promotions'


class MovDeltasmarketplaceRelacionproductocategoria(models.Model):
    idu_numareaweb = models.IntegerField()
    partnumber = models.CharField(primary_key=True, max_length=64)
    parentgroupidentifier = models.CharField(max_length=254)
    sequence = models.IntegerField()
    delete = models.SmallIntegerField()
    idu_carga = models.ForeignKey(CtlCargasMarketplace, models.DO_NOTHING, db_column='idu_carga')

    class Meta:
        managed = False
        db_table = 'mov_deltasmarketplace_relacionproductocategoria'
        unique_together = (('partnumber', 'parentgroupidentifier', 'delete'),)


class MovDeltasmarketplaceRelacionproductoitem(models.Model):
    partnumber = models.CharField(primary_key=True, max_length=64)
    parentpartnumber = models.CharField(max_length=254)
    idu_producto = models.BigIntegerField()
    des_valoratributomx = models.CharField(max_length=64)
    des_valoratributo = models.CharField(max_length=254)
    sequence = models.SmallIntegerField()
    delete = models.SmallIntegerField()
    idu_carga = models.ForeignKey(CtlCargasMarketplace, models.DO_NOTHING, db_column='idu_carga')

    class Meta:
        managed = False
        db_table = 'mov_deltasmarketplace_relacionproductoitem'
        unique_together = (('partnumber', 'parentpartnumber', 'sequence', 'delete', 'idu_carga'),)


class MovDeltasmarketplaceVendedores(models.Model):
    idu_seller = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=254)
    logo = models.CharField(max_length=254)
    registrydate = models.DateTimeField()
    description = models.CharField(max_length=2048)
    warrantypolicies = models.TextField()
    shippingpolicies = models.TextField()
    returnpolicies = models.TextField()
    premium = models.SmallIntegerField()
    status = models.CharField(max_length=1)
    field1 = models.CharField(max_length=254)
    field2 = models.CharField(max_length=254)
    field3 = models.CharField(max_length=254)
    delete = models.SmallIntegerField()
    idu_carga = models.ForeignKey(CtlCargasMarketplace, models.DO_NOTHING, db_column='idu_carga')

    class Meta:
        managed = False
        db_table = 'mov_deltasmarketplace_vendedores'


class MovDepartamentos(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    numdepto = models.SmallIntegerField()
    descdepto = models.CharField(unique=True, max_length=30)
    activo = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mov_departamentos'
        unique_together = (('numarea', 'numdepto'),)


class MovEntregasbodegas(models.Model):
    num_folio = models.IntegerField()
    fec_fechaservicio = models.DateField()
    num_codigo = models.IntegerField()
    num_cantidad = models.IntegerField()
    des_ultimomovimiento = models.CharField(max_length=100, blank=True, null=True)
    fec_liquidada = models.DateField()
    num_bodega = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mov_entregasbodegas'


class MovEstatuscodigos(models.Model):
    idu_registro = models.AutoField(primary_key=True)
    num_folio = models.BigIntegerField()
    idu_estatuscodigo = models.IntegerField()
    num_area = models.IntegerField()
    num_codigo = models.IntegerField()
    num_talla = models.IntegerField()
    num_cantidad = models.IntegerField()
    fec_movimiento = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mov_estatuscodigos'


class MovEstatuspedido(models.Model):
    idu_registroventa = models.AutoField(primary_key=True)
    num_folio = models.BigIntegerField()
    idu_estatuspedido = models.IntegerField()
    fec_movimiento = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mov_estatuspedido'


class MovEstatuspedidohistorial(models.Model):
    num_folio = models.BigIntegerField()
    idu_estatuspedido = models.IntegerField()
    num_empleado = models.IntegerField()
    fec_actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mov_estatuspedidohistorial'


class MovExistencias(models.Model):
    numarea = models.SmallIntegerField()
    numbodega = models.SmallIntegerField(primary_key=True)
    numcodigo = models.IntegerField()
    numtalla = models.SmallIntegerField()
    precioventa = models.IntegerField()
    disponible = models.IntegerField()
    tipoarticulo = models.SmallIntegerField()
    preciocredito = models.IntegerField()
    preciorebaja = models.IntegerField()
    preciofrontera = models.IntegerField()
    num_existencia = models.SmallIntegerField()
    agotado = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'mov_existencias'
        unique_together = (('numbodega', 'numarea', 'numcodigo', 'numtalla'),)


class MovExistenciastienda(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    numtienda = models.SmallIntegerField()
    numcodigo = models.IntegerField()
    numtalla = models.SmallIntegerField()
    disponible = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mov_existenciastienda'
        unique_together = (('numarea', 'numcodigo', 'numtalla', 'numtienda'),)


class MovFacturacion(models.Model):
    id = models.IntegerField(blank=True, null=True)
    rfc = models.CharField(max_length=-1, blank=True, null=True)
    razonsocial = models.CharField(max_length=-1, blank=True, null=True)
    ciudad = models.CharField(max_length=-1, blank=True, null=True)
    estado = models.CharField(max_length=-1, blank=True, null=True)
    colonia = models.CharField(max_length=-1, blank=True, null=True)
    calle = models.CharField(max_length=-1, blank=True, null=True)
    codigopostal = models.IntegerField(blank=True, null=True)
    referencia = models.CharField(max_length=-1, blank=True, null=True)
    cliente = models.CharField(max_length=-1, blank=True, null=True)
    numerocasa = models.IntegerField(blank=True, null=True)
    numerointerior = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_facturacion'


class MovFacturasafectadasVentar(models.Model):
    num_factura = models.BigIntegerField()
    num_estado = models.SmallIntegerField()
    num_tienda = models.IntegerField()
    fec_compra = models.DateField(blank=True, null=True)
    des_servidorlog = models.CharField(max_length=-1, blank=True, null=True)
    clv_facturademoto = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'mov_facturasafectadas_ventar'


class MovFamilias(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    numdepto = models.SmallIntegerField()
    numclase = models.SmallIntegerField()
    numfamilia = models.SmallIntegerField()
    descfamilia = models.CharField(max_length=50)
    activo = models.SmallIntegerField()
    flagriesgo = models.SmallIntegerField()
    plazos = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mov_familias'
        unique_together = (('numarea', 'numdepto', 'numclase', 'numfamilia'),)


class MovFamiliassindescuento(models.Model):
    dcf = models.IntegerField()
    dcfinicio = models.IntegerField(blank=True, null=True)
    dcffin = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    aplicanuevoudi = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_familiassindescuento'


class MovFoliosmp(models.Model):
    num_foliomp = models.BigIntegerField(blank=True, null=True)
    num_guia = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_foliosmp'


class MovHitsarticulos(models.Model):
    numarea = models.OneToOneField(CatArticulos, models.DO_NOTHING, db_column='numarea', primary_key=True)
    numcodigo = models.IntegerField()
    fecha = models.DateTimeField()
    hits = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mov_hitsarticulos'
        unique_together = (('numarea', 'numcodigo'),)


class MovLogApartadosinexistencia(models.Model):
    idu_registro = models.BigAutoField()
    fol_orden = models.BigIntegerField()
    num_codigo = models.BigIntegerField()
    num_area = models.SmallIntegerField()
    num_departamento = models.SmallIntegerField()
    num_clase = models.SmallIntegerField()
    num_familia = models.SmallIntegerField()
    nom_articulo = models.CharField(max_length=-1)
    num_preciolista = models.IntegerField()
    num_preciooferta = models.IntegerField()
    fec_movimiento = models.DateField()
    hor_movimiento = models.TimeField()
    num_cantidadsolicitada = models.SmallIntegerField()
    num_cantidaddisponible = models.SmallIntegerField()
    num_ciudadentrega = models.IntegerField()
    nom_tiendacommerce = models.CharField(max_length=-1)
    des_bodegasnodo = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'mov_log_apartadosinexistencia'


class MovLogCierre(models.Model):
    id = models.AutoField()
    operacion = models.IntegerField(blank=True, null=True)
    gndate = models.DateField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_log_cierre'


class MovLogTransaccionesTdavirtual(models.Model):
    idu_logproceso = models.BigIntegerField(primary_key=True)
    idu_transaccion = models.ForeignKey(CtlProcesosTdavirtual, models.DO_NOTHING, db_column='idu_transaccion')
    fec_proceso = models.DateField()
    hor_inicia = models.TimeField()
    hor_finaliza = models.TimeField()
    hor_intervalo = models.TimeField()
    opc_finaliza = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'mov_log_transacciones_tdavirtual'


class MovLogcambios(models.Model):
    numcodigo = models.IntegerField(blank=True, null=True)
    numempleado = models.BigIntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    numarea = models.SmallIntegerField()
    numtipocambio = models.SmallIntegerField()
    numcodigopivote = models.TextField(blank=True, null=True)
    codigosrelacionados = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_logcambios'


class MovLogregistroempleado(models.Model):
    idu_log = models.AutoField()
    num_empleado = models.IntegerField()
    nom_empleado = models.CharField(max_length=100, blank=True, null=True)
    nom_email = models.CharField(max_length=50, blank=True, null=True)
    nom_password = models.CharField(max_length=50, blank=True, null=True)
    fec_movimiento = models.DateTimeField()
    opc_estatusempleado = models.BooleanField()
    idu_empresa = models.SmallIntegerField()
    num_ciudad = models.IntegerField()
    opc_genero = models.SmallIntegerField()
    fec_nacimiento = models.DateField()
    idu_movimientoregistroempleado = models.SmallIntegerField()
    num_clientecoppel = models.IntegerField()
    num_empleado_sesion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mov_logregistroempleado'


class MovLogrespuestas(models.Model):
    idrespuesta = models.IntegerField(blank=True, null=True)
    numempleado = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_logrespuestas'


class MovMarcas(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    nummarca = models.IntegerField()
    descmarca = models.CharField(max_length=30)
    exclusividadcoppel = models.SmallIntegerField()
    activo = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mov_marcas'
        unique_together = (('numarea', 'nummarca'),)


class MovMedidas(models.Model):
    numcodigo = models.IntegerField(primary_key=True)
    peso = models.IntegerField()
    largo = models.IntegerField()
    ancho = models.IntegerField()
    alto = models.IntegerField()
    piescubicos = models.IntegerField()
    kilatajeorofino = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mov_medidas'


class MovPagobancario(models.Model):
    id = models.AutoField()
    hora = models.CharField(max_length=-1, blank=True, null=True)
    sucursal = models.IntegerField(blank=True, null=True)
    monto = models.IntegerField(blank=True, null=True)
    foliobanco = models.IntegerField(blank=True, null=True)
    referencia = models.CharField(max_length=-1, blank=True, null=True)
    folio = models.IntegerField(blank=True, null=True)
    saldo = models.FloatField(blank=True, null=True)
    pagado = models.IntegerField(blank=True, null=True)
    menor = models.IntegerField(blank=True, null=True)
    mayor = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    fechatransaccion = models.DateField(blank=True, null=True)
    retraso = models.IntegerField(blank=True, null=True)
    tipopago = models.IntegerField(blank=True, null=True)
    intentocompletar = models.IntegerField(blank=True, null=True)
    flagventasistema = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_pagobancario'


class MovPedidoinformaciongeneral(models.Model):
    cc_vencido = models.CharField(max_length=-1, blank=True, null=True)
    sobreprecio12 = models.IntegerField(blank=True, null=True)
    sobreprecio18 = models.IntegerField(blank=True, null=True)
    folio = models.IntegerField(blank=True, null=True)
    puntajeparcelulares = models.IntegerField(blank=True, null=True)
    puntajeparaltoriesgo = models.IntegerField(blank=True, null=True)
    sobreprecioropa = models.IntegerField(blank=True, null=True)
    tasainteresropa = models.IntegerField(blank=True, null=True)
    cc_vencidoropa = models.CharField(max_length=-1, blank=True, null=True)
    nuevosaldoropa = models.IntegerField(blank=True, null=True)
    importeropa = models.IntegerField(blank=True, null=True)
    saldoropa = models.IntegerField(blank=True, null=True)
    importemuebles = models.IntegerField(blank=True, null=True)
    pagoinicialropa = models.IntegerField(blank=True, null=True)
    pagoinicialmuebles = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_pedidoinformaciongeneral'


class MovPedidoinformacionpersonal(models.Model):
    nombre_de = models.CharField(max_length=-1, blank=True, null=True)
    apellidopaterno_de = models.CharField(max_length=-1, blank=True, null=True)
    apellidomaterno_de = models.CharField(max_length=-1, blank=True, null=True)
    telefono_de = models.CharField(max_length=-1, blank=True, null=True)
    celular_de = models.CharField(max_length=-1, blank=True, null=True)
    email_de = models.CharField(max_length=-1, blank=True, null=True)
    nombre_para = models.CharField(max_length=-1, blank=True, null=True)
    apellidopaterno_para = models.CharField(max_length=-1, blank=True, null=True)
    apellidomaterno_para = models.CharField(max_length=-1, blank=True, null=True)
    estado_para = models.CharField(max_length=-1, blank=True, null=True)
    ciudad_para = models.CharField(max_length=-1, blank=True, null=True)
    colonia_para = models.CharField(max_length=-1, blank=True, null=True)
    calle_para = models.CharField(max_length=-1, blank=True, null=True)
    entrecalles_para = models.CharField(max_length=-1, blank=True, null=True)
    codigopostal_para = models.CharField(max_length=-1, blank=True, null=True)
    numerocasa_para = models.IntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=-1, blank=True, null=True)
    id = models.AutoField(unique=True)
    idsession = models.CharField(max_length=64)
    flag_sesion = models.IntegerField(blank=True, null=True)
    nombreciudad_para = models.CharField(max_length=64, blank=True, null=True)
    nombreciudad_de = models.CharField(max_length=64, blank=True, null=True)
    dineroelectronico = models.IntegerField(blank=True, null=True)
    dineroelectronico_propuesto = models.IntegerField(blank=True, null=True)
    pagoinicial = models.IntegerField(blank=True, null=True)
    pagoinicial_propuesto = models.IntegerField(blank=True, null=True)
    clavecliente = models.IntegerField(blank=True, null=True)
    dineroelectronicoropa = models.IntegerField(blank=True, null=True)
    dineroelectronicomuebles = models.IntegerField(blank=True, null=True)
    pagoinicialropa = models.IntegerField(blank=True, null=True)
    pagoinicialmuebles = models.IntegerField(blank=True, null=True)
    importe = models.IntegerField(blank=True, null=True)
    importeropa = models.IntegerField(blank=True, null=True)
    importemuebles = models.IntegerField(blank=True, null=True)
    pagoinicialropa_propuesto = models.IntegerField(blank=True, null=True)
    pagoinicialmuebles_propuesto = models.IntegerField(blank=True, null=True)
    dineroelectronicoropa_propuesto = models.IntegerField(blank=True, null=True)
    dineroelectronicomuebles_propuesto = models.IntegerField(blank=True, null=True)
    validacioncreditoropa_propuesto = models.IntegerField(blank=True, null=True)
    coloniaref_para = models.IntegerField(blank=True, null=True)
    flagplazo18 = models.IntegerField(blank=True, null=True)
    flagplazo18_propuesto = models.IntegerField(blank=True, null=True)
    chk_facturacion = models.IntegerField(blank=True, null=True)
    flag_dineroelectronico = models.IntegerField(blank=True, null=True)
    importemueblescredito = models.IntegerField(blank=True, null=True)
    importeropacredito = models.IntegerField(blank=True, null=True)
    validacioncreditomuebles_propuesto = models.IntegerField(blank=True, null=True)
    dineroelectronicomaximomuebles = models.IntegerField(blank=True, null=True)
    creditocoppel = models.IntegerField(blank=True, null=True)
    importemueblescredito18 = models.IntegerField(blank=True, null=True)
    sobreprecioropa = models.IntegerField(blank=True, null=True)
    gnfechatransaccion = models.DateField(blank=True, null=True)
    cuentabancaria = models.IntegerField(blank=True, null=True)
    fechagndominio = models.DateField(blank=True, null=True)
    tiempoactualizacion = models.DateTimeField(blank=True, null=True)
    referencia = models.CharField(max_length=16, blank=True, null=True)
    nsess = models.CharField(max_length=-1, blank=True, null=True)
    seq_abc = models.IntegerField(blank=True, null=True)
    seq_carrito = models.IntegerField(blank=True, null=True)
    seq_orden = models.IntegerField(blank=True, null=True)
    seq_credito = models.IntegerField(blank=True, null=True)
    tipopago = models.IntegerField(blank=True, null=True)
    fechaultimaoperacion = models.DateTimeField(blank=True, null=True)
    tokenorden = models.CharField(max_length=-1, blank=True, null=True)
    pagoinicialropa_cliente = models.IntegerField(blank=True, null=True)
    pagoinicialmuebles_cliente = models.IntegerField(blank=True, null=True)
    pagoinicial_cliente = models.IntegerField(blank=True, null=True)
    dateultimaoperacion = models.DateTimeField(blank=True, null=True)
    flag_guest = models.IntegerField(blank=True, null=True)
    forma_validacion = models.IntegerField(blank=True, null=True)
    fechacreacion = models.DateTimeField(blank=True, null=True)
    nom_completousuario = models.CharField(max_length=100, blank=True, null=True)
    nom_completousuario_para = models.CharField(max_length=100, blank=True, null=True)
    num_extpara = models.CharField(max_length=6, blank=True, null=True)
    num_intpara = models.CharField(max_length=6, blank=True, null=True)
    num_opcionbloqueo = models.SmallIntegerField(blank=True, null=True)
    num_importetdcropa = models.IntegerField()
    num_importetdcmuebles = models.IntegerField()
    num_empleado = models.IntegerField()
    prc_saturacion = models.IntegerField()
    imp_nuevosaldo = models.IntegerField()
    num_puntajefinal = models.IntegerField()
    imp_pagoultimosdocemeses = models.IntegerField()
    prc_saturacion_ropa = models.IntegerField()
    imp_nuevosaldo_ropa = models.IntegerField()
    num_puntajefinal_ropa = models.IntegerField()
    imp_pagoultimosdocemeses_ropa = models.IntegerField()
    prc_saturacion_muebles = models.IntegerField()
    imp_nuevosaldo_muebles = models.IntegerField()
    num_puntajefinal_muebles = models.IntegerField()
    imp_pagoultimosdocemeses_muebles = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mov_pedidoinformacionpersonal'


class MovProcesoventas(models.Model):
    sec_serial = models.AutoField()
    des_session = models.CharField(max_length=50)
    num_cliente = models.IntegerField()
    clv_tipoprocesoventa = models.SmallIntegerField(blank=True, null=True)
    clv_tipoopcionventa = models.SmallIntegerField(blank=True, null=True)
    fol_procesoventa = models.IntegerField(blank=True, null=True)
    fec_procesoventa = models.DateTimeField(blank=True, null=True)
    clv_respuestaventas = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_procesoventas'


class MovProductosmercadolibre(models.Model):
    partnumber = models.CharField(max_length=64, blank=True, null=True)
    numarea = models.SmallIntegerField(blank=True, null=True)
    numdepto = models.SmallIntegerField(blank=True, null=True)
    numclase = models.SmallIntegerField(blank=True, null=True)
    numfamilia = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    numtalla = models.SmallIntegerField(blank=True, null=True)
    type = models.CharField(max_length=16, blank=True, null=True)
    isproduct = models.BooleanField(blank=True, null=True)
    parentpartnumber = models.CharField(max_length=64, blank=True, null=True)
    category = models.CharField(max_length=264, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    shortdescription = models.CharField(max_length=255, blank=True, null=True)
    longdescription = models.TextField(blank=True, null=True)
    keyword = models.CharField(max_length=254, blank=True, null=True)
    marca = models.CharField(max_length=120, blank=True, null=True)
    thumbnail = models.CharField(max_length=120, blank=True, null=True)
    fullimage = models.CharField(max_length=120, blank=True, null=True)
    sequence = models.CharField(max_length=5, blank=True, null=True)
    language_id = models.CharField(max_length=5, blank=True, null=True)
    available = models.IntegerField(blank=True, null=True)
    published = models.IntegerField(blank=True, null=True)
    buyable = models.IntegerField(blank=True, null=True)
    availabilitydate_localspecific = models.DateTimeField(blank=True, null=True)
    promotion_price_currency = models.CharField(max_length=25, blank=True, null=True)
    contado_price = models.IntegerField(blank=True, null=True)
    credito_price = models.IntegerField(blank=True, null=True)
    promotion_price = models.CharField(max_length=10, blank=True, null=True)
    flag_price = models.CharField(max_length=10, blank=True, null=True)
    fechainicialpromo = models.DateField(blank=True, null=True)
    fechafinalpromo = models.DateField(blank=True, null=True)
    field1 = models.CharField(max_length=264, blank=True, null=True)
    field2 = models.CharField(max_length=264, blank=True, null=True)
    manufacturer = models.CharField(max_length=254, blank=True, null=True)
    region_telcel = models.CharField(max_length=264, blank=True, null=True)
    dcf = models.CharField(max_length=25, blank=True, null=True)
    nivel = models.SmallIntegerField(blank=True, null=True)
    flag_cambio_category = models.BooleanField(blank=True, null=True)
    delete_value = models.CharField(max_length=25, blank=True, null=True)
    urlkeyword = models.CharField(max_length=250, blank=True, null=True)
    pagetitle = models.CharField(max_length=150, blank=True, null=True)
    metadescription = models.CharField(max_length=250, blank=True, null=True)
    gtin = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_productosmercadolibre'


class MovPromocionesmuebles(models.Model):
    numcodigo = models.IntegerField(primary_key=True)
    fechainicial = models.DateField()
    fechafinal = models.DateField()

    class Meta:
        managed = False
        db_table = 'mov_promocionesmuebles'


class MovSecuenciaTercerNiveles(models.Model):
    idu_areacodigo = models.SmallIntegerField(blank=True, null=True)
    idu_departamentocodigo = models.SmallIntegerField(blank=True, null=True)
    idu_clasecodigo = models.SmallIntegerField(blank=True, null=True)
    idu_familiacodigo = models.SmallIntegerField(blank=True, null=True)
    idu_articulocodigo = models.IntegerField(blank=True, null=True)
    partnumber = models.CharField(max_length=10)
    productname = models.CharField(max_length=200, blank=True, null=True)
    categoryname = models.CharField(max_length=60, blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    parentgroupuniqueid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_secuencia_tercer_niveles'


class MovSegumientoEstafeta(models.Model):
    idu_seguimiento = models.AutoField()
    num_folio = models.BigIntegerField()
    nom_history = models.TextField()
    fec_fechamovimiento = models.DateField(blank=True, null=True)
    nom_estatus = models.CharField(max_length=-1, blank=True, null=True)
    hor_ejecucion = models.TimeField()

    class Meta:
        managed = False
        db_table = 'mov_segumiento_estafeta'


class MovSepomex(models.Model):
    numcodigopostal = models.IntegerField()
    colonia = models.CharField(max_length=65)
    asentamiento = models.CharField(max_length=65)
    municipio = models.CharField(max_length=65)
    estado = models.CharField(max_length=65)
    ciudad = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'mov_sepomex'


class MovStoresbodegas(models.Model):
    num_ciudad = models.IntegerField()
    num_bodega = models.IntegerField()
    idu_store = models.IntegerField()
    des_movimiento = models.CharField(max_length=10, blank=True, null=True)
    fec_movimiento = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_storesbodegas'


class MovStoresbodegasEtl(models.Model):
    num_ciudad = models.IntegerField(blank=True, null=True)
    num_bodega = models.IntegerField(blank=True, null=True)
    idu_store = models.IntegerField(blank=True, null=True)
    des_movimiento = models.CharField(max_length=10, blank=True, null=True)
    fec_movimiento = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_storesbodegas_etl'


class MovTallasarticulos(models.Model):
    numarea = models.SmallIntegerField(primary_key=True)
    numcodigo = models.IntegerField()
    numtalla = models.SmallIntegerField()
    precioventa = models.SmallIntegerField()
    comprar = models.SmallIntegerField()
    desctalla = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_tallasarticulos'
        unique_together = (('numarea', 'numcodigo', 'numtalla'),)


class MovTareasurtido(models.Model):
    idu_tareasurtido = models.AutoField()
    fec_tarea = models.DateField(primary_key=True)
    opc_ejecucion = models.SmallIntegerField()
    num_totalnotas = models.IntegerField()
    num_notasdia = models.IntegerField()
    num_notasactualizadas = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mov_tareasurtido'


class MovTasainteres(models.Model):
    numarea = models.SmallIntegerField()
    tasainteres = models.SmallIntegerField()
    tasainteresriesgo = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mov_tasainteres'


class MovTiendasregioncelulares(models.Model):
    num_tienda = models.SmallIntegerField()
    num_bodega = models.SmallIntegerField()
    num_ciudadpertenece = models.SmallIntegerField()
    num_ciudad = models.SmallIntegerField()
    num_ciudaddistribucion = models.SmallIntegerField()
    des_ciudadcelular = models.CharField(max_length=4)
    num_regioncelular = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mov_tiendasregioncelulares'


class MovTiendavirtualtallasfamilia(models.Model):
    numdepto = models.SmallIntegerField()
    numclase = models.SmallIntegerField()
    numfamilia = models.SmallIntegerField()
    numtalla = models.SmallIntegerField()
    desctalla = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_tiendavirtualtallasfamilia'


class MovToken(models.Model):
    token = models.CharField(max_length=10, blank=True, null=True)
    cliente = models.IntegerField(blank=True, null=True)
    telefono = models.CharField(max_length=12, blank=True, null=True)
    fechacreacion = models.DateTimeField(blank=True, null=True)
    tipotelefono = models.IntegerField(blank=True, null=True)
    borrarestatus = models.IntegerField(blank=True, null=True)
    tipotoken = models.IntegerField(blank=True, null=True)
    tipolector = models.IntegerField(blank=True, null=True)
    lectortoken = models.CharField(max_length=-1, blank=True, null=True)
    estatusentregado = models.IntegerField(blank=True, null=True)
    id = models.AutoField()
    fechaentrega = models.DateTimeField(blank=True, null=True)
    fechauso = models.DateTimeField(blank=True, null=True)
    borradonuevapeticion = models.IntegerField(blank=True, null=True)
    tipooperacion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_token'


class MovTrackedeltas(models.Model):
    dfecha = models.DateTimeField()
    field1 = models.IntegerField()
    field2 = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'mov_trackedeltas'


class MovTrackerror(models.Model):
    dfecha = models.DateTimeField()
    field1 = models.IntegerField()
    csqlerrm = models.CharField(max_length=-1)
    csqlstate = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'mov_trackerror'


class MovVentaRopa(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    cantidad = models.SmallIntegerField(blank=True, null=True)
    talla = models.CharField(max_length=-1, blank=True, null=True)
    folio = models.IntegerField(blank=True, null=True)
    fechaventa = models.DateField(blank=True, null=True)
    numbodega = models.SmallIntegerField(blank=True, null=True)
    tipoventa = models.CharField(max_length=1, blank=True, null=True)
    flagsurtido = models.CharField(max_length=1)
    flagenviado = models.CharField(max_length=1)
    flagapartado = models.CharField(max_length=1)
    precio = models.IntegerField()
    id_serial = models.AutoField(primary_key=True)
    nu_guia = models.CharField(max_length=25, blank=True, null=True)
    flagvendido = models.CharField(max_length=1, blank=True, null=True)
    sn_codigo_confirmado = models.IntegerField(blank=True, null=True)
    sn_impreso = models.IntegerField(blank=True, null=True)
    precio_surtido = models.IntegerField(blank=True, null=True)
    fh_surtido = models.DateTimeField(blank=True, null=True)
    flag_ordensingle = models.IntegerField(blank=True, null=True)
    flag_statuscodigo = models.IntegerField()
    num_foliomp = models.BigIntegerField()
    num_tipoembalaje = models.SmallIntegerField()
    idu_paquetera = models.IntegerField(blank=True, null=True)
    idu_multicarrier = models.IntegerField(blank=True, null=True)
    flag_contingencia = models.SmallIntegerField(blank=True, null=True)
    dias_entrega = models.IntegerField(blank=True, null=True)
    costo_guia = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    num_location_id = models.IntegerField(blank=True, null=True)
    des_location_company = models.CharField(max_length=-1, blank=True, null=True)
    flag_entrega_tienda = models.SmallIntegerField(blank=True, null=True)
    id_quotation = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_venta_ropa'


class MovVentaRopaXto(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    cantidad = models.SmallIntegerField(blank=True, null=True)
    talla = models.CharField(max_length=-1, blank=True, null=True)
    folio = models.IntegerField(blank=True, null=True)
    fechaventa = models.DateField(blank=True, null=True)
    numbodega = models.SmallIntegerField(blank=True, null=True)
    tipoventa = models.CharField(max_length=1, blank=True, null=True)
    flagsurtido = models.CharField(max_length=1, blank=True, null=True)
    flagenviado = models.CharField(max_length=1, blank=True, null=True)
    flagapartado = models.CharField(max_length=1, blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    id_serial = models.IntegerField(blank=True, null=True)
    nu_guia = models.CharField(max_length=25, blank=True, null=True)
    flagvendido = models.CharField(max_length=1, blank=True, null=True)
    sn_codigo_confirmado = models.IntegerField(blank=True, null=True)
    sn_impreso = models.IntegerField(blank=True, null=True)
    precio_surtido = models.IntegerField(blank=True, null=True)
    fh_surtido = models.DateTimeField(blank=True, null=True)
    flag_ordensingle = models.IntegerField(blank=True, null=True)
    flag_statuscodigo = models.IntegerField(blank=True, null=True)
    num_foliomp = models.BigIntegerField(blank=True, null=True)
    num_tipoembalaje = models.SmallIntegerField(blank=True, null=True)
    idu_paquetera = models.IntegerField(blank=True, null=True)
    idu_multicarrier = models.IntegerField(blank=True, null=True)
    flag_contingencia = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_venta_ropa_xto'


class MovVentasCatalogo(models.Model):
    idu_mov_ventas = models.BigAutoField()
    num_tienda = models.IntegerField()
    des_ip = models.CharField(max_length=30, blank=True, null=True)
    des_formatotienda = models.CharField(max_length=30, blank=True, null=True)
    num_orden = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'mov_ventas_catalogo'
        unique_together = (('num_orden', 'num_tienda'),)


class MovVentascoppelcomtienda(models.Model):
    num_tienda = models.SmallIntegerField(blank=True, null=True)
    num_area = models.SmallIntegerField(blank=True, null=True)
    num_factura = models.IntegerField(blank=True, null=True)
    fec_venta = models.DateField(blank=True, null=True)
    num_areavendedor = models.SmallIntegerField(blank=True, null=True)
    num_vendedor = models.IntegerField(blank=True, null=True)
    num_folioorden = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mov_ventascoppelcomtienda'


class MovVentasoe(models.Model):
    idu_pedido = models.IntegerField()
    num_notafactura = models.IntegerField()
    num_foliomp = models.BigIntegerField()
    num_area = models.SmallIntegerField()
    num_codigo = models.IntegerField()
    num_cantidad = models.SmallIntegerField()
    num_talla = models.SmallIntegerField()
    num_precio = models.SmallIntegerField()
    fec_venta = models.DateField()
    num_bodega = models.SmallIntegerField()
    id_serial = models.IntegerField(primary_key=True)
    num_guia = models.CharField(max_length=25, blank=True, null=True)
    flag_ordensingle = models.IntegerField()
    flag_estatuscodigo = models.IntegerField()
    num_tipoembalaje = models.SmallIntegerField()
    num_codigo_confirmado = models.SmallIntegerField()
    num_codigo_enviado = models.SmallIntegerField()
    num_folioplataforma = models.BigIntegerField()
    fecha_movimiento = models.DateTimeField(blank=True, null=True)
    flag_etiquetamaster_confirmado = models.IntegerField(blank=True, null=True)
    idu_paquetera = models.IntegerField(blank=True, null=True)
    idu_multicarrier = models.IntegerField(blank=True, null=True)
    opc_movimientoaoficinadeenvios = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mov_ventasoe'


class MovZonasrelacionado(models.Model):
    numciudad = models.IntegerField(primary_key=True)
    numcolonia = models.IntegerField()
    nomzona = models.CharField(max_length=50)
    poblacionzona = models.CharField(max_length=50)
    municipiozona = models.CharField(max_length=50)
    codigopostalzona = models.IntegerField()
    numciudadcoppel = models.IntegerField()
    numcoloniacoppel = models.IntegerField()
    nomzonacoppel = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'mov_zonasrelacionado'
        unique_together = (('numciudad', 'numcolonia'),)


class Nodo(models.Model):
    nom_store = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nodo'
# Unable to inspect table 'nodos_logisticos'
# The error was: permission denied for table nodos_logisticos


class Numfolio(models.Model):
    split_part = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'numfolio'


class Numfolioorden(models.Model):
    num_folio = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'numfolioorden'


class Numimagenes(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'numimagenes'


class Numtotal(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'numtotal'


class Nutienda(models.Model):
    num_tienda = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nutienda'


class ParamIdupedido(models.Model):
    idu_pedido = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'param_idupedido'


class PgTsCfg(models.Model):
    ts_name = models.TextField(primary_key=True)
    prs_name = models.TextField()
    locale = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_ts_cfg'


class PgTsCfgmap(models.Model):
    ts_name = models.TextField(primary_key=True)
    tok_alias = models.TextField()
    dict_name = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'pg_ts_cfgmap'
        unique_together = (('ts_name', 'tok_alias'),)


class ProcCodigosregionestelcel(models.Model):
    num_codigogeneral = models.CharField(max_length=-1)
    num_codigoregion = models.IntegerField()
    num_regiontelcel = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'proc_codigosregionestelcel'


class Rdatoscatclientes(models.Model):
    numcasa = models.CharField(max_length=12, blank=True, null=True)
    calle = models.CharField(max_length=40, blank=True, null=True)
    colonia = models.CharField(max_length=30, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    cp = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rdatoscatclientes'


class Rdatosplantilla(models.Model):
    idu_plantilla = models.IntegerField(blank=True, null=True)
    nom_trigger = models.CharField(max_length=100, blank=True, null=True)
    nom_plantilla = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rdatosplantilla'


class Rdatosregresa(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numbodega = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    numtalla = models.SmallIntegerField(blank=True, null=True)
    precioventa = models.IntegerField(blank=True, null=True)
    disponible = models.IntegerField(blank=True, null=True)
    tipoarticulo = models.SmallIntegerField(blank=True, null=True)
    preciocredito = models.IntegerField(blank=True, null=True)
    preciorebaja = models.IntegerField(blank=True, null=True)
    preciofrontera = models.IntegerField(blank=True, null=True)
    num_existencia = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rdatosregresa'


class RepComparador(models.Model):
    partnumber = models.CharField(max_length=-1, blank=True, null=True)
    precio = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rep_comparador'


class RepOfertasCambio(models.Model):
    imkp = models.CharField(max_length=-1, blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    precio_old = models.IntegerField(blank=True, null=True)
    diferencia = models.IntegerField(blank=True, null=True)
    id_tienda = models.IntegerField(blank=True, null=True)
    tienda = models.CharField(max_length=-1, blank=True, null=True)
    sku = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rep_ofertas_cambio'


class RepOfertasEliminar(models.Model):
    partnumber = models.CharField(max_length=-1, blank=True, null=True)
    offer_id = models.CharField(max_length=-1, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    precedence = models.CharField(max_length=-1, blank=True, null=True)
    identifier = models.IntegerField(blank=True, null=True)
    startdate = models.CharField(max_length=-1, blank=True, null=True)
    enddate = models.CharField(max_length=-1, blank=True, null=True)
    mpoffer_id = models.CharField(max_length=-1, blank=True, null=True)
    buyboxweight = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(db_column='NAME', max_length=-1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rep_ofertas_eliminar'


class RepOfertasMiraklCambio(models.Model):
    offer_id = models.IntegerField(blank=True, null=True)
    product_sku = models.CharField(max_length=10485760, blank=True, null=True)
    min_shipping_price = models.CharField(max_length=10485760, blank=True, null=True)
    min_shipping_price_additional = models.CharField(max_length=10485760, blank=True, null=True)
    min_shipping_zone = models.CharField(max_length=10485760, blank=True, null=True)
    min_shipping_type = models.CharField(max_length=10485760, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True)
    price_additional_info = models.CharField(max_length=10485760, blank=True, null=True)
    quantity = models.CharField(max_length=10485760, blank=True, null=True)
    description = models.CharField(max_length=10485760, blank=True, null=True)
    state_code = models.CharField(max_length=10485760, blank=True, null=True)
    shop_id = models.CharField(max_length=10485760, blank=True, null=True)
    shop_name = models.CharField(max_length=10485760, blank=True, null=True)
    professional = models.CharField(max_length=10485760, blank=True, null=True)
    premium = models.CharField(max_length=10485760, blank=True, null=True)
    logistic_class = models.CharField(max_length=10485760, blank=True, null=True)
    active = models.CharField(max_length=10485760, blank=True, null=True)
    favorite_rank = models.CharField(max_length=10485760, blank=True, null=True)
    channels = models.CharField(max_length=10485760, blank=True, null=True)
    deleted = models.CharField(max_length=10485760, blank=True, null=True)
    origin_price = models.CharField(max_length=10485760, blank=True, null=True)
    discount_start_date = models.CharField(max_length=10485760, blank=True, null=True)
    discount_end_date = models.CharField(max_length=10485760, blank=True, null=True)
    available_start_date = models.CharField(max_length=10485760, blank=True, null=True)
    available_end_date = models.CharField(max_length=10485760, blank=True, null=True)
    discount_price = models.CharField(max_length=10485760, blank=True, null=True)
    currency_iso_code = models.CharField(max_length=10485760, blank=True, null=True)
    discount_ranges = models.CharField(max_length=10485760, blank=True, null=True)
    leadtime_to_ship = models.CharField(max_length=10485760, blank=True, null=True)
    allow_quote_requests = models.CharField(max_length=10485760, blank=True, null=True)
    price_ranges = models.CharField(max_length=10485760, blank=True, null=True)
    fulfillment_center_code = models.CharField(max_length=10485760, blank=True, null=True)
    shop_sku = models.CharField(max_length=10485760, blank=True, null=True)
    cfwarrantypolicy = models.CharField(max_length=10485760, blank=True, null=True)
    cfwarrantyperiod = models.CharField(max_length=10485760, blank=True, null=True)
    cfshippingpackageweight = models.CharField(max_length=10485760, blank=True, null=True)
    cfshippingpackageheight = models.CharField(max_length=10485760, blank=True, null=True)
    cfshippingpackagelength = models.CharField(max_length=10485760, blank=True, null=True)
    cfshippingpackagewidth = models.CharField(max_length=10485760, blank=True, null=True)
    cfproducttaxid = models.CharField(max_length=10485760, blank=True, null=True)
    measurement_units = models.CharField(max_length=10485760, blank=True, null=True)
    imkp = models.CharField(max_length=10485760, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rep_ofertas_mirakl_cambio'


class RepProductosCambioPrecio(models.Model):
    offer_id = models.IntegerField(blank=True, null=True)
    product_sku = models.CharField(max_length=10485760, blank=True, null=True)
    min_shipping_price = models.CharField(max_length=10485760, blank=True, null=True)
    min_shipping_price_additional = models.CharField(max_length=10485760, blank=True, null=True)
    min_shipping_zone = models.CharField(max_length=10485760, blank=True, null=True)
    min_shipping_type = models.CharField(max_length=10485760, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True)
    price_additional_info = models.CharField(max_length=10485760, blank=True, null=True)
    quantity = models.CharField(max_length=10485760, blank=True, null=True)
    description = models.CharField(max_length=10485760, blank=True, null=True)
    state_code = models.CharField(max_length=10485760, blank=True, null=True)
    shop_id = models.IntegerField(blank=True, null=True)
    shop_name = models.CharField(max_length=10485760, blank=True, null=True)
    professional = models.CharField(max_length=10485760, blank=True, null=True)
    premium = models.CharField(max_length=10485760, blank=True, null=True)
    logistic_class = models.CharField(max_length=10485760, blank=True, null=True)
    active = models.CharField(max_length=10485760, blank=True, null=True)
    favorite_rank = models.CharField(max_length=10485760, blank=True, null=True)
    channels = models.CharField(max_length=10485760, blank=True, null=True)
    deleted = models.CharField(max_length=10485760, blank=True, null=True)
    origin_price = models.CharField(max_length=10485760, blank=True, null=True)
    discount_start_date = models.CharField(max_length=10485760, blank=True, null=True)
    discount_end_date = models.CharField(max_length=10485760, blank=True, null=True)
    available_start_date = models.CharField(max_length=10485760, blank=True, null=True)
    available_end_date = models.CharField(max_length=10485760, blank=True, null=True)
    discount_price = models.CharField(max_length=10485760, blank=True, null=True)
    currency_iso_code = models.CharField(max_length=10485760, blank=True, null=True)
    discount_ranges = models.CharField(max_length=10485760, blank=True, null=True)
    leadtime_to_ship = models.CharField(max_length=10485760, blank=True, null=True)
    allow_quote_requests = models.CharField(max_length=10485760, blank=True, null=True)
    price_ranges = models.CharField(max_length=10485760, blank=True, null=True)
    fulfillment_center_code = models.CharField(max_length=10485760, blank=True, null=True)
    shop_sku = models.CharField(max_length=10485760, blank=True, null=True)
    cfwarrantypolicy = models.CharField(max_length=10485760, blank=True, null=True)
    cfwarrantyperiod = models.CharField(max_length=10485760, blank=True, null=True)
    cfshippingpackageweight = models.CharField(max_length=10485760, blank=True, null=True)
    cfshippingpackageheight = models.CharField(max_length=10485760, blank=True, null=True)
    cfshippingpackagelength = models.CharField(max_length=10485760, blank=True, null=True)
    cfshippingpackagewidth = models.CharField(max_length=10485760, blank=True, null=True)
    cfproducttaxid = models.CharField(max_length=10485760, blank=True, null=True)
    measurement_units = models.CharField(max_length=10485760, blank=True, null=True)
    imkp = models.CharField(max_length=10485760, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rep_productos_cambio_precio'


class RepProductosTiendaNoMirakl(models.Model):
    partnumber = models.CharField(max_length=10485760, blank=True, null=True)
    offer_id = models.CharField(max_length=10485760, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    precedence = models.CharField(max_length=10485760, blank=True, null=True)
    identifier = models.IntegerField(blank=True, null=True)
    startdate = models.CharField(max_length=10485760, blank=True, null=True)
    enddate = models.CharField(max_length=10485760, blank=True, null=True)
    mpoffer_id = models.CharField(max_length=10485760, blank=True, null=True)
    buyboxweight = models.CharField(max_length=10485760, blank=True, null=True)
    name = models.CharField(db_column='NAME', max_length=10485760, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rep_productos_tienda_no_mirakl'


class Replicamonterreysan(models.Model):
    revisadopor = models.CharField(max_length=45)
    atendioensan = models.CharField(max_length=45)
    fechachequeo = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'replicamonterreysan'


class Respuesta(models.Model):
    case = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'respuesta'


class ResultRecord(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numareaweb = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'result_record'


class Resultbuyboxweight(models.Model):
    coalesce = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resultbuyboxweight'


class Rpreciosproductostelcel(models.Model):
    contado_price = models.IntegerField(blank=True, null=True)
    credito_price = models.IntegerField(blank=True, null=True)
    promotion_price = models.CharField(max_length=10, blank=True, null=True)
    flag_price = models.CharField(max_length=10, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    currencycode = models.CharField(max_length=16, blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    field1 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rpreciosproductostelcel'


class RptEstadisticacapturacorreos(models.Model):
    divisionalempleadocodigo = models.IntegerField(blank=True, null=True)
    divisionaliniciales = models.CharField(max_length=-1, blank=True, null=True)
    divisional = models.CharField(max_length=-1, blank=True, null=True)
    regionalempleadocodigo = models.IntegerField(blank=True, null=True)
    regionaliniciales = models.CharField(max_length=-1, blank=True, null=True)
    regional = models.CharField(max_length=-1, blank=True, null=True)
    zonaempleadocodigo = models.IntegerField(blank=True, null=True)
    zonainiciales = models.CharField(max_length=-1, blank=True, null=True)
    zona = models.CharField(max_length=-1, blank=True, null=True)
    tiendacodigo = models.SmallIntegerField(blank=True, null=True)
    tienda = models.CharField(max_length=-1, blank=True, null=True)
    areacodigo = models.IntegerField(blank=True, null=True)
    area = models.CharField(max_length=-1, blank=True, null=True)
    centro = models.IntegerField(blank=True, null=True)
    gerenteempleadocodigo = models.IntegerField(blank=True, null=True)
    gerente = models.CharField(max_length=-1, blank=True, null=True)
    empleadocodigo = models.IntegerField(blank=True, null=True)
    oportunidades = models.BigIntegerField(blank=True, null=True)
    capturados = models.BigIntegerField(blank=True, null=True)
    validos = models.BigIntegerField(blank=True, null=True)
    division = models.CharField(max_length=-1, blank=True, null=True)
    region = models.CharField(max_length=-1, blank=True, null=True)
    regioniniciales = models.CharField(max_length=-1, blank=True, null=True)
    empleado = models.CharField(max_length=-1, blank=True, null=True)
    anioretail = models.SmallIntegerField(blank=True, null=True)
    semanaretail = models.SmallIntegerField(blank=True, null=True)
    fechainicial = models.DateField(blank=True, null=True)
    fechafinal = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rpt_estadisticacapturacorreos'


class Sbodegas(models.Model):
    num_valor = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sbodegas'


class Scolumnas(models.Model):
    num_valor = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scolumnas'


class Seourl(models.Model):
    seourl_id = models.BigIntegerField(primary_key=True)
    tokenname = models.CharField(max_length=254)
    tokenvalue = models.CharField(max_length=254)
    priority = models.FloatField(blank=True, null=True)
    change_frequency = models.CharField(max_length=3, blank=True, null=True)
    mobile_priority = models.FloatField(blank=True, null=True)
    mobile_chg_freq = models.CharField(max_length=3, blank=True, null=True)
    optcounter = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'seourl'


class Seourlkeyword(models.Model):
    seourlkeyword_id = models.BigIntegerField(primary_key=True)
    seourl_id = models.BigIntegerField()
    language_id = models.IntegerField()
    storeent_id = models.IntegerField()
    urlkeyword = models.CharField(max_length=254)
    mobileurlkeyword = models.CharField(max_length=254, blank=True, null=True)
    status = models.IntegerField()
    optcounter = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'seourlkeyword'


class Sestados(models.Model):
    idu_estados = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sestados'


class Snombreareaweb(models.Model):
    fun_obtenernombreareaweb = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snombreareaweb'


class Snombrezona(models.Model):
    des_colonia = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snombrezona'


class Sregiondestino(models.Model):
    num_region = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sregiondestino'


class Stextojson(models.Model):
    field_column_field = models.TextField(db_column='?column?', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'stextojson'


class Stockitems(models.Model):
    item = models.IntegerField(primary_key=True)
    area = models.ForeignKey(Areas, models.DO_NOTHING)
    item_size = models.SmallIntegerField()
    nationalitemflag = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'stockitems'
        unique_together = (('item', 'area', 'item_size'),)


class Strigger(models.Model):
    coalesce = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'strigger'


class SysFlagerpd(models.Model):
    idu_flag = models.AutoField(primary_key=True)
    nom_flag = models.CharField(max_length=-1, blank=True, null=True)
    des_flag = models.CharField(max_length=-1, blank=True, null=True)
    valor = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_flagerpd'


class Tablafunctions(models.Model):
    generalfunction = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tablafunctions'


class Tablatypes(models.Model):
    generaltype = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tablatypes'


class TaskExecution(models.Model):
    task_execution_id = models.BigIntegerField(primary_key=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    task_name = models.CharField(max_length=100, blank=True, null=True)
    exit_code = models.IntegerField(blank=True, null=True)
    exit_message = models.CharField(max_length=2500, blank=True, null=True)
    error_message = models.CharField(max_length=2500, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    external_execution_id = models.CharField(max_length=255, blank=True, null=True)
    parent_execution_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_execution'


class TaskExecutionParams(models.Model):
    task_execution = models.ForeignKey(TaskExecution, models.DO_NOTHING)
    task_param = models.CharField(max_length=2500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_execution_params'


class TaskLock(models.Model):
    lock_key = models.CharField(primary_key=True, max_length=36)
    region = models.CharField(max_length=100)
    client_id = models.CharField(max_length=36, blank=True, null=True)
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'task_lock'
        unique_together = (('lock_key', 'region'),)


class TaskTaskBatch(models.Model):
    task_execution = models.ForeignKey(TaskExecution, models.DO_NOTHING)
    job_execution_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'task_task_batch'


class TbCarrito(models.Model):
    idsession = models.CharField(max_length=50, blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    numarea = models.SmallIntegerField(blank=True, null=True)
    cantidad = models.SmallIntegerField(blank=True, null=True)
    talla = models.CharField(max_length=10, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    id = models.AutoField()
    flag_sesion = models.CharField(max_length=64, blank=True, null=True)
    disponibilidadarticulo = models.IntegerField(blank=True, null=True)
    fechaentregaarticulo = models.DateField(blank=True, null=True)
    armararticulo = models.IntegerField(blank=True, null=True)
    preciocontadounitario = models.IntegerField(blank=True, null=True)
    articulonuevo = models.IntegerField(blank=True, null=True)
    preciopromocion = models.IntegerField(blank=True, null=True)
    disponibilidadmuebles = models.IntegerField(blank=True, null=True)
    fechaentregamuebles = models.DateField(blank=True, null=True)
    preciocreditounitario = models.IntegerField(blank=True, null=True)
    flag_armado = models.IntegerField(blank=True, null=True)
    folio = models.IntegerField(blank=True, null=True)
    preciooriginal = models.IntegerField(blank=True, null=True)
    nomarticuloweb = models.CharField(max_length=-1, blank=True, null=True)
    nomarticulo = models.CharField(max_length=-1, blank=True, null=True)
    idu_carrito = models.BigIntegerField(blank=True, null=True)
    num_foliotelcel = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tb_carrito'
        unique_together = (('folio', 'numcodigo', 'numarea', 'talla'),)


class TbCarritoentregadetalle(models.Model):
    folio = models.IntegerField()
    numcodigo = models.IntegerField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    bodega = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    fechaultimaactualizacion = models.DateField(blank=True, null=True)
    cvesort = models.IntegerField(blank=True, null=True)
    clavemovto = models.IntegerField(blank=True, null=True)
    id = models.AutoField()
    causa = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_carritoentregadetalle'


class TbFacturacion(models.Model):
    id = models.IntegerField(blank=True, null=True)
    rfc = models.CharField(max_length=-1, blank=True, null=True)
    razonsocial = models.CharField(max_length=-1, blank=True, null=True)
    ciudad = models.CharField(max_length=-1, blank=True, null=True)
    estado = models.CharField(max_length=-1, blank=True, null=True)
    colonia = models.CharField(max_length=-1, blank=True, null=True)
    calle = models.CharField(max_length=-1, blank=True, null=True)
    codigopostal = models.IntegerField(blank=True, null=True)
    referencia = models.CharField(max_length=-1, blank=True, null=True)
    cliente = models.CharField(max_length=-1, blank=True, null=True)
    numerocasa = models.IntegerField(blank=True, null=True)
    numerointerior = models.CharField(max_length=10, blank=True, null=True)
    folio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_facturacion'


class TbPagobancario(models.Model):
    id = models.AutoField()
    hora = models.CharField(max_length=-1, blank=True, null=True)
    sucursal = models.IntegerField(blank=True, null=True)
    monto = models.IntegerField(blank=True, null=True)
    foliobanco = models.BigIntegerField(blank=True, null=True)
    referencia = models.CharField(max_length=-1, blank=True, null=True)
    folio = models.IntegerField(blank=True, null=True)
    saldo = models.FloatField(blank=True, null=True)
    pagado = models.IntegerField(blank=True, null=True)
    menor = models.IntegerField(blank=True, null=True)
    mayor = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    fechatransaccion = models.DateField(blank=True, null=True)
    retraso = models.IntegerField(blank=True, null=True)
    tipopago = models.IntegerField(blank=True, null=True)
    intentocompletar = models.IntegerField(blank=True, null=True)
    flagventasistema = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_pagobancario'


class TbPedidoinformaciongeneral(models.Model):
    cc_vencido = models.CharField(max_length=-1, blank=True, null=True)
    sobreprecio12 = models.IntegerField(blank=True, null=True)
    sobreprecio18 = models.IntegerField(blank=True, null=True)
    folio = models.IntegerField(blank=True, null=True)
    puntajeparcelulares = models.IntegerField(blank=True, null=True)
    puntajeparaltoriesgo = models.IntegerField(blank=True, null=True)
    sobreprecioropa = models.IntegerField(blank=True, null=True)
    tasainteresropa = models.IntegerField(blank=True, null=True)
    cc_vencidoropa = models.CharField(max_length=-1, blank=True, null=True)
    nuevosaldoropa = models.IntegerField(blank=True, null=True)
    importeropa = models.IntegerField(blank=True, null=True)
    saldoropa = models.IntegerField(blank=True, null=True)
    importemuebles = models.IntegerField(blank=True, null=True)
    pagoinicialropa = models.IntegerField(blank=True, null=True)
    pagoinicialmuebles = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_pedidoinformaciongeneral'


class TbPedidoinformacionpersonal(models.Model):
    nombre_de = models.CharField(max_length=-1, blank=True, null=True)
    apellidopaterno_de = models.CharField(max_length=-1, blank=True, null=True)
    apellidomaterno_de = models.CharField(max_length=-1, blank=True, null=True)
    telefono_de = models.CharField(max_length=-1, blank=True, null=True)
    celular_de = models.CharField(max_length=-1, blank=True, null=True)
    email_de = models.CharField(max_length=-1, blank=True, null=True)
    nombre_para = models.CharField(max_length=-1, blank=True, null=True)
    apellidopaterno_para = models.CharField(max_length=-1, blank=True, null=True)
    apellidomaterno_para = models.CharField(max_length=-1, blank=True, null=True)
    estado_para = models.CharField(max_length=-1, blank=True, null=True)
    ciudad_para = models.CharField(max_length=-1, blank=True, null=True)
    colonia_para = models.CharField(max_length=-1, blank=True, null=True)
    calle_para = models.CharField(max_length=-1, blank=True, null=True)
    entrecalles_para = models.CharField(max_length=-1, blank=True, null=True)
    codigopostal_para = models.CharField(max_length=-1, blank=True, null=True)
    numerocasa_para = models.IntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=-1, blank=True, null=True)
    id = models.AutoField()
    idsession = models.CharField(max_length=64)
    flag_sesion = models.IntegerField(blank=True, null=True)
    nombreciudad_para = models.CharField(max_length=64, blank=True, null=True)
    nombreciudad_de = models.CharField(max_length=64, blank=True, null=True)
    dineroelectronico = models.IntegerField(blank=True, null=True)
    dineroelectronico_propuesto = models.IntegerField(blank=True, null=True)
    pagoinicial = models.IntegerField(blank=True, null=True)
    pagoinicial_propuesto = models.IntegerField(blank=True, null=True)
    clavecliente = models.IntegerField(blank=True, null=True)
    dineroelectronicoropa = models.IntegerField(blank=True, null=True)
    dineroelectronicomuebles = models.IntegerField(blank=True, null=True)
    pagoinicialropa = models.IntegerField(blank=True, null=True)
    pagoinicialmuebles = models.IntegerField(blank=True, null=True)
    importe = models.IntegerField(blank=True, null=True)
    importeropa = models.IntegerField(blank=True, null=True)
    importemuebles = models.IntegerField(blank=True, null=True)
    pagoinicialropa_propuesto = models.IntegerField(blank=True, null=True)
    pagoinicialmuebles_propuesto = models.IntegerField(blank=True, null=True)
    dineroelectronicoropa_propuesto = models.IntegerField(blank=True, null=True)
    dineroelectronicomuebles_propuesto = models.IntegerField(blank=True, null=True)
    validacioncreditoropa_propuesto = models.IntegerField(blank=True, null=True)
    coloniaref_para = models.IntegerField(blank=True, null=True)
    flagplazo18 = models.IntegerField(blank=True, null=True)
    flagplazo18_propuesto = models.IntegerField(blank=True, null=True)
    chk_facturacion = models.IntegerField(blank=True, null=True)
    flag_dineroelectronico = models.IntegerField(blank=True, null=True)
    importemueblescredito = models.IntegerField(blank=True, null=True)
    importeropacredito = models.IntegerField(blank=True, null=True)
    validacioncreditomuebles_propuesto = models.IntegerField(blank=True, null=True)
    dineroelectronicomaximomuebles = models.IntegerField(blank=True, null=True)
    creditocoppel = models.IntegerField(blank=True, null=True)
    importemueblescredito18 = models.IntegerField(blank=True, null=True)
    folio = models.IntegerField(unique=True, blank=True, null=True)
    tipopago = models.IntegerField(blank=True, null=True)
    pagado = models.IntegerField(blank=True, null=True)
    fechamovimiento = models.DateTimeField(blank=True, null=True)
    fila = models.AutoField()
    sobreprecioropa = models.IntegerField(blank=True, null=True)
    referencia = models.CharField(max_length=-1, blank=True, null=True)
    pagorequerido = models.IntegerField(blank=True, null=True)
    pagoentregado = models.IntegerField(blank=True, null=True)
    folioropa = models.IntegerField(blank=True, null=True)
    foliomuebles = models.IntegerField(blank=True, null=True)
    facturaelectronicamuebles = models.IntegerField(blank=True, null=True)
    confirmacionapartado = models.IntegerField(blank=True, null=True)
    facturaelectronicaropa = models.IntegerField(blank=True, null=True)
    cuentabancaria = models.CharField(max_length=-1, blank=True, null=True)
    gnfechatransaccion = models.DateField(blank=True, null=True)
    flagapartado = models.IntegerField(blank=True, null=True)
    flag_guest = models.IntegerField(blank=True, null=True)
    forma_validacion = models.IntegerField(blank=True, null=True)
    nsess = models.CharField(max_length=-1, blank=True, null=True)
    flag_cancelacion = models.IntegerField(blank=True, null=True)
    flag_cat_atendido = models.BooleanField(blank=True, null=True)
    motivo_cancelacion = models.CharField(max_length=-1, blank=True, null=True)
    finalizoventa = models.BooleanField(blank=True, null=True)
    abonomensualropa = models.IntegerField(blank=True, null=True)
    nom_completousuario = models.CharField(max_length=100, blank=True, null=True)
    nom_completousuario_para = models.CharField(max_length=100, blank=True, null=True)
    num_extpara = models.CharField(max_length=6, blank=True, null=True)
    num_intpara = models.CharField(max_length=6, blank=True, null=True)
    num_opcionbloqueo = models.SmallIntegerField(blank=True, null=True)
    num_importetdcropa = models.IntegerField()
    num_importetdcmuebles = models.IntegerField()
    num_empleado = models.IntegerField()
    prc_saturacion = models.IntegerField()
    imp_nuevosaldo = models.IntegerField()
    num_puntajefinal = models.IntegerField()
    imp_pagoultimosdocemeses = models.IntegerField()
    prc_saturacion_ropa = models.IntegerField()
    imp_nuevosaldo_ropa = models.IntegerField()
    num_puntajefinal_ropa = models.IntegerField()
    imp_pagoultimosdocemeses_ropa = models.IntegerField()
    prc_saturacion_muebles = models.IntegerField()
    num_puntajefinal_muebles = models.IntegerField()
    imp_pagoultimosdocemeses_muebles = models.IntegerField()
    imp_nuevosaldo_muebles = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tb_pedidoinformacionpersonal'


class TbReferenciaBanco(models.Model):
    id = models.AutoField()
    folio = models.IntegerField(unique=True, blank=True, null=True)
    referencia = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_referencia_banco'


class TempCtlDetalleplantilla(models.Model):
    numdetalleplantilla = models.AutoField(primary_key=True)
    numdetallecaracteristica = models.IntegerField()
    numarea = models.SmallIntegerField(blank=True, null=True)
    numdepto = models.SmallIntegerField(blank=True, null=True)
    numclase = models.SmallIntegerField(blank=True, null=True)
    numfamilia = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_ctl_detalleplantilla'


class TempVtatda800(models.Model):
    hora = models.FloatField(blank=True, null=True)
    fec_movimiento = models.DateTimeField(blank=True, null=True)
    desc_canalventa = models.CharField(max_length=20, blank=True, null=True)
    idu_pedido = models.IntegerField(blank=True, null=True)
    num_clientecoppel = models.BigIntegerField(blank=True, null=True)
    num_empleadocoppel = models.IntegerField(blank=True, null=True)
    num_folioropa = models.IntegerField(blank=True, null=True)
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.IntegerField(blank=True, null=True)
    num_cantidad = models.IntegerField(blank=True, null=True)
    num_preciooriginal = models.IntegerField(blank=True, null=True)
    des_articulo = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_vtatda800'


class TempVtatda80026May(models.Model):
    mespedido = models.FloatField(blank=True, null=True)
    diapedido = models.FloatField(blank=True, null=True)
    horapedido = models.FloatField(blank=True, null=True)
    mespago = models.FloatField(blank=True, null=True)
    diapago = models.FloatField(blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    fec_movimiento = models.DateTimeField(blank=True, null=True)
    fec_facturanota = models.DateField(blank=True, null=True)
    desc_canalventa = models.CharField(max_length=20, blank=True, null=True)
    idu_pedido = models.IntegerField(blank=True, null=True)
    num_clientecoppel = models.BigIntegerField(blank=True, null=True)
    num_empleadocoppel = models.IntegerField(blank=True, null=True)
    num_folioropa = models.IntegerField(blank=True, null=True)
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.IntegerField(blank=True, null=True)
    num_cantidad = models.IntegerField(blank=True, null=True)
    num_preciooriginal = models.IntegerField(blank=True, null=True)
    des_articulo = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_vtatda80026may'


class TempVtatda800Abr(models.Model):
    hora = models.FloatField(blank=True, null=True)
    fec_movimiento = models.DateTimeField(blank=True, null=True)
    desc_canalventa = models.CharField(max_length=20, blank=True, null=True)
    idu_pedido = models.IntegerField(blank=True, null=True)
    num_clientecoppel = models.BigIntegerField(blank=True, null=True)
    num_folioropa = models.IntegerField(blank=True, null=True)
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.IntegerField(blank=True, null=True)
    num_cantidad = models.IntegerField(blank=True, null=True)
    num_preciooriginal = models.IntegerField(blank=True, null=True)
    des_articulo = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_vtatda800abr'


class TempVtatda800Ene(models.Model):
    mespedido = models.FloatField(blank=True, null=True)
    diapedido = models.FloatField(blank=True, null=True)
    horapedido = models.FloatField(blank=True, null=True)
    mespago = models.FloatField(blank=True, null=True)
    diapago = models.FloatField(blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    fec_movimiento = models.DateTimeField(blank=True, null=True)
    fec_facturanota = models.DateField(blank=True, null=True)
    desc_canalventa = models.CharField(max_length=20, blank=True, null=True)
    idu_pedido = models.IntegerField(blank=True, null=True)
    num_clientecoppel = models.BigIntegerField(blank=True, null=True)
    num_empleadocoppel = models.IntegerField(blank=True, null=True)
    num_folioropa = models.IntegerField(blank=True, null=True)
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.IntegerField(blank=True, null=True)
    num_cantidad = models.IntegerField(blank=True, null=True)
    num_preciooriginal = models.IntegerField(blank=True, null=True)
    des_articulo = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_vtatda800ene'


class TempVtatda800Feb(models.Model):
    mespedido = models.FloatField(blank=True, null=True)
    diapedido = models.FloatField(blank=True, null=True)
    hora = models.FloatField(blank=True, null=True)
    mespago = models.FloatField(blank=True, null=True)
    diapago = models.FloatField(blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    fec_movimiento = models.DateTimeField(blank=True, null=True)
    desc_canalventa = models.CharField(max_length=20, blank=True, null=True)
    idu_pedido = models.IntegerField(blank=True, null=True)
    num_clientecoppel = models.BigIntegerField(blank=True, null=True)
    num_empleadocoppel = models.IntegerField(blank=True, null=True)
    num_folioropa = models.IntegerField(blank=True, null=True)
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.IntegerField(blank=True, null=True)
    num_cantidad = models.IntegerField(blank=True, null=True)
    num_preciooriginal = models.IntegerField(blank=True, null=True)
    des_articulo = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_vtatda800feb'


class TempVtatda800Mar(models.Model):
    hora = models.FloatField(blank=True, null=True)
    fec_movimiento = models.DateTimeField(blank=True, null=True)
    desc_canalventa = models.CharField(max_length=20, blank=True, null=True)
    idu_pedido = models.IntegerField(blank=True, null=True)
    num_clientecoppel = models.BigIntegerField(blank=True, null=True)
    num_folioropa = models.IntegerField(blank=True, null=True)
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.IntegerField(blank=True, null=True)
    num_cantidad = models.IntegerField(blank=True, null=True)
    num_preciooriginal = models.IntegerField(blank=True, null=True)
    des_articulo = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_vtatda800mar'


class Tempventadia13(models.Model):
    idu_pedido = models.IntegerField(blank=True, null=True)
    fec_movimiento = models.DateTimeField(blank=True, null=True)
    fec_facturanota = models.DateField(blank=True, null=True)
    fec_orden = models.DateTimeField(blank=True, null=True)
    num_folioropa = models.IntegerField(blank=True, null=True)
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.IntegerField(blank=True, null=True)
    num_cantidad = models.IntegerField(blank=True, null=True)
    num_preciooriginal = models.IntegerField(blank=True, null=True)
    des_articulo = models.CharField(max_length=12, blank=True, null=True)
    num_estatus = models.IntegerField(blank=True, null=True)
    descripcionestatus = models.TextField(blank=True, null=True)
    num_totalarticulosropa = models.SmallIntegerField(blank=True, null=True)
    num_importeropa = models.IntegerField(blank=True, null=True)
    num_engancheropa = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempventadia13'


class TmpAreawebTemplate(models.Model):
    id = models.AutoField()
    num_areaweb = models.IntegerField(blank=True, null=True)
    num_template = models.IntegerField(blank=True, null=True)
    nom_elemento = models.CharField(max_length=20, blank=True, null=True)
    nom_ruta_imagen = models.CharField(max_length=200, blank=True, null=True)
    nom_ruta_enlace = models.CharField(max_length=200, blank=True, null=True)
    nom_alt = models.CharField(max_length=200, blank=True, null=True)
    nom_descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_areaweb_template'


class TmpCarrito(models.Model):
    id_tabla = models.SmallIntegerField(blank=True, null=True)
    idsession = models.CharField(max_length=50, blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    numarea = models.SmallIntegerField(blank=True, null=True)
    cantidad = models.SmallIntegerField(blank=True, null=True)
    talla = models.CharField(max_length=10, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    id = models.AutoField()
    flag_sesion = models.CharField(max_length=64, blank=True, null=True)
    disponibilidadarticulo = models.IntegerField(blank=True, null=True)
    fechaentregaarticulo = models.DateField(blank=True, null=True)
    armararticulo = models.IntegerField(blank=True, null=True)
    preciocontadounitario = models.IntegerField(blank=True, null=True)
    articulonuevo = models.IntegerField(blank=True, null=True)
    preciopromocion = models.IntegerField(blank=True, null=True)
    disponibilidadmuebles = models.IntegerField(blank=True, null=True)
    fechaentregamuebles = models.DateField(blank=True, null=True)
    preciocreditounitario = models.IntegerField(blank=True, null=True)
    flag_armado = models.IntegerField(blank=True, null=True)
    folio = models.IntegerField(blank=True, null=True)
    preciooriginal = models.IntegerField(blank=True, null=True)
    nomarticuloweb = models.CharField(max_length=-1, blank=True, null=True)
    nomarticulo = models.CharField(max_length=-1, blank=True, null=True)
    idu_carrito = models.BigIntegerField(blank=True, null=True)
    num_foliotelcel = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tmp_carrito'


class TmpCarritoentregadetalle(models.Model):
    id_tabla = models.SmallIntegerField(blank=True, null=True)
    folio = models.IntegerField()
    numcodigo = models.IntegerField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    bodega = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    fechaultimaactualizacion = models.DateField(blank=True, null=True)
    cvesort = models.IntegerField(blank=True, null=True)
    clavemovto = models.IntegerField(blank=True, null=True)
    id = models.AutoField()
    causa = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_carritoentregadetalle'


class TmpCatAreaswebCoppel(models.Model):
    numareaweb = models.SmallIntegerField(blank=True, null=True)
    nomareaweb = models.CharField(max_length=50, blank=True, null=True)
    numarea = models.SmallIntegerField(blank=True, null=True)
    parent_numarea_web = models.SmallIntegerField(blank=True, null=True)
    meta_keyword = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ordenamiento = models.SmallIntegerField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    flag_menu_left = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_cat_areasweb_coppel'


class TmpCatArticulos(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numdepto = models.SmallIntegerField(blank=True, null=True)
    numclase = models.SmallIntegerField(blank=True, null=True)
    numfamilia = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    modelo = models.CharField(max_length=35, blank=True, null=True)
    nummarca = models.SmallIntegerField(blank=True, null=True)
    nomarticulo = models.CharField(max_length=120, blank=True, null=True)
    descarticulo = models.TextField(blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    preciovntaint = models.IntegerField(blank=True, null=True)
    preciovntafrontera = models.IntegerField(blank=True, null=True)
    exclusivo = models.SmallIntegerField(blank=True, null=True)
    publicar = models.SmallIntegerField(blank=True, null=True)
    nuevo = models.SmallIntegerField(blank=True, null=True)
    numestatus = models.SmallIntegerField(blank=True, null=True)
    meta_keyword = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.CharField(max_length=255, blank=True, null=True)
    numdisponibilidad = models.SmallIntegerField(blank=True, null=True)
    comprar = models.SmallIntegerField(blank=True, null=True)
    entrada = models.SmallIntegerField(blank=True, null=True)
    tipoarticulo = models.SmallIntegerField(blank=True, null=True)
    flagpromocion = models.SmallIntegerField(blank=True, null=True)
    nomarticuloweb = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_cat_articulos'


class TmpCatBodzonasoficialescentralizadasetl(models.Model):
    numerocoloniacoppel = models.IntegerField(blank=True, null=True)
    nombrezona = models.CharField(max_length=30, blank=True, null=True)
    numerocodigopostal = models.IntegerField(blank=True, null=True)
    numerociudad = models.IntegerField(blank=True, null=True)
    des_ciudad = models.CharField(max_length=30)
    des_estado = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tmp_cat_bodzonasoficialescentralizadasetl'


class TmpCatClientes(models.Model):
    numusuario = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellidopaterno = models.CharField(max_length=30)
    apellidomaterno = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=-1)
    ciudad = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    calle = models.CharField(max_length=40)
    colonia = models.CharField(max_length=30)
    numcasa = models.CharField(max_length=12)
    clientecoppel = models.CharField(max_length=2)
    numclientecoppel = models.IntegerField()
    telefono = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    ext = models.CharField(max_length=20)
    cp = models.CharField(max_length=5)
    saldo = models.DecimalField(max_digits=65535, decimal_places=65535)
    otra = models.CharField(max_length=5)
    registro = models.CharField(max_length=1)
    correovalido = models.IntegerField()
    confirmado = models.CharField(max_length=1)
    interior = models.CharField(max_length=12)
    numciudad = models.IntegerField()
    numcolonia = models.IntegerField()
    numcalle = models.IntegerField()
    fechanacimiento = models.DateField()
    sexo = models.BooleanField()
    fecharegistro = models.DateField()
    celular = models.CharField(max_length=128, blank=True, null=True)
    entrecalles = models.CharField(max_length=-1, blank=True, null=True)
    domicilioobservaciones = models.CharField(max_length=-1, blank=True, null=True)
    id = models.AutoField()
    fechacreacion = models.DateTimeField(blank=True, null=True)
    fec_actualizacion = models.DateTimeField(blank=True, null=True)
    tipo_registro = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tmp_cat_clientes'


class TmpCatGaleriaarticulo(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    nomimagen = models.CharField(max_length=30, blank=True, null=True)
    numgaleria = models.BigIntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_cat_galeriaarticulo'


class TmpCategorias(models.Model):
    numcodigo = models.IntegerField()
    numarea = models.SmallIntegerField()
    numdepto = models.SmallIntegerField()
    numclase = models.SmallIntegerField()
    numfamilia = models.SmallIntegerField()
    code = models.CharField(max_length=256, blank=True, null=True)
    numareaweb = models.SmallIntegerField()
    nomareaweb = models.CharField(max_length=256, blank=True, null=True)
    parent = models.SmallIntegerField()
    cant = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tmp_categorias'


class TmpClientes(models.Model):
    numusuario = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    apellidopaterno = models.CharField(max_length=30, blank=True, null=True)
    apellidomaterno = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=-1, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    pais = models.CharField(max_length=20, blank=True, null=True)
    calle = models.CharField(max_length=40, blank=True, null=True)
    colonia = models.CharField(max_length=30, blank=True, null=True)
    numcasa = models.CharField(max_length=12, blank=True, null=True)
    clientecoppel = models.CharField(max_length=2, blank=True, null=True)
    numclientecoppel = models.IntegerField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    ext = models.CharField(max_length=20, blank=True, null=True)
    cp = models.CharField(max_length=5, blank=True, null=True)
    saldo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    otra = models.CharField(max_length=5, blank=True, null=True)
    registro = models.CharField(max_length=1, blank=True, null=True)
    correovalido = models.IntegerField(blank=True, null=True)
    confirmado = models.CharField(max_length=1, blank=True, null=True)
    interior = models.CharField(max_length=12, blank=True, null=True)
    numciudad = models.IntegerField(blank=True, null=True)
    numcolonia = models.IntegerField(blank=True, null=True)
    numcalle = models.IntegerField(blank=True, null=True)
    fechanacimiento = models.DateField(blank=True, null=True)
    sexo = models.BooleanField(blank=True, null=True)
    fecharegistro = models.DateField(blank=True, null=True)
    celular = models.CharField(max_length=128, blank=True, null=True)
    entrecalles = models.CharField(max_length=-1, blank=True, null=True)
    domicilioobservaciones = models.CharField(max_length=-1, blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    fechacreacion = models.DateTimeField(blank=True, null=True)
    fec_actualizacion = models.DateTimeField(blank=True, null=True)
    tipo_registro = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_clientes'


class TmpClientescarterasecommerce(models.Model):
    num_cliente = models.FloatField(blank=True, null=True)
    num_telefonocasa = models.FloatField(blank=True, null=True)
    num_telefonocelular = models.FloatField(blank=True, null=True)
    des_estatustelefonocasa = models.TextField(blank=True, null=True)
    des_estatustelefonocelular = models.TextField(blank=True, null=True)
    flg_flagclienteactivo = models.FloatField(blank=True, null=True)
    fec_fechaultimoabono = models.DateTimeField(blank=True, null=True)
    fec_fechaaltacartera = models.DateTimeField(blank=True, null=True)
    des_sexo = models.TextField(blank=True, null=True)
    des_complemento = models.TextField(blank=True, null=True)
    num_altatienda = models.FloatField(blank=True, null=True)
    fec_fecha = models.DateTimeField(blank=True, null=True)
    fec_nacimiento = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_clientescarterasecommerce'


class TmpClientesrecargas(models.Model):
    des_correoelectronico = models.CharField(max_length=300)
    idu_clientecodigo = models.CharField(primary_key=True, max_length=-1)
    num_cantidadrecargas = models.CharField(max_length=-1, blank=True, null=True)
    imp_importerecargas = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_clientesrecargas'


class TmpColoniasmal(models.Model):
    num_bodega = models.SmallIntegerField(blank=True, null=True)
    num_ciudad = models.SmallIntegerField(blank=True, null=True)
    num_zona = models.IntegerField(blank=True, null=True)
    nom_zona = models.CharField(max_length=30, blank=True, null=True)
    num_ruta = models.SmallIntegerField(blank=True, null=True)
    num_ciudadpertenece = models.SmallIntegerField(blank=True, null=True)
    num_orden = models.IntegerField(blank=True, null=True)
    des_latitud = models.CharField(max_length=20, blank=True, null=True)
    des_longitud = models.CharField(max_length=20, blank=True, null=True)
    des_estado = models.CharField(max_length=30, blank=True, null=True)
    des_ciudad = models.CharField(max_length=30, blank=True, null=True)
    des_colonia = models.CharField(max_length=30, blank=True, null=True)
    num_codigopostal = models.IntegerField(blank=True, null=True)
    fec_ultimomovto = models.DateField(blank=True, null=True)
    nom_empultimomovto = models.CharField(max_length=60, blank=True, null=True)
    num_prioridad = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_coloniasmal'


class TmpCtlSurtidoRopaAntes(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    cantidad = models.SmallIntegerField(blank=True, null=True)
    talla = models.SmallIntegerField(blank=True, null=True)
    folio = models.IntegerField(blank=True, null=True)
    fechaventa = models.DateField(blank=True, null=True)
    numbodega = models.SmallIntegerField(blank=True, null=True)
    tipoventa = models.CharField(max_length=1, blank=True, null=True)
    flagsurtido = models.CharField(max_length=1, blank=True, null=True)
    fechaactualiza = models.DateTimeField(blank=True, null=True)
    num_empleado = models.IntegerField(blank=True, null=True)
    num_folioorden = models.BigIntegerField(blank=True, null=True)
    flag_ordensingle = models.IntegerField(blank=True, null=True)
    fec_nota = models.DateTimeField(blank=True, null=True)
    fec_surtiroficina = models.DateField(blank=True, null=True)
    fec_notatienda = models.DateField(blank=True, null=True)
    fec_concentrado = models.DateTimeField(blank=True, null=True)
    fec_procesado = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_ctl_surtido_ropa_antes'


class TmpDataloadColonias(models.Model):
    address_id = models.BigIntegerField(blank=True, null=True)
    id_colonia = models.CharField(max_length=-1, blank=True, null=True)
    id_ciudad = models.CharField(max_length=-1, blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    zipcode = models.CharField(max_length=-1, blank=True, null=True)
    lastcreate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_dataload_colonias'


class TmpDatosArticuloDetalle(models.Model):
    num_codigo = models.IntegerField()
    num_area = models.SmallIntegerField()
    num_depto = models.SmallIntegerField()
    num_clase = models.SmallIntegerField()
    num_familia = models.SmallIntegerField()
    nom_articulo = models.CharField(max_length=-1, blank=True, null=True)
    nom_marca = models.CharField(max_length=-1, blank=True, null=True)
    nom_modelo = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_datos_articulo_detalle'


class TmpDatosCatalogo(models.Model):
    nom_nivel1 = models.CharField(max_length=-1)
    nom_nivel2 = models.CharField(max_length=-1)
    nom_nivel3 = models.CharField(max_length=-1)
    nom_url = models.CharField(max_length=-1)
    num_areaweb = models.SmallIntegerField()
    flag_activo = models.BooleanField()
    num_parent_areaweb = models.SmallIntegerField()
    num_area = models.SmallIntegerField()
    num_depto = models.SmallIntegerField()
    num_clase = models.SmallIntegerField()
    num_familia = models.SmallIntegerField()
    nivel1_real = models.CharField(max_length=-1)
    nivel2_real = models.CharField(max_length=-1)
    nivel3_real = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'tmp_datos_catalogo'


class TmpEnviocorreos(models.Model):
    email = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tmp_enviocorreos'


class TmpFallaestatusGuias(models.Model):
    num_guia = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'tmp_fallaestatus_guias'


class TmpGaleriaarticuloCount(models.Model):
    numarea = models.SmallIntegerField()
    numcodigo = models.IntegerField()
    numimagenes = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tmp_galeriaarticulo_count'


class TmpGerentestiendasSitetostore(models.Model):
    nom_gerente = models.CharField(max_length=80, blank=True, null=True)
    num_tienda = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_gerentestiendas_sitetostore'


class TmpMaeExistenciasAntes(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numbodega = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    numtalla = models.SmallIntegerField(blank=True, null=True)
    precioventa = models.IntegerField(blank=True, null=True)
    disponible = models.IntegerField(blank=True, null=True)
    tipoarticulo = models.SmallIntegerField(blank=True, null=True)
    preciocredito = models.IntegerField(blank=True, null=True)
    preciofrontera = models.IntegerField(blank=True, null=True)
    num_existencia = models.SmallIntegerField(blank=True, null=True)
    agotado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_mae_existencias_antes'


class TmpMaeInventarios(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numbodega = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    numtalla = models.SmallIntegerField(blank=True, null=True)
    precioventa = models.IntegerField(blank=True, null=True)
    disponible = models.IntegerField(blank=True, null=True)
    tipoarticulo = models.SmallIntegerField(blank=True, null=True)
    preciocredito = models.IntegerField(blank=True, null=True)
    preciofrontera = models.IntegerField(blank=True, null=True)
    num_existencia = models.SmallIntegerField(blank=True, null=True)
    agotado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_mae_inventarios'


class TmpMenuCoppelCom(models.Model):
    categoria = models.CharField(max_length=100)
    seccion = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    keywords = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'tmp_menu_coppel_com'


class TmpMenuCoppelTotal(models.Model):
    num1 = models.SmallIntegerField(blank=True, null=True)
    nom1 = models.CharField(max_length=50, blank=True, null=True)
    num2 = models.SmallIntegerField(blank=True, null=True)
    nom2 = models.CharField(max_length=50, blank=True, null=True)
    nom3 = models.CharField(max_length=50, blank=True, null=True)
    num3 = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_menu_coppel_total'


class TmpMovDeltasExclusivosCoppel(models.Model):
    numcodigo = models.IntegerField()
    numarea = models.SmallIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'tmp_mov_deltas_exclusivos_coppel'
        unique_together = (('numarea', 'numcodigo'),)


class TmpMovDeltasmarketplaceProductos(models.Model):
    idu_producto = models.BigIntegerField(primary_key=True)
    partnumber = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    name = models.CharField(max_length=2000)
    shortdescription = models.CharField(max_length=254)
    longdescription = models.CharField(max_length=4000)
    thumbnail = models.CharField(max_length=254)
    fullimage = models.CharField(max_length=254)
    published = models.SmallIntegerField()
    keyword = models.CharField(max_length=254)
    delete = models.SmallIntegerField()
    manufacturerpartnumber = models.CharField(max_length=64)
    manufacturer = models.CharField(max_length=64)
    url = models.CharField(max_length=254)
    field1 = models.IntegerField()
    field2 = models.IntegerField()
    field3 = models.FloatField()
    field4 = models.CharField(max_length=254)
    field5 = models.CharField(max_length=254)
    buyable = models.IntegerField()
    parentpartnumber = models.CharField(max_length=64)
    urlkeyword = models.CharField(max_length=254)
    metadescription = models.CharField(max_length=1024)
    pagetitle = models.CharField(max_length=254)
    idu_carga = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tmp_mov_deltasmarketplace_productos'
        unique_together = (('idu_producto', 'partnumber'),)


class TmpMovVentaRopaAntes(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    cantidad = models.SmallIntegerField(blank=True, null=True)
    talla = models.CharField(max_length=-1, blank=True, null=True)
    folio = models.IntegerField(blank=True, null=True)
    fechaventa = models.DateField(blank=True, null=True)
    numbodega = models.SmallIntegerField(blank=True, null=True)
    tipoventa = models.CharField(max_length=1, blank=True, null=True)
    flagsurtido = models.CharField(max_length=1, blank=True, null=True)
    flagenviado = models.CharField(max_length=1, blank=True, null=True)
    flagapartado = models.CharField(max_length=1, blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    id_serial = models.IntegerField(blank=True, null=True)
    nu_guia = models.CharField(max_length=25, blank=True, null=True)
    flagvendido = models.CharField(max_length=1, blank=True, null=True)
    sn_codigo_confirmado = models.IntegerField(blank=True, null=True)
    sn_impreso = models.IntegerField(blank=True, null=True)
    precio_surtido = models.IntegerField(blank=True, null=True)
    fh_surtido = models.DateTimeField(blank=True, null=True)
    flag_ordensingle = models.IntegerField(blank=True, null=True)
    flag_statuscodigo = models.IntegerField(blank=True, null=True)
    num_foliomp = models.BigIntegerField(blank=True, null=True)
    num_tipoembalaje = models.SmallIntegerField(blank=True, null=True)
    idu_paquetera = models.IntegerField(blank=True, null=True)
    idu_multicarrier = models.IntegerField(blank=True, null=True)
    flag_contingencia = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_mov_venta_ropa_antes'


class TmpNombreweb(models.Model):
    codigo = models.IntegerField()
    nombreweb = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'tmp_nombreweb'


class TmpNombrewebBkp(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    nomarticuloweb = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_nombreweb_bkp'


class TmpNombrewebRes(models.Model):
    codigo = models.IntegerField(blank=True, null=True)
    nombreweb = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_nombreweb_res'


class TmpNotascompletas(models.Model):
    num_notafactura = models.BigIntegerField(blank=True, null=True)
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.IntegerField(blank=True, null=True)
    nom_posicion = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_notascompletas'


class TmpNotaspendientes(models.Model):
    num_notafactura = models.IntegerField(blank=True, null=True)
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_notaspendientes'


class TmpPedidoinformaciongeneral(models.Model):
    id_tabla = models.SmallIntegerField(blank=True, null=True)
    cc_vencido = models.CharField(max_length=-1, blank=True, null=True)
    sobreprecio12 = models.IntegerField(blank=True, null=True)
    sobreprecio18 = models.IntegerField(blank=True, null=True)
    folio = models.IntegerField(blank=True, null=True)
    puntajeparcelulares = models.IntegerField(blank=True, null=True)
    puntajeparaltoriesgo = models.IntegerField(blank=True, null=True)
    sobreprecioropa = models.IntegerField(blank=True, null=True)
    tasainteresropa = models.IntegerField(blank=True, null=True)
    cc_vencidoropa = models.CharField(max_length=-1, blank=True, null=True)
    nuevosaldoropa = models.IntegerField(blank=True, null=True)
    importeropa = models.IntegerField(blank=True, null=True)
    saldoropa = models.IntegerField(blank=True, null=True)
    importemuebles = models.IntegerField(blank=True, null=True)
    pagoinicialropa = models.IntegerField(blank=True, null=True)
    pagoinicialmuebles = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_pedidoinformaciongeneral'


class TmpPedidoinformacionpersonal(models.Model):
    id_tabla = models.SmallIntegerField(blank=True, null=True)
    nombre_de = models.CharField(max_length=-1, blank=True, null=True)
    apellidopaterno_de = models.CharField(max_length=-1, blank=True, null=True)
    apellidomaterno_de = models.CharField(max_length=-1, blank=True, null=True)
    telefono_de = models.CharField(max_length=-1, blank=True, null=True)
    celular_de = models.CharField(max_length=-1, blank=True, null=True)
    email_de = models.CharField(max_length=-1, blank=True, null=True)
    nombre_para = models.CharField(max_length=-1, blank=True, null=True)
    apellidopaterno_para = models.CharField(max_length=-1, blank=True, null=True)
    apellidomaterno_para = models.CharField(max_length=-1, blank=True, null=True)
    estado_para = models.CharField(max_length=-1, blank=True, null=True)
    ciudad_para = models.CharField(max_length=-1, blank=True, null=True)
    colonia_para = models.CharField(max_length=-1, blank=True, null=True)
    calle_para = models.CharField(max_length=-1, blank=True, null=True)
    entrecalles_para = models.CharField(max_length=-1, blank=True, null=True)
    codigopostal_para = models.CharField(max_length=-1, blank=True, null=True)
    numerocasa_para = models.IntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=-1, blank=True, null=True)
    id = models.AutoField()
    idsession = models.CharField(max_length=64)
    flag_sesion = models.IntegerField(blank=True, null=True)
    nombreciudad_para = models.CharField(max_length=64, blank=True, null=True)
    nombreciudad_de = models.CharField(max_length=64, blank=True, null=True)
    dineroelectronico = models.IntegerField(blank=True, null=True)
    dineroelectronico_propuesto = models.IntegerField(blank=True, null=True)
    pagoinicial = models.IntegerField(blank=True, null=True)
    pagoinicial_propuesto = models.IntegerField(blank=True, null=True)
    clavecliente = models.IntegerField(blank=True, null=True)
    dineroelectronicoropa = models.IntegerField(blank=True, null=True)
    dineroelectronicomuebles = models.IntegerField(blank=True, null=True)
    pagoinicialropa = models.IntegerField(blank=True, null=True)
    pagoinicialmuebles = models.IntegerField(blank=True, null=True)
    importe = models.IntegerField(blank=True, null=True)
    importeropa = models.IntegerField(blank=True, null=True)
    importemuebles = models.IntegerField(blank=True, null=True)
    pagoinicialropa_propuesto = models.IntegerField(blank=True, null=True)
    pagoinicialmuebles_propuesto = models.IntegerField(blank=True, null=True)
    dineroelectronicoropa_propuesto = models.IntegerField(blank=True, null=True)
    dineroelectronicomuebles_propuesto = models.IntegerField(blank=True, null=True)
    validacioncreditoropa_propuesto = models.IntegerField(blank=True, null=True)
    coloniaref_para = models.IntegerField(blank=True, null=True)
    flagplazo18 = models.IntegerField(blank=True, null=True)
    flagplazo18_propuesto = models.IntegerField(blank=True, null=True)
    chk_facturacion = models.IntegerField(blank=True, null=True)
    flag_dineroelectronico = models.IntegerField(blank=True, null=True)
    importemueblescredito = models.IntegerField(blank=True, null=True)
    importeropacredito = models.IntegerField(blank=True, null=True)
    validacioncreditomuebles_propuesto = models.IntegerField(blank=True, null=True)
    dineroelectronicomaximomuebles = models.IntegerField(blank=True, null=True)
    creditocoppel = models.IntegerField(blank=True, null=True)
    importemueblescredito18 = models.IntegerField(blank=True, null=True)
    sobreprecioropa = models.IntegerField(blank=True, null=True)
    gnfechatransaccion = models.DateField(blank=True, null=True)
    cuentabancaria = models.IntegerField(blank=True, null=True)
    fechagndominio = models.DateField(blank=True, null=True)
    tiempoactualizacion = models.DateTimeField(blank=True, null=True)
    referencia = models.CharField(max_length=16, blank=True, null=True)
    nsess = models.CharField(max_length=-1, blank=True, null=True)
    seq_abc = models.IntegerField(blank=True, null=True)
    seq_carrito = models.IntegerField(blank=True, null=True)
    seq_orden = models.IntegerField(blank=True, null=True)
    seq_credito = models.IntegerField(blank=True, null=True)
    tipopago = models.IntegerField(blank=True, null=True)
    fechaultimaoperacion = models.DateTimeField(blank=True, null=True)
    tokenorden = models.CharField(max_length=-1, blank=True, null=True)
    pagoinicialropa_cliente = models.IntegerField(blank=True, null=True)
    pagoinicialmuebles_cliente = models.IntegerField(blank=True, null=True)
    pagoinicial_cliente = models.IntegerField(blank=True, null=True)
    dateultimaoperacion = models.DateTimeField(blank=True, null=True)
    flag_guest = models.IntegerField(blank=True, null=True)
    forma_validacion = models.IntegerField(blank=True, null=True)
    fechacreacion = models.DateTimeField(blank=True, null=True)
    nom_completousuario = models.CharField(max_length=100, blank=True, null=True)
    nom_completousuario_para = models.CharField(max_length=100, blank=True, null=True)
    num_extpara = models.CharField(max_length=6, blank=True, null=True)
    num_intpara = models.CharField(max_length=6, blank=True, null=True)
    num_opcionbloqueo = models.SmallIntegerField(blank=True, null=True)
    num_importetdcropa = models.IntegerField()
    num_importetdcmuebles = models.IntegerField()
    num_empleado = models.IntegerField()
    folio = models.IntegerField(blank=True, null=True)
    pagado = models.IntegerField(blank=True, null=True)
    fechamovimiento = models.DateTimeField(blank=True, null=True)
    pagorequerido = models.IntegerField(blank=True, null=True)
    pagoentregado = models.IntegerField(blank=True, null=True)
    folioropa = models.IntegerField(blank=True, null=True)
    foliomuebles = models.IntegerField(blank=True, null=True)
    facturaelectronicamuebles = models.IntegerField(blank=True, null=True)
    confirmacionapartado = models.IntegerField(blank=True, null=True)
    facturaelectronicaropa = models.IntegerField(blank=True, null=True)
    flagapartado = models.IntegerField(blank=True, null=True)
    flag_cancelacion = models.IntegerField(blank=True, null=True)
    flag_cat_atendido = models.BooleanField(blank=True, null=True)
    motivo_cancelacion = models.CharField(max_length=-1, blank=True, null=True)
    finalizoventa = models.BooleanField(blank=True, null=True)
    abonomensualropa = models.IntegerField(blank=True, null=True)
    prc_saturacion = models.IntegerField()
    imp_nuevosaldo = models.IntegerField()
    num_puntajefinal = models.IntegerField()
    imp_pagoultimosdocemeses = models.IntegerField()
    prc_saturacion_ropa = models.IntegerField()
    imp_nuevosaldo_ropa = models.IntegerField()
    num_puntajefinal_ropa = models.IntegerField()
    imp_pagoultimosdocemeses_ropa = models.IntegerField()
    prc_saturacion_muebles = models.IntegerField()
    imp_nuevosaldo_muebles = models.IntegerField()
    num_puntajefinal_muebles = models.IntegerField()
    imp_pagoultimosdocemeses_muebles = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tmp_pedidoinformacionpersonal'


class TmpPedidositemmarketplace(models.Model):
    idu_tmppedidosmk = models.BigAutoField(primary_key=True)
    idu_pedidosmkpl = models.ForeignKey(CtlPedidosmarketplace, models.DO_NOTHING, db_column='idu_pedidosmkpl')
    idu_detallepedidomk = models.ForeignKey(CtlDetallepedidosmarketplace, models.DO_NOTHING, db_column='idu_detallepedidomk')
    idu_estatusordenmk = models.ForeignKey(CatEstatusordenmarketplace, models.DO_NOTHING, db_column='idu_estatusordenmk')
    des_status_item = models.CharField(max_length=30)
    des_status_pedido = models.CharField(max_length=30)
    des_error_tmp = models.CharField(max_length=500)
    fec_creacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tmp_pedidositemmarketplace'


class TmpPedidosmueblesOficinadeenvios(models.Model):
    des_correoelectronico = models.CharField(max_length=100)
    idu_clientecodigo = models.CharField(max_length=20)
    nom_cliente = models.CharField(max_length=200)
    des_domicilio = models.CharField(max_length=200)
    des_observaciones = models.CharField(max_length=200)
    nom_recibe = models.CharField(max_length=100)
    num_telefono = models.CharField(max_length=20)
    num_telefonoquienrecibe = models.CharField(max_length=20)
    sec_orden = models.CharField(max_length=10)
    sec_factura = models.CharField(max_length=10)
    des_tipopago = models.CharField(max_length=100)
    num_cantidad = models.CharField(max_length=10)
    imp_totalfacturadocontado = models.CharField(max_length=10)
    fec_fechaorden = models.CharField(max_length=10)
    nom_ciudadrecibe = models.CharField(max_length=50)
    nom_estadorecibe = models.CharField(max_length=50)
    nom_bodegatraspaso = models.CharField(max_length=50)
    fec_fechapromesa = models.CharField(max_length=10)
    idu_articulocodigo = models.CharField(max_length=10)
    des_articulocodigo = models.CharField(max_length=120)
    des_centrodistribucion = models.CharField(max_length=50)
    des_estatusentrega = models.CharField(max_length=100)
    fec_fechastatus = models.CharField(max_length=10)
    idu_bodegacodigo = models.CharField(max_length=10)
    nom_bodegaentrega = models.CharField(max_length=50)
    des_tipoentrega = models.CharField(max_length=5)
    num_tienda = models.CharField(max_length=10)
    fec_entregarealizada = models.CharField(max_length=10)
    fec_entradatienda = models.CharField(max_length=10)
    idu_pedido = models.IntegerField()
    num_bodegatraspaso = models.IntegerField()
    num_bodegaentrega = models.IntegerField()
    num_area = models.IntegerField()
    num_ciudad = models.IntegerField()
    fec_activacion = models.CharField(max_length=10)
    des_estatus = models.CharField(max_length=50)
    idu_conexion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tmp_pedidosmuebles_oficinadeenvios'


class TmpPreciosDb2(models.Model):
    codigo = models.IntegerField(blank=True, null=True)
    precio_lista = models.IntegerField(blank=True, null=True)
    precio_promocion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_precios_db2'


class TmpPreciosDl(models.Model):
    sku = models.CharField(max_length=254)
    price = models.CharField(max_length=14)

    class Meta:
        managed = False
        db_table = 'tmp_precios_dl'


class TmpPreclasificados(models.Model):
    num_notafactura = models.IntegerField(blank=True, null=True)
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_preclasificados'


class TmpProductosPrimerNivel(models.Model):
    numarea = models.SmallIntegerField()
    numdepto = models.SmallIntegerField()
    numclase = models.SmallIntegerField()
    numfamilia = models.SmallIntegerField()
    numcodigo = models.IntegerField()
    nomarticuloweb = models.CharField(max_length=254)
    nivel = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tmp_productos_primer_nivel'


class TmpProductosSegundoNivel(models.Model):
    numarea = models.SmallIntegerField()
    numdepto = models.SmallIntegerField()
    numclase = models.SmallIntegerField()
    numfamilia = models.SmallIntegerField()
    numcodigo = models.IntegerField()
    nomarticuloweb = models.CharField(max_length=254)
    nivel = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tmp_productos_segundo_nivel'


class TmpPruebablacklist(models.Model):
    secuencia = models.AutoField()
    auxiliar = models.IntegerField(blank=True, null=True)
    cve_identidad = models.IntegerField(blank=True, null=True)
    cve_domicilio = models.IntegerField(blank=True, null=True)
    cve_orden = models.IntegerField(blank=True, null=True)
    respuesta = models.IntegerField(blank=True, null=True)
    resultado = models.IntegerField(blank=True, null=True)
    tarjeta = models.CharField(max_length=-1, blank=True, null=True)
    proceso = models.CharField(max_length=-1, blank=True, null=True)
    fol_secuencia = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_pruebablacklist'


class TmpSecuenciaTercerNiveles(models.Model):
    partnumber = models.CharField(max_length=254, blank=True, null=True)
    parentgroupidentifier = models.CharField(max_length=254, blank=True, null=True)
    seq = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_secuencia_tercer_niveles'


class TmpSoclientesupervisarFiltrado(models.Model):
    num_solicitud = models.IntegerField(blank=True, null=True)
    status_solicitud = models.CharField(max_length=1, blank=True, null=True)
    situacionespecial = models.CharField(max_length=1, blank=True, null=True)
    causasituacionespecial = models.SmallIntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=15, blank=True, null=True)
    apellidopaterno = models.CharField(max_length=15, blank=True, null=True)
    apellidomaterno = models.CharField(max_length=15, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    estadocivil = models.CharField(max_length=1, blank=True, null=True)
    fechanacimiento = models.DateField(blank=True, null=True)
    num_tienda = models.SmallIntegerField(blank=True, null=True)
    correoelectronico = models.CharField(max_length=60, blank=True, null=True)
    num_telefono = models.IntegerField(blank=True, null=True)
    num_telefonocelular = models.BigIntegerField(blank=True, null=True)
    num_ciudad = models.SmallIntegerField(blank=True, null=True)
    puntosparcn = models.SmallIntegerField(blank=True, null=True)
    tipoos = models.CharField(max_length=1, blank=True, null=True)
    tipoproducto = models.CharField(max_length=5, blank=True, null=True)
    fechaaltacliente = models.DateField(blank=True, null=True)
    fechamovto = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_soclientesupervisar_filtrado'


class TmpSoclientesupervisarFiltradoRestriccion(models.Model):
    num_solicitud = models.IntegerField(blank=True, null=True)
    status_solicitud = models.CharField(max_length=1, blank=True, null=True)
    num_tienda = models.SmallIntegerField(blank=True, null=True)
    fechamovto = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_soclientesupervisar_filtrado_restriccion'


class TmpSoclientesupervisarRefiltrado(models.Model):
    num_solicitud = models.IntegerField(blank=True, null=True)
    status_solicitud = models.CharField(max_length=1, blank=True, null=True)
    situacionespecial = models.CharField(max_length=1, blank=True, null=True)
    causasituacionespecial = models.SmallIntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=15, blank=True, null=True)
    apellidopaterno = models.CharField(max_length=15, blank=True, null=True)
    apellidomaterno = models.CharField(max_length=15, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    estadocivil = models.CharField(max_length=1, blank=True, null=True)
    fechanacimiento = models.DateField(blank=True, null=True)
    num_tienda = models.SmallIntegerField(blank=True, null=True)
    correoelectronico = models.CharField(max_length=60, blank=True, null=True)
    num_telefono = models.IntegerField(blank=True, null=True)
    num_telefonocelular = models.BigIntegerField(blank=True, null=True)
    num_ciudad = models.SmallIntegerField(blank=True, null=True)
    puntosparcn = models.SmallIntegerField(blank=True, null=True)
    tipoos = models.CharField(max_length=1, blank=True, null=True)
    tipoproducto = models.CharField(max_length=5, blank=True, null=True)
    fechaaltacliente = models.DateField(blank=True, null=True)
    fechamovto = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_soclientesupervisar_refiltrado'


class TmpTemporalfamiliacomplementaria(models.Model):
    idu_familiacomplementaria = models.IntegerField()
    idu_familiapivote = models.IntegerField()
    idu_area = models.IntegerField()
    idu_departamento = models.IntegerField()
    idu_clase = models.IntegerField()
    idu_familia = models.IntegerField()
    opc_estatus = models.SmallIntegerField()
    num_prioridad = models.IntegerField()
    idu_usuario = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tmp_temporalfamiliacomplementaria'


class TmpTipoArticulo(models.Model):
    numarea = models.SmallIntegerField(blank=True, null=True)
    numbodega = models.SmallIntegerField(blank=True, null=True)
    numcodigo = models.IntegerField(blank=True, null=True)
    numtalla = models.SmallIntegerField(blank=True, null=True)
    precioventa = models.IntegerField(blank=True, null=True)
    disponible = models.IntegerField(blank=True, null=True)
    tipoarticulo = models.SmallIntegerField(blank=True, null=True)
    preciocredito = models.IntegerField(blank=True, null=True)
    preciofrontera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_tipo_articulo'


class TmpUnidadesropaActuales(models.Model):
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.IntegerField(blank=True, null=True)
    num_bodega = models.SmallIntegerField(blank=True, null=True)
    num_unidades = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_unidadesropa_actuales'


class TmpUnidadesropaIniciales(models.Model):
    num_codigo = models.IntegerField(blank=True, null=True)
    num_talla = models.IntegerField(blank=True, null=True)
    num_bodega = models.SmallIntegerField(blank=True, null=True)
    num_unidades = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_unidadesropa_iniciales'


class TmpVentaporrOficinadeenvios(models.Model):
    num_factura = models.IntegerField()
    num_codigo = models.IntegerField()
    num_tienda = models.IntegerField()
    telefono_quien_recoge = models.CharField(max_length=20)
    nom_recibe = models.CharField(max_length=100)
    fec_entregarealizada = models.CharField(max_length=10)
    fec_entradatienda = models.CharField(max_length=10)
    fec_activacion = models.CharField(max_length=10)
    des_estatus = models.CharField(max_length=50)
    idu_conexion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tmp_ventaporr_oficinadeenvios'


class TmpXcitystore(models.Model):
    code_city = models.IntegerField(blank=True, null=True)
    stateprovabbr = models.IntegerField(blank=True, null=True)
    language_id = models.TextField(blank=True, null=True)
    coppel_name_city = models.TextField(blank=True, null=True)
    geoloc_name_city = models.TextField(blank=True, null=True)
    store_name = models.CharField(max_length=50, blank=True, null=True)
    store_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_xcitystore'


class TmpZonascondosbodegas3(models.Model):
    num_bodega = models.SmallIntegerField(blank=True, null=True)
    num_ciudad = models.SmallIntegerField(blank=True, null=True)
    num_zona = models.IntegerField(blank=True, null=True)
    nom_zona = models.CharField(max_length=30, blank=True, null=True)
    num_ruta = models.SmallIntegerField(blank=True, null=True)
    num_ciudadpertenece = models.SmallIntegerField(blank=True, null=True)
    num_orden = models.IntegerField(blank=True, null=True)
    des_latitud = models.CharField(max_length=20, blank=True, null=True)
    des_longitud = models.CharField(max_length=20, blank=True, null=True)
    des_estado = models.CharField(max_length=35, blank=True, null=True)
    des_ciudad = models.CharField(max_length=60, blank=True, null=True)
    des_colonia = models.CharField(max_length=60, blank=True, null=True)
    num_codigopostal = models.IntegerField(blank=True, null=True)
    fec_ultimomovto = models.DateTimeField(blank=True, null=True)
    nom_empultimomovto = models.CharField(max_length=60, blank=True, null=True)
    num_prioridad = models.SmallIntegerField(blank=True, null=True)
    flg_actualizado = models.SmallIntegerField(blank=True, null=True)
    keyx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_zonascondosbodegas3'


class TmpZonasycoloniasligadas(models.Model):
    num_bodega = models.SmallIntegerField()
    num_ciudad = models.SmallIntegerField()
    num_zona = models.IntegerField()
    nom_zona = models.CharField(max_length=30)
    num_ruta = models.SmallIntegerField()
    num_ciudadpertenece = models.SmallIntegerField()
    num_orden = models.IntegerField()
    des_latitud = models.CharField(max_length=20)
    des_longitud = models.CharField(max_length=20)
    num_codigopostal = models.IntegerField()
    fec_ultimomovto = models.CharField(max_length=10, blank=True, null=True)
    nom_empultimomovto = models.CharField(max_length=60)
    num_prioridad = models.SmallIntegerField()
    flg_actualizado = models.SmallIntegerField()
    keyx = models.IntegerField(blank=True, null=True)
    num_cedisropa = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_zonasycoloniasligadas'


class Tmpdatosde(models.Model):
    num_clientecoppel = models.BigIntegerField(blank=True, null=True)
    folioorden = models.BigIntegerField(blank=True, null=True)
    factura = models.IntegerField(blank=True, null=True)
    nota = models.IntegerField(blank=True, null=True)
    fechaprimeracomprade = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmpdatosde'


class Tmpdatosnode(models.Model):
    num_clientecoppel = models.BigIntegerField(blank=True, null=True)
    folioorden = models.BigIntegerField(blank=True, null=True)
    factura = models.IntegerField(blank=True, null=True)
    nota = models.IntegerField(blank=True, null=True)
    fechaprimeracomprade = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmpdatosnode'


class Tmplgpagos(models.Model):
    idu_pedido = models.IntegerField(blank=True, null=True)
    nom_email = models.CharField(max_length=-1, blank=True, null=True)
    num_clientecoppel = models.BigIntegerField(blank=True, null=True)
    num_empleadocoppel = models.IntegerField(blank=True, null=True)
    nom_cliente = models.CharField(max_length=-1, blank=True, null=True)
    nom_apepaterno = models.CharField(max_length=100, blank=True, null=True)
    nom_apematerno = models.CharField(max_length=100, blank=True, null=True)
    num_importetotal = models.IntegerField(blank=True, null=True)
    fec_orden = models.DateTimeField(blank=True, null=True)
    num_telefono = models.CharField(max_length=20, blank=True, null=True)
    opc_celular = models.BooleanField(blank=True, null=True)
    num_folio = models.BigIntegerField(blank=True, null=True)
    num_estatus = models.IntegerField(blank=True, null=True)
    num_totalarticulosmuebles = models.SmallIntegerField(blank=True, null=True)
    num_totalarticulosropa = models.SmallIntegerField(blank=True, null=True)
    num_importeropa = models.IntegerField(blank=True, null=True)
    num_importemuebles = models.IntegerField(blank=True, null=True)
    num_engancheropa = models.IntegerField(blank=True, null=True)
    des_articulo = models.CharField(max_length=12, blank=True, null=True)
    num_enganchemuebles = models.IntegerField(blank=True, null=True)
    num_folioropa = models.IntegerField(blank=True, null=True)
    num_foliomuebles = models.IntegerField(blank=True, null=True)
    fec_movimiento = models.DateTimeField(blank=True, null=True)
    num_pagorecibido = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmplgpagos'


class Tmptodasdetallepedido(models.Model):
    idu_pedido = models.IntegerField(blank=True, null=True)
    nom_email = models.CharField(max_length=-1, blank=True, null=True)
    num_clientecoppel = models.BigIntegerField(blank=True, null=True)
    num_empleadocoppel = models.IntegerField(blank=True, null=True)
    nom_cliente = models.CharField(max_length=-1, blank=True, null=True)
    nom_apepaterno = models.CharField(max_length=100, blank=True, null=True)
    nom_apematerno = models.CharField(max_length=100, blank=True, null=True)
    num_importetotal = models.IntegerField(blank=True, null=True)
    fec_orden = models.DateTimeField(blank=True, null=True)
    num_telefono = models.CharField(max_length=20, blank=True, null=True)
    opc_celular = models.BooleanField(blank=True, null=True)
    num_folio = models.BigIntegerField(blank=True, null=True)
    num_estatus = models.IntegerField(blank=True, null=True)
    num_totalarticulosmuebles = models.SmallIntegerField(blank=True, null=True)
    num_totalarticulosropa = models.SmallIntegerField(blank=True, null=True)
    num_importeropa = models.IntegerField(blank=True, null=True)
    num_importemuebles = models.IntegerField(blank=True, null=True)
    num_engancheropa = models.IntegerField(blank=True, null=True)
    des_articulo = models.CharField(max_length=12, blank=True, null=True)
    num_enganchemuebles = models.IntegerField(blank=True, null=True)
    num_folioropa = models.IntegerField(blank=True, null=True)
    num_foliomuebles = models.IntegerField(blank=True, null=True)
    fec_movimiento = models.DateTimeField(blank=True, null=True)
    num_pagorecibido = models.IntegerField(blank=True, null=True)
    desc_canalventa = models.CharField(max_length=20, blank=True, null=True)
    desc_servicio = models.CharField(max_length=20, blank=True, null=True)
    fec_facturanota = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmptodasdetallepedido'


class Totalattrrequerido(models.Model):
    fun_obteneratributosrequeridosmarketplace = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'totalattrrequerido'


class VEstatus(models.Model):
    idu_estatuspedidocommerce = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_estatus'


class VariantesViejas(models.Model):
    parentpartnumber = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'variantes_viejas'


class Vnomareaweb(models.Model):
    nomareaweb = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vnomareaweb'


class Vregistrosesperados(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vregistrosesperados'


class Vtasainteres(models.Model):
    num_tasainteresmarketplace = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vtasainteres'


class Xcampanias(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    fecha_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xcampanias'


class Xcampaniasusuarios(models.Model):
    id_campania = models.IntegerField()
    id_folio = models.IntegerField()
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    numero_ticket = models.IntegerField()
    numero_cliente = models.IntegerField()
    monto_compra = models.DecimalField(max_digits=65535, decimal_places=65535)
    estatus_compra = models.CharField(max_length=50, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    tipo_servicio = models.CharField(max_length=50)
    tienda = models.CharField(max_length=50, blank=True, null=True)
    clave = models.CharField(max_length=50, blank=True, null=True)
    tipomovimiento = models.CharField(max_length=50, blank=True, null=True)
    fecha_registro = models.DateTimeField()
    fecha_compra = models.DateTimeField()
    sn_ganador = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xcampaniasusuarios'
        unique_together = (('id', 'id_folio', 'numero_ticket'),)


class Xcediscp(models.Model):
    xcediscp_id = models.AutoField(primary_key=True)
    cedis_id = models.IntegerField(blank=True, null=True)
    cedis_cp = models.IntegerField(blank=True, null=True)
    field1 = models.CharField(max_length=255, blank=True, null=True)
    field2 = models.CharField(max_length=255, blank=True, null=True)
    field3 = models.CharField(max_length=255, blank=True, null=True)
    optcounter = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xcediscp'
