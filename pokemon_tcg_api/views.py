from django.shortcuts import render

from pokemontcgsdk import Card

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        cards = Card.where(q=f'name:{name}')
        count = len(Card.where(q=f'name:{name}'))
        return render(request, 'index.html', {
            'name': name,
            'cards': cards,
            'count': count,
        })
    return render(request, 'index.html')
