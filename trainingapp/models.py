from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=50)
    adm = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Lecturers(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    department = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name+" "+self.status


#Create a staff model
#firstname, Lastname,Position,Phonenumber,Email,hiredate
#return Firstname and Lastname
class Employees(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    hire_date = models.DateField()

    def __str__(self):
        return self.Firstname+" "+self.Lastname



class Parents(models.Model):
    name = models.CharField(max_length=50)
    phone= models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Contacts(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name
#mpesa api
class Transaction(models.Model):
        phone_number = models.CharField(max_length=15)
        amount = models.DecimalField(max_digits=10, decimal_places=2)
        transaction_id = models.CharField(max_length=100, unique=True)
        status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')])
        date = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"{self.phone_number} - {self.amount} - {self.status}"


class Admission1(models.Model):
    firstname =models.CharField(max_length =50)
    lastname =models.CharField(max_length =50)
    email =models.EmailField()
    date =models.DateField()
    gender= models.CharField(max_length=50)
    address= models.CharField(max_length=50)
    phone= models.CharField(max_length=50)
    image = models.ImageField(upload_to='students/')  # New field


    def __str__(self):
        return self.firstname
