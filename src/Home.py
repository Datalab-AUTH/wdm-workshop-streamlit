import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")


st.title("Home page")
st.markdown("""
    #### This is the Home page for the streamlit example in the WDM course
    """)


URL = 'https://raw.githubusercontent.com/sermpezis/ai4netmon/main/data/aggregate_data/asn_aggregate_data.csv' # this is a 24MB csv file


# @st.cache_data(show_spinner="Fetching data ...", ttl=300)
# def get_df():
#     return pd.read_csv(URL, header=0, index_col=0)
# df = get_df()

df = pd.read_csv(URL, header=0, index_col=0)




# display_columns = st.multiselect(label='Select columns to displary', 
#     options=df.columns, 
#     default=[c for c in df.columns if c.startswith('AS_rank')], 
#     # format_func=lambda x:'Pavlos'+x.upper(), 
#     key=None, 
#     help="select columns to display on the following table", 
#     disabled=False, 
#     label_visibility="visible"
#     )

# nb_rows = st.slider(label='select nb of rows to display', min_value=1, max_value=df.shape[0], value=df.shape[0], 
#     step=100
#     )


st.dataframe(df)
# st.dataframe(df[display_columns])
# st.dataframe(df.iloc[0:nb_rows][display_columns])



# st.line_chart(data=df, 
#     x = 'AS_rank_rank',
#     y='AS_rank_peer', 
#     )
