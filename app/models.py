from django.db import models
from asyncio import format_helpers

sex = [
    ('F','Female'),
    ('M','Male'),
]


class IELTS(models.Model):
    image = models.ImageField(upload_to='{{ i.image.url }}', null=True, blank=True)
    candidate_id = models.CharField(max_length=9)
    date = models.DateField()
    family_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    
    date_of_birth = models.DateField(help_text='Year | Month | Day')
    sex = models.CharField(choices=sex, max_length=2)
    region_address = models.CharField(max_length=200)
    nationally = models.CharField(max_length=100)
    first_language = models.CharField(max_length=100)
    grammar = models.FloatField(null=True, blank=True)
    pronunciation = models.FloatField(null=True, blank=True)
    fluency = models.FloatField(null=True, blank=True)
    lexical = models.FloatField(null=True, blank=True)
    # overal = models.FloatField()
    # cefr_level = models.CharField(max_length=100)
    admission_comments = models.TextField(null=True, blank=True)
    test_number = models.IntegerField()
    candidate_number = models.IntegerField(null=True, blank=True, unique=True)

    @property
    def overal(self):
        return round(self.grammar + self.pronunciation + self.fluency + self.lexical)/4

    @property
    def cefr_level(self):
       
        if (4.00) <= self.overal <= (5.00):
            return "B1"
        if (5.5) <= self.overal <= (6.5):
            return "B2"
        if (7.00) <= self.overal <= (8.00):
            return "C1"
        if (8.00) <= self.overal <= (9.00): 
            return "C2"
        else:
            return "No"


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
