from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(RegisteredTrip)
class RegisterdTripAdmin(admin.ModelAdmin):
    list_display = ('user','order_id')
    search_fields = ('order_id','user__phone',)

# admin.site.register(RegisteredTrip)
admin.site.register(OrderPayment)
admin.site.register(FailedPayment)