from django import forms
import graphene
from graphene import relay

from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.rest_framework.mutation import SerializerMutation

from apps.articles.models import Category, Article
from apps.articles.serializers import CategorySerializer


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

    def resolve_category(self, info, **kwargs):
        print('ffffffffffff')
        id = kwargs.get('id')
        return Category.objects.get(pk=id)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_articles(self, info, **kwargs):
        return Article.objects.select_related('category').all()


class CategoryInput(graphene.InputObjectType):
    name = graphene.String()


class CreateCategoryMutation(graphene.Mutation):
    class Arguments:
        input = CategoryInput(required=True)

    ok = graphene.Boolean()
    category = graphene.Field(CategoryType)

    def mutate(self, info, input):
        ok = True
        category = Category(name=input.name)
        category.save()
        return CreateCategoryMutation(ok, category)


class Mutation(graphene.ObjectType):
    create_category = CreateCategoryMutation.Field()
