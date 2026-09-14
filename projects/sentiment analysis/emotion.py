import streamlit as st
from textblob import TextBlob

st.set_page_config(
    page_title="AI Sentiment Analyzer",
    page_icon="😊",
    layout="centered"
)

# Title
st.title("😊 AI Sentiment Analyzer")
st.write("Analyze the sentiment of any text using Natural Language Processing.")

st.divider()

# Input
text = st.text_area(
    "📝 Enter your text",
    placeholder="Example: I really love this product!",
    height=150
)

# Analyze button
if st.button("🔍 Analyze Sentiment", use_container_width=True):

    if text.strip() == "":
        st.warning("⚠️ Please enter some text first.")

    else:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

        # Sentiment detection
        if polarity > 0:
            sentiment = "Positive 😊"
            message = "This text has a positive sentiment."
            st.success(sentiment)

        elif polarity < 0:
            sentiment = "Negative 😡"
            message = "This text has a negative sentiment."
            st.error(sentiment)

        else:
            sentiment = "Neutral 😐"
            message = "This text has a neutral sentiment."
            st.info(sentiment)

        st.subheader("📊 Analysis Result")

        st.write("**Sentiment:**", sentiment)
        st.write("**Polarity Score:**", round(polarity, 2))

        st.write(message)

        # Sentiment meter
        st.progress((polarity + 1) / 2)

st.divider()

st.caption("Built with Python • TextBlob • Streamlit")