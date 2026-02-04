from django.contrib import admin

import chatroom.models as m

@admin.register(m.Message)
class DecisionLogAdmin(admin.ModelAdmin):
    list_display = ("author", "posted", "content",)
    search_fields = ("author", "content",)
