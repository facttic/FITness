from django.contrib import admin
from FITness.candidate.models import Technology, Candidate, CandidateExpertise

admin.site.register(Candidate)
admin.site.register(Technology)
admin.site.register(CandidateExpertise)
