from django.db import models

class Author(models.Model):

    email = models.EmailField(primary_key=True, blank=False)
    name = models.CharField(max_length=100)
    test_field = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.email

class Post(models.Model):

    POST_TYPES = [('c', 'copyright'), ('n', 'native')]

    title = models.CharField(max_length=100, blank=False)
    subtitle = models.CharField(max_length=250)
    content = models.TextField(blank=False)
    issued = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads')
    post_type = models.CharField(choices=POST_TYPES, max_length=1)

    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

