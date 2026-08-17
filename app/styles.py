def load_css():
    return """
<style>

/* ================================================= */
/* Hide Streamlit Branding */
/* ================================================= */

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}


/* ================================================= */
/* Main Layout */
/* ================================================= */

.block-container {
    padding-top: 1rem;
    padding-bottom: 0.5rem;
    max-width: 1400px;
}


/* ================================================= */
/* SIDEBAR */
/* ================================================= */

section[data-testid="stSidebar"] {
    background: #f8fafc;
    border-right: 1px solid #e5e7eb;
}

/* Reduce sidebar internal padding */

section[data-testid="stSidebar"] > div:first-child {
    padding-top: 1.2rem;
    padding-left: 1rem;
    padding-right: 1rem;
}

/* Sidebar headings */

section[data-testid="stSidebar"] h1 {
    color: #111827;
    font-size: 22px;
    margin-bottom: 8px;
}

section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #374151;
    font-size: 17px;
    margin-top: 8px;
    margin-bottom: 8px;
}

/* Sidebar horizontal lines */

section[data-testid="stSidebar"] hr {
    margin-top: 12px;
    margin-bottom: 12px;
}


/* ================================================= */
/* SIDEBAR ONLINE STATUS */
/* ================================================= */

section[data-testid="stSidebar"] [data-testid="stAlert"] {
    padding: 7px 10px;
    min-height: 0;
    border-radius: 8px;
    font-size: 13px;
}


/* ================================================= */
/* SIDEBAR BUTTONS */
/* ================================================= */

/* All sidebar buttons */

section[data-testid="stSidebar"] .stButton button {
    width: 100%;
    min-height: 36px;
    height: 36px;
    padding: 5px 10px;

    border-radius: 9px;

    border: 1px solid #d1d5db;

    background: white;

    font-size: 13px;
    font-weight: 500;

    transition: 0.2s;
}

/* Sidebar button hover */

section[data-testid="stSidebar"] .stButton button:hover {
    border-color: #6366f1;
    background: #eef2ff;
    color: #4338ca;

    transform: none;
}


/* ================================================= */
/* SIDEBAR FILE UPLOADER */
/* ================================================= */

section[data-testid="stSidebar"] [data-testid="stFileUploader"] {
    border: none;
    padding: 0;
    background: transparent;
}

/* Upload area */

section[data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] {
    padding: 8px;
    min-height: 80px;

    border: 1px solid #e5e7eb;
    border-radius: 9px;

    background: white;
}

/* Upload button */

section[data-testid="stSidebar"]
[data-testid="stFileUploader"] button {
    min-height: 32px;
    height: 32px;

    padding: 4px 10px;

    border-radius: 8px;

    font-size: 12px;
}

/* Upload text */

section[data-testid="stSidebar"]
[data-testid="stFileUploader"] small {
    font-size: 11px;
}


/* ================================================= */
/* SIDEBAR CHAT HISTORY */
/* ================================================= */

/* Chat history buttons */

section[data-testid="stSidebar"] [data-testid="stButton"] {
    margin-bottom: 4px;
}

/* Make history buttons compact */

section[data-testid="stSidebar"]
[data-testid="stButton"] button {
    min-height: 34px;
    height: 34px;

    padding: 4px 8px;

    font-size: 12px;

    text-align: left;
}


/* ================================================= */
/* SIDEBAR NEW CHAT */
/* ================================================= */

section[data-testid="stSidebar"] .stButton button[kind="secondary"] {
    font-size: 13px;
}


/* ================================================= */
/* MAIN TITLES */
/* ================================================= */

.main-title {
    font-size: 46px;
    font-weight: 800;
    color: #111827;
    margin-bottom: 0px;
}

.sub-title {
    color: #6b7280;
    font-size: 18px;
    margin-top: -8px;
    margin-bottom: 25px;
}


/* ================================================= */
/* MAIN AREA BUTTONS */
/* ================================================= */

.stButton button {
    width: 100%;

    height: 46px;

    border-radius: 14px;

    border: 1px solid #d1d5db;

    background: white;

    font-weight: 600;

    transition: 0.25s;
}

.stButton button:hover {
    border-color: #6366f1;

    background: #eef2ff;

    color: #4338ca;

    transform: translateY(-2px);
}


/* ================================================= */
/* CHAT INPUT */
/* ================================================= */

[data-testid="stChatInput"] {
    border-radius: 18px;
}

[data-testid="stChatInput"] textarea {
    font-size: 16px;
}


/* ================================================= */
/* USER CHAT */
/* ================================================= */

[data-testid="stChatMessage"]:has(
    [data-testid="chatAvatarIcon-user"]
) {
    background: #eef2ff;

    border-radius: 18px;

    padding: 12px;

    margin-bottom: 12px;

    border-left: 5px solid #6366f1;
}


/* ================================================= */
/* ASSISTANT CHAT */
/* ================================================= */

[data-testid="stChatMessage"]:has(
    [data-testid="chatAvatarIcon-assistant"]
) {
    background: white;

    border-radius: 18px;

    padding: 16px;

    margin-bottom: 18px;

    border: 1px solid #e5e7eb;

    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.05);
}


/* ================================================= */
/* METRICS */
/* ================================================= */

[data-testid="stMetric"] {
    background: white;

    border-radius: 12px;

    padding: 10px;

    border: 1px solid #e5e7eb;
}


/* ================================================= */
/* EXPANDERS */
/* ================================================= */

.streamlit-expanderHeader {
    font-weight: 600;
}


/* ================================================= */
/* SUCCESS BOX */
/* ================================================= */

[data-testid="stAlert"] {
    border-radius: 12px;
}


/* ================================================= */
/* DIVIDER */
/* ================================================= */

hr {
    border: none;

    border-top: 1px solid #ececec;
}


/* ================================================= */
/* SCROLLBAR */
/* ================================================= */

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-thumb {
    background: #cbd5e1;

    border-radius: 20px;
}

::-webkit-scrollbar-thumb:hover {
    background: #94a3b8;
}

</style>
"""
