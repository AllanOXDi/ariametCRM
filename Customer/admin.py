from django.contrib import admin
from .models import Customer, Product, Offers, Transaction

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Offers)
admin.site.register(Transaction)
