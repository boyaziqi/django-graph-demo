import graphene

from apps.articles.schema import Query as ArticleQuery
from apps.articles.schema import Mutation as ArticleMutation


class Query(ArticleQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=ArticleMutation)
