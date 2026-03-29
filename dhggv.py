import streamlit as st

st.set_page_config(page_title="Computer Center", layout="wide")

---------- SIDEBAR ----------

st.sidebar.title("📚 Navigation") page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

---------- HOME PAGE ----------

if page == "Home": st.markdown(""" <style> .hero { background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://images.unsplash.com/photo-1581092334651-ddf26d9a09d0'); background-size: cover; padding: 120px; text-align: center; color: white; border-radius: 10px; } </style> """, unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>Welcome to Sample Computer Center</h1>
    <p>You can develop your skills here</p>
    <br>
    <button style="padding:10px 20px; background:#ff7a00; color:white; border:none;">Join Now</button>
</div>
""", unsafe_allow_html=True)

st.write("## Our Courses")
col1, col2, col3 = st.columns(3)

with col1:
    st.info("Python Programming")
with col2:
    st.info("Web Development")
with col3:
    st.info("Basic Computer")

---------- ABOUT PAGE ----------

elif page == "About": st.title("About Us") st.write("We are a professional computer training center.")

st.write("### Services")
st.write("- Computer Courses")
st.write("- Programming Training")
st.write("- Job Guidance")

st.write("### Timing")
st.write("Mon - Sat: 9AM - 6PM")

st.write("### Address")
st.write("Delhi, India")

---------- CONTACT PAGE ----------

elif page == "Contact": st.title("Contact Us")

name = st.text_input("Name")
phone = st.text_input("Phone")
message = st.text_area("Message")

if st.button("Submit"):
    if name and phone and message:
        st.success("Form Submitted Successfully ✅")
        st.write(f"Name: {name}")
        st.write(f"Phone: {phone}")
        st.write(f"Message: {message}")
    else:
        st.error("Fill all fields ❌")

st.write("### Location")
st.markdown("""
<iframe src="https://www.google.com/maps?q=Delhi&output=embed"
width="100%" height="300"></iframe>
""", unsafe_allow_html=True)
