from django.contrib import admin

# Register your models here.
from .models import Message

class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('pub_date',)

admin.site.register(Message,RatingAdmin)