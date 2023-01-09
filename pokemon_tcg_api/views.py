from django.shortcuts import render

from pokemontcgsdk import Card as APICard

from .models import Card

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        api_cards = APICard.where(q=f'name:{name}')

        for api_card in api_cards:
            new_card = Card(id=api_card.id, name=api_card.name)
            new_card.full_clean()
            new_card.save()

        cards = Card.objects.filter(name__contains=name)
        return render(request, 'index.html', {
            'name': name,
            'cards': cards,
            'count': cards.count(),
        })
    return render(request, 'index.html')
