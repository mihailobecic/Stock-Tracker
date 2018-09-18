from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Portfolios, StockPortfolio
# Create your views here.


class HomeView(generic.ListView):
    template_name = 'stock_tracker/home.html'

    def get_queryset(self):
        return Portfolios.objects.All()

class PortfolioView(generic.ListView):
    model = StockPortfolio
    template_name = 'stock_tracker/stockportfolio.html'


class PortfolioCreate(LoginRequiredMixin, generic.CreateView):
    model = Portfolios
    fields = ['portfolio_name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AddStock(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = StockPortfolio
    template_name = 'stock_tracker/addstock.html'
    fields = ['ticker','portfolio_name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#lass StockPrice(LoginRequiredMixin, generic.ListView):











