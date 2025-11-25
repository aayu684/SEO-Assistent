
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

import json

# Load environment variables
load_dotenv()

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("API Key not found. Please check your .env file.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

def generate_seo_content(content_type, description, tone):
    # Platform-specific guidelines
    guidelines = {
        "YouTube Video": "Description length: STRICTLY Max 300 words. Include CTAs to like, share, and subscribe.",
        "Blog Post": "Meta Description length: STRICTLY Max 160 characters. Encourage reading more or sharing.",
        "Social Media Post": "Description length: STRICTLY Max 280 characters. Short, punchy, and engaging.",
        "Product Description": "Description length: STRICTLY Max 200 words. Focus on benefits and 'Buy Now' CTA.",
        "Website Page": "Meta Description length: STRICTLY Max 160 characters. Professional and clickable."
    }
    
    specific_instruction = guidelines.get(content_type, "Standard SEO best practices.")

    prompt = f"""
    Act as an expert SEO specialist.
    I have a piece of content with the following details:
    
    Content Type: {content_type}
    Description: {description}
    Target Tone: {tone}
    
    Instructions:
    {specific_instruction}
    - Ensure the Title and Description strictly match the "{tone}" tone.
    
    Output Format:
    Provide the output strictly as a valid JSON object with the following keys:
    - "title": (string) The optimized title.
    - "description": (string) The optimized description.
    - "tags": (list of strings) 10-15 relevant tags.
    
    Do not include any markdown formatting (like ```json) or explanations. Just the raw JSON string.
    """
    
    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        # Clean up potential markdown code blocks
        if text.startswith("```json"):
            text = text[7:]
        if text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
            
        return json.loads(text.strip())
    except Exception as e:
        return {"error": f"Error generating content: {e}"}

# Streamlit UI Configuration
st.set_page_config(
    page_title="SEO Assistant Pro",
    page_icon="🚀",
    layout="centered"
)

# Header
st.title("🚀 SEO Assistant Pro")
st.markdown("Generate viral-ready titles, descriptions & tags in seconds.")

# Main Content
with st.container():
    with st.form("seo_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            content_type = st.selectbox(
                "Content Type",
                ["Blog Post", "YouTube Video", "Social Media Post", "Product Description", "Website Page"],
                help="Where will this content be published?"
            )
        
        with col2:
            tone = st.selectbox(
                "Target Tone",
                ["Catchy", "Clickbait", "Serious", "Casual", "Professional", "Humorous"],
                help="What vibe are you going for?"
            )
        
        description = st.text_area(
            "What's your content about?",
            placeholder="e.g., A 10-minute tutorial on how to bake the perfect sourdough bread...",
            height=120
        )
        
        submitted = st.form_submit_button("Generate SEO Info")

# Results Display
if submitted:
    if not description:
        st.warning("⚠️ Please enter a description to get started.")
    else:
        with st.spinner("🔮 Brewing SEO magic..."):
            result = generate_seo_content(content_type, description, tone)
            
            if "error" in result:
                st.error(result["error"])
            else:
                # Title Section
                st.subheader("📌 Optimized Title")
                st.text_input("Title", value=result['title'], label_visibility="collapsed")
                
                # Description Section
                st.subheader("📝 Meta Description")
                st.text_area("Description", value=result['description'], height=150, label_visibility="collapsed")
                
                # Tags Section
                st.subheader("🏷️ Smart Tags")
                st.text_area("Tags", value=", ".join(result['tags']), height=100, label_visibility="collapsed")
