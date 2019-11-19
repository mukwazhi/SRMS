from django.contrib import admin
from .models import RiskDetail, Officials, Documents, Location, Station


class RiskDetailAdmin(admin.ModelAdmin):
    list_display = [ 'station','report_no','hazard_type', 'location_of_incident','likelyhood','severity', 'proposed_mitigation']

# class RiskEvaluationAdmin(admin.ModelAdmin):
#     list_display = [ 'report_number','action_required', 'resources_required', 'responsible_official', 'status', 'reopen']

class OfficialsAdmin(admin.ModelAdmin):
    list_display = ['name','position','email','contact']

class DocumentsAdmin(admin.ModelAdmin):
    list_display = ['title','file','valid_to','archive']

class LocationAdmin(admin.ModelAdmin):
    list_display = ['location','description']

class StationAdmin(admin.ModelAdmin):
    list_display = ['station','description']

admin.site.register(RiskDetail, RiskDetailAdmin)
admin.site.register(Documents, DocumentsAdmin)
admin.site.register(Officials, OfficialsAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Station, StationAdmin)

