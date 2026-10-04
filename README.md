# AI Travel Agent

An intelligent travel planning assistant designed to coordinate multi-agent workflows, process travel data, and deliver automated itineraries using customizable tools.

# 📁 Project Structure

AI-Travel-agent/
├── agents/            # AI agent logic and workflow handlers
├── data/              # Travel datasets, templates, and sample configurations
├── tools/             # Custom tools and API integrations
├── app.py             # Primary application entry point
├── requirments.txt    # Python dependencies
└── README.md          # Project documentation

# 🚀 Features
 * Agentic Workflows: Modular agents in agents/ tailored for tasks like itinerary generation, location lookup, and budget estimation.

* Tool Integration: Custom utilities in tools/ that enable agents to query external data and APIs.

* Interactive Interface: Application runner (app.py) for launching the user interface or backend service.

# 🛠️ Prerequisites & Installation
Prerequisites
Python 3.8 or higher installed on your machine.

# Setup
1. Clone the repository:

Bash

git clone https://github.com/banul25/AI-Travel-agent.git

cd AI-Travel-agent

2. Set up a virtual environment (recommended):

Bash

python -m venv venv

source venv/bin/activate  # On Windows use: venv\Scripts\activate

3.Install required dependencies:

Bash

pip install -r requirments.txt

4.Configure Environment Variables:

Create a .env file in the root directory to store required API keys:

Code snippet

OPENAI_API_KEY=your_api_key_here

# 💻 Running the Application
Launch the main application using Python:

Bash

python app.py
