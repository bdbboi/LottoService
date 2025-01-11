from django.contrib import admin
from .models import WinningNumbers, LottoTicket

@admin.register(WinningNumbers)
class WinningNumbersAdmin(admin.ModelAdmin):
    list_display = ('draw_date', 'numbers')
    ordering = ('-draw_date',)

@admin.register(LottoTicket)
class LottoTicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'purchase_type', 'created_at', 'is_winner') 
    list_filter = ('purchase_type', 'is_winner') 
    search_fields = ('id',)  
    