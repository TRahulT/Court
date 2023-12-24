import string
import uuid
from random import random

from django.db import models



class AdvocateProfile(models.Model):
    name_of_agency = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    post = models.CharField(max_length=100)
    fh_name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    enrollment = models.CharField(max_length=200)
    experience = models.IntegerField()
    specialization = models.TextField
    address1 = models.CharField(max_length=300, null=True, blank=True)
    address2 = models.CharField(max_length=300, null=True, blank=True)
    address3 = models.CharField(max_length=300, null=True, blank=True)
    phone_number = models.CharField(max_length=10)
    jurisdiction = models.TextField
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Client(models.Model):
    name = models.CharField(max_length=100)
    fh_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class CaseType(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name


class AddCase(models.Model):
    client_details = models.ForeignKey(Client, on_delete=models.CASCADE)
    sarvhit_number = models.CharField(max_length=10, unique=True,null=True,blank=True)
    case_type = models.ForeignKey(CaseType, on_delete=models.CASCADE)
    filling_number = models.CharField(max_length=200)
    filling_date = models.CharField(max_length=25)
    registration_number = models.CharField(max_length=200)
    registration_date = models.DateField
    cnr_number = models.CharField(max_length=20)
    first_hearing = models.CharField(max_length=25)
    case_stage = models.CharField(max_length=100)
    court_no = models.CharField(max_length=100)
    petitioner = models.CharField(max_length=50)
    advocate_name = models.CharField(max_length=100)
    police_station = models.CharField(max_length=250)
    fir_number = models.CharField(max_length=100)
    fir_year = models.CharField(max_length=4)
    fir_date = models.CharField(max_length=20, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            super(AddCase, self).save(*args, **kwargs)  # Save the object to generate an ID if it doesn't exist

        # Generate a random UUID
        random_uuid = str(uuid.uuid4())
        # Remove hyphens and convert to uppercase
        random_uuid = random_uuid.replace("-", "").upper()
        # Construct sarvhit_number by combining the object's ID and random UUID
        self.sarvhit_number = f"{self.id}{random_uuid[:4]}"
        super(AddCase, self).save(*args, **kwargs)


class Rules(models.Model):
    case = models.ForeignKey(AddCase, on_delete=models.CASCADE)
    under_act = models.CharField(max_length=200)
    under_section = models.CharField(max_length=200)


class RespondentAdvocate(models.Model):
    case_resp = models.ForeignKey(AddCase, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    resp_advocate = models.CharField(max_length=200, null=True, blank=True)
    adv_no = models.CharField(max_length=10, null=True, blank=True)


class NextListening(models.Model):
    case_detail = models.ForeignKey(AddCase, on_delete=models.CASCADE)
    next_hearing_date = models.CharField(null=False,blank=False,max_length=25)
    case_stage = models.CharField(max_length=100)
    court_no_judge = models.CharField(max_length=100)


class InterimOrder(models.Model):
    next_hearing_details = models.OneToOneField(NextListening, on_delete=models.CASCADE)
    order_details = models.FileField(upload_to='copy_of_orders/')


class CaseFile(models.Model):
    case=models.ForeignKey(AddCase,on_delete=models.CASCADE)
    file=models.FileField(upload_to="case_file/")

