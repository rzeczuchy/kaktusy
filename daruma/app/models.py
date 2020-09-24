from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError

def check_single_instance(instance):
    model = instance.__class__
    if (model.objects.count() > 0 and instance.pk != model.objects.get().pk):
        raise ValidationError("You can only have a single instance of this class.")

# Create your models here.
class CompanyDetail(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company', blank=True, null=True)
    full_name = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)

    def clean(self):
        check_single_instance(self)

    def __str__(self):
        return self.full_name

class Page(models.Model):
    title = models.CharField(max_length=100)
    meta_description = models.CharField(max_length=150)
    hero_title = models.CharField(max_length=100)
    hero_subtitle = models.CharField(max_length=250)

    class Meta:
        abstract = True

class Home(Page):
    intro_title = models.CharField(max_length=100)
    intro_content = RichTextField(blank=True, null=True)
    logos_title = models.CharField(max_length=100)
    team_title = models.CharField(max_length=100)
    team_link_text = models.CharField(max_length=100)
    contact_title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Home"

    def clean(self):
        check_single_instance(self)

    def __str__(self):
        return "Home"

class Team(Page):
    team_title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Team"

    def clean(self):
        check_single_instance(self)

    def __str__(self):
        return "Team"

class Blog(Page):
    class Meta:
        verbose_name_plural = "Blog"

    def clean(self):
        check_single_instance(self)

    def __str__(self):
        return "Blog"

class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    added = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name_plural = "Inquiries"

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    published_time = models.DateTimeField('published at')
    author = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=250)
    main_content = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Subpage(Page):
    content = RichTextField(blank=True, null=True)

    class Meta:
        abstract = True

class PrivacyPolicy(Subpage):
    class Meta:
        verbose_name_plural = "Privacy Policy"

    def clean(self):
        check_single_instance(self)

    def __str__(self):
        return "Privacy Policy"

class TermsOfService(Subpage):
    class Meta:
        verbose_name_plural = "Terms of Service"

    def clean(self):
        check_single_instance(self)

    def __str__(self):
        return "Terms of Service"

class Disclaimer(Subpage):
    class Meta:
        verbose_name_plural = "Disclaimer"

    def clean(self):
        check_single_instance(self)

    def __str__(self):
        return "Disclaimer"

class TeamMember(models.Model):
    portrait = models.ImageField(upload_to='images')
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PartnerLogo(models.Model):
    image = models.ImageField(upload_to='logos')

    def __str__(self):
        return "Logo " + str(self.id)