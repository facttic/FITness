from django.contrib import admin
from FITness.opportunity.models import Opportunity, Client, OpportunityProfile, ProfileExpertise

admin.site.register(Client)
admin.site.register(Opportunity)
admin.site.register(OpportunityProfile)
admin.site.register(ProfileExpertise)
