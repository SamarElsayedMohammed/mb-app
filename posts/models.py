from django.db import models

# Create your models here.
class Post(models.Model):
    """Model definition for Post."""

    # TODO: Define fields here

    text = models.CharField(max_length=1000)

    # class Meta:
    #     """Meta definition for Post."""

    #     verbose_name = 'Post'
    #     verbose_name_plural = 'Posts'

    def __str__(self):
        """Unicode representation of Post."""
        return self.text[:50]

