from django.contrib import admin

# Register your models here.
from .models import Passage, TypingRecord

admin.site.register(Passage)
admin.site.register(TypingRecord)