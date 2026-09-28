# 对应：第13章 AI 时代爬虫的发展趋势与展望
# 小节：13.6 新协议与技术趋势
# 条目：13.6.3 GraphQL 接口的爬取
# 清单：02
# 说明：摘自书稿示例，未改写。

import requests

def query_graphql(endpoint: str, query: str, variables: dict = None) -> dict:
    """通用的 GraphQL 查询函数"""
    payload = {'query': query}
    if variables:
        payload['variables'] = variables
    
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 ...',
    }
    
    response = requests.post(endpoint, json=payload, headers=headers)
    return response.json()

# 示例：查询商品列表
query = """
query GetProducts($category: String!, $first: Int!) {
    products(category: $category, first: $first) {
        edges {
            node {
                id
                name
                price
                rating
            }
        }
        pageInfo {
            hasNextPage
            endCursor
        }
    }
}
"""

result = query_graphql(
    endpoint='https://api.example.com/graphql',
    query=query,
    variables={'category': 'electronics', 'first': 20}
)

products = result['data']['products']['edges']
for item in products:
    print(item['node'])
