import streamlit as st


def show_home() -> None:
    """
    Displays the home page with a title, a general description,
    and buttons to access other tabs along with short descriptions.
    """
    st.title("Home")
    st.write("Welcome to the application. This is a general description of the app.")

    if st.button("Go to Extraction"):
        st.session_state.selected_tab = "Extraction"
    st.write("Short description: Extraction tab for data gathering.")

    if st.button("Go to Analysis"):
        st.session_state.selected_tab = "Analysis"
    st.write("Short description: Analysis tab for deeper insights.")

    if st.button("Go to Visualization"):
        st.session_state.selected_tab = "Visualization"
    st.write("Short description: Visualization tab for graphical representations.")

    if st.button("Go to Comparison"):
        st.session_state.selected_tab = "Comparison"
    st.write("Short description: Comparison tab for comparing datasets or results.")

    if st.button("Go to Tables"):
        st.session_state.selected_tab = "Tables"
    st.write("Short description: Tables tab for data tabulation.")


def show_extraction() -> None:
    """
    Displays the Extraction tab content with a title,
    description, and a Back button.
    """
    st.title("Extraction")
    st.write("This is the Extraction tab. Here you can extract data.")

    if st.button("Back"):
        st.session_state.selected_tab = "Home"


def show_analysis() -> None:
    """
    Displays the Analysis tab content with a title,
    description, and a Back button.
    """
    st.title("Analysis")
    st.write("This is the Analysis tab. Here you can analyze your data.")

    if st.button("Back"):
        st.session_state.selected_tab = "Home"


def show_visualization() -> None:
    """
    Displays the Visualization tab content with a title,
    description, and a Back button.
    """
    st.title("Visualization")
    st.write("This is the Visualization tab. Here you can visualize your data.")

    if st.button("Back"):
        st.session_state.selected_tab = "Home"


def show_comparison() -> None:
    """
    Displays the Comparison tab content with a title,
    description, and a Back button.
    """
    st.title("Comparison")
    st.write("This is the Comparison tab. Here you can compare different data sets.")

    if st.button("Back"):
        st.session_state.selected_tab = "Home"


def show_tables() -> None:
    """
    Displays the Tables tab content with a title,
    description, and a Back button.
    """
    st.title("Tables")
    st.write("This is the Tables tab. Here you can display data in tabular form.")

    if st.button("Back"):
        st.session_state.selected_tab = "Home"


def main() -> None:
    """
    Main function to run the Streamlit application,
    controlling navigation and displaying the relevant tabs.
    """
    # Set default page configuration and collapse the sidebar by default
    st.set_page_config(initial_sidebar_state="collapsed")

    # Initialize 'selected_tab' if not present
    if "selected_tab" not in st.session_state:
        st.session_state.selected_tab = "Home"

    # Build a simple sidebar with one button per tab.
    st.sidebar.title("Menu")

    if st.sidebar.button("Home", key="home_button"):
        st.session_state.selected_tab = "Home"
    if st.sidebar.button("Extraction", key="extraction_button"):
        st.session_state.selected_tab = "Extraction"
    if st.sidebar.button("Analysis", key="analysis_button"):
        st.session_state.selected_tab = "Analysis"
    if st.sidebar.button("Visualization", key="visualization_button"):
        st.session_state.selected_tab = "Visualization"
    if st.sidebar.button("Comparison", key="comparison_button"):
        st.session_state.selected_tab = "Comparison"
    if st.sidebar.button("Tables", key="tables_button"):
        st.session_state.selected_tab = "Tables"

    # Display content based on the selected tab
    if st.session_state.selected_tab == "Home":
        show_home()
    elif st.session_state.selected_tab == "Extraction":
        show_extraction()
    elif st.session_state.selected_tab == "Analysis":
        show_analysis()
    elif st.session_state.selected_tab == "Visualization":
        show_visualization()
    elif st.session_state.selected_tab == "Comparison":
        show_comparison()
    elif st.session_state.selected_tab == "Tables":
        show_tables()


if __name__ == "__main__":
    main()
