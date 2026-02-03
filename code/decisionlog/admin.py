from django.contrib import admin

import decisionlog.models as m

@admin.register(m.DecisionLogEntry)
class DecisionLogAdmin(admin.ModelAdmin):
    list_display = ("author", "created_time",)
    search_fields = ("author", "content",)
