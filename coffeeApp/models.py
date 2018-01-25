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
	SALENO = models.IntegerField()
	TRANSNR = models.CharField(max_length=20, null=True)
	LOTNR = models.IntegerField()
	MARKS = models.CharField(max_length=100)
	MARKS2 = models.CharField(max_length=100)
	BAGMARK = models.CharField(max_length=20, null=True)
	REF = models.CharField(max_length=20, null=True) # Changed from Ref2
	PRODUCERCODE = models.ForeignKey('directoryApp.Producer', null=True) # Foreign Key. Changed from Ref
	GRADE_GR = models.ForeignKey('CoffeeGrades', null=True) # Foreign Key
	BAGSNR = models.IntegerField(null=True)
	BAGSBOUGHTNR = models.IntegerField(null=True)
	WEIGHT_Kgr = models.IntegerField(null=True)
	WEIGHTBOUGHT_Kgr = models.IntegerField(null=True)
	BUYERCODE = models.ForeignKey('directoryApp.Dealer', on_delete=models.CASCADE, null=True) # Foreign Key
	PRICE = models.IntegerField(null=True)
	RESPRICE = models.IntegerField(null=True)
	AUCTCODE = models.IntegerField(null=True)
	SEATNR = models.IntegerField(null=True)
	STATUS = models.IntegerField(null=True)
	ISODATE = models.DateField(auto_now=False, auto_now_add=False)
	NOTES = models.TextField(blank=True, null=True)

