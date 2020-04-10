from django.contrib import admin
from FITness.opportunity.models import Opportunity, Client, OpportunityTechnologies

# Register your models here.
admin.site.register(Opportunity)
admin.site.register(Client)
admin.site.register(OpportunityTechnologies)