import openai

def recommend_research(query):

    # 更复杂的提示词，明确要求分开输出每个部分
    prompt = f"""
    I am looking for research directions, methods, and skills related to '{query}'. Please provide detailed suggestions for each part as follows:
    
    1. **Research Directions**: Suggest several research directions that are most relevant to '{query}', including any emerging areas, key challenges, and potential impact in the field.
    
    2. **Research Methods**: Propose the research methodologies, techniques, or frameworks that are commonly used or newly emerging in '{query}', and explain why they are suitable for the field.
    
    3. **Skills Required**: Identify the key skills and expertise required for conducting research in '{query}', covering both technical and non-technical aspects (e.g., programming, data analysis, domain-specific knowledge, communication).
    
    4. **Learning Plan**: Based on the skills above, suggest a structured learning plan. Include resources, courses, and practical activities to help acquire these skills step by step. Specify whether the learning plan is for a beginner or advanced learner.
    """

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[  # Ensure that the messages are passed correctly
            {"role": "user", "content": prompt}
        ]
    )
    # Extract and return the response content (using correct access pattern)
    return response.choices[0].message.content

