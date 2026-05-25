# import streamlit as st

# from nltk.tokenize import sent_tokenize

# from src.summarizer import generate_summary
# from src.keyword_extractor import extract_keywords


# # ---------------------------------------------------
# # PAGE CONFIG
# # ---------------------------------------------------

# st.set_page_config(
#     page_title="AI Text Summarizer & Keyword Extractor",
#     page_icon="🧠",
#     layout="wide"
# )


# # ---------------------------------------------------
# # CUSTOM CSS
# # ---------------------------------------------------

# st.markdown("""
# <style>

# .main {
#     background-color: #0E1117;
# }

# h1 {
#     text-align: center;
#     color: #FFFFFF;
#     font-size: 50px !important;
# }

# .subtitle {
#     text-align: center;
#     color: #BBBBBB;
#     font-size: 18px;
#     margin-bottom: 30px;
# }

# .summary-box {
#     background-color: #1E293B;
#     padding: 25px;
#     border-radius: 15px;
#     color: white;
#     font-size: 18px;
#     line-height: 1.8;
#     border-left: 6px solid #38BDF8;
# }

# .keyword-card {
#     background: linear-gradient(135deg, #2563EB, #7C3AED);
#     color: white;
#     padding: 12px 20px;
#     border-radius: 12px;
#     text-align: center;
#     font-size: 17px;
#     font-weight: 600;
#     margin-bottom: 15px;
#     box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
# }

# .stat-card {
#     background-color: #111827;
#     padding: 20px;
#     border-radius: 15px;
#     text-align: center;
#     color: white;
#     box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
# }

# .footer {
#     text-align: center;
#     color: gray;
#     margin-top: 50px;
#     font-size: 14px;
# }

# </style>
# """, unsafe_allow_html=True)


# # ---------------------------------------------------
# # HEADER
# # ---------------------------------------------------

# st.markdown("<h1>🧠 AI Text Summarizer & Keyword Extractor</h1>", unsafe_allow_html=True)

# st.markdown(
#     "<p class='subtitle'>Generate intelligent summaries and extract important keywords using NLP techniques.</p>",
#     unsafe_allow_html=True
# )


# # ---------------------------------------------------
# # TEXT INPUT
# # ---------------------------------------------------

# text_input = st.text_area(
#     "📄 Enter your text here:",
#     height=300,
#     placeholder="Paste your article, notes, or paragraph here..."
# )


# # ---------------------------------------------------
# # SUMMARY SLIDER
# # ---------------------------------------------------

# summary_ratio = st.slider(
#     "📌 Select summary percentage:",
#     10,
#     50,
#     30
# )


# # ---------------------------------------------------
# # GENERATE BUTTON
# # ---------------------------------------------------

# if st.button("✨ Generate Results"):

#     if text_input.strip() == "":
#         st.warning("⚠ Please enter some text.")

#     else:

#         # Total sentences
#         total_sentences = len(sent_tokenize(text_input))

#         # Calculate summary size
#         num_sentences = max(
#             1,
#             int((summary_ratio / 100) * total_sentences)
#         )

#         # Generate summary
#         summary = generate_summary(
#             text_input,
#             num_sentences
#         )

#         # Extract keywords
#         keywords = extract_keywords(text_input)


#         # ---------------------------------------------------
#         # SUMMARY SECTION
#         # ---------------------------------------------------

#         st.subheader("📌 Summary")

#         st.markdown(
#             f"""
#             <div class="summary-box">
#             {summary}
#             </div>
#             """,
#             unsafe_allow_html=True
#         )


#         # ---------------------------------------------------
#         # KEYWORDS SECTION
#         # ---------------------------------------------------

#         st.subheader("🔑 Keywords")

#         cols = st.columns(3)

#         for i, keyword in enumerate(keywords):

#             with cols[i % 3]:

#                 st.markdown(
#                     f"""
#                     <div class="keyword-card">
#                         {keyword}
#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )


#         # ---------------------------------------------------
#         # STATISTICS SECTION
#         # ---------------------------------------------------

#         original_words = len(text_input.split())
#         summary_words = len(summary.split())

#         compression = round(
#             ((original_words - summary_words) / original_words) * 100,
#             2
#         )

#         st.subheader("📊 Statistics")

#         col1, col2, col3 = st.columns(3)

#         with col1:
#             st.markdown(
#                 f"""
#                 <div class="stat-card">
#                     <h3>{original_words}</h3>
#                     <p>Original Words</p>
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )

#         with col2:
#             st.markdown(
#                 f"""
#                 <div class="stat-card">
#                     <h3>{summary_words}</h3>
#                     <p>Summary Words</p>
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )

#         with col3:
#             st.markdown(
#                 f"""
#                 <div class="stat-card">
#                     <h3>{compression}%</h3>
#                     <p>Compression Rate</p>
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )


# # ---------------------------------------------------
# # FOOTER
# # ---------------------------------------------------

# st.markdown(
#     """
#     <div class="footer">
#         Built with ❤️ using NLP, Streamlit, and Python
#     </div>
#     """,
#     unsafe_allow_html=True
# )
import streamlit as st
from nltk.tokenize import sent_tokenize

from wordcloud import WordCloud
import matplotlib.pyplot as plt

from src.summarizer import generate_summary
from src.keyword_extractor import extract_keywords


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Text Summarizer & Keyword Extractor",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1 {
    text-align: center;
    color: #FFFFFF;
    font-size: 48px !important;
}

.subtitle {
    text-align: center;
    color: #BBBBBB;
    font-size: 18px;
    margin-bottom: 30px;
}

.summary-box {
    background-color: #1E293B;
    padding: 25px;
    border-radius: 15px;
    color: white;
    font-size: 18px;
    line-height: 1.8;
    border-left: 6px solid #38BDF8;
}

.keyword-card {
    background: linear-gradient(135deg, #2563EB, #7C3AED);
    color: white;
    padding: 14px;
    border-radius: 12px;
    text-align: center;
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
}

.stat-card {
    background-color: #111827;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    color: white;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 50px;
    font-size: 14px;
}

.sidebar .sidebar-content {
    background-color: #111827;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("🧠 NLP Controls")

st.sidebar.markdown("---")

st.sidebar.subheader("📌 Summary Settings")

summary_ratio = st.sidebar.slider(
    "Summary Percentage",
    10,
    50,
    30
)

num_keywords = st.sidebar.slider(
    "Number of Keywords",
    5,
    20,
    10
)

show_wordcloud = st.sidebar.checkbox(
    "☁ Show Word Cloud",
    value=True
)

st.sidebar.markdown("---")

st.sidebar.subheader("📂 Upload File")

uploaded_file = st.sidebar.file_uploader(
    "Upload TXT File",
    type=["txt"]
)

st.sidebar.markdown("---")

st.sidebar.subheader("🧠 NLP Techniques Used")

st.sidebar.markdown("""
✔ Tokenization  
✔ Stopword Removal  
✔ Lemmatization  
✔ Frequency Analysis  
✔ TF-IDF  
✔ Extractive Summarization  
""")

st.sidebar.markdown("---")


# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown(
    "<h1>🧠 AI Text Summarizer & Keyword Extractor</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>Generate intelligent summaries and extract important keywords using NLP techniques.</p>",
    unsafe_allow_html=True
)


# ---------------------------------------------------
# FILE HANDLING
# ---------------------------------------------------

text_input = ""

if uploaded_file is not None:

    text_input = uploaded_file.read().decode("utf-8")


# ---------------------------------------------------
# TEXT AREA
# ---------------------------------------------------

text_input = st.text_area(
    "📄 Enter your text here:",
    value=text_input,
    height=300,
    placeholder="Paste your article, notes, or paragraph here..."
)


# ---------------------------------------------------
# GENERATE BUTTON
# ---------------------------------------------------

if st.button("✨ Generate Results"):

    if text_input.strip() == "":

        st.warning("⚠ Please enter some text.")

    else:

        with st.spinner("Generating summary and extracting keywords..."):

            # Sentence count
            total_sentences = len(sent_tokenize(text_input))

            # Dynamic sentence selection
            num_sentences = max(
                1,
                int((summary_ratio / 100) * total_sentences)
            )

            # Generate summary
            summary = generate_summary(
                text_input,
                num_sentences
            )

            # Extract keywords
            keywords = extract_keywords(
                text_input,
                num_keywords
            )

        # ---------------------------------------------------
        # SUMMARY SECTION
        # ---------------------------------------------------

        st.subheader("📌 Summary")

        st.markdown(
            f"""
            <div class="summary-box">
            {summary}
            </div>
            """,
            unsafe_allow_html=True
        )

        # Download button
        st.download_button(
            label="📥 Download Summary",
            data=summary,
            file_name="summary.txt",
            mime="text/plain"
        )


        # ---------------------------------------------------
        # KEYWORDS SECTION
        # ---------------------------------------------------

        st.subheader("🔑 Keywords")

        cols = st.columns(3)

        for i, keyword in enumerate(keywords):

            with cols[i % 3]:

                st.markdown(
                    f"""
                    <div class="keyword-card">
                        {keyword}
                    </div>
                    """,
                    unsafe_allow_html=True
                )


        # ---------------------------------------------------
        # WORD CLOUD
        # ---------------------------------------------------

        if show_wordcloud:

            st.subheader("☁ Word Cloud")

            wordcloud = WordCloud(
                width=800,
                height=400,
                background_color='black'
            ).generate(text_input)

            fig, ax = plt.subplots(figsize=(10, 5))

            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis("off")

            st.pyplot(fig)


        # ---------------------------------------------------
        # STATISTICS
        # ---------------------------------------------------

        original_words = len(text_input.split())
        summary_words = len(summary.split())

        compression = round(
            ((original_words - summary_words) / original_words) * 100,
            2
        )

        st.subheader("📊 Statistics")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.markdown(
                f"""
                <div class="stat-card">
                    <h3>{original_words}</h3>
                    <p>Original Words</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:

            st.markdown(
                f"""
                <div class="stat-card">
                    <h3>{summary_words}</h3>
                    <p>Summary Words</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:

            st.markdown(
                f"""
                <div class="stat-card">
                    <h3>{compression}%</h3>
                    <p>Compression Rate</p>
                </div>
                """,
                unsafe_allow_html=True
            )


# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown(
    """
    <div class="footer">
        Built with ❤️ using NLP, Streamlit, and Python
    </div>
    """,
    unsafe_allow_html=True
)