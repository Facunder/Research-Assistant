import openai

# GPT-4生成项目框架和代码
def generate_project_framework(topic):
    prompt = f"""
    You are an AI project development assistant tasked with generating a complete project framework and basic code based on a specified technical topic (e.g., quantization). Please create the project based on the following requirements:

    1. **Project Structure**: Provide a complete project directory structure, including all major folders and files. Each file's purpose should be briefly described.

    2. **Code Framework**: Based on the project's functional requirements, provide some basic code examples. Each example should demonstrate a basic functional module that can be called within the project.

    3. **Specific Tasks**: For the topic "{topic}", generate a project structure that includes the following components, using the quantization topic as an example:
        - Data processing
        - Model building
        - Training and evaluation
        - Quantization implementation (e.g., model compression, quantization algorithms, etc.)
        - Testing and validation
        - Visualization (e.g., loss charts during training)
        For other topics, please refer to the structure and content similar to the quantization example.

    4. **Technology Stack Recommendations**: List potential tools, libraries, and frameworks that could be used for the project. Try to select commonly used and practical tools.

    Please ensure the project structure is clear and the code is simple, readable, and well-organized. The generated project structure and code should also have some degree of extensibility for future development.
    """
                                                
                                              
    # 请求GPT-4生成项目框架和代码
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[  # Ensure that the messages are passed correctly
            {"role": "user", "content": prompt}
        ]
    )
    # Extract and return the response content (using correct access pattern)
    return response.choices[0].message.content


