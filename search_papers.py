import arxiv

def search_papers(query, max_results=5, sort_by="date"):
    """
    根据关键词检索相关论文，返回标题、发表时间和摘要

    参数：
    - query (str): 检索的关键词
    - max_results (int): 检索论文的数量
    - sort_by (str): 排序方式，可以是 'date' 或 'relevance'

    返回：
    - results (list): 含有论文标题、发表时间和摘要的列表
    """
    # 设置排序方式
    if sort_by == "relevance":
        sort_criterion = arxiv.SortCriterion.Relevance
    else:
        sort_criterion = arxiv.SortCriterion.SubmittedDate
    
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=sort_criterion
    )
    
    results = []
    for result in search.results():
        paper_info = {
            'title': result.title,
            'published': result.published,
            'summary': result.summary
        }
        results.append(paper_info)
    
    # 将搜索结果写入文件
    with open("search_results.txt", "w", encoding="utf-8") as f:
        for paper in results:
            f.write(f"Title: {paper['title']}\n")
            f.write(f"Published: {paper['published']}\n")
            f.write(f"Summary: {paper['summary']}\n")
            f.write("\n" + "-"*50 + "\n")

    return results

