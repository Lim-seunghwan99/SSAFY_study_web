from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('content',)
        # __all__이 아닌 content만 남은 이유 :
        # 전체 필드로 하면 article도 같이 보인다.