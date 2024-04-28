import streamlit as st
from views.tabs.story_tab import render_story_tab
from views.tabs.marketing_campaign_tab import render_mktg_campaign_tab
from views.tabs.image_playground_tab import render_image_playground_tab
from views.tabs.video_playground_tab import render_video_playground_tab

def render_view(text_model_pro, multimodal_model_pro):
    st.header("Vertex AI Gemini API", divider="rainbow")
    story_tab, mkt_tab, image_tab, video_tab = st.tabs([
      "Story",
      "Marketing Campaign",
      "Image Playground",
      "Video Playground"
    ])

    with story_tab:
        render_story_tab(text_model_pro)
    with mkt_tab:
        render_mktg_campaign_tab(text_model_pro)
    with image_tab:
        render_image_playground_tab(multimodal_model_pro)
    with video_tab:
        render_video_playground_tab(multimodal_model_pro)
