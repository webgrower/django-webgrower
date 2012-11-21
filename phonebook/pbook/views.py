from pbook.models import Book
from pbook.models import Phone
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    books = Book.objects.all()
    return render_to_response('pbook/home.html', {
        'title': 'Phone books example on Django',
        'books': books,
        'request': request,
    }, RequestContext(request))

def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render_to_response('pbook/view_book.html', {
        'title': book.name,
        'book': book,
        'request': request,
    }, RequestContext(request))

def view_contact(request, contact_id):
    phone = get_object_or_404(Phone, id=contact_id)
    return render_to_response('pbook/view_contact.html', {
        'title': phone.first_name + ' ' + phone.last_name,
        'phone': phone,
        'request': request,
    })
