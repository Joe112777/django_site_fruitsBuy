from django.contrib import admin
from fruits.models import Fruits,Order

class FruitsAdmin(admin.ModelAdmin):
    list_display=('title','price')
    search_fields=('title','price')

class OrderAdmin(admin.ModelAdmin):
    list_display=('name','email','fruits','quantity','pay')
    list_filter=('name',)
    name_hierarchy='name'
    ordering = ('-name',)
    fields=('name','fruits','quantity','pay')
    #filter_horizontal=('name',)

admin.site.register(Fruits,FruitsAdmin)
admin.site.register(Order,OrderAdmin)




