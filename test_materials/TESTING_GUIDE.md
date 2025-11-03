# 🧪 EchoVault Testing Guide

This folder contains all materials needed to thoroughly test EchoVault's three modes.

## 📁 Folder Structure

```
test_materials/
├── sample_files/           # Files for testing Ingest & Recall modes
│   ├── project_proposal.txt
│   ├── meeting_notes.txt
│   ├── technical_spec.md
│   ├── code_review.txt
│   └── user_guide.md
├── folder_a/              # First folder for Sync mode testing
│   ├── financial_report_q4.txt
│   ├── marketing_strategy.txt
│   ├── product_roadmap.txt
│   └── team_roster.txt
└── folder_b/              # Second folder for Sync mode testing
    ├── financial_report_q4.txt  (modified version)
    ├── product_roadmap.txt      (duplicate)
    ├── client_list.txt          (unique)
    └── compliance_checklist.txt (unique)
```

## 🎯 Test Scenarios

### Mode 1: INGEST MODE Testing

#### Test 1.1: Single File Upload
**Steps:**
1. Go to Streamlit interface (http://localhost:8501)
2. Select "Ingest Mode" from sidebar
3. Choose "Upload Files" tab
4. Upload: `sample_files/project_proposal.txt`
5. Wait for processing

**Expected Results:**
- ✅ File uploaded successfully
- ✅ AI summary generated
- ✅ Tags extracted
- ✅ File stored in `data/files/`

#### Test 1.2: Multiple File Upload
**Steps:**
1. Upload all 5 files from `sample_files/` at once
2. Wait for batch processing

**Expected Results:**
- ✅ All 5 files processed
- ✅ Each file has unique summary
- ✅ Different tags for different content types

#### Test 1.3: Folder Scanning
**Steps:**
1. Choose "Scan Folder" tab
2. Enter path: `D:\echovault\test_materials\sample_files`
3. Click "Scan Folder"

**Expected Results:**
- ✅ All files in folder detected
- ✅ Recursive scanning works
- ✅ Metadata stored correctly

---

### Mode 2: RECALL MODE Testing

#### Test 2.1: Basic Search
**Steps:**
1. Select "Recall Mode" from sidebar
2. Enter query: "project timeline and budget"

**Expected Results:**
- ✅ project_proposal.txt ranked high (contains budget info)
- ✅ Relevant excerpts shown
- ✅ Results ranked by relevance

#### Test 2.2: Technical Search
**Steps:**
1. Query: "API endpoints and architecture"

**Expected Results:**
- ✅ technical_spec.md appears first
- ✅ Summary mentions FastAPI and architecture

#### Test 2.3: Meeting Search
**Steps:**
1. Query: "team meeting action items"

**Expected Results:**
- ✅ meeting_notes.txt appears
- ✅ Shows action items in summary

#### Test 2.4: File Download
**Steps:**
1. Click on any search result
2. Click "Download File" button

**Expected Results:**
- ✅ Original file downloads correctly
- ✅ File content intact

---

### Mode 3: SYNC MODE Testing

#### Test 3.1: Folder Comparison
**Steps:**
1. Select "Sync Mode" from sidebar
2. Enter Folder A path: `D:\echovault\test_materials\folder_a`
3. Enter Folder B path: `D:\echovault\test_materials\folder_b`
4. Click "Analyze Folders"

**Expected Results:**
- ✅ **Unique to Folder A:**
  - marketing_strategy.txt
  - team_roster.txt
  
- ✅ **Unique to Folder B:**
  - client_list.txt
  - compliance_checklist.txt
  
- ✅ **Common Files:**
  - financial_report_q4.txt (with differences noted)
  - product_roadmap.txt (exact duplicate)

#### Test 3.2: AI Recommendations
**Steps:**
1. Review the AI-generated archiving suggestions

**Expected Results:**
- ✅ Identifies financial_report_q4.txt has been modified
- ✅ Suggests keeping newer version
- ✅ Recommends archiving exact duplicates
- ✅ Provides organization strategy

---

## 🔍 What to Look For

### Performance
- File processing completes in reasonable time (< 30s per file)
- Search results appear quickly (< 5s)
- UI remains responsive during operations

### Accuracy
- Summaries capture main points of documents
- Tags are relevant to content
- Search results match query intent
- Folder comparison is accurate

### Error Handling
- Unsupported files show clear error messages
- Invalid paths are handled gracefully
- API errors don't crash the application

---

## 📊 Test Queries to Try

### Ingest Mode Queries
- Try uploading the same file twice (should handle duplicates)
- Upload an empty text file
- Scan an empty folder

### Recall Mode Queries
- "budget and financial information"
- "code review feedback"
- "user documentation"
- "meeting decisions"
- "technical architecture"
- "roadmap for next year"

### Sync Mode Scenarios
- Compare folder_a with itself (should show all common)
- Compare empty folders
- Compare folder with many subdirectories

---

## 🐛 Known Test Cases

### Edge Cases to Test
1. **Large Files**: Create a file > 10MB
2. **Special Characters**: Files with unicode names
3. **Empty Content**: Files with no text
4. **Many Files**: Upload 50+ files at once

---

## ✅ Testing Checklist

### Ingest Mode
- [ ] Upload single file
- [ ] Upload multiple files
- [ ] Scan folder
- [ ] Verify summaries are accurate
- [ ] Check tags are relevant
- [ ] Confirm files stored in data/

### Recall Mode
- [ ] Perform semantic search
- [ ] Try multiple query types
- [ ] Download files
- [ ] Verify search relevance
- [ ] Test empty queries
- [ ] Test with no files indexed

### Sync Mode
- [ ] Compare two folders
- [ ] Identify unique files
- [ ] Find duplicates
- [ ] Review AI recommendations
- [ ] Test with nested folders
- [ ] Compare empty folders

### Integration
- [ ] Backend API responding
- [ ] Frontend connecting to backend
- [ ] Error messages displaying
- [ ] Success notifications showing
- [ ] Data persisting between sessions

---

## 📝 Notes

**Sample File Characteristics:**

1. **project_proposal.txt** (1.2KB)
   - Business document
   - Financial data
   - Timeline information

2. **meeting_notes.txt** (1.0KB)
   - Action items
   - Team decisions
   - Meeting details

3. **technical_spec.md** (2.5KB)
   - Architecture details
   - API documentation
   - Technical requirements

4. **code_review.txt** (1.8KB)
   - Code quality assessment
   - Security notes
   - Compliance verification

5. **user_guide.md** (3.2KB)
   - Usage instructions
   - Troubleshooting
   - Best practices

**Folder Comparison Designed to Show:**
- Modified files (financial_report_q4.txt)
- Exact duplicates (product_roadmap.txt)
- Unique files in each folder
- AI archiving recommendations

---

## 🎯 Success Criteria

Your EchoVault system passes testing if:
1. ✅ All 5 sample files ingest successfully
2. ✅ Search returns relevant results for all queries
3. ✅ Folder comparison correctly identifies differences
4. ✅ AI summaries are coherent and accurate
5. ✅ No crashes or unhandled errors
6. ✅ Data persists across restarts

---

## 🚀 Quick Start Testing

```bash
# Make sure backend is running
D:/echovault/.venv/Scripts/python.exe main.py

# In another terminal, start frontend
D:/echovault/.venv/Scripts/python.exe -m streamlit run frontend.py

# Then follow the test scenarios above!
```

Good luck with testing! 🏅
