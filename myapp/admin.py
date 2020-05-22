from django.contrib import admin
from .models import Registro, MonederoCuidacoches,MonederoConductor, Cuidacoches, Conductor, Relacion

# Register your models here.
admin.site.register(Registro)
admin.site.register(MonederoConductor)
admin.site.register(MonederoCuidacoches)
admin.site.register(Conductor)
admin.site.register(Cuidacoches)
admin.site.register(Relacion)

