from django.contrib import admin
from backend.models import *

admin.site.register(Student)
admin.site.register(Product)
admin.site.register(Team)
admin.site.register(Blog)
admin.site.register(Slide)
admin.site.register(Project)
admin.site.register(Testimony)
@admin.register(MissionVisionValues)
class MissionVisionValuesAdmin(admin.ModelAdmin):
    list_display = ('section', 'title', 'icon')
    list_filter = ('section',)
    search_fields = ('title', 'description')