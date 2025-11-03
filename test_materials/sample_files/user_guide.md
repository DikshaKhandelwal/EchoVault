# EchoVault User Guide

Welcome to EchoVault! This guide will help you get started with the intelligent file management system.

## Getting Started

### Prerequisites
- Python 3.12 or higher
- OpenAI API key
- Modern web browser

### Installation
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your `.env` file with OpenAI API key
4. Start the backend: `python main.py`
5. Start the frontend: `streamlit run frontend.py`

## Features Overview

### 🗂️ Ingest Mode
Upload and organize your files automatically.

**How to use:**
1. Select "Ingest Mode" from the sidebar
2. Choose between:
   - **Upload Files**: Select one or multiple files from your computer
   - **Scan Folder**: Enter a folder path to scan all supported files
3. Click the upload/scan button
4. Wait for processing (AI will extract text, generate summaries, and create embeddings)

**Supported File Types:**
- Text files (`.txt`)
- Markdown files (`.md`)
- PDF documents (`.pdf`)
- Word documents (`.docx`)

### 🔍 Recall Mode
Search and retrieve your files using natural language.

**How to use:**
1. Select "Recall Mode" from the sidebar
2. Enter your search query (e.g., "meeting notes about project timeline")
3. View search results ranked by relevance
4. Click on any file to:
   - View AI-generated summary
   - See file metadata
   - Download the original file

**Search Tips:**
- Use natural language queries
- Be specific to get better results
- Try different phrasings if you don't find what you need

### 🔄 Sync Mode
Compare folders and get intelligent archiving recommendations.

**How to use:**
1. Select "Sync Mode" from the sidebar
2. Enter two folder paths to compare
3. Click "Analyze Folders"
4. Review:
   - Files unique to Folder A
   - Files unique to Folder B
   - Common files in both folders
5. Get AI-powered recommendations for archiving

**Use Cases:**
- Organizing project archives
- Identifying duplicate files
- Cleaning up old directories
- Preparing for backups

## Best Practices

### File Organization
- Use descriptive filenames
- Keep related files in the same folder
- Regularly archive old files

### Search Optimization
- Index files regularly
- Use specific keywords in your queries
- Review and update file summaries

### System Maintenance
- Clear old files from the system periodically
- Back up your `data/` folder regularly
- Monitor API usage to stay within limits

## Troubleshooting

### Backend won't start
- Check if port 8000 is available
- Verify your OpenAI API key is set correctly
- Ensure all dependencies are installed

### Frontend connection issues
- Make sure backend is running first
- Check that you're accessing http://localhost:8501
- Clear browser cache if needed

### Files not processing
- Verify file format is supported
- Check file size (large files take longer)
- Review console logs for error messages

## Support

For issues or questions:
- Check the README.md file
- Review error logs in the terminal
- Contact the development team

---

**Version**: 1.0  
**Last Updated**: November 3, 2025  
**Built for**: Code Olympics Challenge 🏅
