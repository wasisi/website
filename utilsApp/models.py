from django.db import models
from django.utils.timezone import now as timezone_now

#Models to be used around the Wasisi site that
#provide uniform naming. All attributes are in lower case
#except from ID attributes. The mixins here are all abstract
#classes meaning tables are not created for them in the DB


class CreationModificationDateMixin(models.Model):
    """
        Abstarct base class that provides  creation and modification date and time
        fields to derived models
    """

    #when the instance of the model was created
    created = models.DateTimeField(auto_now_add=True,editable=False,)

    #when the instance of the model was updated
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UniqueTitleMixin(models.Model):
    """
        Abstract base class for models with a unique title
    """

    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
		    abstract = True

    def __str__(self):
        return self.title


class ActiveMixin(models.Model):
    """
        Abstract base class for models that require an active field
    """
    #the boolean flag
    active =models.BooleanField(default=True)

    class Meta:
        abstract=True

    def is_active(self):

        if self.active==1:
            return True
        return False

class AffiliationMixin(models.Model):
    """
    Abstract base class for models with affiliation
    """
    affiliation_name = models.CharField(max_length=200,unique=False)

    class Meta:
		    abstract = True

class UniqueIDMixin(models.Model):
    """
    Abstract base class of models with unique id
    """

    ID = models.IntegerField(unique=True)

    class Meta:
        abstract = True




