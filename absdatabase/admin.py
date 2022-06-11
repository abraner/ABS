from django.contrib import admin
from .models import ProdQueue, CustomerInfo, Time, TaxRate



admin.site.site_url = "/absdatabase/1/main"

admin.site.site_header = 'ABS Bidding Dashboard'
admin.site.register(ProdQueue)
admin.site.register(CustomerInfo)
admin.site.register(Time)
admin.site.register(TaxRate)