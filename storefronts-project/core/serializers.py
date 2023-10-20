from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password',
                  'email', 'first_name', 'last_name']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
