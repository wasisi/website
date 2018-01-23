from django.db import models
from django.conf import settings

# Create your models here.

class CoffeeGrades(models.Model):
	class Meta:
		verbose_name_plural = "Coffee Grades" #this fixes incorrect plural "countys" from appearing in django admin
	SIZE_CHOICES = (
           ('0 - 5', 'very small'),
           ('6 - 10', 'small'),
           ('11 - 15', 'medium'),
           ('16 - 20', 'large'),
           ('21 - 25', 'very large'),
       )
	grade = models.CharField(max_length=200, db_index=True)
	grade_name = models.CharField(max_length=20, blank=True, null=True)
	size = models.CharField(max_length=10,
							choices=SIZE_CHOICES,
							blank=True, 
							null=True)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.grade

class CoffeeTransactions(models.Model):
	class Meta:
		verbose_name_plural = "Nairobi Coffee Exchange Transactions" #this fixes incorrect plural "countys" from appearing in django admin
	TRANSNR = models.CharField(max_length=20)
	LOTNT = models.IntegerField()
	MARKS = models.CharField(max_length=100)
	MARKS2 = models.CharField(max_length=100)
	REF = models.ForeignKey('directoryApp.Producer') # Foreign Key
	REF2 = models.CharField(max_length=20)
	BAGMARK = models.CharField(max_length=20)
	GRADE_GR = models.ForeignKey('CoffeeGrades') # Foreign Key
	BAGSNR = models.CharField(max_length=3)
	WEIGHT_Kgr = models.IntegerField()
	SALENO = models.IntegerField()
	BAGSBOUGHTNR = models.IntegerField()
	WEIGHTBOUGHT_Kgr = models.IntegerField()
	BUYERCODE = models.ForeignKey('directoryApp.Dealer') # Foreign Key
	PRICE = models.IntegerField()
	SEATNR = models.IntegerField()
	AUCTCODE = models.IntegerField()
	STATUS = models.IntegerField()
	ISODATE = models.DateField(auto_now=False, auto_now_add=False)
	SEASON = models.CharField(max_length=10)
	NOTES = models.TextField(blank=True, null=True)

