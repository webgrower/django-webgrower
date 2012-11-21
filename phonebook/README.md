#Django PhoneBook Example

This Example shows you, how to make a simply phone book with Twitter Bootstrap. This example is a part of tutorials in WebGrower repo on GitHub.
Enjoy!

## Some notes
### Using static requires RequestContext
So, if you are using `render_to_response` shortcut, don't forget to write code like this:
```python
def index(request):
    books = Book.objects.all()
    return render_to_response('pbook/home.html', {
        'title': 'Phone books example on Django',
        'books': books,
        'request': request,
    }, RequestContext(request)) # from django.template import RequestContext
```
### Url tag may be simply!
You can name your URL in `urls.py`
```python
url(r'^$', 'index', name='home'),
```
and use this name in your template:
```html
{% url home %}
```

**That's all! Good luck!**
