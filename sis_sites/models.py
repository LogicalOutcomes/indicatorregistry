from django.db import models
from django.template import Template, Context


class Snippet(models.Model):
    name = models.CharField(max_length=128)
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'Snippets'

    def __unicode__(self):
        return self.name


class ContentBlock(models.Model):
    snippet = models.ForeignKey(Snippet)
    page = models.ForeignKey('flatpages.FlatPage')
    content = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Content Blocks'
        ordering = ['order']

    def __unicode__(self):
        return u"{} - {}".format(self.snippet.name, self.order)

    def render(self):
        template = Template(self.snippet.content)
        context = Context({
            'content': self.content,
            'value': self.value,
        })
        return template.render(context)
