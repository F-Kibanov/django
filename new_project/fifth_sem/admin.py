from django.contrib import admin
from third_sem.models import Post, Author, Coin
from third_sem.models import Client, Product, Order


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'birthday']
    ordering = ['name', 'birthday']
    list_filter = ['name', 'birthday']
    search_fields = ['name']
    search_help_text = 'Поиск по полю имя автора'

    readonly_fields = ['birthday']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'surname'],
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'description': 'Биография автора',
                'fields': ['bio', 'birthday'],
            },
        ),
        (
            'Contacts',
            {
                'description': 'Author contacts',
                'fields': ['email'],
            },
        ),
    ]


class PostAdmin(admin.ModelAdmin):
    @admin.action(description='Drop content')
    def reset_content(modeladmin, request, queryset):
        queryset.update(content='')

    list_display = ['title', 'content', 'author']
    ordering = ['title', 'author']
    list_filter = ['title', 'author', 'publish_date']
    search_fields = ['title']
    search_help_text = 'Поиск по полю заголовок'
    actions = [reset_content]

    readonly_fields = ['is_published', 'publish_date']

    fieldsets = [
        (
            'Post',
            {
                'classes': ['wide'],
                'fields': ['title', 'publish_date'],
            },
        ),
        (
            'Text',
            {
                'classes': ['collapse'],
                'description': 'content',
                'fields': ['content', 'category'],
            },
        ),
        (
            'Author',
            {
                'description': 'Author contacts',
                'fields': ['author', 'views', 'is_published'],
            },
        ),
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Coin)

"""Домашнее задание к семинару №5"""


class ClientAdmin(admin.ModelAdmin):
    @admin.action(description='Drop name')
    def drop_name(modeladmin, request, queryset):
        queryset.update(name='')

    @admin.action(description='Drop surname')
    def drop_surname(modeladmin, request, queryset):
        queryset.update(surname='')

    list_display = ['name', 'surname', 'email', 'phone', 'address']
    ordering = ['name', 'surname', 'phone']
    list_filter = ['name', 'surname', 'email']
    search_fields = ['email', 'phone']
    search_help_text = 'Поиск клиента по почте или телефону'
    actions = [drop_name, drop_surname]

    readonly_fields = ['register_date']

    fieldsets = [
        (
            'Client',
            {
                'classes': ['wide'],
                'fields': ['name', 'surname'],
            },
        ),
        (
            'Contacts',
            {
                'classes': ['collapse'],
                'description': 'Виды связи',
                'fields': ['email', 'phone'],
            },
        ),
        (
            'Details',
            {
                'description': 'Author contacts',
                'fields': ['address', 'register_date'],
            },
        ),
    ]


class ProductAdmin(admin.ModelAdmin):
    @admin.action(description='Drop quantity to 0')
    def drop_quantity(modeladmin, request, queryset):
        queryset.update(product_quantity=0)

    list_display = ['product_name', 'product_price', 'product_quantity']
    ordering = ['product_price', 'product_name', 'product_quantity']
    list_filter = ['product_name', 'product_price']
    search_fields = ['product_name', 'product_description']
    search_help_text = 'Поиск продукта по названию или описанию'
    actions = [drop_quantity]

    readonly_fields = ['product_add_date']

    fieldsets = [
        (
            'Product',
            {
                'classes': ['wide'],
                'fields': ['product_name', 'product_price'],
            },
        ),
        (
            'Description',
            {
                'classes': ['collapse'],
                'description': 'Product description',
                'fields': ['product_description', 'product_quantity'],
            },
        ),
        (
            'More',
            {
                'description': 'Product add date',
                'fields': ['product_add_date'],
            },
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    @admin.action(description='Give all products for free')
    def gift(modeladmin, request, queryset):
        queryset.update(total_price=0)

    list_display = ['client', 'product']
    ordering = ['client', 'total_price']
    list_filter = ['client', 'product']
    search_fields = ['client', 'product']
    search_help_text = 'Поиск клиента или продукта в заказах'
    actions = [gift]

    fieldsets = [
        (
            'Order',
            {
                'classes': ['wide'],
                'fields': ['client', 'product'],
            },
        ),
        (
            'Total',
            {
                'classes': ['collapse'],
                'description': 'Total price',
                'fields': ['total_price'],
            },
        ),
    ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
