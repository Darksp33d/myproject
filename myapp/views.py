from django.http import HttpResponse
from .models import MyModel
from django.http import JsonResponse
from .models import MyModel
from django.http import HttpResponse
from .models import MyModel
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

# User data

@require_http_methods(["GET"])
def user_data(request, user_id):
    try:
        my_model = MyModel.objects.get(user_id=user_id)
        data = {
            'user_id': my_model.user_id,
            'username': my_model.username,
            # Add more fields as needed
        }
        return JsonResponse(data)
    except MyModel.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    
@require_http_methods(["POST"])
def create_user(request):
    user_id = request.POST.get('user_id')
    username = request.POST.get('username')
    # Add more fields as needed
    my_model = MyModel(user_id=user_id, username=username)
    my_model.save()
    return JsonResponse({'success': 'User created'}, status=201)

@require_http_methods(["PUT"])
def update_user(request, user_id):
    try:
        my_model = MyModel.objects.get(user_id=user_id)
        my_model.username = request.POST.get('username')
        # Update more fields as needed
        my_model.save()
        return JsonResponse({'success': 'User updated'})
    except MyModel.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    
@require_http_methods(["DELETE"])
def delete_user(request, user_id):
    try:
        my_model = MyModel.objects.get(user_id=user_id)
        my_model.delete()
        return JsonResponse({'success': 'User deleted'})
    except MyModel.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    
@require_http_methods(["GET"])
def list_users(request):
    my_models = MyModel.objects.all()
    data = [{'user_id': my_model.user_id, 'username': my_model.username} for my_model in my_models]
    return JsonResponse(data, safe=False)

@require_http_methods(["GET"])
def search_users(request):
    query = request.GET.get('query')
    my_models = MyModel.objects.filter(username__icontains=query)
    data = [{'user_id': my_model.user_id, 'username': my_model.username} for my_model in my_models]
    return JsonResponse(data, safe=False)

@require_http_methods(["GET"])
def filter_users(request):
    filter_param = request.GET.get('filter_param')
    my_models = MyModel.objects.filter(filter_param=filter_param)
    data = [{'user_id': my_model.user_id, 'username': my_model.username} for my_model in my_models]
    return JsonResponse(data, safe=False)