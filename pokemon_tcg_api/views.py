from django.core.files import File
from django.shortcuts import render

from io import BytesIO
import os
import requests

from pokemontcgsdk import Card as APICard

from .models import Card


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        api_cards = APICard.where(q=f'name:{name}')

        for api_card in api_cards:
            new_card, _ = Card.objects.get_or_create(
                id=api_card.id, name=api_card.name)

            image_content = requests.get(
                api_card.images.small, stream=True).content

            new_card.image.save(os.path.basename(
                f'{new_card.id}.png'), File(BytesIO(image_content), 'rb'))

            new_card.full_clean()
            new_card.save()

        cards = Card.objects.filter(name__contains=name)
        return render(request, 'index.html', {
            'name': name,
            'cards': cards,
            'count': cards.count(),
        })
    return render(request, 'index.html')
