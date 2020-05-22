from django.db import models


class Registro(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    ci = models.IntegerField()
    num_registro = models.IntegerField(primary_key=True)
    direccion = models.TextField(default=None, null=True)
    nombre_trabajo = models.CharField(max_length=50)
    latitud = models.FloatField(default=0)
    longitud = models.FloatField(default=0)
    horario_inicio = models.TimeField(default=None, null=True)
    horario_fin = models.TimeField(default=None, null=True)

    def __str__(self):
        return "num_reg: {}".format(self.num_registro)


class Cuidacoches(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    ci = models.IntegerField()
    num_registro = models.IntegerField(primary_key=True)
    direccion = models.TextField(default=None, null=True)
    horario_inicio = models.TimeField(default=None, null=True)
    horario_fin = models.TimeField(default=None, null=True)
    telefono = models.IntegerField(null=True)
    mail = models.EmailField(default=None, null=True)
    fecha_nacimiento = models.DateField(null=True)
    cuenta_bancaria = models.IntegerField(null=True)
    banco = models.CharField(max_length=50, null=True)
    promedio_calificacion = models.FloatField(null=True)
    cantidad_votos = models.IntegerField(null=True)
    estado = models.BooleanField(default=True)
    cant_lugares = models.IntegerField(default=20)
    lugares_disponibles = models.IntegerField(default=cant_lugares)
    password = models.CharField(max_length=8, null=True)
    nombre_trabajo = models.CharField(max_length=50)
    latitud = models.FloatField(default=0)
    longitud = models.FloatField(default=0)



    def __str__(self):
        return "num_reg cuidacoches: {}".format(self.num_registro)


class MonederoCuidacoches(models.Model):
    ci = models.ForeignKey(Cuidacoches, on_delete=models.CASCADE)
    monto = models.IntegerField(null=False)

    def agregar_propina(self, propina):
        self.monto += propina
        self.save()


class Conductor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    ci = models.IntegerField(unique=True, null=True)
    telefono = models.IntegerField(null=True)
    mail = models.EmailField(null=True)
    cuenta_bancaria = models.IntegerField(null=True)
    banco = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    username = models.CharField(max_length=20, default="user", null=True)
    password = models.CharField(max_length=8, null=True)
    notificacion = models.IntegerField(null=False, default=0)

    def __str__(self):
        return "ci conductor: {}".format(self.ci)

    def alta_conductor(self):
        self.save()

    def baja_conductor(self):
        self.estado = False
        self.save()

    def editar_conductor(self):
        self.save()


class MonederoConductor(models.Model):
    ci = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    monto = models.IntegerField(default=500)

    def dar_propina(self, propina):
        self.monto -= propina
        self.save()


class Relacion(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    cuidacoches = models.ForeignKey(Cuidacoches, on_delete=models.CASCADE)
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    calificacion = models.IntegerField(null=True)
    comentario = models.TextField(max_length=200, null=True)
    fecha = models.DateTimeField(auto_now=True)
    propina = models.IntegerField(null=True)

    def alta_relacion(self):
        self.save()

    def calificar(self, calificacion):
        self.calificacion = calificacion
        self.save()

    def comentar(self, comentario):
        self.comentario = comentario
        self.save()

