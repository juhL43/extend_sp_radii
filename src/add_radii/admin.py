from django.contrib import admin

# Register your models here.
from .models import db_ions

class profileAdmin(admin.ModelAdmin):
	class Meta:
		model = db_ions

admin.site.register(db_ions, profileAdmin)
