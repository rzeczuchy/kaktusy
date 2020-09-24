from django.contrib import admin
from .models import *

# Edit admin header and title.
admin.site.site_header = "ABCD admin"
admin.site.site_title = "ABCD admin"

class PageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
        
    def has_delete_permission(self, request, obj=None):
        return False

# Register your models here.
admin.site.register(Post)
admin.site.register(TeamMember)
admin.site.register(PartnerLogo)
admin.site.register(CompanyDetail, PageAdmin)
admin.site.register(PrivacyPolicy, PageAdmin)
admin.site.register(TermsOfService, PageAdmin)
admin.site.register(Disclaimer, PageAdmin)
admin.site.register(Inquiry)
admin.site.register(Home, PageAdmin)
admin.site.register(Team, PageAdmin)
admin.site.register(Blog, PageAdmin)