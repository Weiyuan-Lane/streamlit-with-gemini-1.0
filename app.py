import os
import streamlit as st

from views import home
from google_cloud_utils import gemini_pro, cloud_logging

# ENV Vars
PROJECT_ID = os.environ.get('PROJECT_ID')
LOCATION = os.environ.get('REGION')

@st.cache_resource
def load_models_and_cache():
    text_model_pro, multimodal_model_pro = gemini_pro.load_models(PROJECT_ID, LOCATION)
    return text_model_pro, multimodal_model_pro

# RUN!
cloud_logging.init()
text_model_pro, multimodal_model_pro = load_models_and_cache()
home.render_view(text_model_pro, multimodal_model_pro)
