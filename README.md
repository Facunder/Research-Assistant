# AI Research Assistant Project

This project is an AI-powered research assistant designed to interact with arXiv papers and provide various functionalities to help users analyze and gather insights from research papers. It includes features like paper search, deep analysis, trend analysis, research recommendations, and project framework generation.

## Features

1. **Search Papers**: Search for papers based on a keyword from arXiv and retrieve their titles, publication dates, and abstracts.
2. **Analyze Papers**: Analyze a given PDF paper by extracting key technologies, references, and visualizing experimental data.
3. **Research Recommendations**: Provide suggestions on research directions, methods, and skills based on a specific topic.
4. **Trend Analysis**: Analyze research trends over time for a given keyword, visualizing the number of papers published each year.
5. **Project Framework Generation**: Generate a complete project framework and basic code based on a specific technical topic (e.g., quantization).

## Table of Contents

- [Features](#features)
- [Modules](#modules)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Modules

- **`search_papers.py`**: Provides functionality to search for papers on arXiv by keyword.
- **`analyze_paper.py`**: Performs deep analysis of a given paper, including extracting key technologies and references.
- **`recommend_research.py`**: Generates research recommendations and a learning plan for a specific topic.
- **`analyze_trends.py`**: Analyzes and visualizes research trends over time for a given keyword.
- **`generate_framework.py`**: Generates a project framework for a given technical topic, with code templates and tool suggestions.
- **`app.py`**: The entry point for the application, providing a Streamlit interface to use all features.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-research-assistant.git
cd AI-research-assistant
```

### 2. Install dependencies

Make sure you have Python 3.6+ installed, then run the following command to install required dependencies:

```bash
pip install -r requirements.txt
```

The dependencies include:
- `openai`: for GPT-4o integration.
- `arxiv`: for accessing the arXiv API.
- `PyMuPDF`: for reading and processing PDFs.
- `matplotlib`: for visualizing data.
- `streamlit`: for building the interactive web interface.

### 3. Set up your OpenAI API key

Visit [OpenAI](https://openai.com/) and create an account if you don't have one. Once you have an API key, replace the `"YOUR_API_KEY"` placeholder in the `recommend_research.py` and `generate_framework.py` files with your actual key.

## Usage

To run the application, use Streamlit:

```bash
streamlit run app.py
```

This will launch a web interface where you can choose between different features and interact with the AI-powered research assistant.

### Available Features in the Web Interface:

1. **Search Papers**:  
   Enter a keyword and a maximum number of results, and get a list of papers related to your search topic.  
   Example:  
   - Enter `machine learning` and set `max_results` to `5` to retrieve 5 papers.

2. **Analyze a Paper**:  
   Upload a PDF of a paper for analysis. The system will extract technologies, references, and experimental data from the document.  
   Example:  
   - Upload a PDF file like `quantization_paper.pdf`.

3. **Research Recommendations**:  
   Enter a research topic, and the system will suggest research directions, methods, and skills needed to explore the topic.  
   Example:  
   - Enter `quantization` to get recommendations on how to research this topic.

4. **Trend Analysis**:  
   Enter a keyword and analyze the trends in research over time, visualizing the number of papers published each year.  
   Example:  
   - Enter `machine learning` to track research trends in this field.

5. **Generate Project Framework**:  
   Generate a project framework based on a technical topic, including code templates and tool suggestions.  
   Example:  
   - Enter `quantization` to generate a project framework on quantization, including data processing, model building, training, and testing code templates.

## Example Workflow

1. **Search for Papers**: Use the search functionality in the Streamlit app to find the latest research papers on a topic.
2. **Analyze a Paper**: Upload a PDF of a paper to extract key technologies, references, and visualize experimental data.
3. **Get Research Recommendations**: Enter a topic like `machine learning quantization` to get suggestions on methods and skills to explore.
4. **Visualize Trends**: Track trends over time by analyzing the number of papers published each year in a specific field.
5. **Generate a Project Framework**: Generate a full project structure and basic code for a topic like `quantization`, including data processing, model building, and testing components.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

