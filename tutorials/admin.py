from django.contrib import admin

# Register your models here.
from .models import Tutorial, Snippet


#
# class Tutorial_list_Admin(admin.ModelAdmin):
#     # fieldsets = [
#     #     (None, {'fields': ['文章分类']}),
#     #     ('作者', {'fields': ['author']}),
#     # ]
#     pass


class TutorialAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None, {'fields': ['category']}),
    #     ('作者', {'fields': ['author']}),
    # ]
    # list_display = ('title', 'category', 'was_published_recently','author','create_time','modified_time')
    # list_display = ['create_time']
    list_display = ['title', 'description', 'published']

    # pass
class SnippetAdmin(admin.ModelAdmin):
    list_display = ['title', 'language', 'owner','created']
# class TagAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Tutorial, TutorialAdmin)
# admin.site.register(tutorial_detail, Tutorial_detail_Admin)
admin.site.register(Snippet, SnippetAdmin)
