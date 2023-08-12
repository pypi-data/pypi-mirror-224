# D
## 快速开始

### 自动注册模型到Admin

setting.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'DjangoDynamicDrive.dynamic',
    # 你的APP
    'testapp',
]
```

### 数据库路由，指定Django app 使用所选择的数据库

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'default',
        'USER': '你的账户',
        'PASSWORD': '你的密码',
        'HOST': '数据库的IP或者host',
        'PORT': '数据库服务开放的端口',
    },
    'logsdb': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'logs',
        'USER': '你的账户',
        'PASSWORD': '你的密码',
        'HOST': '数据库的IP或者host',
        'PORT': '数据库服务开放的端口',
    }
}

# 数据库路由
DATABASE_ROUTERS = ['DjangoDynamicDrive.db.database_router.DatabaseAppsRouter']
# 应用与数据库映射
DATABASE_APPS_MAPPING = {
    'testapp': 'logsdb',
    # app名称：数据库路由
}
```

数据库迁移

```bash
python manage.py makemigrations
python manage.py migrate --database=logsdb
```

