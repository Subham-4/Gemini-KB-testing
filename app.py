import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro") 

#sample generation
reply = model.generate_content("How is the day today?")
print(reply.text)