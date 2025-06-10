from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    user = request.user
    user.delete()
    return Response({'message': 'Your account and all related data have been deleted.'})
