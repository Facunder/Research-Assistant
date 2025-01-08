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

    # # 如果GPT返回的数据为空，则直接返回
    # if not data:
    #     print("No experiment data found in the paper.")
    #     return

    # # 提取数字数据（假设数据是数值并以空格或换行分隔）
    # experiment_data = [float(value) for value in re.findall(r"[-+]?\d*\.\d+|\d+", data)]

    # if not experiment_data:
    #     print("No valid experimental data found.")
    #     return

    # # 可视化数据，假设数据为一个数值列表
    # plt.figure(figsize=(10, 6))
    # plt.bar(range(len(experiment_data)), experiment_data)
    # plt.xlabel("Experiment Index")
    # plt.ylabel("Measured Value")
    # plt.title("Experimental Results Visualization")
    # plt.show()
    return response.choices[0].message.content

def analyze_paper(pdf_path):
    with fitz.open(pdf_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    
    technologies = extract_technologies(text)
    references = extract_references(text)
    experiments =extract_experiment(text)
    
    return {"technologies": technologies, "references": references, "experiments":experiments}
