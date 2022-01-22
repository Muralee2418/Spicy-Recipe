from django.contrib import admin
from recipies.models import Recipie
from recipies.models import ScrapRecipie
from recipies.models import Author
from recipies.models import comments

admin.site.register(Recipie)
admin.site.register(Author)
admin.site.register(comments)
admin.site.register(ScrapRecipie)