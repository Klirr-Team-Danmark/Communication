from django.db import models

class Message(models.Model):
    author = models.CharField(max_length=32)
    content = models.TextField()
    posted = models.DateTimeField(
        verbose_name="posted", auto_now_add=True, null=False
    )

    class Meta:
        ordering = ["-posted"]
