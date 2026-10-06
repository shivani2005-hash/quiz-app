import streamlit as st
st.title("Online Quiz Portal")
rollno=st.text_input("Roll Number")
if rollno:
    st.success(f"Welcome {rollno}")
    subject=st.radio("Select Subject",
                     ["Python","English","Maths"],index=None,
                     horizontal=True)
    st.divider()
    if subject=="Python":
        st.subheader("Python Quiz")
        q1=st.radio(
            "1.Which symbol is used for comments",
            ["//","*","$","#"],index=None
             )
        q2=st.radio(
                    "2.Which Function is used to read the data from user?",
                    ["print()","display()","read()","input()"],index=None
                     )
        q3=st.radio(
                    "3.function keyword  in python?",
                    ["fun","def","import","define"],index=None
                     )
        answers=[
            q1=="#",
            q2=="input()",
            q3=="def"

        ]
        if st.button("Submit Quiz"):
                score=sum(answers)
                st.success("Your Result")
                st.write(f"Roll Number:{rollno}")
                st.write(f"Selected Subject:{subject}")
                st.metric("your score",
                          f"{score}/3")
                if score==3:
                    st.balloons()
                    st.success("Excellent")
                else:
                    st.warning("Keep Practicing!")
else:
     st.info("Please Enter roll no")