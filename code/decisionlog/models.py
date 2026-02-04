from django.db import models

# Create your models here.
class DecisionLogEntry(models.Model):
    """An entry in the decision log"""

    content = models.TextField(verbose_name="content")
    created_time = models.DateTimeField(verbose_name="created")
    author = models.CharField(verbose_name="author", max_length=40)

    class Meta:
        ordering = ["created_time"]

    def __str__(self):
        return f"{self.author} at {self.created_time}"
