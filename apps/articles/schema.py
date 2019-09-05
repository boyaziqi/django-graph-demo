from graphene import relay

from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from apps.articles.models import Category, Article


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'articles']
        interfaces = (relay.Node,)


class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'content': ['icontains'],
            'created_at': ['exact'],
        }
        interfaces = (relay.Node,)


class Query(object):
    category = relay.Node.Field(CategoryType)
    all_categories = DjangoFilterConnectionField(CategoryType)
    article = relay.Node.Field(ArticleType)
    all_articles = DjangoFilterConnectionField(ArticleType)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_articles(self, info, **kwargs):
        return Article.objects.select_related('category').all()