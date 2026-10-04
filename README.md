# AI Travel Agent

An intelligent travel planning assistant designed to coordinate **multi-agent workflows**, process travel data, and deliver automated travel itineraries using customizable tools and integrations.

## 📁 Project Structure

```text
AI-Travel-agent/
│
├── agents/
│   └── # AI agent logic and workflow handlers
│
├── data/
│   └── # Travel datasets, templates, and sample configurations
│
├── tools/
│   └── # Custom tools and API integrations
│
├── app.py
│   # Primary application entry point
│
├── requirments.txt
│   # Python dependencies
│
└── README.md
    # Project documentation
```

## 🚀 Features

### 🤖 Agentic Workflows

The project uses modular AI agents located in the `agents/` directory.

Agents can handle tasks such as:

* Travel itinerary generation
* Location lookup
* Destination recommendations
* Budget estimation
* Travel planning

### 🔧 Tool Integration

Custom tools are available in the `tools/` directory.

These tools allow agents to interact with external data sources and APIs to provide more useful travel information.

### 💻 Interactive Interface

The `app.py` file acts as the primary application entry point and can be used to launch the user interface or backend service.

## 🛠️ Prerequisites

Before running the project, make sure you have:

* Python **3.8 or higher**
* Git
* Required API keys
* Internet connection for external API integrations

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/banul25/AI-Travel-agent.git
```

Navigate to the project directory:

```bash
cd AI-Travel-agent
```

### 2. Create a Virtual Environment

Creating a virtual environment is recommended to keep project dependencies isolated.

#### Windows

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
```

Activate the environment:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirments.txt
```

> **Note:** The dependency file is named `requirments.txt` in the current repository.

## ⚙️ Configuration

Create a `.env` file in the root directory of the project.

Add the required API keys:

```env
OPENAI_API_KEY=your_api_key_here
```

### Environment Variables

| Variable         | Description                                    |
| ---------------- | ---------------------------------------------- |
| `OPENAI_API_KEY` | API key used for OpenAI-based AI functionality |

> **Important:** Never commit your `.env` file or API keys to GitHub.

Add `.env` to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

## 💻 Running the Application

After installing the dependencies and configuring the environment variables, launch the application using:

```bash
python app.py
```

The application will start using the configuration defined in the project.

## 🧠 How It Works

The AI Travel Agent follows a multi-agent workflow:

```text
              User Request
                   │
                   ▼
            Travel Planning
                   │
                   ▼
            Agent Coordinator
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
    Itinerary   Location    Budget
      Agent       Agent      Agent
        │          │          │
        └──────────┼──────────┘
                   ▼
             Tool Integration
                   │
                   ▼
            Result Processing
                   │
                   ▼
          Personalized Itinerary
```

### Workflow

1. The user provides a travel request.
2. The system analyzes the travel requirements.
3. Appropriate agents are selected.
4. Agents process their assigned tasks.
5. Tools and external APIs are used when required.
6. Results from different agents are combined.
7. A personalized travel itinerary is generated.

## 🧩 Main Components

| Component         | Purpose                                          |
| ----------------- | ------------------------------------------------ |
| `agents/`         | Contains AI agents and workflow logic            |
| `data/`           | Contains travel datasets and configuration files |
| `tools/`          | Contains custom tools and API integrations       |
| `app.py`          | Main application entry point                     |
| `requirments.txt` | Python dependency list                           |
| `.env`            | Stores API credentials and configuration         |
| `README.md`       | Project documentation                            |

## 🔮 Future Improvements

Potential improvements for the project include:

* Add hotel and flight search.
* Add real-time weather information.
* Integrate maps and location services.
* Add restaurant recommendations.
* Add travel budget optimization.
* Add persistent user preferences.
* Add a web-based user interface.
* Support multiple AI models.
* Add real-time travel information.
* Deploy the application as a cloud service.

## 📄 License

This project is developed for educational and experimental purposes.
