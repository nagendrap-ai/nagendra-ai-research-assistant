def load_css():
    return """
<style>

/* ================================================= */
/* HIDE STREAMLIT BRANDING */
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
/* MAIN LAYOUT */
/* ================================================= */

.block-container {
    padding-top: 1rem;
    padding-bottom: 0.5rem;
    max-width: 1400px;
}


/* ================================================= */
/* SIDEBAR */
/* ================================================= */

/* Sidebar background */

section[data-testid="stSidebar"] {
    background: #f8fafc;
    border-right: 1px solid #e5e7eb;
}


/* Sidebar main container */

section[data-testid="stSidebar"] .block-container {
    padding-top: 0.7rem;
    padding-bottom: 0.5rem;
}


/* ================================================= */
/* SIDEBAR TITLE */
/* ================================================= */

section[data-testid="stSidebar"] h1 {
    font-size: 22px;
    font-weight: 700;

    margin-top: 0;
    margin-bottom: 8px;

    color: #111827;
}


/* ================================================= */
/* SIDEBAR HEADINGS */
/* ================================================= */

section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #374151;

    margin-top: 8px;
    margin-bottom: 7px;

    line-height: 1.2;
}


/* ================================================= */
/* SIDEBAR DIVIDERS */
/* ================================================= */

section[data-testid="stSidebar"] hr {
    border: none;
    border-top: 1px solid #dfe3e8;

    margin-top: 10px;
    margin-bottom: 10px;
}


/* ================================================= */
/* SIDEBAR ONLINE STATUS */
/* ================================================= */

section[data-testid="stSidebar"] [data-testid="stAlert"] {
    padding: 7px 10px;

    min-height: 0;

    margin-top: 3px;
    margin-bottom: 10px;

    border-radius: 8px;

    font-size: 13px;
}


/* ================================================= */
/* SIDEBAR FILE UPLOADER */
/* ================================================= */

section[data-testid="stSidebar"] [data-testid="stFileUploader"] {
    border: none;

    padding: 0;

    margin-top: 0;
    margin-bottom: 8px;

    background: transparent;
}


/* Upload dropzone */

section[data-testid="stSidebar"]
[data-testid="stFileUploaderDropzone"] {

    padding: 7px;

    min-height: 78px;

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
/* SIDEBAR BUTTONS */
/* ================================================= */

section[data-testid="stSidebar"] .stButton {
    margin-top: 3px;
    margin-bottom: 3px;
}


/* All sidebar buttons */

section[data-testid="stSidebar"] .stButton button {

    width: 100%;

    min-height: 36px;
    height: 36px;

    padding: 4px 10px;

    border-radius: 9px;

    border: 1px solid #d1d5db;

    background: white;

    color: #374151;

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
/* VOICE CHAT + NEW CHAT */
/* ================================================= */

section[data-testid="stSidebar"] .stButton button {

    margin-top: 0;
    margin-bottom: 0;
}


/* ================================================= */
/* CHAT HISTORY */
/* ================================================= */

section[data-testid="stSidebar"]
[data-testid="stButton"] {

    margin-top: 2px;
    margin-bottom: 2px;
}


/* Chat history buttons */

section[data-testid="stSidebar"]
[data-testid="stButton"] button {

    min-height: 34px;
    height: 34px;

    padding: 4px 8px;

    font-size: 12px;

    text-align: left;
}


/* ================================================= */
/* SIDEBAR CAPTION */
/* ================================================= */

section[data-testid="stSidebar"] .stCaption {

    margin-top: 3px;
    margin-bottom: 3px;

    font-size: 12px;
}


/* ================================================= */
/* MAIN TITLES */
/* ================================================= */

.main-title {

    font-size: 46px;

    font-weight: 800;

    color: #ffffff;

    margin-bottom: 0;
}

.sub-title {

    color: #cbd5e1;

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
