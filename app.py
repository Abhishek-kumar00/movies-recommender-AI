import streamlit as st
from movies_pal import movies_team  # import your existing agent

st.set_page_config(page_title="🎬 Movie Pal")
st.title("🎬 Movie Pal")

user_input = st.text_area("Ask something about movies:")

if st.button("Ask"):
    with st.spinner("Thinking..."):
        response = movies_team.run(user_input)
        if hasattr(response, "message"):
            st.write(response.message.content)
        elif hasattr(response, "content"):
            st.write(response.content)
        else:
            st.write(response)

