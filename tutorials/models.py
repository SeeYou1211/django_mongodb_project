from django.db import models

# Create your models here.
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles


class Tutorial(models.Model):
    title = models.CharField(verbose_name='标题', max_length=70, blank=False, default='')
    description = models.CharField('描述', max_length=200, blank=False, default='')
    published = models.BooleanField('发表', default=False)

    class Meta:
        verbose_name = '标题'
        verbose_name_plural = verbose_name
        ordering = ['-published']


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted((item[1][0], item[0]) for item in LEXERS)
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(verbose_name='创建时间', db_column="创建时间", auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(max_length=100, default='python', choices=LANGUAGE_CHOICES)
    # 以下添加权限处理
    # 代码片段始终与创建者相关联。
    # 只有通过身份验证的用户可以创建片段。
    # 只有代码片段的创建者可以更新或删除它。
    # 未经身份验证的请求应具有完全只读访问权限。
    style = models.CharField(max_length=100, default='friendly', choices=STYLE_CHOICES)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)

    highlighted = models.TextField()

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        """
        使用`pygments`库创建一个高亮显示的HTML表示代码段。
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)
