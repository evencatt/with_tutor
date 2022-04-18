from django.contrib import admin
from .models import GrammarTheme, GrammarSubsections, GrammarMaterial, GrammarVoices

class GrammarAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'pub_date')
    empty_value_display = '-пусто-'


class GrammarSubsectionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'pub_date')
    empty_value_display = '-пусто-'


class GrammarMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'pub_date')
    empty_value_display = '-пусто-'


class GrammarVoicesAdmin(admin.ModelAdmin):
    list_display = ('voice', )


admin.site.register(GrammarTheme, GrammarAdmin)
admin.site.register(GrammarSubsections, GrammarSubsectionsAdmin)
admin.site.register(GrammarMaterial, GrammarMaterialAdmin)
admin.site.register(GrammarVoices, GrammarVoicesAdmin)