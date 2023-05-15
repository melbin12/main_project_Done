from django.contrib import admin

from cart.models import orderplaced

# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    # def has_delete_permission(self, request, obj=None):
    #     return False
admin.site.register(orderplaced, AccountAdmin)
