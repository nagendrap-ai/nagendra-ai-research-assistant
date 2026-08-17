import sys
from app.chatbot import start_chat
from app.ingest import ingest_pdfs

if len(sys.argv) > 1 and sys.argv[1].lower() == "ingest":
    ingest_pdfs()
else:
    start_chat()