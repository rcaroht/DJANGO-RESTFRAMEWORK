from django.db import models

# Create your models here.

class bd_raw_data_old(models.Model):
    nombre = models.CharField(verbose_name="nombrePersona",null=False,max_length=60)
    apellido = models.CharField(verbose_name="apellidoPersona",null=False,max_length=60)
    edad = models.DateField(verbose_name="Fecha_Nacimiento",null=False)


#Clase para renombrar  https://es.stackoverflow.com/questions/91112/qu%c3%a9-es-la-clase-meta-y-como-funciona-en-los-modelos-de-django
    class Meta:                                                         
            db_table = "RegDatosPersona"
            verbose_name = "Pregunta"
            verbose_name_plural = "Preguntas"
    
#Función para retornar el dato específico. En este caso el texto del nombre.
#Cada vez que se cree un registro, se mostrará el texto del nombre.
    def __str__(self) -> str:
          return self.nombre 
          

#Clase para crear la tabla que almacenará los datos transformados.
class bd_raw_data_new(models.Model):
    nombre_completo = models.CharField(verbose_name="nombreCompleto", null=False, max_length=120)
    edad_nominal = models.IntegerField(verbose_name="edadActual")


    class Meta:
        db_table = "RegnuevosDatosPersona"
        verbose_name_plural = "RegnuevosDatoPersonas"

