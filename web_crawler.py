def crawl_news():
    print("=== 模拟网页采集结果 ===")
    # 模拟从网页中提取到的标题和链接数据
    mock_data = [
        {"title": "示例新闻1：自动化运维技术分享", "url": "https://example.com/news1"},
        {"title": "示例新闻2：Python数据采集实战", "url": "https://example.com/news2"},
        {"title": "示例新闻3：网络接口对接最佳实践", "url": "https://example.com/news3"}
    ]

    for i, item in enumerate(mock_data, 1):
        print(f"{i}. 标题：{item['title']}")
        print(f"   链接：{item['url']}")


if __name__ == "__main__":
    crawl_news()
    print("\n脚本用途：用于自动化采集网页数据，可扩展为业务数据汇总、竞品信息监控等工具")