# Azure Cloud Resume Challenge

A simple resume website with a visitor counter, built with FastAPI backend and vanilla HTML/CSS/JavaScript frontend.

## Project Structure

```
resume-challenge/
├── backend/
│   ├── main.py              # FastAPI application
│   └── requirements.txt     # Python dependencies
└── frontend/
    ├── index.html          # Resume HTML
    ├── style.css           # Styling
    └── script.js           # Visitor counter logic
```

## Features

- Clean, professional resume layout
- Visitor counter that increments with each visit
- FastAPI backend with REST API
- CORS enabled for local development
- Responsive design

## Local Setup

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run the FastAPI server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Open the `frontend/index.html` file in your web browser, or use a simple HTTP server:

```bash
cd frontend
python -m http.server 8080
```

Then visit `http://localhost:8080`

## API Endpoints

- `GET /` - Root endpoint
- `GET /api/counter` - Get current visitor count
- `POST /api/counter` - Increment and get visitor count
- `GET /health` - Health check endpoint

## Customization

1. Edit `frontend/index.html` to update your resume content
2. Modify `frontend/style.css` to change the styling
3. Update the `API_URL` in `frontend/script.js` when deploying to Azure

## Next Steps for Azure Deployment

1. Deploy backend as Azure Function or Azure App Service
2. Host frontend on Azure Static Web Apps or Azure Blob Storage
3. Replace file-based storage with Azure Cosmos DB
4. Set up Azure CDN for better performance
5. Configure custom domain and HTTPS
6. Implement Infrastructure as Code (Terraform/Bicep)
7. Set up CI/CD pipeline with GitHub Actions

## Technologies Used

- **Backend**: Python, FastAPI, Uvicorn
- **Frontend**: HTML, CSS, JavaScript
- **Future**: Azure Functions, Cosmos DB, Static Web Apps, CDN