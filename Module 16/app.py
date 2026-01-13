import streamlit as st

def main():
    st.title("Hello, World")

 if st.button("Click Me"):
   st.write("Button Checked")
st.checkbox("Check me")
if st.checkbox("Check me to show some text"):
      st.write("Your seeing this text because u checked the checkbox")

user_input = st.text_input("Enter text","Sample Text")
st.write("You have entered:", user_input)
age = st.number_input("Enter you age", min_value=0, max_value=100 )
st.write(f"Your age is: {age}")

message = st.text_area("Enter a message")
st.write(f"Your Message: {message}")

choice = st.radio("Pick one",["Choice 1", "Choice 2", "Choice 3"])
st.write (f"Your choose: {choice}")
if st.button("Sucess"):
    st.sucess("Operation was sucessful")

if __name__ == "__main__":
  main()