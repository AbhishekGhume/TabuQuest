# import streamlit as st
# import pandas as pd
# from utils.data_loader import load_data, clean_data
# from utils.query_parser import QueryParser
# from utils.query_executor import QueryExecutor
# from utils.visualizer import Visualizer
# import time
# import os
# from dotenv import load_dotenv

# load_dotenv()  # Load environment variables from .env

# api_key = os.getenv("GEMINI_API_KEY")
# if not api_key:
#     raise ValueError("❌ GEMINI_API_KEY is missing! Check your .env file.")

# # Configure Gemini API
# import google.generativeai as genai
# genai.configure(api_key=api_key)

# # Configure Streamlit
# st.set_page_config(page_title="TabuQuest", layout="wide")
# st.title("📊 TabuQuest: Natural Language Data Analysis")

# # Initialize session state
# if "df" not in st.session_state:
#     st.session_state.df = None

# # File Upload Section
# with st.expander("📁 Upload Data", expanded=True):
#     uploaded_file = st.file_uploader(
#         "Upload CSV/Excel file", 
#         type=["csv", "xlsx", "xls"],
#         help="Supported formats: CSV, Excel"
#     )
    
#     if uploaded_file:
#         try:
#             df = load_data(uploaded_file)
#             df = clean_data(df)
#             st.session_state.df = df
#             st.success("✅ Data loaded successfully!")
#         except Exception as e:
#             st.error(f"❌ Error loading data: {str(e)}")

# # Preview Data Section (Moved outside the Upload Data expander)
# if st.session_state.df is not None:
#     with st.expander("🔍 Preview Data", expanded=False):
#         st.dataframe(st.session_state.df.head(), use_container_width=True)

# # Query Section
# if st.session_state.df is not None:
#     with st.form("query_form"):
#         query = st.text_input(
#             "Ask a question about your data:", 
#             placeholder="E.g., 'Show average sales by region'"
#         )
        
#         submitted = st.form_submit_button("Analyze")
        
#         if submitted and query:
#             try:
#                 # Parse and execute query
#                 start_time = time.time()
                
#                 parser = QueryParser()
#                 executor = QueryExecutor(st.session_state.df)
                
#                 code = parser.parse_query(query)
#                 result = executor.execute(code)
                
#                 processing_time = time.time() - start_time
                
#                 # Display results
#                 st.subheader("Results")
#                 col1, col2 = st.columns([1, 2])
                
#                 with col1:
#                     st.markdown("### Data")
#                     st.dataframe(result, use_container_width=True)
                    
#                 with col2:
#                     st.markdown("### Visualization")
#                     try:
#                         fig = Visualizer.auto_visualize(result)
#                         if fig:
#                             st.plotly_chart(fig, use_container_width=True)
#                         else:
#                             st.info("ℹ️ No visualization available for this result")
#                     except Exception as e:
#                         st.warning(f"⚠️ Visualization error: {str(e)}")
                        
#                 st.caption(f"⏱ Processed in {processing_time:.2f}s | Generated code: `{code}`")
                
#             except Exception as e:
#                 st.error(f"❌ Analysis failed: {str(e)}")
#                 st.caption(f"📝 Generated code before failure: `{code}`")  # Always show code

# # Add footer
# st.markdown("---")
# st.markdown("Built with ♥ using Gemini API and Streamlit")
































# import streamlit as st
# import pandas as pd
# from utils.data_loader import load_data, clean_data
# from utils.query_parser import QueryParser
# from utils.query_executor import QueryExecutor
# from utils.visualizer import Visualizer
# import time
# import os
# from dotenv import load_dotenv

# load_dotenv()  # Load environment variables from .env

# api_key = os.getenv("GEMINI_API_KEY")
# if not api_key:
#     raise ValueError("❌ GEMINI_API_KEY is missing! Check your .env file.")

# # Configure Gemini API
# import google.generativeai as genai
# genai.configure(api_key=api_key)

# # Configure Streamlit
# st.set_page_config(page_title="TabuQuest", layout="wide")
# st.title("📊 TabuQuest: Natural Language Data Analysis")

# # Initialize session state
# if "df" not in st.session_state:
#     st.session_state.df = None

# # File Upload Section
# with st.expander("📁 Upload Data", expanded=True):
#     uploaded_file = st.file_uploader(
#         "Upload CSV/Excel file", 
#         type=["csv", "xlsx", "xls"],
#         help="Supported formats: CSV, Excel"
#     )
    
#     if uploaded_file:
#         try:
#             df = load_data(uploaded_file)
#             df = clean_data(df)
#             st.session_state.df = df
#             st.success("✅ Data loaded successfully!")
#         except Exception as e:
#             st.error(f"❌ Error loading data: {str(e)}")

# # Preview Data Section (Moved outside the Upload Data expander)
# if st.session_state.df is not None:
#     with st.expander("🔍 Preview Data", expanded=False):
#         st.dataframe(st.session_state.df.head(), use_container_width=True)

# # # Query Section
# if st.session_state.df is not None:
#     with st.form("query_form"):
#         query = st.text_input(
#             "Ask a question about your data:", 
#             placeholder="E.g., 'Show students with CGPA above 8'"
#         )
        
#         submitted = st.form_submit_button("Analyze")
        
#         if submitted and query:
#             try:
#                 start_time = time.time()
#                 parser = QueryParser()
#                 executor = QueryExecutor(st.session_state.df)
                
#                 # Get columns for context
#                 columns = st.session_state.df.columns.tolist()
#                 code = parser.parse_query(query, columns)
#                 result = executor.execute(code)
                
#                 processing_time = time.time() - start_time
                
#                 # Store result and original dataframe in session state
#                 st.session_state.result = result
#                 st.session_state.original_df = st.session_state.df  # Store original dataset
                
#                 # Display results
#                 st.subheader("Results")
#                 st.dataframe(result, use_container_width=True)
#                 st.caption(f"⏱ Processed in {processing_time:.2f}s | Code: `{code}`")
                
#             except Exception as e:
#                 st.error(f"Analysis failed: {str(e)}")
#                 if 'code' in locals():
#                     st.caption(f"Generated code: `{code}`")

#     # Visualization Configuration Section
#     if 'result' in st.session_state and 'original_df' in st.session_state:
#         st.markdown("---")
#         st.subheader("📊 Custom Visualization")
        
#         # Use original dataset columns for visualization
#         columns = st.session_state.original_df.columns.tolist()
        
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             x_axis = st.selectbox("Select X-axis", columns, index=0)
#         with col2:
#             y_axis = st.selectbox("Select Y-axis (optional)", [None] + columns, index=0)
#         with col3:
#             chart_type = st.selectbox("Select Chart Type", ["scatter", "line", "bar", "histogram", "box"])
        
#         if st.button("Visualize"):
#             try:
#                 # Use the original dataset for visualization
#                 fig = Visualizer.custom_visualize(
#                     st.session_state.original_df,  # Use original dataset
#                     x_axis=x_axis,
#                     y_axis=y_axis,
#                     chart_type=chart_type
#                 )
#                 if fig:
#                     st.plotly_chart(fig, use_container_width=True)
#                 else:
#                     st.info("No visualization available for the selected configuration")
#             except Exception as e:
#                 st.error(f"Custom visualization failed: {str(e)}")

# # Add footer
# st.markdown("---")
# st.markdown("Built with ♥ using Gemini API and Streamlit")












import streamlit as st
import pandas as pd
from utils.data_loader import load_data, clean_data, load_data_from_mysql
from utils.query_parser import QueryParser
from utils.query_executor import QueryExecutor
from utils.visualizer import Visualizer
import time
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("❌ GEMINI_API_KEY is missing! Check your .env file.")

# Configure Gemini API
import google.generativeai as genai
genai.configure(api_key=api_key)

# Configure Streamlit
st.set_page_config(page_title="TabuQuest", layout="wide")
st.title("📊 TabuQuest: Natural Language Data Analysis")

# Initialize session state
if "df" not in st.session_state:
    st.session_state.df = None

# Data Source Selection
data_source = st.radio("Select Data Source", ["Upload File", "Connect to MySQL Database"])

if data_source == "Upload File":
    # File Upload Section
    with st.expander("📁 Upload Data", expanded=True):
        uploaded_file = st.file_uploader(
            "Upload CSV/Excel file", 
            type=["csv", "xlsx", "xls"],
            help="Supported formats: CSV, Excel"
        )
        
        if uploaded_file:
            try:
                df = load_data(uploaded_file)
                df = clean_data(df)
                st.session_state.df = df
                st.success("✅ Data loaded successfully!")
            except Exception as e:
                st.error(f"❌ Error loading data: {str(e)}")

elif data_source == "Connect to MySQL Database":
    # MySQL Connection Section
    with st.expander("🔗 Connect to MySQL Database", expanded=True):
        host = st.text_input("MySQL Host", "localhost")
        user = st.text_input("MySQL Username", "root")
        password = st.text_input("MySQL Password", type="password")
        database = st.text_input("Database Name")
        table = st.text_input("Table Name")
        
        if st.button("Connect to MySQL"):
            try:
                df = load_data_from_mysql(host, user, password, database, table)
                df = clean_data(df)
                st.session_state.df = df
                st.success("✅ Data loaded successfully from MySQL!")
            except Exception as e:
                st.error(f"❌ Error loading data from MySQL: {str(e)}")

# Preview Data Section
if st.session_state.df is not None:
    with st.expander("🔍 Preview Data", expanded=False):
        st.dataframe(st.session_state.df.head(), use_container_width=True)

# Query Section
if st.session_state.df is not None:
    st.markdown("---")
    st.subheader("🔍 Query Your Data")

    # Text Input for Query
    with st.form("query_form"):
        query = st.text_input(
            "Ask a question about your data:", 
            placeholder="E.g., 'Show students with CGPA above 8'"
        )
        
        submitted = st.form_submit_button("Analyze")
        
        if submitted and query:
            try:
                start_time = time.time()
                parser = QueryParser()
                executor = QueryExecutor(st.session_state.df)
                
                # Get columns for context
                columns = st.session_state.df.columns.tolist()
                code = parser.parse_query(query, columns)
                result = executor.execute(code)
                
                processing_time = time.time() - start_time
                
                # Store result in session state
                st.session_state.result = result
                
                # Display results
                st.subheader("Results")
                st.dataframe(result, use_container_width=True)
                st.caption(f"⏱ Processed in {processing_time:.2f}s | Code: `{code}`")
                
            except Exception as e:
                st.error(f"Analysis failed: {str(e)}")
                if 'code' in locals():
                    st.caption(f"Generated code: `{code}`")

    # Visualization Configuration Section
    if 'result' in st.session_state:
        st.markdown("---")
        st.subheader("📊 Custom Visualization")
        
        # Use dataset columns for visualization
        columns = st.session_state.df.columns.tolist()
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            x_axis = st.selectbox("Select X-axis", columns, index=0)
        with col2:
            y_axis = st.selectbox("Select Y-axis (optional)", [None] + columns, index=0)
        with col3:
            chart_type = st.selectbox("Select Chart Type", ["scatter", "line", "bar", "histogram", "box"])
        
        if st.button("Visualize"):
            try:
                fig = Visualizer.custom_visualize(
                    st.session_state.df,  
                    x_axis=x_axis,
                    y_axis=y_axis,
                    chart_type=chart_type
                )
                if fig:
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.info("No visualization available for the selected configuration")
            except Exception as e:
                st.error(f"Custom visualization failed: {str(e)}")

# Add footer
st.markdown("---")
st.markdown("Built with ♥ using Gemini API and Streamlit")