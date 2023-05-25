import streamlit as st

def main():
    st.title("Greeting App")
   
    # Get user input
    name = st.text_input("Enter your name:")
   
    # Display greeting message
    if st.button("Greet"):
        if name:
            st.success(f"Hello, {name}!")
        else:
            st.warning("Please enter a name.")

if __name__ == '__main__':
    main()
