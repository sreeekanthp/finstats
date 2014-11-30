from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class IncomeType(models.Model):
    """
    Model for the income types. Eg: Salary etc.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return '{0}'.format(self.name)

class ExpenseType(models.Model):
    """
    Model for the expense types. Eg: Food/Travel etc.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return '{0}'.format(self.name)

class Income(models.Model):
    """
    Model for the income entries.
    """
    user = models.ForeignKey(User)
    type = models.ForeignKey(IncomeType)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField(blank=True)

    def __unicode__(self):
        return '{0} - {1} - {2}'.format(self.user, self.type, self.amount)

class Expense(models.Model):
    """
    Model for the expense entries.
    """
    user = models.ForeignKey(User)
    type = models.ForeignKey(ExpenseType)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField(blank=True)

    def __unicode__(self):
        return '{0} - {1} - {2}'.format(self.user, self.type, self.amount)
