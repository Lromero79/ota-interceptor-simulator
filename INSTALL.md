# Installation Guide

## Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

## Easy Python Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Lromero79/ota-interceptor-simulator.git
cd ota-interceptor-simulator
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment
- **On Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **On macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure API Keys (Optional)
Create a `.env` file in the project root:
```
GOOGLE_MAPS_API_KEY=your_key_here
```

### 6. Run the Application
```bash
python main.py
```

## Troubleshooting

### Permission Errors
- On Linux/macOS, ensure execute permissions: `chmod +x main.py`
- Run with `python` prefix if direct execution fails

### Missing Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Map Issues
- Add your Google Maps API key to `.env`
- Verify API key has Maps JavaScript API enabled

### Port Already in Use
- Modify the port in `main.py` if default port is occupied
- Default: `http://localhost:5000`

## Full Details
For additional configuration and advanced setup, refer to the project README.
