from django.db import models

class SWITCHES(models.Model):
    """Model definition for SWITCHES."""
    label = models.CharField(max_length=50,blank=True)
    switchMode = models.BooleanField(blank=False)
    duration = models.CharField(max_length=50,blank=True)
    

    def __str__(self):
        return self.label

