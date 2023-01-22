import os

from django.core.management import BaseCommand
from catalog.models import Product, Category

import json


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        """Clear rows in db and fill it with new data"""
        Category.objects.all().delete()

        # UTF-8 problem, this is like json.read() from 'fixtures-category.json',
        # {'model': 'catalog.category'}, symbols changed to cirilical
        c_data = [{
            "pk": 1,
            "name": "Галантерея",
            "description": "Разная жизненная мелочь"
        }, {
            "pk": 2,
            "name": "Обувь",
            "description": "Всяки разные обутки"
        }]

        category_list = []
        for category in c_data:
            category_list.append(
                Category(**category)
            )

        Category.objects.bulk_create(category_list)
