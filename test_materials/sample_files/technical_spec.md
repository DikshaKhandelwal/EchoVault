# Technical Specification: EchoVault System

## Overview
EchoVault is a file management system that leverages AI to provide intelligent organization, search, and archiving capabilities.

## Architecture

### Backend (FastAPI)
- **Framework**: FastAPI 0.115.0
- **Server**: Uvicorn
- **Port**: 8000

### Frontend (Streamlit)
- **Framework**: Streamlit 1.38.0
- **Port**: 8501

### AI Integration
- **Provider**: OpenAI
- **Model**: GPT-4o-mini
- **Use Cases**: Summarization, tagging, semantic search

## Features

### 1. Ingest Mode
- **File Upload**: Single or multiple files
- **Folder Scanning**: Recursive directory scanning
- **Supported Formats**: TXT, MD, PDF, DOCX
- **Processing**: Text extraction, summarization, embedding generation

### 2. Recall Mode
- **Search**: Semantic search using embeddings
- **Query**: Natural language queries
- **Results**: Ranked by relevance
- **Actions**: View details, download files

### 3. Sync Mode
- **Comparison**: Compare two folders
- **Analysis**: Identify differences and duplicates
- **Recommendations**: AI-generated archiving suggestions

## Data Storage

### File Storage
```
data/
├── files/          # Original uploaded files
└── metadata.json   # File metadata and embeddings
```

### Metadata Schema
```json
{
  "file_id": "unique_identifier",
  "filename": "document.txt",
  "path": "/path/to/file",
  "content": "extracted_text",
  "summary": "ai_generated_summary",
  "tags": ["tag1", "tag2"],
  "embedding": [0.1, 0.2, ...],
  "timestamp": "2025-11-03T10:00:00"
}
```

## API Endpoints

### Ingest
- `POST /ingest/upload` - Upload files
- `POST /ingest/scan` - Scan folder

### Recall
- `POST /recall/search` - Semantic search
- `GET /recall/files` - List all files
- `GET /recall/file/{file_id}` - Get file details

### Sync
- `POST /sync/compare` - Compare folders
- `POST /sync/suggest` - Get archiving suggestions

## Security Considerations
- API key stored in .env file
- File size limits (50MB)
- Path traversal protection
- Input validation on all endpoints

## Performance
- Async file processing
- Batch embedding generation
- Efficient similarity search using NumPy

## Future Enhancements
- Database integration (PostgreSQL/MongoDB)
- User authentication
- Real-time folder watching
- Advanced file deduplication
- Multi-language support
