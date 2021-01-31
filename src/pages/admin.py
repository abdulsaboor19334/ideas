from django.contrib import admin
from .models import Posts,Vote,Comments, Topic

admin.site.register(Posts)
admin.site.register(Vote)
admin.site.register(Comments)
admin.site.register(Topic)
