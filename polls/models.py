from django.db import models

# Create your models here.
class Address(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    country = models.IntegerField()
    street = models.TextField(max_length=200)

    def __str__(self):
        return f'{self.street}...'

class Person(models.Model):
    name = models.CharField(max_length=30)
    address = models.ForeignKey(Address, models.DO_NOTHING)

    def __str__(self):
        return f'{self.name} : {self.address}'

class Permission(models.Model):
    type = models.CharField(max_length=30)
    action = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images')
    persons = models.ManyToManyField(Person, blank=True, null=True)


    def __str__(self):
        return self.type

class City(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=35)  # Field name made lowercase.
    countrycode = models.ForeignKey('Country', models.DO_NOTHING, db_column='CountryCode')  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=20)  # Field name made lowercase.
    population = models.IntegerField(db_column='Population')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'city'

    def __str__(self):
        return f'{self.name} - {self.countrycode}'

class Country(models.Model):
    code = models.CharField(db_column='Code', primary_key=True, max_length=3)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=52)  # Field name made lowercase.
    continent = models.CharField(db_column='Continent', max_length=13)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=26)  # Field name made lowercase.
    surfacearea = models.FloatField(db_column='SurfaceArea')  # Field name made lowercase.
    indepyear = models.SmallIntegerField(db_column='IndepYear', blank=True, null=True)  # Field name made lowercase.
    population = models.IntegerField(db_column='Population')  # Field name made lowercase.
    lifeexpectancy = models.FloatField(db_column='LifeExpectancy', blank=True, null=True)  # Field name made lowercase.
    gnp = models.FloatField(db_column='GNP', blank=True, null=True)  # Field name made lowercase.
    gnpold = models.FloatField(db_column='GNPOld', blank=True, null=True)  # Field name made lowercase.
    localname = models.CharField(db_column='LocalName', max_length=45)  # Field name made lowercase.
    governmentform = models.CharField(db_column='GovernmentForm', max_length=45)  # Field name made lowercase.
    headofstate = models.CharField(db_column='HeadOfState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    capital = models.IntegerField(db_column='Capital', blank=True, null=True)  # Field name made lowercase.
    code2 = models.CharField(db_column='Code2', max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'country'

    def __str__(self):
        return f'{self.code} ({self.name})'

class Countrylanguage(models.Model):
    countrycode = models.OneToOneField(Country, models.DO_NOTHING, db_column='CountryCode', primary_key=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=30)  # Field name made lowercase.
    isofficial = models.CharField(db_column='IsOfficial', max_length=1)  # Field name made lowercase.
    percentage = models.FloatField(db_column='Percentage')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'countrylanguage'
        unique_together = (('countrycode', 'language'),)

    def __str__(self):
        return f'{self.language}'



