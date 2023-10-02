from django.contrib import admin

from .models import Tag
from .models import Product
from .models import Pack

# Register your models here.
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Pack)
