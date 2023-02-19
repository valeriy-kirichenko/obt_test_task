from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from objectpack.actions import ObjectPack

from .ui import (
    ContentTypeAddWindow,
    GroupAddWindow,
    PermissionAddWindow,
    UserAddWindow
)


class ContentTypePack(ObjectPack):

    model = ContentType
    add_window = edit_window = ContentTypeAddWindow

    # разрешим добавлять ссылку на list_window в меню Desktop'а
    # и на рабочий стол
    add_to_menu = add_to_desktop = True

    columns = [
        {
            'data_index': 'app_label',
            'header': u'Приложение',
        },
        {
            'data_index': 'model',
            'header': u'Модель',
        },
    ]


class UserPack(ObjectPack):

    model = User
    add_window = edit_window = UserAddWindow

    # разрешим добавлять ссылку на list_window в меню Desktop'а
    # и на рабочий стол
    add_to_menu = add_to_desktop = True

    columns = [
        {
            'data_index': 'username',
            'header': u'Имя пользоваетля',
        },
        {
            'data_index': 'first_name',
            'header': u'Имя',
        },
        {
            'data_index': 'last_name',
            'header': u'Фамилия',
        },
        {
            'data_index': 'email',
            'header': u'Электронная почта',
        },
        {
            'data_index': 'is_superuser',
            'header': u'Статус суперпользователя',
        },
        {
            'data_index': 'is_staff',
            'header': u'Статус персонала',
        },
        {
            'data_index': 'is_active',
            'header': u'Активный пользователь',
        },
    ]


class GroupPack(ObjectPack):

    model = Group
    add_window = edit_window = GroupAddWindow

    # разрешим добавлять ссылку на list_window в меню Desktop'а
    # и на рабочий стол
    add_to_menu = add_to_desktop = True

    columns = [
        {
            'data_index': 'name',
            'header': u'Название',
        },
    ]


class PermissionPack(ObjectPack):

    model = Permission
    add_window = edit_window = PermissionAddWindow

    # разрешим добавлять ссылку на list_window в меню Desktop'а
    # и на рабочий стол
    add_to_menu = add_to_desktop = True

    columns = [
        {
            'data_index': '__str__',
            'header': u'Права',
        },
    ]

    def save_row(self, obj, create_new, request, context):
        obj.content_type = ContentType.objects.get(
            id=int(request.POST['content_type.app_label'])
        )
        super().save_row(obj, create_new, request, context)
