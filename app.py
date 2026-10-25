import streamlit as st
from google import genai
from google.genai import types
from datetime import date
from gtts import gTTS
import io
import re
import hashlib


# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Sahaara AI | A Little Support, Anytime 🌸",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# 2. ENCHANTING LITE PINK THEME & MOBILE-OPTIMIZED STYLES
# Soft rose water, pastel blossom glow, warm velvety text
# =========================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap');

    :root {
        --pink-bg-1: #fff5f8;
        --pink-bg-2: #fdeef5;
        --pink-card: rgba(255, 255, 255, 0.86);
        --pink-card-border: rgba(244, 180, 205, 0.5);
        --pink-primary: #ec4899;
        --pink-dark: #be185d;
        --pink-accent: #f472b6;
        --pink-soft: #fce7f0;
        --text-main: #381a2b;
        --text-body: #4e293f;
        --text-muted: #784c66;
        --shadow-soft: 0 10px 30px -4px rgba(225, 140, 175, 0.14), 0 4px 12px rgba(235, 160, 190, 0.08);
        --shadow-glow: 0 0 25px rgba(244, 114, 182, 0.22);
    }

    /* Base application background */
    .stApp {
        background:
            radial-gradient(ellipse at 8% 6%, rgba(255, 192, 208, 0.48), transparent 42%),
            radial-gradient(ellipse at 92% 14%, rgba(255, 218, 230, 0.58), transparent 40%),
            radial-gradient(ellipse at 50% 90%, rgba(254, 205, 222, 0.38), transparent 48%),
            linear-gradient(135deg, #fff7fa 0%, #fdeff5 50%, #fff2f6 100%) !important;
        color: var(--text-body);
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Header styling */
    [data-testid="stHeader"] {
        background: rgba(255, 245, 249, 0.75) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border-bottom: 1px solid rgba(244, 185, 208, 0.3);
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #fff8fb 0%, #fdeef5 50%, #fdf0f6 100%) !important;
        border-right: 1px solid rgba(244, 180, 205, 0.45) !important;
    }

    [data-testid="stSidebar"] * {
        color: var(--text-main) !important;
    }

    [data-testid="stSidebar"] .stCaption p {
        color: var(--text-muted) !important;
    }

    /* Headings */
    h1, h2, h3, h4 {
        font-family: 'Outfit', sans-serif !important;
        color: var(--text-main) !important;
        font-weight: 700 !important;
        letter-spacing: -0.5px;
    }

    p, li, label, .stMarkdown {
        color: var(--text-body);
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Hero Banner */
    .hero {
        position: relative;
        overflow: hidden;
        padding: 34px 32px;
        margin: 6px 0 24px 0;
        border-radius: 28px;
        border: 1.5px solid rgba(244, 175, 202, 0.55);
        background:
            radial-gradient(circle at 90% 15%, rgba(255, 222, 236, 0.75), transparent 36%),
            radial-gradient(circle at 10% 85%, rgba(254, 205, 225, 0.55), transparent 32%),
            linear-gradient(125deg, rgba(255, 245, 249, 0.96), rgba(254, 233, 243, 0.92));
        box-shadow: 0 16px 42px -6px rgba(235, 130, 168, 0.18), var(--shadow-glow);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
    }

    .hero-eyebrow {
        color: #db2777;
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 2.2px;
        text-transform: uppercase;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }

    .hero-title {
        color: #381528;
        font-family: 'Outfit', sans-serif;
        font-size: clamp(32px, 4.8vw, 48px);
        font-weight: 800;
        letter-spacing: -1.2px;
        line-height: 1.18;
        margin: 10px 0 6px 0;
    }

    .hero-title span {
        background: linear-gradient(135deg, #ec4899 0%, #db2777 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        color: #5d354d;
        font-size: 16px;
        line-height: 1.75;
        max-width: 680px;
        margin-top: 8px;
    }

    .hero-tags-container {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 16px;
    }

    .hero-tag {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 7px 15px;
        border: 1px solid rgba(244, 150, 185, 0.45);
        border-radius: 30px;
        color: #831843;
        background: rgba(255, 255, 255, 0.85);
        font-size: 12.5px;
        font-weight: 600;
        box-shadow: 0 2px 8px rgba(230, 120, 160, 0.08);
    }

    /* Section Headings */
    .section-heading {
        color: var(--text-main);
        font-family: 'Outfit', sans-serif;
        font-weight: 700;
        font-size: 21px;
        margin: 22px 0 4px 0;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .section-caption {
        color: var(--text-muted);
        font-size: 13.5px;
        margin-bottom: 14px;
        line-height: 1.6;
    }

    /* Cards */
    .glass-card {
        padding: 22px;
        border-radius: 22px;
        border: 1px solid var(--pink-card-border);
        background: var(--pink-card);
        box-shadow: var(--shadow-soft);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
    }

    .quote-card {
        padding: 24px 26px;
        border-radius: 22px;
        border: 1.5px solid rgba(244, 175, 202, 0.5);
        background:
            radial-gradient(circle at 95% 5%, rgba(255, 225, 238, 0.6), transparent 35%),
            linear-gradient(115deg, rgba(255, 245, 249, 0.95), rgba(254, 235, 244, 0.92));
        box-shadow: var(--shadow-soft);
        margin-bottom: 14px;
    }

    .quote-label {
        color: #db2777;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 1.8px;
        text-transform: uppercase;
    }

    .quote-text {
        color: #381528;
        font-family: 'Outfit', sans-serif;
        font-size: 20px;
        font-weight: 600;
        line-height: 1.65;
        margin: 10px 0;
    }

    .quote-source {
        color: #855571;
        font-size: 13px;
        line-height: 1.6;
        font-weight: 500;
    }

    /* Islamic Reflection Card */
    .islamic-card {
        padding: 24px 26px;
        border-radius: 24px;
        border: 1.5px solid rgba(167, 243, 208, 0.65);
        background:
            radial-gradient(circle at 92% 10%, rgba(209, 250, 229, 0.5), transparent 35%),
            linear-gradient(125deg, rgba(255, 247, 250, 0.95), rgba(254, 238, 245, 0.92));
        box-shadow: var(--shadow-soft);
        margin: 18px 0 20px 0;
    }

    .islamic-title {
        color: #065f46;
        font-family: 'Outfit', sans-serif;
        font-size: 24px;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .islamic-subtitle {
        color: #4a2c3d;
        font-size: 14px;
        line-height: 1.8;
    }

    /* Welcome Card */
    .welcome-card {
        padding: 22px 24px;
        border-radius: 22px;
        border: 1px solid rgba(244, 180, 205, 0.5);
        background: rgba(255, 255, 255, 0.88);
        box-shadow: var(--shadow-soft);
        margin: 14px 0 18px 0;
    }

    .welcome-title {
        color: #db2777;
        font-family: 'Outfit', sans-serif;
        font-size: 19px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .welcome-text {
        color: #4e293f;
        line-height: 1.8;
        font-size: 14.5px;
    }

    /* Voice Note Studio Card */
    .voice-studio-card {
        padding: 22px 24px;
        border-radius: 22px;
        border: 1.5px dashed rgba(236, 72, 153, 0.5);
        background:
            radial-gradient(circle at 90% 10%, rgba(255, 225, 238, 0.5), transparent 30%),
            linear-gradient(135deg, rgba(255, 245, 249, 0.94), rgba(254, 234, 243, 0.92));
        box-shadow: var(--shadow-soft);
        margin: 16px 0 20px 0;
    }

    .voice-studio-title {
        color: #be185d;
        font-family: 'Outfit', sans-serif;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 6px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .voice-studio-subtitle {
        color: #784c66;
        font-size: 13.5px;
        line-height: 1.6;
        margin-bottom: 14px;
    }

    /* Audio Player Styling */
    audio {
        width: 100% !important;
        height: 42px !important;
        border-radius: 24px !important;
        margin-top: 8px !important;
        outline: none !important;
        filter: drop-shadow(0 2px 6px rgba(236, 72, 153, 0.12));
    }

    /* Chat Messages */
    [data-testid="stChatMessage"] {
        background: rgba(255, 255, 255, 0.94) !important;
        border: 1px solid rgba(244, 185, 208, 0.45) !important;
        border-radius: 20px !important;
        padding: 14px 18px !important;
        margin-bottom: 12px !important;
        box-shadow: 0 4px 16px rgba(225, 140, 175, 0.08) !important;
    }

    [data-testid="stChatMessage"] p {
        color: #3b1d2e !important;
        line-height: 1.8 !important;
        font-size: 15px !important;
    }

    /* Chat Input & Bottom Container (Fixed for mobile) */
    [data-testid="stBottom"],
    [data-testid="stBottom"] > div {
        background: transparent !important;
    }

    [data-testid="stChatInput"] {
        border: 1.5px solid rgba(244, 150, 185, 0.6) !important;
        border-radius: 26px !important;
        background: rgba(255, 255, 255, 0.98) !important;
        box-shadow: 0 8px 30px rgba(230, 120, 160, 0.18) !important;
    }

    [data-testid="stChatInput"] textarea {
        color: #381528 !important;
        caret-color: #ec4899 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 15.5px !important;
        background: transparent !important;
    }

    [data-testid="stChatInput"] button {
        color: #ec4899 !important;
    }

    [data-testid="stChatInput"] textarea::placeholder {
        color: #a47590 !important;
    }

    /* Form elements & Selectboxes */
    .stTextInput input,
    .stSelectbox div[data-baseweb="select"],
    .stTextArea textarea {
        background-color: #ffffff !important;
        color: #381528 !important;
        border-color: rgba(244, 165, 195, 0.5) !important;
        border-radius: 14px !important;
    }

    .stSelectbox [data-testid="stMarkdownContainer"] p {
        color: #381528 !important;
        font-weight: 500;
    }

    /* Streamlit Buttons */
    .stButton > button {
        color: #4a2135 !important;
        background: rgba(255, 255, 255, 0.9) !important;
        border: 1.5px solid rgba(244, 165, 195, 0.55) !important;
        border-radius: 16px !important;
        min-height: 46px !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 3px 10px rgba(230, 130, 165, 0.08) !important;
    }

    .stButton > button:hover {
        color: #be185d !important;
        border-color: #ec4899 !important;
        background: linear-gradient(135deg, #fff0f5 0%, #fce7f0 100%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 18px rgba(236, 72, 153, 0.22) !important;
    }

    /* Primary Buttons */
    .stButton > button[kind="primary"] {
        color: #ffffff !important;
        background: linear-gradient(135deg, #f472b6 0%, #db2777 100%) !important;
        border: none !important;
        box-shadow: 0 4px 18px rgba(219, 39, 119, 0.28) !important;
    }

    .stButton > button[kind="primary"]:hover {
        color: #ffffff !important;
        background: linear-gradient(135deg, #f472b6 0%, #be185d 100%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 24px rgba(219, 39, 119, 0.38) !important;
    }

    /* Audio Input Widget */
    [data-testid="stAudioInput"] {
        background: rgba(255, 255, 255, 0.9) !important;
        border-radius: 20px !important;
        border: 1.5px solid rgba(244, 160, 195, 0.5) !important;
        padding: 8px 14px !important;
        box-shadow: 0 4px 14px rgba(235, 140, 175, 0.1) !important;
    }

    /* Alerts */
    [data-testid="stAlert"] {
        border-radius: 18px;
        border: 1px solid rgba(244, 180, 205, 0.4);
    }

    hr {
        border-color: rgba(244, 180, 205, 0.35) !important;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #855872;
        font-size: 13px;
        line-height: 1.9;
        padding: 28px 12px 14px 12px;
        margin-top: 32px;
        border-top: 1px solid rgba(244, 180, 205, 0.35);
    }

    .footer strong {
        color: #be185d;
    }

    /* =========================================================
       PHONE & MOBILE RESPONSIVE TWEAKS (max-width: 768px)
       Smooth touch targets, responsive cards, no overflow
       ========================================================= */
    @media (max-width: 768px) {
        .hero {
            padding: 22px 18px;
            border-radius: 20px;
            margin-bottom: 16px;
        }

        .hero-title {
            font-size: 27px !important;
            letter-spacing: -0.8px;
        }

        .hero-subtitle {
            font-size: 14.5px;
            line-height: 1.65;
        }

        .section-heading {
            font-size: 18.5px;
            margin: 18px 0 4px 0;
        }

        .quote-card {
            padding: 18px 20px;
        }

        .quote-text {
            font-size: 17px;
        }

        .islamic-title {
            font-size: 20px;
        }

        .stButton > button {
            min-height: 48px !important;
            font-size: 13.5px !important;
            padding: 8px 12px !important;
            white-space: normal !important;
            word-wrap: break-word !important;
        }

        [data-testid="stChatMessage"] {
            padding: 12px 14px !important;
            border-radius: 16px !important;
        }

        /* Prevent iOS auto-zoom on input focus */
        input, textarea, select {
            font-size: 16px !important;
        }

        audio {
            height: 38px !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# 3. HELPER FUNCTIONS FOR VOICE & SPEECH
# =========================================================
def clean_text_for_speech(text: str) -> str:
    """Prepares text for natural speech by removing markdown and emojis."""
    # Remove markdown headers
    clean = re.sub(r"#+\s*", "", text)
    # Remove markdown bold/italics
    clean = re.sub(r"[*_]{1,3}(.*?)[*_]{1,3}", r"\1", clean)
    # Remove markdown links [text](url) -> text
    clean = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", clean)
    # Remove bullet symbols
    clean = re.sub(r"^\s*[-*•]\s+", "", clean, flags=re.MULTILINE)
    # Remove emojis using unicode ranges
    emoji_pattern = re.compile(
        "[\U00010000-\U0010ffff]|[\u2600-\u27bf]|[\u2300-\u23ff]|[\u2b50-\u2b55]|[\ufe00-\ufe0f]",
        flags=re.UNICODE,
    )
    clean = emoji_pattern.sub("", clean)
    # Normalize whitespaces
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean


def generate_sahaara_voice(text: str, conv_language: str):
    """Generates a warm, soothing voice response using gTTS."""
    cleaned = clean_text_for_speech(text)
    if not cleaned:
        return None

    # Limit length for rapid TTS generation if text is very long
    if len(cleaned) > 500:
        cleaned = cleaned[:500] + "..."

    try:
        if conv_language == "Hindi":
            tts = gTTS(text=cleaned, lang="hi")
        elif "Hinglish" in conv_language:
            # Indian accent English sounds exceptionally natural for Hinglish & warmth
            tts = gTTS(text=cleaned, lang="en", tld="co.in")
        else:
            tts = gTTS(text=cleaned, lang="en")

        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        return audio_buffer.getvalue()
    except Exception:
        return None


# =========================================================
# 4. SESSION STATE INITIALIZATION
# =========================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "pending_prompt" not in st.session_state:
    st.session_state.pending_prompt = None

if "pending_audio" not in st.session_state:
    st.session_state.pending_audio = None

if "processed_audio_hashes" not in st.session_state:
    st.session_state.processed_audio_hashes = set()

if "quote_index" not in st.session_state:
    st.session_state.quote_index = date.today().toordinal() % 8

SUPPORT_MODES = [
    "Let me talk",
    "Give me a fresh perspective",
    "Make me laugh",
    "Share some wisdom",
    "Help me take a small step",
    "Islamic reflection (optional)",
]

if "support_mode_selection" not in st.session_state:
    st.session_state.support_mode_selection = "Let me talk"

def set_islamic_mode():
    st.session_state.support_mode_selection = "Islamic reflection (optional)"

def set_general_mode():
    st.session_state.support_mode_selection = "Let me talk"


# =========================================================
# 5. QUOTE COLLECTION
# =========================================================
GENERAL_QUOTES = [
    (
        "You do not have to solve your whole life today. "
        "Just take the next kind step.",
        "Sahaara reflection",
    ),
    (
        "Rest is not failure. Sometimes it is how you gather "
        "the strength to begin again.",
        "Sahaara reflection",
    ),
    (
        "Your current chapter is not the whole story.",
        "Sahaara reflection",
    ),
    (
        "You deserve kindness from yourself, too.",
        "Sahaara reflection",
    ),
    (
        "Small progress still counts, even when nobody sees it.",
        "Sahaara reflection",
    ),
    (
        "You can miss someone and still choose what is healthy for you.",
        "Sahaara reflection",
    ),
    (
        "Feelings are real, but they do not have to make every decision.",
        "Sahaara reflection",
    ),
    (
        "You are allowed to begin again without having everything figured out.",
        "Sahaara reflection",
    ),
]

ISLAMIC_QUOTES = [
    (
        "For indeed, with hardship comes ease.",
        "Quran 94:5–6 — English meaning; translation wording may vary.",
    ),
    (
        "Do not despair of the mercy of Allah.",
        "Quran 39:53 — excerpt from an English translation.",
    ),
    (
        "Allah does not burden a soul beyond what it can bear.",
        "Quran 2:286 — English meaning; translation wording may vary.",
    ),
    (
        "And He is with you wherever you are.",
        "Quran 57:4 — excerpt from an English translation.",
    ),
]


# =========================================================
# 6. SIDEBAR: CONTROLS, MODES & VOICE SETTINGS
# =========================================================
with st.sidebar:
    st.markdown("## 🌸 Sahaara AI")
    st.caption("A little support, whenever you need it.")
    st.divider()

    language = st.selectbox(
        "🌐 Conversation language",
        [
            "Hinglish (Hindi + English)",
            "English",
            "Hindi",
        ],
        index=0,
    )

    current_mode_index = (
        SUPPORT_MODES.index(st.session_state.support_mode_selection)
        if st.session_state.support_mode_selection in SUPPORT_MODES
        else 0
    )

    mode = st.selectbox(
        "✨ Choose your support mode",
        SUPPORT_MODES,
        index=current_mode_index,
        key="support_mode_selection",
    )

    st.divider()

    st.markdown("### 🎙️ Voice & Sound")
    voice_responses_enabled = st.toggle(
        "🔊 Voice playback for responses",
        value=True,
        help="Sahaara will speak her supportive responses aloud with a gentle voice.",
    )

    st.divider()

    st.markdown("### 🌷 What Sahaara offers")
    st.markdown(
        """
        - 🌸 A safe space to express yourself
        - 🎙️ Send voice notes or type anytime
        - 🔊 Listen to gentle voice responses
        - 🪞 Fresh, comforting perspectives
        - 😂 Light humour when you need a smile
        - 📖 Stories and thoughtful wisdom
        - 🌱 Small, manageable next steps
        """
    )

    # Clickable Islamic Reflection Corner button
    if mode == "Islamic reflection (optional)":
        st.button(
            "🌸 Back to General Mode",
            use_container_width=True,
            key="btn_sidebar_exit_islamic",
            on_click=set_general_mode,
        )
    else:
        st.button(
            "🌙 Optional Islamic reflections",
            use_container_width=True,
            key="btn_sidebar_enter_islamic",
            on_click=set_islamic_mode,
        )

    st.divider()

    # Quick AI key setup if secret is not set in Streamlit Cloud
    has_secret_key = bool(st.secrets.get("GEMINI_API_KEY", "").strip())
    if not has_secret_key:
        with st.expander("🔑 AI Key (Quick Connect)", expanded=True):
            st.caption("Add your Gemini key below to connect immediately:")
            user_key = st.text_input(
                "Gemini API Key",
                type="password",
                value=st.session_state.get("user_gemini_key", ""),
                placeholder="Paste key here",
                key="sidebar_key_input",
                help="Enter your key here to activate Sahaara immediately in this session.",
            )
            if user_key:
                st.session_state.user_gemini_key = user_key.strip()
                st.success("Key active! 🌸")

    st.markdown("### 🔒 Your privacy")
    st.caption(
        "Avoid sharing passwords, financial details, addresses "
        "or sensitive personal data. Sahaara is an emotional support "
        "companion, not an emergency or crisis service."
    )

    if st.button(
        "🗑️ Clear conversation",
        use_container_width=True,
        key="clear_conversation",
    ):
        st.session_state.messages = []
        st.session_state.pending_prompt = None
        st.session_state.pending_audio = None
        st.session_state.first_visit = True
        st.rerun()

    st.divider()
    st.caption("Designed with care by Mahdi Nawaz 🌸")


# =========================================================
# 7. HERO HEADER (ENCHANTING LITE PINK)
# =========================================================
st.markdown(
    """
    <div class="hero">
        <div class="hero-eyebrow">🌸 YOUR SAFE SPACE TO PAUSE & BREATHE</div>
        <div class="hero-title">Hello, dear human. <span>🌸</span></div>
        <div class="hero-title" style="font-size:clamp(26px,3.8vw,36px); margin-top: -2px;">
            Welcome to Sahaara.
        </div>
        <div class="hero-subtitle">
            A comforting, warm AI companion for the days that feel heavy,
            the thoughts you cannot quite explain, and the moments when
            you need someone who will truly listen without judgement.
        </div>
        <div class="hero-tags-container">
            <div class="hero-tag">🌸 Safe & Non-Judgmental</div>
            <div class="hero-tag">🎙️ Voice Messages & Text</div>
            <div class="hero-tag">🌱 One Step at a Time</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# 8. DAILY QUOTE SECTION
# =========================================================
st.markdown(
    '<div class="section-heading">✨ A little reminder for today</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-caption">'
    'Keep a thought that feels helpful. You do not need to force positivity.'
    '</div>',
    unsafe_allow_html=True,
)

quote_list = (
    ISLAMIC_QUOTES
    if mode == "Islamic reflection (optional)"
    else GENERAL_QUOTES
)

current_quote_index = st.session_state.quote_index % len(quote_list)
quote_text, quote_source = quote_list[current_quote_index]

st.markdown(
    f"""
    <div class="quote-card">
        <div class="quote-label">A MOMENT OF REFLECTION</div>
        <div class="quote-text">“{quote_text}”</div>
        <div class="quote-source">― {quote_source}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

quote_col1, quote_col2 = st.columns([1, 3])

with quote_col1:
    if st.button(
        "🔄 Another quote",
        use_container_width=True,
        key="next_quote",
    ):
        st.session_state.quote_index += 1
        st.rerun()


# =========================================================
# 9. DEDICATED ISLAMIC REFLECTION CORNER
# =========================================================
if mode == "Islamic reflection (optional)":
    btn_back_col, _ = st.columns([1, 2])
    with btn_back_col:
        st.button(
            "🌸 Return to General Companion Mode",
            key="btn_main_exit_islamic",
            on_click=set_general_mode,
            use_container_width=True,
        )

    st.markdown(
        """
        <div class="islamic-card">
            <div class="islamic-title">🌙 Islamic Reflection Corner</div>
            <div class="islamic-subtitle">
                A gentle space to reflect on sabr, shukr, tawakkul,
                dua, hope and Allah's mercy. You can explore these
                ideas without judgement or pressure.
                <br><br>
                Spiritual reflection can offer comfort, but feeling
                sad or anxious does not mean your faith is weak.
                Seeking trusted human support or professional help
                is also okay.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 🕌 What would you like to reflect on?")
    st.caption(
        "Choose a topic below, or simply write what is on your mind."
    )

    islamic_topics = [
        (
            "🤲 Finding peace",
            "Offer a compassionate Islamic reflection about finding "
            "peace during difficult times. Include one practical, "
            "optional step.",
        ),
        (
            "🌿 Sabr and patience",
            "Explain sabr in simple language, with a practical example. "
            "Do not suggest that patience means tolerating abuse or danger.",
        ),
        (
            "💚 Hope in Allah's mercy",
            "Share a gentle reflection on hope in Allah's mercy. "
            "Use a Quran reference only if you can identify it accurately.",
        ),
        (
            "📖 A story from the Quran",
            "Tell a short, accurate story explicitly found in the Quran "
            "and explain its lesson. Do not invent dialogue or details.",
        ),
        (
            "🌸 Gratitude and shukr",
            "Explain shukr in simple language and suggest one small "
            "optional daily practice. Do not dismiss genuine pain.",
        ),
        (
            "🕊️ When life feels difficult",
            "Respond compassionately to someone having a difficult day "
            "from an Islamic perspective. Never imply sadness means "
            "weak iman or that hardship is necessarily punishment.",
        ),
        (
            "🤍 Dua and tawakkul",
            "Explain dua and tawakkul in accessible language. "
            "Do not promise a guaranteed outcome or invent a dua.",
        ),
        (
            "🌱 Starting again",
            "Offer an encouraging Islamic reflection about making a "
            "fresh start, taking responsibility and showing oneself mercy.",
        ),
    ]

    for start in range(0, len(islamic_topics), 2):
        topic_cols = st.columns(2)

        for offset, col in enumerate(topic_cols):
            index = start + offset
            if index >= len(islamic_topics):
                continue

            label, topic_prompt = islamic_topics[index]

            with col:
                if st.button(
                    label,
                    use_container_width=True,
                    key=f"islamic_topic_{index}",
                ):
                    st.session_state.pending_prompt = (
                        topic_prompt
                        + "\nUse the selected conversation language. "
                        "Never invent Quran verses, Arabic text, hadith, "
                        "source references or religious rulings. "
                        "Distinguish Quran, hadith, scholarly interpretation "
                        "and personal reflection. If uncertain, say so."
                    )
else:
    isl_entry_col1, _ = st.columns([1, 2])
    with isl_entry_col1:
        st.button(
            "🌙 Open Islamic Reflection Corner 🤲",
            key="btn_main_enter_islamic",
            on_click=set_islamic_mode,
            use_container_width=True,
        )


# =========================================================
# 10. WELCOME CARD
# =========================================================
if not st.session_state.messages:
    st.markdown(
        """
        <div class="welcome-card">
            <div class="welcome-title">🌷 You can start wherever you are.</div>
            <div class="welcome-text">
                You do not need perfect words. Tell me what happened,
                what you are feeling, or what you wish someone understood.
                I will listen first and respond with tenderness and care.
                <br><br>
                💬 <strong>Type a message</strong>, 🎙️ <strong>send a voice note</strong>, or pick a mood below.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# 11. MOOD CHECK-IN (RESPONSIVE GRID)
# =========================================================
st.markdown(
    '<div class="section-heading">💭 How are you feeling right now?</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-caption">'
    'Tap a feeling that fits, or simply speak or type below.'
    '</div>',
    unsafe_allow_html=True,
)

moods = [
    ("😔 Low", "I am feeling low today. Please listen first and help me express what I am feeling."),
    ("💔 Heartbroken", "I am feeling heartbroken. Help me process my feelings without judging me."),
    ("😰 Anxious", "I am feeling anxious. Help me slow down and work through what is worrying me."),
    ("😤 Angry", "I am feeling angry. Help me understand the feeling and respond in a healthy way."),
    ("🥱 Unmotivated", "I feel unmotivated. Help me find one small and realistic next step."),
    ("😂 Bored", "I am bored. Suggest something fun, light or interesting to do."),
]

mood_cols = st.columns(3)

for index, (label, prompt) in enumerate(moods):
    with mood_cols[index % 3]:
        if st.button(
            label,
            use_container_width=True,
            key=f"mood_{index}",
        ):
            st.session_state.pending_prompt = prompt


# =========================================================
# 12. QUICK ACTIVITIES
# =========================================================
st.markdown(
    '<div class="section-heading">✨ A little something for you</div>',
    unsafe_allow_html=True,
)

activities = [
    (
        "😂 Make me laugh",
        "Help me smile with gentle, friendly humour. You can use a "
        "light joke or suggest a funny show. Do not mock my feelings.",
    ),
    (
        "🪞 New perspective",
        "Help me look at my situation from a fresh, compassionate "
        "perspective without dismissing my feelings.",
    ),
    (
        "📖 A meaningful story",
        "Share a short, meaningful story from history, culture or "
        "everyday life and explain its lesson. Clearly distinguish "
        "verified history from fictional illustrative stories.",
    ),
    (
        "🌱 A tiny challenge",
        "Suggest one small, achievable action I can take today. "
        "Make it realistic and do not overload me with tasks.",
    ),
]

activity_cols = st.columns(2)

for index, (label, prompt) in enumerate(activities):
    with activity_cols[index % 2]:
        if st.button(
            label,
            use_container_width=True,
            key=f"activity_{index}",
        ):
            st.session_state.pending_prompt = prompt


# =========================================================
# =========================================================
# 13. CONVERSATION HISTORY AREA
# =========================================================
st.markdown(
    '<div class="section-heading">💬 Your conversation with Sahaara</div>',
    unsafe_allow_html=True,
)

history_area = st.container()


# =========================================================
# 14. VOICE NOTE RECORDER (Clean & Minimal)
# =========================================================
voice_rec_col, voice_send_col = st.columns([3, 1])

with voice_rec_col:
    recorded_audio = st.audio_input(
        "Record your voice note",
        key="sahaara_voice_recorder",
        label_visibility="collapsed",
    )

with voice_send_col:
    if recorded_audio is not None:
        if st.button(
            "🚀 Send",
            type="primary",
            use_container_width=True,
            key="send_recorded_voice_btn",
        ):
            raw_audio_bytes = recorded_audio.getvalue()
            st.session_state.pending_audio = raw_audio_bytes
            st.rerun()


# =========================================================
# 15. CHAT TEXT INPUT (At bottom)
# =========================================================
user_input = st.chat_input(
    "Or type your message to Sahaara... 🌸"
)

if user_input and user_input.strip():
    st.session_state.pending_prompt = user_input.strip()


# =========================================================
# 16. SUPPORTIVE SYSTEM PROMPT & BOUNDARIES
# =========================================================
SYSTEM_PROMPT = f"""
You are Sahaara AI, a warm, thoughtful and emotionally supportive AI
companion with a gentle, calming presence. Your job is to help users feel
heard, comforted, and explore healthy, realistic next steps. You are not a
human, therapist, doctor or emergency service.

SELECTED LANGUAGE: {language}
SELECTED MODE: {mode}

LANGUAGE:
- If the language is Hinglish, use natural, empathetic Hindi-English.
- If English, use clear, friendly, comforting English.
- If Hindi, use natural Hindi in a readable and respectful style.
- Respect the language the user uses when they clearly prefer another one.

YOUR PERSONALITY:
- Be warm, calm, kind, respectful and genuine.
- Listen first. Validate the emotion before offering advice.
- Do not assume you know the user's full situation.
- Ask at most one gentle follow-up question when useful.
- Give manageable responses, not huge lectures.
- Do not be overly cheerful when the user is suffering.
- Do not shame, blame, judge, mock or lecture the user.
- Do not claim you have human feelings or lived experiences.

SUPPORT APPROACH:
1. Understand what the user is saying.
2. Acknowledge their feelings without automatically agreeing with every
   interpretation or assumption.
3. Offer a useful perspective or ask what kind of support they want.
4. When appropriate, suggest one small, practical next step.
5. Respect the user's choice if they only want to talk.

MODE GUIDANCE:
- Let me talk: prioritise listening, validation and gentle questions.
- Give me a fresh perspective: offer balanced alternatives without
  dismissing the user's experience.
- Make me laugh: use gentle humour when appropriate. Never make fun of
  grief, trauma, abuse, disability or the user's vulnerability.
- Share some wisdom: use accurate ideas from philosophy, cultures,
  history or real-life experiences. Do not fabricate quotations or facts.
- Help me take a small step: offer one or two realistic actions.
- Islamic reflection (optional): respond respectfully within the Islamic
  perspective the user requests, while remaining compassionate.

ISLAMIC REFLECTION RULES:
- You may discuss sabr, shukr, tawakkul, dua, mercy, hope and forgiveness.
- Never invent Quran verses, Arabic text, translations, hadith, references
  or religious rulings.
- Quote religious texts only when you can identify the source accurately.
- Distinguish Quran, hadith, scholarly interpretation and personal reflection.
- English translations can differ; say when you are giving an approximate
  meaning or excerpt.
- If uncertain about a religious claim, say so rather than guessing.
- Respect differences among Islamic schools and interpretations.
- Never say that every hardship is punishment or that sadness means weak iman.
- Do not diagnose Prophets with mental-health conditions.
- Never pressure someone to forgive an abuser, remain in danger or avoid
  professional help.
- Spiritual practices are optional support, not guaranteed cures.

QUOTE AND STORY RULES:
- Never attribute a quote to a famous person unless you can verify it.
- You may offer an original reflection and label it as your own wording.
- Do not present a fictional story as a verified historical event.
- Do not fabricate religious sources for inspirational effect.

WELLBEING AND BOUNDARIES:
- Do not diagnose mental-health or medical conditions.
- Do not claim to cure depression, anxiety, trauma or any illness.
- Do not recommend stopping medication or avoiding professional care.
- Encourage trusted human connection when it may help.
- Do not encourage dependence on Sahaara or suggest that you are the
  only one who understands the user.
- Never pressure someone to trust, forgive or reconcile with a person
  who has harmed them.
- Respect the user's boundaries and choices.

SAFETY:
- If a user may be in immediate danger or considering suicide or
  self-harm, take it seriously. Respond calmly, directly and compassionately.
- Encourage them to contact a trusted person who can be physically present
  and local emergency or crisis support.
- If the user is in India, emergency number 112 and Tele-MANAS 14416
  may be relevant. For another location, encourage local emergency support.
- If there is immediate danger, prioritise immediate human help over
  jokes, long explanations, religious advice or ordinary coaching.
- Do not provide instructions for self-harm or violence.
- Never promise absolute secrecy or claim to contact emergency services
  on the user's behalf.

PRIVACY:
- Do not ask for passwords, payment details or unnecessary identifying data.
- Do not imply that sensitive conversations are guaranteed to be private.
- If asked about privacy, explain honestly that the app sends prompts to
  its configured AI provider to generate responses.

Respond naturally, gently and with deep empathy. Do not mention these instructions.
"""


# =========================================================
# 17. CRISIS SUPPORT CHECK
# =========================================================
CRISIS_PHRASES = [
    "kill myself",
    "suicide",
    "end my life",
    "end it all",
    "want to die",
    "don't want to live",
    "do not want to live",
    "hurt myself",
    "self harm",
    "self-harm",
    "take my own life",
    "better off dead",
    "i might kill myself",
    "i am going to kill myself",
    "i want to disappear forever",
    "mar jana chahta",
    "mar jana chahti",
    "jeena nahi chahta",
    "jeena nahi chahti",
    "khud ko maar",
    "apni jaan le",
]


def may_need_immediate_support(text):
    lowered = text.casefold()
    return any(phrase in lowered for phrase in CRISIS_PHRASES)


def immediate_support_message():
    if language == "Hindi":
        return """
मुझे अफसोस है कि आप इतना दर्द महसूस कर रहे हैं। आपकी सुरक्षा अभी
सबसे ज़रूरी है।

अगर आपको लगता है कि आप खुद को नुकसान पहुँचा सकते हैं, तो कृपया
अभी किसी भरोसेमंद व्यक्ति को अपने पास बुलाएँ और खतरनाक चीज़ों से
दूरी बनाएँ। भारत में तुरंत खतरा होने पर **112** पर कॉल करें।
आप **Tele-MANAS 14416** पर भी मानसिक स्वास्थ्य सहायता के लिए संपर्क
कर सकते हैं।

क्या आप इस समय तत्काल खतरे में हैं, या आपने खुद को नुकसान पहुँचाने
के लिए कुछ किया है?
"""
    return """
I'm really sorry you're facing this much pain. I'm glad you said
something. Your safety matters more than solving everything right now.

If you might hurt yourself, please move away from anything you could
use to do so and contact someone you trust who can stay with you.
If you are in immediate danger in India, call **112**. You can also
contact **Tele-MANAS at 14416** for mental-health support.

Are you in immediate danger right now, or have you already done
anything to hurt yourself?
"""


# =========================================================
# 18. GENERATE THE ASSISTANT RESPONSE (TEXT & VOICE)
# =========================================================
if st.session_state.pending_prompt or st.session_state.pending_audio:
    user_audio_bytes = st.session_state.pending_audio
    prompt = st.session_state.pending_prompt
    st.session_state.pending_prompt = None
    st.session_state.pending_audio = None

    api_key = (
        st.session_state.get("user_gemini_key", "").strip()
        or st.secrets.get("GEMINI_API_KEY", "").strip()
    )

    if not api_key or api_key == "YOUR ACTUAL KEY":
        reply = (
            "🌸 **Sahaara needs to connect to its AI service.**\n\n"
            "To activate Sahaara online:\n\n"
            "**Permanent Fix (Recommended)**:\n"
            "1. On your laptop, click the black **`Manage app`** button in the bottom-right corner.\n"
            "2. Click the three dots (**`⋮`**) ➡️ **Settings** ➡️ **Secrets**.\n"
            "3. Paste:\n"
            "```toml\nGEMINI_API_KEY = \"your_gemini_api_key\"\n```\n"
            "4. Click **Save**.\n\n"
            "**Instant Fix (This session)**:\n"
            "Open the sidebar ⬅️ and enter your key under **🔑 AI Key (Quick Connect)**."
        )
        st.session_state.messages.append(
            {"role": "user", "content": prompt or "🎙️ [Voice Note]"}
        )
        st.session_state.messages.append(
            {"role": "assistant", "content": reply, "audio": None}
        )
    else:
        client = genai.Client(
            api_key=api_key,
            http_options=types.HttpOptions(timeout=60000),
        )

        # Handle incoming voice message
        if user_audio_bytes:
            audio_part = types.Part.from_bytes(data=user_audio_bytes, mime_type="audio/wav")
            audio_instructions = types.Part(
                text=(
                    "The user has sent a voice message.\n"
                    "Step 1: First line MUST be: [TRANSCRIPTION: <exact words user spoke, or 'Audio message' if quiet>]\n"
                    "Step 2: On subsequent lines, give your warm, empathetic response as Sahaara AI based on the system instructions."
                )
            )

            try:
                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=[audio_part, audio_instructions],
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT,
                        temperature=0.75,
                        max_output_tokens=800,
                    ),
                )
                full_text = response.text.strip() if response.text else ""

                # Extract transcription
                transcription = "Audio message"
                transcription_match = re.search(r"\[TRANSCRIPTION:\s*(.*?)\]", full_text, flags=re.DOTALL)
                if transcription_match:
                    transcription = transcription_match.group(1).strip()
                    reply = full_text[transcription_match.end():].strip()
                else:
                    reply = full_text

                if not reply:
                    reply = "I'm listening and right here with you. Feel free to tell me more whenever you're ready 🌸"

                # Check crisis in transcription
                if may_need_immediate_support(transcription):
                    reply = immediate_support_message()

                # Add user voice message to history with audio
                st.session_state.messages.append({
                    "role": "user",
                    "content": transcription if transcription != "Audio message" else "",
                    "audio": user_audio_bytes,
                })

            except Exception:
                reply = (
                    "I heard your voice note, but I had a little trouble connecting to my AI service just now. "
                    "Please try sending it once more or type what's on your mind 🌸"
                )
                st.session_state.messages.append({
                    "role": "user",
                    "content": "",
                    "audio": user_audio_bytes,
                })

        # Handle text message
        else:
            st.session_state.messages.append(
                {"role": "user", "content": prompt}
            )

            try:
                if may_need_immediate_support(prompt):
                    reply = immediate_support_message()
                else:
                    conversation = []
                    # Pass recent context
                    for message in st.session_state.messages[-12:]:
                        role = "user" if message["role"] == "user" else "model"
                        conversation.append(
                            types.Content(
                                role=role,
                                parts=[types.Part(text=message["content"])],
                            )
                        )

                    response = client.models.generate_content(
                        model="gemini-3.5-flash-lite",
                        contents=conversation,
                        config=types.GenerateContentConfig(
                            system_instruction=SYSTEM_PROMPT,
                            temperature=0.75,
                            max_output_tokens=800,
                        ),
                    )

                    reply = (
                        response.text.strip()
                        if response.text
                        else "I'm here with you. Could you tell me a little more? 🌸"
                    )

            except Exception:
                reply = (
                    "I'm sorry — I couldn't connect to the AI service just now. "
                    "Please check your internet connection and try again. Your message is safe here."
                )

        # Generate Sahaara voice playback if enabled
        reply_voice_bytes = None
        if voice_responses_enabled:
            reply_voice_bytes = generate_sahaara_voice(reply, language)

        st.session_state.messages.append(
            {"role": "assistant", "content": reply, "audio": reply_voice_bytes}
        )

        st.session_state.first_visit = False


# =========================================================
# 19. DISPLAY CHAT HISTORY WITH VOICE PLAYBACK
# =========================================================
with history_area:
    if not st.session_state.messages:
        st.caption(
            "Your conversation will appear here. Start with a mood, "
            "a quick activity, a voice note or the message box below 🌸"
        )

    for idx, message in enumerate(st.session_state.messages):
        avatar = "🌸" if message["role"] == "user" else "💛"

        with st.chat_message(message["role"], avatar=avatar):
            # User message
            if message["role"] == "user":
                if message.get("audio"):
                    st.markdown(
                        """
                        <div style="display:inline-flex; align-items:center; gap:6px; background:rgba(255,225,238,0.7); padding:4px 12px; border-radius:20px; font-weight:700; font-size:13px; color:#be185d; margin-bottom:6px;">
                            🎙️ Voice Message
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    st.audio(message["audio"], format="audio/wav")
                    if message.get("content"):
                        st.markdown(f"*{message['content']}*")
                else:
                    st.markdown(message["content"])

            # Sahaara assistant message
            elif message["role"] == "assistant":
                if message.get("audio"):
                    st.markdown(
                        """
                        <div style="display:inline-flex; align-items:center; gap:6px; background:rgba(255,235,245,0.8); padding:4px 12px; border-radius:20px; font-weight:700; font-size:13px; color:#be185d; margin-bottom:6px;">
                            🎙️ Sahaara's Voice Note
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    st.audio(message["audio"], format="audio/mp3")
                elif voice_responses_enabled:
                    if st.button("🔊 Listen to Sahaara", key=f"gen_voice_{idx}"):
                        audio_res = generate_sahaara_voice(message["content"], language)
                        if audio_res:
                            message["audio"] = audio_res
                            st.rerun()

                st.markdown(message["content"])


# =========================================================
# 20. FOOTER
# =========================================================
st.markdown(
    """
    <div class="footer">
        <strong>Made with 🌸 by Mahdi Nawaz</strong>
        <br>
        Sahaara AI is a supportive emotional companion, not a replacement
        for professional mental-health care or emergency services.
        <br>
        Be gentle with yourself. One kind step at a time. 💕
    </div>
    """,
    unsafe_allow_html=True,
)
