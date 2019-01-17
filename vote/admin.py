from django.contrib import admin

# Register your models here.

from vote.models import Vote, VoteTopic



admin.site.register(VoteTopic)

class VoteAdmin(admin.ModelAdmin):
    list_display = ["id","topic", "owner","get_vote_value_display"]
    list_filter = ["owner","vote_value"]

admin.site.register(Vote, VoteAdmin)