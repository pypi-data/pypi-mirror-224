from django.db import models
import datetime


class DbBase(models.Model):
    '''基类'''
    # ID
    id = models.AutoField(primary_key=True, verbose_name='ID')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    # 是否删除
    is_delete = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='是否删除'
    )

    class Meta:
        abstract = True

    def relation(self):
        '''关联'''
        return None

    def save(self):
        '''重写server'''
        super().save()

    def admin_option():
        '''admin页面配置项'''
        return {}

    def exclude_file(model, keys: set):
        '''排除字段'''
        return [field.name for field in model._meta.get_fields() if field.name not in keys]

