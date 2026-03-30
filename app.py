import streamlit as st

# Page settings
st.set_page_config(page_title="Sample Computer Center", layout="wide")

# ---------- SIDEBAR ----------
st.sidebar.title("📚 Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])


# ---------- HOME PAGE ----------
if page == "Home":

    st.markdown("""
    <style>
    .hero {
        background: linear-gradient(rgba(0,0,50,0.7), rgba(0,0,50,0.7)),
                    url('https://images.unsplash.com/photo-1519389950473-47ba0277781c');
        background-size: cover;
        background-position: center;
        padding: 120px;
        text-align: center;
        color: white;
        border-radius: 10px;
    }
    .btn {
        background: #ff7a00;
        padding: 10px 20px;
        color: white;
        border: none;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero">
        <h1>Welcome to Sample Computer Center</h1>
        <p>You can develop your skills here</p>
        <br>
        <button class="btn">Join Now</button>
    </div>
    """, unsafe_allow_html=True)

    st.write("## 💻 Our Courses")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🐍 Python Programming\n\nDuration: 3 Months")

    with col2:
        st.info("🌐 Web Development\n\nDuration: 4 Months")

    with col3:
        st.info("🖥️ Basic Computer\n\nDuration: 2 Months")


# ---------- ABOUT PAGE ----------
elif page == "About":

    st.title("About Us")

    st.write("""
    Sample Computer Center is a professional institute 
    providing quality computer education.
    """)

    st.write("### 📌 Services")
    st.write("- Computer Courses")
    st.write("- Programming Training")
    st.write("- Job Guidance")

    st.write("### ⏰ Timing")
    st.write("Mon - Sat: 9AM - 6PM")

    st.write("### 📍 Address")
    st.write("Delhi, India")


# ---------- CONTACT PAGE ----------
elif page == "Contact":

    st.title("Contact Us")

    name = st.text_input("Name")
    phone = st.text_input("Phone")
    message = st.text_area("Message")

    if st.button("Submit"):
        if name and phone and message:
            st.success("Form Submitted Successfully ✅")

            st.write("### Your Info")
            st.write(f"Name: {name}")
            st.write(f"Phone: {phone}")
            st.write(f"Message: {message}")
        else:
            st.error("Please fill all fields ❌")

    st.write("### 📍 Location")

    st.markdown("""
    <iframe src="https://www.google.com/maps?q=Delhi&output=embed"
    width="100%" height="300"></iframe>
    """, unsafe_allow_html=True)
