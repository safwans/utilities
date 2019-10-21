from newsapi.newsapi_client import NewsApiClient 

# Init
newsapi = NewsApiClient(api_key='e86b1265afc449e1aa6d2e2e676ebc39')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(language='en',
                                          country='us')

# /v2/everything
all_articles = newsapi.get_everything(sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2019-04-01',
                                      to='2019-04-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/sources
sources = newsapi.get_sources()

print('\n'.join(a['publishedAt'] for a in top_headlines['articles']))