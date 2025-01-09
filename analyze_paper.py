import fitz  # PyMuPDF
import matplotlib.pyplot as plt
import openai
import re

openai.api_key = "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"

def extract_technologies(text):
    """
    使用GPT-4提取论文中的关键技术
    """
    prompt = f"Extract the key technologies mentioned in the following research paper:\n\n{text}\n\nKey Technologies:"

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[  # Ensure that the messages are passed correctly
            {"role": "user", "content": prompt}
        ]
    )
    # Extract and return the response content (using correct access pattern)
    return response.choices[0].message.content


def extract_references(text):
    """
    使用GPT-4提取论文中的参考文献
    """
    prompt = f"Extract the references from the following research paper:\n\n{text}\n\nReferences:(give me a list of references)"

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[  # Ensure that the messages are passed correctly
            {"role": "user", "content": prompt}
        ]
    )
    # Extract and return the response content (using correct access pattern)
    return response.choices[0].message.content

def extract_experiment(text):
    """
    使用GPT-4提取论文中的实验数据并生成可视化图表
    """
    # 使用GPT-4提取实验数据
    prompt = f"Extract the experimental results (numerical data) from the following research paper:\n\n{text}\n\nExperimental Data:(give me data and your conclusion)"

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[  # Ensure that the messages are passed correctly
            {"role": "user", "content": prompt}
        ]
    )
    # Extract and return the response content (using correct access pattern)
    return response.choices[0].message.content

def analyze_paper(pdf_file):
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    
    technologies = extract_technologies(text)
    references = extract_references(text)
    experiments = extract_experiment(text)
    
    return {"technologies": technologies, "references": references, "experiments": experiments}

if __name__ == "__main__":
    import sys
    with open(sys.argv[1], "rb") as pdf_file:
        result = analyze_paper(pdf_file)
        print(result)
