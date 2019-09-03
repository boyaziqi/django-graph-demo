import graphene

from graphene_django.types import DjangoObjectType

from apps.articles.models import Category, Article


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class ArticleType(DjangoObjectType):
    class Meta:
        model = Article


class Query(object):
    all_categories = graphene.List(CategoryType)
    all_articles = graphene.List(ArticleType)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_articles(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Article.objects.select_related('category').all()