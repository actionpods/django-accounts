from rest_framework import viewsets

from django.contrib.auth.models import User
from ..models import Profile

from ..serializers.models import UserSerializer, ProfileSerializer

from rest_framework import filters, permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        #'userprofile': reverse('userprofile-list', request=request, format=format),
    })

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    #This viewset automatically provides `list` and `detail` actions.
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username','^user__email','address', 'city')

    def perform_create(self, serializer):
            serializer.save(owner=self.request.user)
