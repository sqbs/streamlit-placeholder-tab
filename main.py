import time
import streamlit as st


def main():
    placeholder = "Placeholder Tab"
    try:
        title = st.experimental_get_query_params().get("title", "")[0]
    except IndexError:
        title = placeholder
    st.set_page_config(page_title=title, page_icon=":file_folder:")
    st.title("{}{}".format(placeholder, ": {}".format(title if title else '') if title != placeholder else ''))
    tab_name = st.text_input("Enter a tab name", value=title if title != placeholder else '')
    if st.button("Submit"):
        st.experimental_set_query_params(title=tab_name)
        time.sleep(0.1)
        st.experimental_rerun()


if __name__ == "__main__":
    main()
