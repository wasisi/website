from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# This allows us to extend Django's user model by adding additional fields e.g. date of birth
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    # above will not work without installing pillow with pip install Pillow
    
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


# This model is being used as an example of an intermediary model. We are using Django user model and we dont want to modify.
# This allows us to add additional fields to the user model stored in another table
# Many to many relationship
# When you need additional fields in many-to-many you create a custom model (e.g. contact)
## You then create a foreign key for each side of the relationship
## Add a ManyToManyField in one of the related models
## Tell Django to use intermediary model by using the "through" parameter


class Contact(models.Model):
	user_from = models.ForeignKey(User, related_name='rel_from_set') # Foreign key that creates the relationship. db  index automatically created
	user_to = models.ForeignKey(User, related_name='rel_to_set') # Foreign key of the user that is being followed. db  index automatically created
	created = models.DateTimeField(auto_now_add=True, db_index=True) # additional field that we want to store

	class Meta:
		ordering = ('-created',)
		def __str__(self):
			return '{} follows {}'.format(self.user_from, 
				self.user_to)        

# Adding field dynamically to user model. check page 171 of Django by Example for alternative approach
# Add following field to User dynamically
User.add_to_class('following', # monkey patch user model. NOT RECOMMENDED WAY OF ADDING FIELD TO Model
	models.ManyToManyField('self',
							through=Contact, # Use model created above. Monkey patch saves us from creating complex queries
							related_name='followers',
							symmetrical=False))