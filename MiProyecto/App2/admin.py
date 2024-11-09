from django.contrib import admin
from .models import *       # 16-importamos los modelos al admin

# 16-unimos los modelos al administrador de Django
 
admin.site.register(Usuarios)
admin.site.register(Productos)
admin.site.register(Ventas_detalles)


