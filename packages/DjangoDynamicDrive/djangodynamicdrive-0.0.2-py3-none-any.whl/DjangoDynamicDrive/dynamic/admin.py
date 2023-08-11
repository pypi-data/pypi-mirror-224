from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.apps import apps
from django.utils.html import format_html
import sys


def get_all_models():
    '''获取全部变量'''
    l = []
    for app_key in apps.all_models:
        for mod in apps.all_models[app_key]:
            if apps.all_models[app_key][mod]:
                l.append(apps.all_models[app_key][mod])
    return l


def create_model_page_option(model):
    list_display = [field.name for field in model._meta.fields]
    admin_class = type(
        'AdminClass',
        (ModelAdmin,),
        {
            'list_display': list_display,
            'list_per_page': 20,
        }
    )
    if 'admin_option' in dir(model) and model.admin_option() and isinstance(model.admin_option(), dict):
        '''设置列表可显示的字段'''
        if model.admin_option().get('list_display'):
            admin_class.list_display = model.admin_option().get('list_display')

        '''每页显示条目数'''
        if model.admin_option().get('size'):
            admin_class.list_per_page = model.admin_option().get('size')

        '''设置过滤选项'''
        if model.admin_option().get('list_filter'):
            admin_class.list_filter = model.admin_option().get('list_filter')
        '''设置可编辑字段'''
        if model.admin_option().get('list_editable'):
            admin_class.list_editable = model.admin_option().get('list_editable')
        '''按日期月份筛选'''
        if model.admin_option().get('date_hierarchy'):
            admin_class.date_hierarchy = model.admin_option().get(
                'date_hierarchy')
        # date_hierarchy = 'create_time'
        '''按发布日期排序'''
        if model.admin_option().get('ordering'):
            admin_class.ordering = model.admin_option().get('ordering')
        '''搜索字段'''
        if model.admin_option().get('search_fields'):
            admin_class.search_fields = model.admin_option().get('search_fields')
        '''允许排序'''
        if model.admin_option().get('sortable_by'):
            admin_class.sortable_by = model.admin_option().get('sortable_by')
        '''设置表单字段排列'''
        if model.admin_option().get('fields'):
            admin_class.fields = model.admin_option().get('fields')
        '''设置表单中不显示的字段'''
        if model.admin_option().get('exclude'):
            admin_class.exclude = model.admin_option().get('exclude')
        '''设置只读字段'''
        if model.admin_option().get('readonly_fields'):
            admin_class.readonly_fields = model.admin_option().get('readonly_fields')
        # 设置默认排序字段# ordering = ('-mod_date',)
        if model.admin_option().get('ordering'):
            admin_class.ordering = model.admin_option().get('ordering')
        else:
            if "id" in list_display:
                admin_class.ordering = ("-id",)
            if "ID" in list_display:
                admin_class.ordering = ("-ID",)
    else:
        if "id" in list_display:
            admin_class.ordering = ("-id",)
        if "ID" in list_display:
            admin_class.ordering = ("-ID",)
    return admin_class


# models = apps.get_models()
models = get_all_models()

for model in models:
    '''设置列表可显示的字段'''
    # 生成模型类，默认显示所有字段
    admin_class = create_model_page_option(model)
    try:
        admin.site.register(model, admin_class)
    except:
        exc_type, exc_value, exc_obj = sys.exc_info()
        print(exc_type, exc_value, exc_obj)
