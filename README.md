# Source Bias Detector for Conflict News

## Overview

This project aims to detect and analyze the sources cited in news articles related to conflicts, to determine if there's any bias based on the origin of these sources. By examining the balance of source origins, such as whether sources are predominantly US-based versus local, the tool provides insights into the impartiality of conflict coverage in news articles. This project leverages articles from the BBC archives and utilizes libraries like Bertopic, HuggingFace, OpenAI, and Streamlit to achieve its goal. Developed as part of a hackathon, this tool is designed to promote transparency and encourage a more nuanced understanding of conflict reporting.

## Features

- **Source Origin Detection**: Automatically detects the origins of sources cited in conflict-related news articles.
- **Bias Analysis**: Analyzes the balance of source origins to identify potential biases in news coverage.
- **User-Defined Queries**: Allows users to specify a conflict and the relevant sides (e.g., US-based vs. local sources) to tailor the analysis to their interests.
- **Article Recommendation**: Suggests articles where one side or the other has greater prominence, based on the user's query.

## Technology Stack

- **BBC Archives**: A rich dataset of news articles covering a wide range of topics, including conflicts, since 2017.
- **Bertopic**: For topic modeling and classification of articles. We use this to identify articles associated to different conflicts. 
- **HuggingFace**: Utilized for its powerful NLP models and tools.
- **OpenAI**: Provides advanced AI models for text analysis and insight generation.
- **Streamlit**: Enables the creation of an interactive web application for users to engage with the tool.

## Getting Started

### Prerequisites

- Python 3.11 or higher
- Pipenv for managing project dependencies

### Installation

1. Clone the repository:

```bash
git clone https://github.com/camorales197/source_analyzer.git
cd source_analyzer
```

2. Install dependencies using Pipenv:

```bash
pipenv install
```

3. Activate the Pipenv shell:

```bash
pipenv shell
```

### Running the Application

1. Launch the Streamlit web application:

```bash
streamlit run app.py
```

2. Open your web browser and go to the URL displayed in your terminal (typically `http://localhost:8501`).

3. Use the application by entering the conflict and sides you are interested in analyzing.

## Contributing

We welcome contributions from the community. If you're interested in helping improve this project, please feel free to reach out and let's talk about it. 

## License

This project is licensed under the MIT License - see the LICENSE file for details.
