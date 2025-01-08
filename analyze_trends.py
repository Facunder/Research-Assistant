import arxiv
import openai
import matplotlib.pyplot as plt
import streamlit as st
from collections import defaultdict


def openai_analysis(titles, year):
    """
    使用 OpenAI 分析特定年份和关键词的研究趋势。
    """
    prompt = (
        f"Please analyze the following research paper titles published in {year}. "
        f"Summarize the main research directions, technologies, and findings based on these titles:\n\n"
        + "\n".join(titles)
    )

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def analyze_trends_and_titles(query, max_results=1000):
    """
    分析关键词在 ArXiv 上的研究趋势，统计每年论文数量，并获取标题进行分析。
    """
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    
    trend_data = defaultdict(int)
    yearly_titles = defaultdict(list)
    
    for result in search.results():
        try:
            year = result.published.year
            trend_data[year] += 1
            yearly_titles[year].append(result.title)
        except AttributeError as e:
            st.warning(f"Error processing result: {result}, {e}")
            continue
    
    # 将趋势数据转换为字典并按年份排序
    trend_data = dict(sorted(trend_data.items()))
    yearly_titles = dict(sorted(yearly_titles.items()))
    
    return trend_data, yearly_titles

def plot_trends(trend_data):
    """
    绘制论文数量随年份变化的图表。
    """
    years = list(trend_data.keys())
    counts = list(trend_data.values())
    
    plt.figure(figsize=(10, 6))
    plt.plot(years, counts, marker='o', color='blue')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Number of Papers', fontsize=14)
    plt.title('Research Trends Over Time', fontsize=16)
    plt.grid()
    st.pyplot(plt)

def summarize_by_openai(yearly_titles):
    """
    使用 OpenAI 对每年的论文标题进行总结分析。
    """
    openai_analyses = {}
    for year, titles in yearly_titles.items():
        st.write(f"Analyzing {len(titles)} papers from {year}...")
        analysis = openai_analysis(titles, year)
        openai_analyses[year] = analysis
    return openai_analyses

def display_openai_analysis(openai_analyses):
    """
    在 Streamlit 界面展示 OpenAI 分析结果。
    """
    for year, analysis in openai_analyses.items():
        st.subheader(f"Analysis for {year}")
        st.write(analysis)
        st.markdown("---")

def main():
    """
    主函数：处理用户输入、分析趋势、绘制图表、展示分析结果。
    """
    st.title("ArXiv Research Trends and Analysis")
    
    # 用户输入关键词和最大论文数量
    query = st.text_input("Enter your search query:", "machine learning")
    max_results = st.number_input("Max number of results:", min_value=10, max_value=10000, value=1000, step=10)
    
    if st.button("Analyze"):
        # 检索和分析数据
        st.write("Searching papers on ArXiv...")
        trend_data, yearly_titles = analyze_trends_and_titles(query, max_results)
        
        # 绘制趋势图
        st.write("Plotting research trends...")
        plot_trends(trend_data)
        
        # 使用 OpenAI 总结分析
        st.write("Analyzing research trends using OpenAI...")
        openai_analyses = summarize_by_openai(yearly_titles)
        
        # 展示分析结果
        st.write("Displaying OpenAI analyses...")
        display_openai_analysis(openai_analyses)

if __name__ == "__main__":
    main()

