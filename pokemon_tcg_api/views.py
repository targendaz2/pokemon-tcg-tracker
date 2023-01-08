from django.shortcuts import render

from pokemontcgsdk import Card as APICard

from .models import Card

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        api_cards = APICard.where(q=f'name:{name}')

        for api_card in api_cards:
            Card(name=api_card.name).save()

        cards = Card.objects.filter(name__contains=name)
        return render(request, 'index.html', {
            'name': name,
            'cards': cards,
            'count': cards.count(),
        })
    return render(request, 'index.html')
