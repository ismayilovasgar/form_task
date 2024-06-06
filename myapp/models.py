from django.db import models

# Create your models here.


class Register(models.Model):
    firstname = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    job_position = models.CharField(max_length=50, null=True, blank=True)
    bussines_area = models.CharField(max_length=50, null=True, blank=True)
    self_description = models.TextField(max_length=200, null=True, blank=True)
    job_expectation = models.TextField(max_length=200, null=True, blank=True)
    programming_lang = models.CharField(max_length=50, null=True, blank=True)
    last_framework = models.CharField(max_length=50, null=True, blank=True)
    last_post_experience = models.CharField(max_length=50, null=True, blank=True)
    last_comp_name = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    phone_code = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.firstname}"
