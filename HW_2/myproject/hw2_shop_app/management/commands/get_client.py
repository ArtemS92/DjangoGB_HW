from django.core.management.base import BaseCommand
from hw2_shop_app.models import Client


class Command(BaseCommand):
    help = "Get client by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='id of client')  # pk - id

    def handle(self, *args, **kwargs):
        id_client = kwargs.get('pk')
        client = Client.objects.filter(pk=id_client).first()  # поиск строки по id
        self.stdout.write(f'{client}')
