from django.views.generic import ListView
from . import models


class HomeView(ListView):
    model = models.Room
    paginate_by = 10
    paginate_orphans = 5