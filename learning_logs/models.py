from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # this is a method to display a simple representation of a model.
    def __str__(self):
        """Return a string representation of the model"""
        return self.text
    
class Entry(models.Model):
    """Somerhing specific learned about a topic"""
    
    # a foreign key is a reference to another record in the database, this is 
    # code which connects each entry to a specific topic.
    
    # cascade tell the django that when a topic is deleted, all entries
    # associated with that topic should be deleted as well. This is called a 
    # cascading delete.
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    
    # the field users will enter their topic information in and when the entry 
    # was created.
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
    
    # which information to show when it refers to individual entries. The ellipses
    # clarifies that we are not always displaying the entire entry.
    def __str__(self):
        """Return string represetation of the model"""
        return f"{self.text[:50]}..."