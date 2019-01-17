from xmlrpc.client import DateTime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Model, TextField, ForeignKey


class VoteTopic(Model):
    proposal = models.TextField(help_text="The proposal text")
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return "proposal by {}: {}".format(self.owner, self.proposal)
    def vote_results(self):
        results = {}
        for i in Vote.VOTE_OPTIONS:
            results[i[1]] = self.vote_set.filter(vote_value=i[0]).count()
        return results


class Vote(models.Model):
    VOTE_NO = 0
    VOTE_YES = 1
    VOTE_ABS = 2

    VOTE_OPTIONS = [
        [VOTE_YES, "yes"],
        [VOTE_NO, "no"],
        [VOTE_ABS, "abstain"]
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    vote_value = models.IntegerField(choices=VOTE_OPTIONS)

    topic = models.ForeignKey(VoteTopic, on_delete=models.CASCADE)

    def __str__(self):
        return "{} voted {} for PROPOSAL_ID:{}".format(self.owner,self.get_vote_value_display(), self.topic.id)