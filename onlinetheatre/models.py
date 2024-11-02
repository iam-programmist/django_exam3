from django.db import models

class HomePage(models.Model):
    film_available = models.CharField(max_length = 100, null = True)
    trailer_name = models.CharField(max_length = 100)
    trailer_genre = models.CharField(max_length = 100)
    trailer_date = models.DateTimeField(auto_now = True)
    watch_trailer = models.CharField(max_length = 50)

    def __str__(self):
        return f'{self.film_available} - {self.trailer_name} - {self.trailer_genre} - {self.trailer_date} - {self.watch_trailer}'
    
class FilmPage(models.Model):
    watch_film = models.ForeignKey(HomePage, on_delete = models.CASCADE, related_name = 'watch_film')
    show_information = models.CharField(max_length = 100)
    show_date = models.DateTimeField(auto_now = True)
    theatre_name = models.CharField(max_length = 100)
    order_ticket = models.CharField(max_length = 50)

    def __str__(self):
        return f'{self.watch_film} - {self.show_information} - {self.show_date} - {self.theatre_name} - {self.order_ticket}'
    
class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 15, unique = True)
    age = models.IntegerField()
    address = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.phone_number}'
    
class OrderTicket(models.Model):
    ticket_quantity = models.IntegerField()
    name_of_user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'name_of_user')
    phone_of_user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'phone_of_user')