#!/bin/bash
# EchoVault Startup Script

echo "🏆 EchoVault - Code Olympics Challenge Entry"
echo "=============================================="
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file not found!"
    echo "📝 Please create .env file with your OpenAI API key:"
    echo "   cp .env.example .env"
    echo "   Then edit .env and add your API key"
    echo ""
    read -p "Press Enter to continue anyway or Ctrl+C to exit..."
fi

echo "🚀 Starting FastAPI Backend..."
echo "   Backend will be available at: http://localhost:8000"
echo ""
echo "💡 After backend starts, open a NEW terminal and run:"
echo "   D:/echovault/.venv/Scripts/python.exe -m streamlit run frontend.py"
echo ""
echo "=============================================="
echo ""

D:/echovault/.venv/Scripts/python.exe main.py
