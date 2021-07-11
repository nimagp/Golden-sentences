from django.db import models

class gold(models.Model):
    speaker=models.CharField (max_length=100)
    gold=models.TextField()
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.speaker
    