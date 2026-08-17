import os
import time
import streamlit as st

from app.styles import load_css
from app.config import PDF_FOLDER
from app.agent import process_question, memory
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

st.markdown(
    load_css(),
    unsafe_allow_html=True
)


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

# ------------------------------------------------------
# Pinned chats
# ------------------------------------------------------

if "pinned_chats" not in st.session_state:
    st.session_state.pinned_chats = set()


# ======================================================
# HELPER FUNCTIONS
# ======================================================

def restore_chat_memory(messages):
    """
    Rebuild AI conversation memory from the selected chat.
    """

    memory.clear()

    for message in messages:

        if message["role"] == "user":

            memory.add_user_message(
                message["content"]
            )

        elif message["role"] == "assistant":

            memory.add_ai_message(
                message["answer"]
            )


def save_current_chat():
    """
    Saves the currently active chat into chat history.
    """

    if (
        st.session_state.current_chat
        and st.session_state.messages
    ):

        st.session_state.chat_history[
            st.session_state.current_chat
        ] = st.session_state.messages.copy()


def load_chat(chat_name):
    """
    Loads a selected chat and restores its memory.
    """

    st.session_state.current_chat = chat_name

    st.session_state.messages = (
        st.session_state.chat_history[
            chat_name
        ].copy()
    )

    st.session_state.pending_prompt = None

    restore_chat_memory(
        st.session_state.messages
    )

    st.rerun()


def delete_chat(chat_name):
    """
    Deletes a chat.
    """

    if chat_name in st.session_state.chat_history:

        del st.session_state.chat_history[
            chat_name
        ]

    # Remove from pinned chats
    st.session_state.pinned_chats.discard(
        chat_name
    )

    # If deleting current chat
    if st.session_state.current_chat == chat_name:

        memory.clear()

        st.session_state.current_chat = None

        st.session_state.messages = []

        st.session_state.pending_prompt = None

        st.session_state.quick_prompt = None

    st.rerun()


def rename_chat(old_name, new_name):
    """
    Renames a chat while preserving its messages
    and pinned status.
    """

    new_name = new_name.strip()

    if not new_name:
        return False

    if new_name == old_name:
        return False

    # Prevent duplicate names
    if new_name in st.session_state.chat_history:
        return False

    # Move conversation
    st.session_state.chat_history[
        new_name
    ] = st.session_state.chat_history.pop(
        old_name
    )

    # Update current chat
    if st.session_state.current_chat == old_name:

        st.session_state.current_chat = new_name

    # Update pinned status
    if old_name in st.session_state.pinned_chats:

        st.session_state.pinned_chats.remove(
            old_name
        )

        st.session_state.pinned_chats.add(
            new_name
        )

    return True


# ======================================================
# SIDEBAR
# ======================================================

with st.sidebar:

    st.title("🤖 Nagendra AI")

    st.success("🟢 Online")

    st.markdown("---")


    # ==================================================
    # DOCUMENT
    # ==================================================

    st.subheader("📄 Document")

    uploaded_pdf = st.file_uploader(
        "Upload PDF",
        type=["pdf"],
        key="sidebar_pdf"
    )

    if uploaded_pdf is not None:

        with st.spinner("📖 Processing PDF..."):

            vector_store = ingest_uploaded_pdf(
                uploaded_pdf
            )

            set_uploaded_vector_store(
                vector_store
            )

            st.session_state.current_pdf = (
                uploaded_pdf
            )

        st.success("✅ Ready")


    st.markdown("---")


    # ==================================================
    # VOICE CHAT
    # ==================================================

    st.button(
        "🎤 Voice Chat (Coming Soon)",
        use_container_width=True,
        disabled=True
    )


    # ==================================================
    # NEW CHAT
    # ==================================================

    if st.button(
        "➕ New Chat",
        use_container_width=True
    ):

        # Save current chat
        save_current_chat()

        # Clear AI memory
        memory.clear()

        # Start fresh chat
        st.session_state.current_chat = None

        st.session_state.messages = []

        st.session_state.quick_prompt = None

        st.session_state.pending_prompt = None

        st.rerun()


    # ==================================================
    # CHAT HISTORY
    # ==================================================

    st.markdown("---")

    st.subheader("💬 Chat History")


    if st.session_state.chat_history:

        # --------------------------------------------------
        # Get all chats
        # --------------------------------------------------

        all_chats = list(
            st.session_state.chat_history.keys()
        )


        # --------------------------------------------------
        # Pinned chats
        # --------------------------------------------------

        pinned_chats = [
            chat
            for chat in all_chats
            if chat in st.session_state.pinned_chats
        ]


        # --------------------------------------------------
        # Unpinned chats
        # --------------------------------------------------

        unpinned_chats = [
            chat
            for chat in reversed(all_chats)
            if chat not in st.session_state.pinned_chats
        ]


        # --------------------------------------------------
        # Final order
        # --------------------------------------------------

        ordered_chats = (
            pinned_chats +
            unpinned_chats
        )


        # ==================================================
        # DISPLAY CHAT ROWS
        # ==================================================

        for chat_name in ordered_chats:

            col1, col2, col3 = st.columns(
                [7, 1, 1],
                gap="small"
            )


            # ==============================================
            # CHAT NAME
            # ==============================================

            with col1:

                display_name = chat_name

                if len(display_name) > 24:

                    display_name = (
                        display_name[:24] +
                        "..."
                    )


                if st.button(
                    display_name,
                    key=f"history_{chat_name}",
                    use_container_width=True
                ):

                    load_chat(chat_name)


            # ==============================================
            # PIN BUTTON
            # ==============================================

            with col2:

                is_pinned = (
                    chat_name
                    in st.session_state.pinned_chats
                )


                if is_pinned:

                    pin_icon = "📌"

                else:

                    pin_icon = "📍"


                if st.button(
                    pin_icon,
                    key=f"pin_{chat_name}",
                    help=(
                        "Unpin chat"
                        if is_pinned
                        else "Pin chat"
                    )
                ):

                    if is_pinned:

                        st.session_state.pinned_chats.remove(
                            chat_name
                        )

                    else:

                        st.session_state.pinned_chats.add(
                            chat_name
                        )

                    st.rerun()


            # ==============================================
            # MORE MENU
            # ==============================================

            with col3:

                with st.popover(
                    "⋯",
                    use_container_width=True
                ):

                    st.markdown(
                        f"**{display_name}**"
                    )

                    st.markdown("---")


                    # ==================================
                    # RENAME
                    # ==================================

                    new_name = st.text_input(
                        "Chat name",
                        value=chat_name,
                        key=f"rename_input_{chat_name}"
                    )


                    if st.button(
                        "✏️ Rename",
                        key=f"rename_{chat_name}",
                        use_container_width=True
                    ):

                        new_name = new_name.strip()


                        if not new_name:

                            st.warning(
                                "Chat name cannot be empty."
                            )

                        elif (
                            new_name != chat_name
                            and new_name
                            in st.session_state.chat_history
                        ):

                            st.warning(
                                "A chat with this name already exists."
                            )

                        elif new_name != chat_name:

                            rename_chat(
                                chat_name,
                                new_name
                            )

                            st.rerun()


                    # ==================================
                    # PIN / UNPIN
                    # ==================================

                    if is_pinned:

                        if st.button(
                            "📌 Unpin",
                            key=f"menu_unpin_{chat_name}",
                            use_container_width=True
                        ):

                            st.session_state.pinned_chats.remove(
                                chat_name
                            )

                            st.rerun()

                    else:

                        if st.button(
                            "📌 Pin",
                            key=f"menu_pin_{chat_name}",
                            use_container_width=True
                        ):

                            st.session_state.pinned_chats.add(
                                chat_name
                            )

                            st.rerun()


                    st.markdown("---")


                    # ==================================
                    # DELETE
                    # ==================================

                    if st.button(
                        "🗑️ Delete",
                        key=f"delete_{chat_name}",
                        use_container_width=True
                    ):

                        delete_chat(
                            chat_name
                        )


    else:

        st.caption(
            "No previous chats"
        )


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

    st.markdown(
        "## 👋 How can I help you today?"
    )

    c1, c2, c3, c4 = st.columns(4)


    # --------------------------------------------------
    # Explain RAG
    # --------------------------------------------------

    with c1:

        if st.button(
            "📄 Explain RAG",
            use_container_width=True
        ):

            st.session_state.quick_prompt = (
                "Explain RAG"
            )


    # --------------------------------------------------
    # Latest AI News
    # --------------------------------------------------

    with c2:

        if st.button(
            "🌐 Latest AI News",
            use_container_width=True
        ):

            st.session_state.quick_prompt = (
                "Latest AI news"
            )


    # --------------------------------------------------
    # Calculator
    # --------------------------------------------------

    with c3:

        if st.button(
            "🧮 Calculator",
            use_container_width=True
        ):

            st.session_state.quick_prompt = (
                "125 * 378"
            )


    # --------------------------------------------------
    # Ask PDFs
    # --------------------------------------------------

    with c4:

        if st.button(
            "📚 Ask PDFs",
            use_container_width=True
        ):

            st.session_state.quick_prompt = (
                "Summarize the uploaded PDFs"
            )


    st.divider()


# ======================================================
# CONVERSATION
# ======================================================

for message in st.session_state.messages:

    # ==================================================
    # USER MESSAGE
    # ==================================================

    if message["role"] == "user":

        with st.chat_message(
            "user",
            avatar="👤"
        ):

            st.markdown(
                message["content"]
            )


    # ==================================================
    # ASSISTANT MESSAGE
    # ==================================================

    else:

        with st.chat_message(
            "assistant",
            avatar="🤖"
        ):

            answer = message["answer"]


            answer = answer.replace(
                "<br>",
                "\n"
            )

            answer = answer.replace(
                "<br/>",
                "\n"
            )

            answer = answer.replace(
                "<br />",
                "\n"
            )


            st.markdown(
                answer
            )


            # ==========================================
            # RESPONSE INFORMATION
            # ==========================================

            with st.container(
                border=True
            ):

                col1, col2 = st.columns(2)


                with col1:

                    st.caption(
                        "🧠 Tool Used"
                    )

                    st.write(
                        message["tool"]
                    )


                with col2:

                    st.caption(
                        "⏱ Response Time"
                    )

                    st.write(
                        f'{message["time"]} sec'
                    )


# ======================================================
# CHAT INPUT
# ======================================================

prompt = st.chat_input(
    "Ask anything... Search • PDFs • Calculator • AI"
)


# ======================================================
# QUICK ACTION BUTTONS
# ======================================================

if st.session_state.quick_prompt:

    prompt = (
        st.session_state.quick_prompt
    )

    st.session_state.quick_prompt = None


# ======================================================
# HANDLE NEW PROMPT
# ======================================================

if prompt:

    # --------------------------------------------------
    # Create chat title for new conversation
    # --------------------------------------------------

    if st.session_state.current_chat is None:

        title = prompt.strip()

        title = title.replace(
            "\n",
            " "
        )


        if len(title) > 35:

            title = (
                title[:35] +
                "..."
            )


        # ------------------------------------------------
        # Avoid duplicate chat names
        # ------------------------------------------------

        original_title = title

        counter = 2

        while title in st.session_state.chat_history:

            title = (
                f"{original_title} ({counter})"
            )

            counter += 1


        st.session_state.current_chat = (
            title
        )


        st.session_state.chat_history[
            title
        ] = []


    # --------------------------------------------------
    # Store user message
    # --------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )


    # --------------------------------------------------
    # Update chat history
    # --------------------------------------------------

    st.session_state.chat_history[
        st.session_state.current_chat
    ] = st.session_state.messages.copy()


    # --------------------------------------------------
    # Mark prompt as pending
    # --------------------------------------------------

    st.session_state.pending_prompt = (
        prompt
    )

    st.rerun()


# ======================================================
# GENERATE AI RESPONSE
# ======================================================

if st.session_state.pending_prompt:

    prompt = (
        st.session_state.pending_prompt
    )

    start_time = time.time()


    with st.spinner(
        "🧠 AI Agent is reasoning..."
    ):

        result = process_question(
            prompt
        )


    elapsed = round(
        time.time() - start_time,
        2
    )


    # --------------------------------------------------
    # Store assistant response
    # --------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "answer": result["answer"],
            "tool": result["tool"],
            "time": elapsed
        }
    )


    # --------------------------------------------------
    # Update chat history
    # --------------------------------------------------

    st.session_state.chat_history[
        st.session_state.current_chat
    ] = st.session_state.messages.copy()


    # --------------------------------------------------
    # Clear pending prompt
    # --------------------------------------------------

    st.session_state.pending_prompt = None

    st.rerun()
