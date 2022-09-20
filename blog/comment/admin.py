from xml.etree.ElementTree import Comment
from django.contrib import admin
from comment.models import Comment

admin.site.register(Comment)
