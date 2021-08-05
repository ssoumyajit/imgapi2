from rest_framework import permissions
from groups.models import Group
from rest_framework import generics
from groups.serializers import GroupSerializer


class IsOwnerOrReadonly(permissions.BasePermission):
    pass
    """
    only the user can edit her data.
    object level (model instance or db row) perm.
    Read permissions are allowed to to any request, so we will always allow
    GET, HEAD OR OPTIONS requests.
    """

    def has_object_permission(self, request, view, obj):
        # check if user who launched request is object owner.
        # if request.method == 'GET:
        # return True
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissions are only allowed to the owner of this instance.
        return obj.username == request.user


# was working on private chat between teacher and student..... confirm once !!
class MessagePermissionBeforeCreate(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """returns True for the user if the condition satisfies"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.username == request.user | obj.teacher == request.user
        return request.user == obj.shareid.username | request.user == obj.shareid.teacher  # might need to get this object
    # in read mode beforehand coz it is all happening before touching the database
    # depth = 1 to get it or Modified Serializer.


class MessagePermissionAfterCreate(permissions.BasePermission):
    pass


'''
if obj.username == request.user:
    return True
else:
    return False
'''


class GroupMemberViews(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupPermission(permissions.BasePermission):
    pass
    # request.user > [ Membership.objects.all().filter.GroupName.members ]
