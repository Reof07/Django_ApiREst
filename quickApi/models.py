from django.db import models

# Create your models here.

class Hero(models.Model):
    ''' Esta clase representa la tabla
        Hero en DB con los campos name, alias
    '''    
    name = models.CharField(max_length= 60)
    alias = models.CharField(max_length= 60)

    #__str__ solo indica django que imprime cuando imprime una instancia django. 
    def __str__(self):
        return(self.name)