import streamlit as st
from search_papers import search_papers
from analyze_paper import analyze_paper
from recommend_research import recommend_research
from analyze_trends import openai_analysis,analyze_trends_and_titles,plot_trends,summarize_by_openai,display_openai_analysis
from generate_framework import generate_project_framework

def app():
    st.title("AI Research Assistant")

    # 选择操作模式
    operation = st.selectbox(
        "Choose an operation",
        ["search", "analyze", "recommend", "trends", "generate_framework"]
    )

    # 执行基本检索功能
    if operation == "search":
        query = st.text_input("Enter search keyword")
        max_results = st.number_input("Enter max results", min_value=1, value=5)
        sort_by = st.selectbox(
            "Choose sorting method", 
            ["date", "relevance"]
        )
        if st.button("Search"):
            if query:
                papers = search_papers(query, max_results, sort_by)
                for paper in papers:
                    st.write(f"**Title:** {paper['title']}")
                    st.write(f"**Published:** {paper['published']}")
                    st.write(f"**Summary:** {paper['summary']}\n")
            else:
                st.warning("Please enter a keyword to search.")

    # 执行深度分析功能
    elif operation == "analyze":
        pdf_path = st.text_input("Enter PDF path for analysis")
        if st.button("Analyze"):
            if pdf_path:
                analysis = analyze_paper(pdf_path)
                st.write(f"**Technologies:** {analysis['technologies']}")
                st.write(f"**References:** {analysis['references']}")
            else:
                st.warning("Please enter the path to a PDF.")

    # 执行研究推荐功能
    elif operation == "recommend":
        topic = st.text_input("Enter research topic for recommendations")
        if st.button("Get Recommendations"):
            if topic:
                recommendations = recommend_research(topic)
                st.write(f"**Recommendations:** {recommendations}")
            else:
                st.warning("Please enter a research topic.")

    # 执行研究趋势分析功能
    elif operation == "trends":
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

    # 执行生成项目框架功能
    elif operation == "generate_framework":
        topic = st.text_input("Enter technical topic to generate framework")
        if st.button("Generate Framework"):
            if topic:
                project_framework = generate_project_framework(topic)
                st.write(f"**Generated Project Framework and Code:**\n{project_framework}")
            else:
                st.warning("Please enter a technical topic.")

if __name__ == "__main__":
    app()
