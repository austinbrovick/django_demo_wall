from __future__ import unicode_literals

from django.db import models



class Post(models.Model):
    creator = models.CharField(max_length=30)
    post = models.TextField(max_length=140)
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post

class Comment(models.Model):
    post = models.ForeignKey(Post)
    creator = models.CharField(max_length=30)
    createdAt = models.DateTimeField(auto_now=True)
    comment = models.TextField(max_length=140)



# one to one OneToOneField()
# many to one ForeignKey()
# many to many ManyToManyField()
