from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType

def search(request):
    query = request.GET.get('q', '')
    results = []
    
    if query:
        # Search across specific models or content
        # Replace 'ModelName' with actual models you'd like to search
        results = ContentType.objects.filter(model__icontains=query)

    return render(request, 'searchresults.html', {'query': query, 'results': results})
