from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Genre (models.Model):
    """Model fo storing books genres"""
    name = models.CharField(max_length= 200, help_text = "Enter the genre of the book",
                            verbose_name = "Genre of the book")

    def __str__(self):
        return self.name


class Language (models.Model):
    """Model fo storing languages of books"""
    name = models.CharField (max_length= 20, help_text="Enter language of book",
                             verbose_name= "Language of book")

    def __str__(self):
        return self.name


class Author (models.Model):
    first_name = models.CharField (max_length= 100, help_text= "Enter the name of author",
                                   verbose_name= "The name of author")
    last_name = models.CharField (max_length= 100, help_text = "Enter the last name of author",
                                  verbose_name= "Last name of author")
    date_of_birth = models.DateField (help_text= "Enter the birthday of author", verbose_name= "Birthday",
                                      null = True, blank = True)
    date_of_death = models.DateField (help_text= "Enter date of death", verbose_name= "Date of death",
                                      null = True, blank = True)

    def __str__(self):
        return self.last_name

class Book (models.Model):
    title = models.CharField (max_length= 200, help_text= "Enter the name of the book",
                              verbose_name= "Name of the book")
    genre = models.ForeignKey('Genre', on_delete= models.CASCADE, help_text= "Choose a genre for the book",
                              verbose_name= "Genre of the book", null= True)
    language = models.ForeignKey ('Language', on_delete= models.CASCADE, help_text = "Choose a language for the book",
                                  verbose_name= "Language of the boot", null = True)
    author = models.ManyToManyField ('Author', help_text = "Choose the author of the book",
                                     verbose_name= "The author of the book")
    summary = models.TextField(max_length= 1000,  help_text= "Enter a short discription of the book",
                               verbose_name= "Book summary")
    isbn = models.CharField (max_length= 13, help_text= "Must contain 13 characters",
                             verbose_name= "ISBN of the book")

    def display_author(self):
        return ', '.join([author.last_name for author in self.author.all()])
    display_author.short_description = 'Authors'


    def __str__(self):
        return self.title

    def get_absolute_url (self):
        """Returns the URL-address for accesing a specific instance of the book"""
        return reverse ('book-detail', args = [str(self.id)])

class Status (models.Model):
    name = models.CharField (max_length= 20, help_text= "Enter the status of the book instance",
                             verbose_name= "The status of the book instance")

    def __str__(self):
        return self.name

class BookInstance (models.Model):
    book = models.ForeignKey ('Book', on_delete= models.CASCADE, null = True)
    inv_nom = models.CharField (max_length= 20, null = True, help_text= "Enter the inventory number of the instance",
                                verbose_name= "The inventory number of the instance")
    imprint = models.CharField (max_length= 200, help_text= "Enter the publisher and the year of release",
                                verbose_name= "Publisher")
    status = models.ForeignKey ('Status', on_delete= models.CASCADE, null = True, help_text= "Change the instance state",
                                verbose_name= "The status of the book instance")
    due_back = models.DateField (null = True, blank = True, help_text= "Enter the end of the status period",
                                 verbose_name= "End date of the status")
    borrower = models.ForeignKey (User, on_delete= models.SET_NULL,
                                  null = True, blank = True,
                                  verbose_name= "Заказчик", help_text= "Выберите заказчика книги")

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    def __str__(self):
        return '%s %s %s' % (self.inv_nom, self.book, self.status)



