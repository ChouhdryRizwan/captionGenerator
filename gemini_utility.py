import os
import json
from PIL import Image

import google.generativeai as genai

# working directory path
working_dir = os.path.dirname(os.path.abspath(__file__))

# path of config_data file
config_file_path = f"{working_dir}/config.json"

config_data = json.load(open("config.json"))

# loading the GEMINI_API_KEY
GEMINI_API_KEY = config_data["GEMINI_API_KEY"]

# configuring google.generativeai with API key
genai.configure(api_key=GEMINI_API_KEY)

# get response from gemini-1.5-flash model - image/text to text
def gemini_pro_vision_response(prompt, image):
    gemini_pro_vision_model = genai.GenerativeModel("gemini-1.5-flash")
    response = gemini_pro_vision_model.generate_content([prompt, image])
    result = response.text
    return result


