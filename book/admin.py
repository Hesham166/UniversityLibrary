from django.contrib import admin
from .models import *


admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(BorrowList)
admin.site.register(BorrowRecord)
