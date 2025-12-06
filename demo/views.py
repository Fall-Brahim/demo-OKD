from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Visitor
import json

def index(request):
    """Page d'accueil avec liste des visiteurs"""
    visitors = Visitor.objects.all()[:10]
    total_visitors = Visitor.objects.count()
    
    context = {
        'visitors': visitors,
        'total_visitors': total_visitors,
    }
    return render(request, 'index.html', context)

@csrf_exempt
def add_visitor(request):
    """API pour ajouter un visiteur - Accepte GET et POST"""
    
    # Si c'est une requête GET (accès direct dans le navigateur)
    if request.method == 'GET':
        return JsonResponse({
            'message': 'API pour enregistrer les visiteurs',
            'method': 'POST',
            'endpoint': '/api/visitor/',
            'total_visitors': Visitor.objects.count(),
            'example': {
                'name': 'Jean Dupont',
                'email': 'jean@example.com',
                'message': 'Bonjour!'
            }
        })
    
    # Si c'est une requête POST (soumission du formulaire)
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name', 'Visiteur Anonyme')
            email = data.get('email', '')
            message = data.get('message', '')
            
            # Récupérer l'IP
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
            
            visitor = Visitor.objects.create(
                name=name,
                email=email,
                message=message,
                ip_address=ip
            )
            
            return JsonResponse({
                'success': True,
                'id': visitor.id,
                'name': visitor.name,
                'visited_at': visitor.visited_at.strftime('%Y-%m-%d %H:%M:%S')
            })
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    
    return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)