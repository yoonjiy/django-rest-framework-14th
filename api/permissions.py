from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    # 인증된 유저에 대해 조회/등록 허용
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # 조회 요청은 항상 True
        if request.method in permissions.SAFE_METHODS:
            return True
        # 작성자에 한해 record에 대한 수정/삭제 허용
        return obj.author == request.user