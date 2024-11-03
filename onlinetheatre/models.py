from django.db import models

class HomePage(models.Model):
    film_available = models.CharField(max_length = 100, null = True)
    trailer_name = models.CharField(max_length = 100)
    trailer_genre = models.CharField(max_length = 100)
    trailer_date = models.DateTimeField(auto_now = True)
    watch_trailer = models.CharField(max_length = 50)

    def __str__(self):
        return f'{self.film_available} - {self.trailer_name} - {self.trailer_genre} - {self.watch_trailer}'
    
class FilmPage(models.Model):
    watch_film = models.ForeignKey(HomePage, on_delete = models.CASCADE, related_name = 'watch_film')
    show_information = models.CharField(max_length = 100)
    show_date = models.DateTimeField(auto_now = True)
    theater_name = models.CharField(max_length = 100)
    order_ticket = models.CharField(max_length = 50)

    def __str__(self):
        return f'{self.show_information} - {self.theater_name} - {self.order_ticket}'
    
class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 15, unique = True)
    age = models.IntegerField()
    address = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.age} - {self.phone_number}'
    
class OrderTicket(models.Model):
    ticket_quantity = models.IntegerField()
    name_of_user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'name_of_user')
    phone_of_user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'phone_of_user')
    order_confirm_date = models.DateTimeField(auto_now = True)
    theater_order_confirm = models.CharField(max_length = 50)

    def __str__(self):
        return f'{self.ticket_quantity} - {self.theater_order_confirm}'

class Payment(models.Model):
    online_payment = models.CharField(max_length = 50)
    cash_payment = models.CharField(max_length = 50, null = True)
    ticket_price_information = models.CharField(max_length = 50)

    def __str__(self):
        return f'{self.online_payment} - {self.cash_payment} - {self.ticket_price_information}'