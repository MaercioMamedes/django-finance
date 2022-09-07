from django.http import HttpResponseNotFound
from django.template import loader


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponseNotFound(content=template.render(), content_type='text/html', charset='utf-8')
