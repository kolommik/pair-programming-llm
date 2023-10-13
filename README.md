# Pair Programming with a Large Language Model Repository

This repository contains Jupyter notebooks for lessons from the [Pair Programming with a LLM course](https://learn.deeplearning.ai/pair-programming-llm).

## Installation

Before running any code, ensure you have the following requirements:

- Python (3.10 or newer)
- [Poetry](https://python-poetry.org/) for package management

### Setup

1. Clone the repository:

```bash
git clone https://github.com/kolommik/pair-programming-llm.git
```

2. Navigate to the project directory:

```bash
cd pair-programming-llm
```

3. Install dependencies using Poetry:

```bash
poetry install
```

4. Activate the virtual environment:

```bash
poetry shell
```

## Project Structure

The repository is structured as follows:

- `/notebooks/google palm`: This directory contains Jupyter notebooks corresponding to the lessons from the course.
- `/notebooks/langchain open ai`: This directory contains Jupyter notebooks with examples of same ideas using OpenAI and langchain.

## Usage

To run any notebook, navigate to the `/notebooks` directory and open the notebook using Jupyter:

```bash
cd notebooks
cd 'google palm'
jupyter notebook notebook_name.ipynb
```

Replace "notebook_name.ipynb" with the name of the notebook you want to run.

## Contributing

This is a private repository, mainly for personal learning and testing. Therefore, contributions are not currently accepted.
