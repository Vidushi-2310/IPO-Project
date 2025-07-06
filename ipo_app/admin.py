
from django.contrib import admin
from .models import IPO

@admin.register(IPO)  
class IPOAdmin(admin.ModelAdmin):
    list_display = (
        'company_name', 'status', 'open_date', 'close_date',
        'ipo_price', 'listing_price', 'current_market_price',
        'listing_gain', 'current_return'
    )
    list_filter = ('status', 'open_date', 'close_date')
    search_fields = ('company_name',)
    readonly_fields = ('listing_gain', 'current_return')

