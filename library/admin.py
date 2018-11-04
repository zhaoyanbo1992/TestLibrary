from django.contrib import admin
from library.models import Reader, Book, Borrowing

# Register your models here.
admin.site.register(Reader)
admin.site.register(Book)
admin.site.register(Borrowing)

admin.site.name = '图书馆管理系统'
admin.site.site_header = '图书馆管理系统'
