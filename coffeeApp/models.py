from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your models here.

class CoffeeGrades(models.Model):
	class Meta:
		verbose_name_plural = "Coffee Grades" #this fixes incorrect plural "countys" from appearing in django admin
	size_choices = (
           ('0 - 5', 'very small'),
           ('6 - 10', 'small'),
           ('11 - 15', 'medium'),
           ('16 - 20', 'large'),
           ('21 - 25', 'very large'),
       )
	grade = models.CharField(max_length=200, db_index=True)
	grade_name = models.CharField(max_length=20, blank=True, null=True)
	size = models.CharField(max_length=10,
							choices=size_choices,
							blank=True, 
							null=True)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.grade

class CoffeeTransactions(models.Model):
	class Meta:
		verbose_name_plural = "Nairobi Coffee Exchange Transactions" #this fixes incorrect plural "countys" from appearing in django admin
	saleno = models.IntegerField()
	transnr = models.CharField(max_length=20, null=True)
	lotnr = models.IntegerField()
	marks = models.CharField(max_length=100)
	marks2 = models.CharField(max_length=100)
	bagmark = models.CharField(max_length=20, null=True)
	ref = models.CharField(max_length=20, null=True) # Changed from Ref2
	producercode = models.ForeignKey('directoryApp.Producer', null=True, on_delete=models.CASCADE) # Foreign Key. Changed from Ref
	grade_gr = models.ForeignKey('CoffeeGrades', null=True,on_delete=models.CASCADE) # Foreign Key
	bagsnr = models.IntegerField(null=True)
	bagsboughtnr = models.IntegerField(null=True)
	weight_kgr = models.IntegerField(null=True)
	weightbought_kgr = models.IntegerField(null=True)
	buyercode = models.ForeignKey('directoryApp.Dealer', on_delete=models.CASCADE, null=True) # Foreign Key
	price = models.IntegerField(null=True)
	resprice = models.IntegerField(null=True)
	auctcode = models.IntegerField(null=True)
	seatnr = models.IntegerField(null=True)
	status = models.IntegerField(null=True)
	isodate = models.DateField(auto_now=False, auto_now_add=False)
	notes = models.TextField(blank=True, null=True)
	users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
		related_name='transactions_liked',
		blank=True)
	@property
	def value(self):
		return (self.price * self.weightbought_kgr)/50
	def unitprice(self):
		return (self.price)/50	

	def get_absolute_url(self):
           return reverse('coffeeApp:transaction_detail', args=[self.id])


