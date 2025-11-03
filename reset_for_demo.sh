#!/bin/bash
# Reset EchoVault for Demo Recording

echo "🎬 RESETTING ECHOVAULT FOR DEMO VIDEO"
echo "======================================"
echo ""

# Check if data folder exists
if [ -d "D:/echovault/data" ]; then
    echo "📁 Found existing data folder..."
    echo "🗑️  Deleting database..."
    rm -rf D:/echovault/data/
    echo "✅ Database cleared!"
else
    echo "✅ No existing database found"
fi

echo ""
echo "🎥 READY TO RECORD!"
echo ""
echo "Next steps:"
echo "1. Start backend: D:/echovault/.venv/Scripts/python.exe main.py"
echo "2. Start frontend: D:/echovault/.venv/Scripts/python.exe -m streamlit run frontend.py"
echo "3. Follow DEMO_VIDEO_GUIDE.txt for recording sequence"
echo ""
echo "Good luck with your demo! 🏅"
