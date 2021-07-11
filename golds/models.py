from django.db import models

class gold(models.Model):
    speaker=models.CharField (max_length=100)
    gold=models.TextField()
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
