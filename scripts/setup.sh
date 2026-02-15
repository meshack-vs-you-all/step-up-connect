#!/bin/bash

# Setup script for Youth Growth Ecosystem Platform

echo "Setting up environment..."

# Backend Setup
echo "Setting up Backend..."
cd backend
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

cd ..

# Frontend Check
echo "Checking Frontend..."
if command -v hugo &> /dev/null; then
    echo "Hugo is installed: $(hugo version)"
else
    echo "Hugo is NOT installed. Please install Hugo Extended."
fi

echo "Setup complete!"
echo "To run the backend: cd backend && source venv/bin/activate && uvicorn main:app --reload"
echo "To run the frontend: cd frontend && hugo server -D"
