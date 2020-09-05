from django.db import models

# Create your models here.
OJ_CHOICES = (
    ('CODEFORCES','CODEFORCES'),
    ('URI', 'URI'),
    ('UVA','UVA'),
    ('HACKERRANK','HACKERRANK'),
    ('LIGHT Oj','LIGHT Oj'),
)

class Solution(models.Model):
    category = models.CharField(max_length=10, choices=OJ_CHOICES, default='codeforces')
    title = models.CharField(max_length=200)
    date=models.DateField()
    link = models.CharField(max_length=255)
    explaination= models.TextField(max_length=10000,blank=True)
    code = models.TextField(max_length=10000)
    img = models.ImageField(upload_to='images',blank=True, null=True)
    has_img = models.BooleanField(default=False)

