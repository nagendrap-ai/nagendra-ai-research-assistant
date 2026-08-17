def load_css():
    return """
<style>

/* ------------------------------------------------ */
/* Hide Streamlit Branding */
/* ------------------------------------------------ */

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

#MainMenu{
    visibility:hidden;
}

/* ------------------------------------------------ */
/* Main Layout */
/* ------------------------------------------------ */

.block-container{
    padding-top:1rem;
    padding-bottom:0.5rem;
    max-width:1400px;
}

/* ------------------------------------------------ */
/* Sidebar */
/* ------------------------------------------------ */

section[data-testid="stSidebar"]{
    background:#f8fafc;
    border-right:1px solid #e5e7eb;
}

section[data-testid="stSidebar"] h1{
    color:#111827;
}

section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3{
    color:#374151;
}

/* ------------------------------------------------ */
/* Titles */
/* ------------------------------------------------ */

.main-title{
    font-size:46px;
    font-weight:800;
    color:#111827;
    margin-bottom:0px;
}

.sub-title{
    color:#6b7280;
    font-size:18px;
    margin-top:-8px;
    margin-bottom:25px;
}

/* ------------------------------------------------ */
/* Buttons */
/* ------------------------------------------------ */

.stButton button{

    width:100%;

    height:46px;

    border-radius:14px;

    border:1px solid #d1d5db;

    background:white;

    font-weight:600;

    transition:0.25s;

}

.stButton button:hover{

    border-color:#6366f1;

    background:#eef2ff;

    color:#4338ca;

    transform:translateY(-2px);

}

/* ------------------------------------------------ */
/* Chat Input */
/* ------------------------------------------------ */

[data-testid="stChatInput"]{

    border-radius:18px;

}

[data-testid="stChatInput"] textarea{

    font-size:16px;

}

/* ------------------------------------------------ */
/* User Chat */
/* ------------------------------------------------ */

[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]){

    background:#eef2ff;

    border-radius:18px;

    padding:12px;

    margin-bottom:12px;

    border-left:5px solid #6366f1;

}

/* ------------------------------------------------ */
/* Assistant Chat */
/* ------------------------------------------------ */

[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]){

    background:white;

    border-radius:18px;

    padding:16px;

    margin-bottom:18px;

    border:1px solid #e5e7eb;

    box-shadow:0 2px 12px rgba(0,0,0,0.05);

}

/* ------------------------------------------------ */
/* Metrics */
/* ------------------------------------------------ */

[data-testid="stMetric"]{

    background:white;

    border-radius:12px;

    padding:10px;

    border:1px solid #e5e7eb;

}

/* ------------------------------------------------ */
/* Expanders */
/* ------------------------------------------------ */

.streamlit-expanderHeader{

    font-weight:600;

}

/* ------------------------------------------------ */
/* Success Box */
/* ------------------------------------------------ */

[data-testid="stAlert"]{

    border-radius:12px;

}

/* ------------------------------------------------ */
/* Divider */
/* ------------------------------------------------ */

hr{

    border:none;

    border-top:1px solid #ececec;

}

/* ------------------------------------------------ */
/* Scrollbar */
/* ------------------------------------------------ */

::-webkit-scrollbar{

    width:8px;

}

::-webkit-scrollbar-thumb{

    background:#cbd5e1;

    border-radius:20px;

}

::-webkit-scrollbar-thumb:hover{

    background:#94a3b8;

}

/* File uploader */

[data-testid="stFileUploader"]{
    border:none;
    padding:0;
    background:transparent;
}


}
</style>
"""