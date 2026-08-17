import os
import time
import streamlit as st

from app.styles import load_css
from app.config import PDF_FOLDER
from app.agent import process_question
from app.rag.uploaded_ingest import ingest_uploaded_pdf
from app.rag.store import (
    set_uploaded_vector_store,
    clear_uploaded_vector_store
)

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="Nagendra AI",
    page_icon="🤖",
    layout="wide",
)

st.markdown(load_css(), unsafe_allow_html=True)

# ======================================================
# SESSION STATE
# ======================================================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = {}

if "current_chat" not in st.session_state:
    st.session_state.current_chat = "Chat 1"

if "messages" not in st.session_state:
    st.session_state.messages = []

if "quick_prompt" not in st.session_state:
    st.session_state.quick_prompt = None

if "pending_prompt" not in st.session_state:
    st.session_state.pending_prompt = None


# ======================================================
# SIDEBAR
# ======================================================

with st.sidebar:

    st.title("🤖 Nagendra AI")

    st.success("🟢 Online")

    st.markdown("---")

    st.subheader("📄 Document")

    uploaded_pdf = st.file_uploader(
        "Upload PDF",
        type=["pdf"],
        key="sidebar_pdf"
    )

    if uploaded_pdf is not None:

        with st.spinner("📖 Processing PDF..."):

            vector_store = ingest_uploaded_pdf(uploaded_pdf)

            set_uploaded_vector_store(vector_store)

            st.session_state.current_pdf = uploaded_pdf

        st.success("✅ Ready")

    st.markdown("---")

    st.button(
    "🎤 Voice Chat (Coming Soon)",
    use_container_width=True,
    disabled=True
    )

    # Continue with New Chat
    # Continue with Chat History


    # -----------------------------
    # New Chat
    # -----------------------------
    if st.button("➕ New Chat", use_container_width=True):

        if st.session_state.messages:

            st.session_state.chat_history[
                st.session_state.current_chat
            ] = st.session_state.messages.copy()

        #chat_number = len(st.session_state.chat_history) + 1

        #st.session_state.current_chat = f"Chat {chat_number}"
        st.session_state.current_chat = None

        st.session_state.messages = []

        st.session_state.quick_prompt = None

        st.rerun()

    st.markdown("---")
    st.subheader("💬 Chat History")

    if st.session_state.chat_history:

        for chat_name in reversed(
            list(st.session_state.chat_history.keys())
        ):

            if st.button(
                chat_name,
                key=f"history_{chat_name}",
                use_container_width=True
            ):

                st.session_state.current_chat = chat_name

                st.session_state.messages = (
                    st.session_state.chat_history[
                        chat_name
                    ].copy()
                )

                st.rerun()

    else:

        st.caption("No previous chats")


# ======================================================
# HEADER
# ======================================================

st.markdown(
    """
<div class="main-title">
🤖 Nagendra AI
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="sub-title">
Personal AI Research Assistant
</div>
""",
    unsafe_allow_html=True,
)

# ======================================================
# WELCOME
# ======================================================

if len(st.session_state.messages) == 0:

    st.markdown("## 👋 How can I help you today?")

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        if st.button(
            "📄 Explain RAG",
            use_container_width=True
        ):
            st.session_state.quick_prompt = "Explain RAG"

    with c2:

        if st.button(
            "🌐 Latest AI News",
            use_container_width=True
        ):
            st.session_state.quick_prompt = "Latest AI news"

    with c3:

        if st.button(
            "🧮 Calculator",
            use_container_width=True
        ):
            st.session_state.quick_prompt = "125 * 378"

    with c4:

        if st.button(
            "📚 Ask PDFs",
            use_container_width=True
        ):
            st.session_state.quick_prompt = "Summarize the uploaded PDFs"

    st.divider()

# ======================================================
# CONVERSATION
# ======================================================

for message in st.session_state.messages:

    if message["role"] == "user":

        with st.chat_message(
            "user",
            avatar="👤"
        ):

            st.markdown(message["content"])

    else:

        with st.chat_message(
            "assistant",
            avatar="🤖"
        ):

            #st.markdown(message["answer"])
            answer = message["answer"]

            answer = answer.replace("<br>", "\n")
            answer = answer.replace("<br/>", "\n")
            answer = answer.replace("<br />", "\n")
            #answer = answer.replace("|", "\n")

            st.markdown(answer)

            with st.container(border=True):

                col1, col2 = st.columns(2)

                with col1:

                    st.caption("🧠 Tool Used")

                    st.write(message["tool"])

                with col2:

                    st.caption("⏱ Response Time")

                    st.write(f'{message["time"]} sec')



# ======================================================
# Upload Area
# ======================================================



# ======================================================
# CHAT INPUT
# ======================================================

prompt = st.chat_input("Ask anything... Search • PDFs • Calculator • AI")

# Quick action buttons
if st.session_state.quick_prompt:

    prompt = st.session_state.quick_prompt

    st.session_state.quick_prompt = None

# ======================================================
# PROCESS QUESTION
# ======================================================

# ======================================================
# Handle New Prompt
# ======================================================

if prompt:

    if prompt:

        if st.session_state.current_chat is None:

            title = prompt.strip()

            title = title.replace("\n", " ")

            if len(title) > 35:
                title = title[:35] + "..."

            st.session_state.current_chat = title

            # Create empty chat immediately
            st.session_state.chat_history[title] = []

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )
    st.session_state.chat_history[
        st.session_state.current_chat
    ] = st.session_state.messages.copy()
    
    st.session_state.pending_prompt = prompt

    st.rerun()


# ======================================================
# Generate AI Response
# ======================================================

if st.session_state.pending_prompt:

    prompt = st.session_state.pending_prompt

    start_time = time.time()

    with st.spinner("🧠 AI Agent is reasoning..."):

        result = process_question(prompt)

    elapsed = round(
        time.time() - start_time,
        2
    )

    answer = (
    result["answer"]
    .replace("<br>", "\n")
    .replace("<br/>", "\n")
    .replace("<br />", "\n")
    )
    st.session_state.messages.append(
        {
            "role": "assistant",
            "answer": result["answer"],
            "tool": result["tool"],
            "time": elapsed
        }
    )

    st.session_state.chat_history[
    st.session_state.current_chat
] = st.session_state.messages.copy()

    st.session_state.pending_prompt = None

    st.rerun()