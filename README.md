# 🚀 SEO Assistant Pro

SEO Assistant Pro is an AI-powered web application that generates optimized titles, descriptions, and tags for blogs, videos, social media posts, and product pages. Built using Google's Gemini 2.5 Flash model, it streamlines SEO content creation with platform-specific guidelines and tone-controlled outputs.

---

## 🧠 Overview

### Digital creators often struggle with:
- Writer’s block
- SEO character/word limits
- Maintaining tone consistency across platforms
- Crafting click-worthy metadata

### SEO Assistant Pro solves these challenges by:
- Automatically generating platform-optimized metadata
- Enforcing strict SEO constraints for each content type
- Maintaining user-selected tones such as Clickbait, Professional, Serious, Humorous

---

## 🏛️ Architecture

SEO Assistant Pro follows a clean, modular architecture:

### **Frontend**
- Built using **Streamlit**
- Clean centered UI with “Hero” section introducing the tool
- Dropdowns for Content Type & Tone
- Text input for description

### **Backend**
- **Python 3.x** handles logic & API communication
- **google.generativeai** for Gemini requests
- **python-dotenv** for secure API key management  

### **AI Engine**
- **Gemini 2.5 Flash model**
- Generates structured JSON containing:
  - Optimized Title  
  - Meta Description  
  - Tags (10–15)
- Enforces length rules per content type  

---

## 🔁 Data Flow  

1. User selects content type and tone  
2. User enters a content description  
3. App constructs a structured SEO-aware prompt  
4. Gemini processes the prompt and returns JSON  
5. App cleans malformed AI output  
6. Streamlit displays Title, Description, and Tags  

---

## ⭐ Features

-  Clean, intuitive UI
-  Supports 5 content types  
-  Multiple tones (Clickbait, Serious, Professional, Humorous, Casual)  
-  Enforces strict limits (160-char meta, 280-char posts, 300-word YouTube desc.)  
-  Cleans malformed JSON before parsing  
-  Easy-to-copy output fields  

---

## 📂 Project Structure
```text
/SEO-Assistant-Pro
│── app.py # Main Streamlit app
│── .env # Gemini API key
│── requirements.txt
│── .gitignore
│── Report.pdf # Full technical documentation
│── README.md
```

---

## 🔧 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/seo-assistant-pro

cd seo-assistant-pro
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Add Gemini API key  
Create `.env` file:
```bash
GEMINI_API_KEY=your_api_key_here
```

### 4️⃣ Run the application
```bash
streamlit run app.py
```

---

## 🖥️ How to Use

1. Launch the app  
2. Select **Content Type**  
3. Select **Tone**  
4. Enter content description  
5. Click **Generate SEO Info**  
6. Copy your Title, Meta Description, and Tags  

---

## 🔮 Future Enhancements

- Keyword volume integration  
- Multi-language support  
- Saved history + favorites  
- Export options (CSV/JSON)  
- A/B testing for metadata variations  

---

## 📌 Conclusion

SEO Assistant Pro demonstrates the power of combining Streamlit UI with the Gemini model to improve SEO workflows. It provides high-quality, structured outputs tailored to each platform, making it a valuable tool for creators and marketers.

## 👨‍💻 Authors
- **Aayushi soni** – [GitHub](https://github.com/aayu684) | [LinkedIn](https://www.linkedin.com/in/aayushisoni6295/)



