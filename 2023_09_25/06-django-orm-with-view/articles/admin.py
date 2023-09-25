from django.contrib import admin
from .models import Article

# 내가 만든 앱은 따로 등록
admin.site.register(Article)