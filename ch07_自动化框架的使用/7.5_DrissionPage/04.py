# 对应：第7章 自动化框架的使用
# 小节：7.5 DrissionPage
# 条目：7.5.6 翻页时需要替换的关键操作
# 清单：04
# 说明：摘自书稿示例，未改写。

for _ in range(3):
    for card in page.eles('css:article.product_pod'):
        print(card.ele('css:h3 a').attr('title'))
    next_link = page.ele('css:li.next a', timeout=2)
    if not next_link:
        break
    page.get(next_link.link)
