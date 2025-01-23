import streamlit as st
import ard_data
import Linktoexcel

st.title("Please Fill Your Details")
name = st.text_input(label="Name")
reg = st.text_input(label="Registration Number ")
phno = st.text_input(label="Phone number")

if st.button("SCAN ID CARD"):
    st.text("TAP CARD ON SENSOR AFTER FILLING DETAILS")
    uid = str(ard_data.scanning_card())
    uid_list = Linktoexcel.readcardno()
    if uid not in uid_list:
        result = Linktoexcel.writedata(name, phno, reg, uid)
        if result == "Successfully Registered.":
            st.markdown(f""" <span style='color:green'>Successfully Registered</span>""",
                        unsafe_allow_html=True)
        else:
            st.markdown(f""" <span style='color:red'>Failed to Register</span>""",
                        unsafe_allow_html=True)
    else:
        st.markdown(f""" <span style='color:red'>You are already Registered</span>""",
                    unsafe_allow_html=True)
