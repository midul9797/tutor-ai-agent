# Tutor Agent Backend

A sophisticated backend system that provides intelligent tutoring capabilities for Mathematics and Physics using Google's Gemini AI model. The system is built with FastAPI and implements a modular architecture with specialized sub-agents for different subjects.

## Features

- **Subject-Specific Agents**: Dedicated agents for Mathematics and Physics
- **Intelligent Query Routing**: Automatically routes questions to appropriate subject agents
- **AI-Powered Responses**: Utilizes Google's Gemini AI for comprehensive answers
- **RESTful API**: FastAPI-based endpoints for easy integration
- **Environment Configuration**: Secure configuration management using .env files

## Prerequisites

- Python 3.8 or higher
- Google Gemini API key

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd backend
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

## Project Structure

```
backend/
├── main.py              # Application entry point
├── api.py              # FastAPI routes and endpoints
├── tutor_agent.py      # Main tutor agent implementation
├── gemini.py           # Gemini AI integration
├── requirements.txt    # Project dependencies
├── .env               # Environment variables
└── sub_agents/        # Subject-specific agents
    ├── Math/
    │   └── math_agent.py
    └── Physics/
        └── physics_agent.py
```

## Usage

1. Start the server:

```bash
uvicorn api:app --reload
```

2. The API will be available at `http://localhost:8000`

3. Send POST requests to `/ask` endpoint with your question:

```bash
curl -X POST "http://localhost:8000/ask" -H "Content-Type: application/json" -d '{"question": "your question here"}'
```

## API Endpoints

- `POST /ask`: Submit a question to the tutor agent
  - Request body: `{"question": "your question"}`
  - Returns: AI-generated response based on the subject

## Dependencies

- fastapi==0.115.9
- google-generativeai==0.8.5
- pydantic==2.11.4
- pydantic-settings==2.9.1
- pydantic_core==2.33.2
- python-dotenv==1.1.0
- uvicorn==0.34.2

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Add your license information here]

## Contact

[Add your contact information here]
