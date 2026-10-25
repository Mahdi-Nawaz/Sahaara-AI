# 🌸 Sahaara AI — A Little Support, Anytime You Need It

> **An AI-powered emotional wellness companion designed to provide a safe, welcoming, and non-judgmental space to express feelings, find new perspectives, send voice notes, and take gentle steps forward.**

[![Streamlit](https://img.shields.io/badge/Streamlit-1.40+-FF4B4B.svg?style=flat&logo=Streamlit)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB.svg?style=flat&logo=Python)](https://python.org)
[![Google Gemini](https://img.shields.io/badge/Google%20GenAI-Gemini-4285F4.svg?style=flat&logo=Google)](https://ai.google.dev/)
[![Theme](https://img.shields.io/badge/Theme-Lite%20Pink%20Pastel-ffb6c1.svg?style=flat)](https://github.com)

---

## 📖 Overview

Many people experience loneliness, heartbreak, anxiety, stress, or the feeling that nobody understands them. Expressing emotions to friends and family can sometimes feel daunting due to fears of judgement or misunderstanding. Generic motivational quotes rarely address what someone is genuinely going through.

**Sahaara AI** bridges this gap. It listens first, acknowledges emotions, and offers comfort appropriate to the situation through conversation, gentle encouragement, humour, stories, daily inspiration, audio voice notes, and an optional Islamic Reflection Corner.

> *Sahaara is an emotional support companion and is not intended to replace human relationships, licensed mental-health professionals, or emergency services.*

---

## ✨ Core Features

### 🌸 1. Lite Pink Sanctuary Theme
* Designed with a calming, ethereal pastel rose palette (`#fff5f8`, `#fdeef5`, `#fff0f6`).
* Frosted glassmorphism cards with smooth border glows and backdrop blurs.
* Modern typography using Google Fonts (**Outfit** & **Plus Jakarta Sans**).
* Responsive layout optimized for phones, tablets, and laptops.

### 🎙️ 2. Voice Messages & Audio Support
* **Send Voice Notes**: Record your thoughts directly from your microphone via the Voice Studio. Gemini transcribes what you said and responds with deep empathy.
* **Sahaara Speaks Aloud**: Enjoy gentle voice playback for all responses powered by `gTTS`, with native Indian English (`tld='co.in'`) for Hinglish and authentic Hindi (`lang='hi'`).
* Toggle voice responses on or off anytime from the sidebar.

### 💭 3. Mood Check-in
Quickly check in with moods such as:
* 😔 **Low**
* 💔 **Heartbroken**
* 😰 **Anxious**
* 😤 **Angry**
* 🥱 **Unmotivated**
* 😂 **Bored**

### ✨ 4. Quick Activities
* 😂 **Make me laugh**: Friendly, gentle humor.
* 🪞 **New perspective**: Fresh, compassionate angles on difficult situations.
* 📖 **A meaningful story**: Inspiring reflections from history and everyday life.
* 🌱 **A tiny challenge**: Manageable, achievable steps you can take today.

### 🌙 5. Dedicated Islamic Reflection Corner (Optional)
* Faith-centered reflections on *sabr* (patience), *shukr* (gratitude), *tawakkul* (trust in Allah), *dua*, and hope.
* Verified references from Quranic meanings.
* Reassuring reminders that sadness and anxiety do not mean weak faith.

### 🌐 6. Multi-Language Support
* **Hinglish** (Hindi + English)
* **English**
* **Hindi**

### 🛡️ 7. Safety & Crisis Protection
* Automatic detection for distress signals with immediate helpline resources:
  * **India Emergency**: `112`
  * **Tele-MANAS National Mental Health Helpline**: `14416`

---

## 🛠️ Technology Stack

* **Frontend & Framework**: [Streamlit](https://streamlit.io/)
* **AI Model**: Google Gemini API (`google-genai` SDK)
* **Text-to-Speech**: [gTTS](https://pypi.org/project/gTTS/)
* **Styling**: Custom CSS3 (Glassmorphism, CSS Grid, Fluid Typography)
* **Audio Input**: Streamlit Native Audio Recording (`st.audio_input`)

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/Sahaara-AI.git
cd Sahaara-AI
```

### 2. Set Up Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Your Gemini API Key
Create `.streamlit/secrets.toml` from the example template:
```bash
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

Open `.streamlit/secrets.toml` and paste your Google Gemini API key:
```toml
GEMINI_API_KEY = "your_actual_gemini_api_key_here"
```
*(Get a free API key at [Google AI Studio](https://aistudio.google.com/)).*

### 5. Run the Application
```bash
streamlit run app.py
```
Open **`http://localhost:8501`** in your browser.

---

## 📁 Project Structure

```
Sahaara-AI/
├── .streamlit/
│   ├── config.toml           # Light pink theme tokens & server settings
│   └── secrets.toml.example  # Template for Gemini API key (secrets.toml is git-ignored)
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── .gitignore                # Protects secrets, virtual environments, and caches
└── README.md                 # Project documentation
```

---

## 🔒 Privacy & Safety Notice

* Never share sensitive passwords, payment credentials, or personal identification in the chat.
* Sahaara is not an emergency service. If you or someone you know is in immediate danger or experiencing a mental health crisis, please reach out to trusted friends, family, or local emergency services.

---

## 🌸 Author

Designed and built with care by **Mahdi Nawaz**.
