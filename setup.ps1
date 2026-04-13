# AI Travel Guide - Setup Script
# Run this script to set up the project for the first time

Write-Host "Setting up AI Travel Guide..." -ForegroundColor Green
Write-Host ""

# Check if Python is installed
Write-Host "Checking Python installation..." -ForegroundColor Yellow
$pythonVersion = python --version 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Found: $pythonVersion" -ForegroundColor Green
} else {
    Write-Host "✗ Python not found. Please install Python 3.8+ from https://www.python.org/downloads/" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Check if pip is available
Write-Host "Checking pip..." -ForegroundColor Yellow
python -m pip --version 2>&1 | Out-Null
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ pip is available" -ForegroundColor Green
} else {
    Write-Host "✗ pip not found" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Create virtual environment if it doesn't exist
if (-Not (Test-Path ".venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv .venv
    Write-Host "✓ Virtual environment created" -ForegroundColor Green
} else {
    Write-Host "✓ Virtual environment already exists" -ForegroundColor Green
}

Write-Host ""

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\.venv\Scripts\Activate.ps1"

Write-Host ""

# Install dependencies
Write-Host "Installing Python dependencies..." -ForegroundColor Yellow
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Write-Host "✓ Dependencies installed" -ForegroundColor Green

Write-Host ""

# Create .env file if it doesn't exist
if (-Not (Test-Path ".env")) {
    Write-Host "Creating .env file from template..." -ForegroundColor Yellow
    Copy-Item ".env.example" ".env"
    Write-Host "✓ .env file created (please edit with your API keys if needed)" -ForegroundColor Green
} else {
    Write-Host "✓ .env file already exists" -ForegroundColor Green
}

Write-Host ""
Write-Host "=========================================" -ForegroundColor Green
Write-Host "Setup Complete!" -ForegroundColor Green
Write-Host "=========================================" -ForegroundColor Green
Write-Host ""
Write-Host "To start the application:" -ForegroundColor Yellow
Write-Host "1. Start the backend server:" -ForegroundColor White
Write-Host "   python server.py" -ForegroundColor Cyan
Write-Host ""
Write-Host "2. Open index.html in your web browser" -ForegroundColor White
Write-Host "   Or run: python -m http.server 8080" -ForegroundColor Cyan
Write-Host "   Then visit: http://localhost:8080" -ForegroundColor Cyan
Write-Host ""
Write-Host "For AI chatbot features, install and run Ollama:" -ForegroundColor Yellow
Write-Host "1. Download from https://ollama.ai" -ForegroundColor White
Write-Host "2. Run: ollama pull phi3:mini" -ForegroundColor Cyan
Write-Host "3. Run: ollama serve" -ForegroundColor Cyan
Write-Host ""
