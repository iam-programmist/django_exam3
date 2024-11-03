from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import HomePage, FilmPage, User, OrderTicket, Payment

class HomePageListView(ListView):
    model = HomePage
    template_name = 'homepage_list.html'

class HomePageDetailView(DetailView):
    model = HomePage
    template_name = 'homepage_detail.html'

class HomePageCreateView(CreateView):
    model = HomePage
    fields = ['film_available', 'trailer_name', 'trailer_genre', 'watch_trailer']
    template_name = 'homepage_form.html'
    success_url = reverse_lazy('homepage_list')

class HomePageUpdateView(UpdateView):
    model = HomePage
    fields = ['film_available', 'trailer_name', 'trailer_genre', 'watch_trailer']
    template_name = 'homepage_form.html'
    success_url = reverse_lazy('homepage_list')

class HomePageDeleteView(DeleteView):
    model = HomePage
    template_name = 'homepage_confirm_delete.html'
    success_url = reverse_lazy('homepage_list')

class FilmPageListView(ListView):
    model = FilmPage
    template_name = 'filmpage_list.html'

class FilmPageDetailView(DetailView):
    model = FilmPage
    template_name = 'filmpage_detail.html'

class FilmPageCreateView(CreateView):
    model = FilmPage
    fields = ['watch_film', 'show_information', 'theater_name', 'order_ticket']
    template_name = 'filmpage_form.html'
    success_url = reverse_lazy('filmpage_list')

class FilmPageUpdateView(UpdateView):
    model = FilmPage
    fields = ['watch_film', 'show_information', 'theater_name', 'order_ticket']
    template_name = 'filmpage_form.html'
    success_url = reverse_lazy('filmpage_list')

class FilmPageDeleteView(DeleteView):
    model = FilmPage
    template_name = 'filmpage_confirm_delete.html'
    success_url = reverse_lazy('filmpage_list')

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'

class UserCreateView(CreateView):
    model = User
    fields = ['first_name', 'last_name', 'phone_number', 'age', 'address']
    template_name = 'user_form.html'
    success_url = reverse_lazy('user_list')

class UserUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'phone_number', 'age', 'address']
    template_name = 'user_from.html'
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

class OrderTicketListView(ListView):
    model = OrderTicket
    template_name = 'orderticket_list.html'

class OrderTicketDetailView(DetailView):
    model = OrderTicket
    template_name = 'orderticket_detail.html'

class OrderTicketCreateView(CreateView):
    model = OrderTicket
    fields = ['ticket_quantity', 'name_of_user', 'phone_of_user', 'theater_order_confirm']
    template_name = 'orderticket_form.html'
    success_url = reverse_lazy('orderticket_list')

class OrderTicketUpdateView(UpdateView):
    model = OrderTicket
    fields = ['ticket_quantity', 'name_of_user', 'phone_of_user', 'theater_order_confirm']
    template_name = 'orderticket_form.html'
    success_url = reverse_lazy('orderticket_list')

class OrderTicketDeleteView(DeleteView):
    model = OrderTicket
    template_name = 'orderticket_confirm_delete.html'
    success_url = reverse_lazy('orderticket_list')

class PaymentListView(ListView):
    model = Payment
    template_name = 'payment_list.html'

class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'payment_detail.html'

class PaymentCreateView(CreateView):
    model = Payment
    fields = ['online_payment', 'cash_payment', 'ticket_price_information']
    template_name = 'payment_form.html'
    success_url = reverse_lazy('payment_list')

class PaymentUpdateView(UpdateView):
    model = Payment
    fields = ['online_payment', 'cash_payment', 'ticket_price_information']
    template_name = 'payment_form.html'
    success_url = reverse_lazy('payment_list')

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'payment_confirm_delete.html'
    success_url = reverse_lazy('payment_list')