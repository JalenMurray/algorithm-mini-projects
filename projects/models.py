from django.db.models import Model, CharField, TextField, ManyToManyField, ImageField
from algorithms.models import Algorithm

class Project(Model):
  title = CharField(max_length=100)
  description = TextField()
  image = ImageField(upload_to='images/', null=True, blank=True)
  algorithms = ManyToManyField(Algorithm)
  demo = CharField(max_length=255, null=True, blank=True)

  def __str__(self):
    return self.title
