from django.contrib import admin
from FITness.candidate.models import Technology, Candidate, CandidateExperience

# Register your models here.
admin.site.register(Technology)
admin.site.register(Candidate)
admin.site.register(CandidateExperience)