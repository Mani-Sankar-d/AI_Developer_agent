# AI Developer Agent

An AI-powered developer agent that can interact with the local filesystem and perform development tasks using natural-language instructions.
Local MCP filesystem server is run and it exposes the filesystem services.
## Features

- Create and manage project directories and files.
- Read and modify files.
- Execute developer-oriented tasks through natural-language instructions.
- Maintain conversation history during a session.
- Use tools to interact with the local system.
- Built with LangGraph for agent workflow and state management.
- Simple interactive CLI interface.
- RAG capabilities to ingest pdf and question answer on it
## Usage

### 1. Clone the repository

```bash
git clone <repository-url>
cd AI_Developer_agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and add the required API keys/configuration.

For example:

```env
API_KEY=your_api_key
MODEL=model_name
```

### 5. Run the agent

The execution script is located outside the `AI_Developer_agent` package.

From the project root, run:

```bash
if AI_Developer_agent is in D:/projects then put .env and execute from D:/projects
<D:/projects> python -m AI_Developer_agent.client_executor

```

The agent will start an interactive CLI:

To exit just prompt "exit"
To use rag prompt "upload" then input path when asked

```text
YOU:
```

Enter a natural-language instruction, for example:

```text
Create a project called PRO in E:\ with an HTML login page.
```

The agent will execute the required operations using its available tools and return the result:

```text
AGENT:
The project has been created...
```

## Project Structure

```text
project-root/
├── AI_Developer_agent/
│   └── backend/
│       └── app/
│           └── agent/
│               ├── graph/
│               ├── tools/
│               └── ...
├── client_executor.py
├── requirements.txt
└── README.md
```
