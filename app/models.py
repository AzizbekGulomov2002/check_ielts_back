from django.db import models
from asyncio import format_helpers
import math
sex = [
    ('F','Female'),
    ('M','Male'),
]


class IELTS(models.Model):
    image = models.ImageField(upload_to='image_candidate', null=True, blank=True)
    candidate_id = models.CharField(max_length=9)
    date = models.DateField()
    family_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)

    date_of_birth = models.DateField(help_text='Year | Month | Day')
    sex = models.CharField(choices=sex, max_length=2)
    region_address = models.CharField(max_length=200)
    nationally = models.CharField(max_length=100)
    first_language = models.CharField(max_length=100)
    listening = models.FloatField(null=True, blank=True)
    reading = models.FloatField(null=True, blank=True)
    writing = models.FloatField(null=True, blank=True)
    speaking = models.FloatField(null=True, blank=True)
    # overal = models.FloatField()
    # cefr_level = models.CharField(max_length=100)
    admission_comments = models.TextField(null=True, blank=True)
    test_number = models.IntegerField()
    candidate_number = models.IntegerField(null=True, blank=True, unique=True)

    @property
    def overal(self):
        arifmethic_mean = (self.listening + self.reading + self.writing + self.speaking) / 4
        if arifmethic_mean != int(arifmethic_mean):
            floor_plus_half = int(arifmethic_mean) + 0.5
            if (arifmethic_mean) <= floor_plus_half:
                return floor_plus_half
            else:
                return math.ceil(arifmethic_mean)
        else:
            return arifmethic_mean




    @property
    def cefr_level(self):
        if 4 <= (self.overal) <= 5:
            return "B1"
        if 5.5 <= (self.overal) <= 6.5:
            return "B2"
        if 7 <= (self.overal) <= 8:
            return "C1"
        if 8 <= (self.overal) <= 9:
            return "C2"


    @property
    def image_show(self):
        return format_helpers('<img src = {} width="60" height="60" style="border-radius:50%;"'.format(self.image.url))
    def save(self, *args, **kwargs):
        super(IELTS, self).save(*args, **kwargs)
        if self.id:
            self.candidate_number = self.id +10000
        super(IELTS, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.candidate_number} | {self.family_name} | {self.overal} | | {self.candidate_id}"


    class Meta:
        verbose_name = 'IELTS'
        verbose_name_plural = 'IELTS'





class Pupil(models.Model):
    name = models.CharField(max_length=400, help_text="Enter Pupil name....")
    date = models.DateField(null=True, blank=True, help_text="Date | Month | Year")
    email_address = models.CharField(max_length=200, help_text="Enter email address ...", null=True)
    phone_number = models.IntegerField()
    passport_id = models.CharField(max_length=200, null=True, blank=True)
    payment = models.BooleanField(help_text="if paid, click the button")
    one_id = models.IntegerField(null=True,blank=True,unique=True)
    def __str__(self):
        return self.name
    @property
    def image_show(self):
        return format_helpers('<img src = {} width="60" height="60" style="border-radius:50%;"'.format(self.image.url))
    def save(self, *args, **kwargs):
        super(Pupil, self).save(*args, **kwargs)
        if self.id:
            self.one_id = self.id +1000
        super(Pupil, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} | {self.email_address} | {self.phone_number} | {self.payment} | {self.one_id}"