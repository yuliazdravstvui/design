from django.db import models

# Create your models here.
class Application(models.Model):
    """
    Model representing a pl genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a floor plans")
    summary = models.TextField(help_text="Опишите заявку")
    file = models.FileField(upload_to='files/', null=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name




