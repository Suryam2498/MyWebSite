import streamlit as st

st.set_page_config(page_title="", page_icon="👋", layout="centered")

# Sidebar
st.sidebar.title("Navigation")

page = st.sidebar.radio("Go to", ["Home", "Projects", "About Me", "Contact"])

# Home Page
if page == "Home":
    st.title("👋 Hi Welcome to Suryam AI World")
    st.write("Welcome to my personal website built with Streamlit.")
    st.image("D:\AWS_AI\img2.jpg", width=400)

# Projects Page
elif page == "Projects":
    st.title("💼 Projects")
    st.write("Here are some of the things I've worked on:")
    st.markdown("- [Project 1](https://github.com/...) - Description")
    st.markdown("- [Project 2](https://github.com/...) - Description")

# About Me Page
elif page == "About Me":
    st.title("📚 About Me")
    st.write("I bring over two decades of extensive experience in the IT industry, with a strong track record of working across a wide spectrum of technologies and domains. Throughout my career, I have developed deep expertise in areas such as Quality Assurance (QA) Automation, DevOps, and most recently, Generative AI.My professional journey has enabled me to lead and contribute to complex, large-scale projects, leveraging cutting-edge tools and methodologies to drive efficiency, quality, and innovation. I have a proven ability to adapt to emerging technologies, architect robust solutions, and collaborate across multidisciplinary teams to deliver high-impact results.With a strong foundation in both development and operations, I bring a holistic view to software lifecycle management. In recent years, I have been actively exploring and applying Generative AI technologies to real-world business challenges, integrating them into automation frameworks, enhancing productivity, and enabling smarter decision-making.I am passionate about continuous learning and leveraging technology to solve problems at scale, and I thrive in dynamic, forward-thinking environments where innovation is at the forefront.")

# Contact Page
elif page == "Contact":
    st.title("📫 Contact Me")
    with st.form(key='contact_form'):
        name = st.text_input("Suryam Mangalampalli")
        email = st.text_input("mnvsuryam@gmail.com")
        message = st.text_area("Future is Gen AI")
        submit = st.form_submit_button("Send")
        if submit:
            st.success("Thanks! I'll get back to you soon.")
