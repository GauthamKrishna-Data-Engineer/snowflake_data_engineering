import streamlit as st

st.title("Streamlit to SharePoint App")

try:
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
    df = session.sql("SELECT CURRENT_DATE() AS current_date").to_pandas()
    st.write("Current Date from Snowflake:", df['current_date'][0])
except Exception as e:
    st.error(f"Error connecting to Snowflake: {e}")
    conn = st.connection("snowflake")
    df = conn.query("SELECT CURRENT_DATE() AS current_date")


st.dataframe(df)