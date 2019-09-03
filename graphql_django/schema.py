import graphene

from apps.articles.schema import Query as ArticleQuery



class Query(ArticleQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)
