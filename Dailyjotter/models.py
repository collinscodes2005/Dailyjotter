from django.db import models
import uuid

# Create your models here.
'''The Author model '''
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=120)
    user_name = models.CharField(max_length=300)
    password = models.CharField(max_length=400)
    
    #image = models.ImageField(upload_to="posts", null=True, blank=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    about = models.CharField(max_length=170, null=True)



    def __str__(self):
        return f"{self.first_name}  { self.surname } "


def image(instance, filename):
    return 'uploads/{}/{}'.format(instance.title, filename)


'''The Post model '''
class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    #image = models.ImageField(upload_to="posts", null=True, blank=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(max_length=400)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


