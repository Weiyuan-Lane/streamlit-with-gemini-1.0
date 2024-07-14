import vertexai
from vertexai.preview.generative_models import (
    Content,
    GenerationConfig,
    GenerativeModel,
    GenerationResponse,
    Image,
    HarmCategory,
    HarmBlockThreshold,
    Part
)

def load_models(gcp_project_id, gcp_location):
  vertexai.init(project=gcp_project_id, location=gcp_location)
  text_model_pro = GenerativeModel("gemini-pro")
  multimodal_model_pro = GenerativeModel("gemini-1.5-flash-001")
  return text_model_pro, multimodal_model_pro

def get_gemini_pro_text_response( model: GenerativeModel,
                                  prompt: str,
                                  generation_config: GenerationConfig,
                                  stream=True):

    safety_settings={
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    }

    responses = model.generate_content(prompt,
                                   generation_config = generation_config,
                                   safety_settings = safety_settings,
                                   stream=True)

    final_response = []
    for response in responses:
        try:
            final_response.append(response.text)
        except IndexError:
            final_response.append("")
            continue
    return " ".join(final_response)


def get_gemini_pro_vision_response(model: GenerativeModel, prompt_list, generation_config={}, stream=True):

    generation_config = {
        'temperature': 0.1,
        'max_output_tokens': 2048
    }

    responses = model.generate_content(prompt_list, generation_config = generation_config, stream=True)

    final_response = []
    for response in responses:
        try:
            final_response.append(response.text)
        except IndexError:
            final_response.append("")
            continue
    return(" ".join(final_response))
