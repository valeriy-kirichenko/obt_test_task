from django.contrib.contenttypes.models import ContentType
from objectpack.ui import BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext


APPS = {
    id: app for app, id in ContentType.objects.values_list('app_label', 'id')
}


class GroupAddWindow(BaseEditWindow):

    def _init_components(self):
        super(GroupAddWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'Название',
            name='name',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(GroupAddWindow, self)._do_layout()
        self.form.items.extend((self.field__name,))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(GroupAddWindow, self).set_params(params)
        self.height = 'auto'


class ContentTypeAddWindow(BaseEditWindow):

    def _init_components(self):
        super(ContentTypeAddWindow, self)._init_components()

        self.field__app_label = ext.ExtStringField(
            label=u'Приложение',
            name='app_label',
            allow_blank=False,
            anchor='100%')

        self.field__model = ext.ExtStringField(
            label=u'Модель',
            name='model',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(ContentTypeAddWindow, self)._do_layout()
        self.form.items.extend((self.field__app_label, self.field__model,))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(ContentTypeAddWindow, self).set_params(params)
        self.height = 'auto'


class PermissionAddWindow(BaseEditWindow):

    def _init_components(self):
        super(PermissionAddWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'Право',
            name='name',
            allow_blank=False,
            anchor='100%')

        self.field__content_type = make_combo_box(
            label=u'Приложение',
            name='content_type.app_label',
            allow_blank=False,
            data=APPS.items(),
            anchor='100%')

        self.field__codename = ext.ExtStringField(
            label=u' Операция',
            name='codename',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(PermissionAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__content_type,
            self.field__name,
            self.field__codename,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(PermissionAddWindow, self).set_params(params)
        self.height = 'auto'


class UserAddWindow(BaseEditWindow):

    def _init_components(self):
        super(UserAddWindow, self)._init_components()

        self.field__password = ext.ExtStringField(
            label=u'Пароль',
            name='password',
            allow_blank=False,
            anchor='100%')

        self.field__is_superuser = ext.ExtCheckBox(
            label=u'Статус суперпользователя',
            name='is_superuser',
            anchor='100%')

        self.field__username = ext.ExtStringField(
            label=u'Имя пользоваетля',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__first_name = ext.ExtStringField(
            label=u'Имя',
            name='first_name',
            anchor='100%')

        self.field__last_name = ext.ExtStringField(
            label=u'Фамилия',
            name='last_name',
            anchor='100%')

        self.field__email = ext.ExtStringField(
            label=u'Электронная почта',
            name='email',
            anchor='100%')

        self.field__is_staff = ext.ExtCheckBox(
            label=u'Статус персонала',
            name='is_staff',
            anchor='100%')

        self.field__is_active = ext.ExtCheckBox(
            label=u'Активный пользователь',
            name='is_active',
            anchor='100%',
            checked=True)

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__password,
            self.field__is_superuser,
            self.field__username,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__is_staff,
            self.field__is_active,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'
