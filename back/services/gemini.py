from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import base64
import json

# Initialize the model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

def  process_image_with_gemini(file, content_type):
    image_data = base64.b64encode(file).decode("utf-8")
    messages = [
        SystemMessage(
            content=[
                {
                    "type": "text",
                    "text": "You are a Nendoroid analyser. Nendoroids are collectible figures based on popular licenses. Each Nendoroid has a number written on the box for identification purposes."
                },
                {
                    "type": "text",
                    "text": """
                    Return only JSON, not formatted, in this format : [{\"name\": \"[name]\", \"license\": \"[license]\", \"id\":  \"[id]\"}]
                    If an attribute is not found, leave it  as null.
                    If a Nendoroid is not found,  return {"error": "Doll not found"}
                    """
                },
            ]
        ),
        HumanMessage(
            content=[
                {
                    "type": "text", 
                    "text": """
                            This is a photo of a Nendoroid box.
                            Return the nendoroid number, name and licence.
                            If there are multiple boxes, return a single JSON object as an array with one element per box.
                            """},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:{content_type};base64,{image_data}"},
                },
            ],
        )
    ]
    response = model.invoke(messages)

    try:
        # Print the model's response
        return json.loads(response.content)
    except Exception as e:
        print("Parsing json response failed")
        print(e)
        return  {"error": "Failed to parse response"}