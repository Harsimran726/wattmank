from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, create_react_agent, BaseMultiActionAgent, initialize_agent, AgentType, create_openai_tools_agent, create_openai_functions_agent, create_tool_calling_agent
from langchain.tools import Tool
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import Runnable
import os
import base64
import mimetypes
from google import genai
from google.genai import types

# Load environment variables
load_dotenv()

# Get API key from environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def save_binary_file(file_name: str, data: bytes) -> None:
    """Save binary data to a file.
    
    Args:
        file_name (str): Name of the file to save
        data (bytes): Binary data to write
    """
    with open(file_name, "wb") as f:
        f.write(data)
    print(f"File saved to: {file_name}")

def generate(image_path: str, additional_text: str = None) -> dict:
    """Generate content using Gemini API.
    
    Args:
        image_path (str): Path to the input image
        additional_text (str, optional): Additional text input from user
    
    Returns:
        dict: Analysis results including text and image
    """
    client = genai.Client(api_key=GEMINI_API_KEY)

    # Read and encode the image
    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')

    model = "gemini-2.0-flash-preview-image-generation"
    
    # Prepare the prompt
    prompt = """You are a professional Solar Energy Assistant specialized in analyzing satellite images of building rooftops. Your goal is to assess the feasibility of solar panel installation and provide detailed, structured, and accurate insights."""
    
    if additional_text:
        prompt += f"\nAdditional context: {additional_text}\n"

    prompt += """
When a rooftop image is provided, perform the following tasks:

1. Analyze the rooftop's shape, surface area, breadth, length, obstacles, shadow and usable solar panel area.

2. Identify and ignore any shaded or obstructed regions (e.g., water tanks, HVAC units, chimneys).

3. Calculate:
    - Usable area (in sq. meters)
    - Estimated number of solar panels (assuming each panel is ~1.7 sq. meters)
    - Total system size in kW (assuming each panel is 400W)
    - Daily and monthly energy output (based on 5.5 sunlight hours per day unless otherwise specified)
    - Also which suits the best Monocrystalline, Polycrystalline , Thin-Film

4. Perform a financial estimation:
    - Approximate installation cost (assume ₹40 per watt)
    - Monthly electricity savings (assume ₹6 per kWh)
    - Payback period in years

5. Return all results in a structured JSON format.
6. Also tell about mounting, tils and inverter setupt:- 
    o	Flush mount (for sloped roofs)
    o	Ballasted mount (for flat roofs)
    o	Tilted mounts (to optimize angle)

7. Include a short, user-friendly recommendation in natural language after the JSON.
8. Return the image with marking + labels including usable and unusable area.

If shadows or obstacles are visible, estimate their area visually and reduce from the total available surface.

Always be cautious with low-resolution or unclear images. If the image quality is insufficient for accurate prediction, return a warning message.

Always return the image with marking and solar gird, keep in mind that only show the solar grid where no obstacles and possible to install.

Format your output exactly like this:
{
    "location": "[if available or inferred]",
    "mounting": "[best mounting suitable for rooftop]",
    "solar_type": "[best suitable solar type]",
    "roof_area_m2": [total estimated area],
    "usable_roof_area_m2": [after shadows/obstacles],
    "estimated_panels": [panel count],
    "system_capacity_kw": [capacity in kW],
    "daily_output_kwh": [daily],
    "monthly_output_kwh": [monthly],
    "estimated_cost_inr": [approx cost],
    "monthly_savings_inr": [approx saving],
    "payback_period_years": [years],
    "recommendation": "[human-friendly advice]",
    "total_obstacles": "[total-obstacles and their names]",
    "breadth": "[breadth]",
    "length": "[length]"
}"""

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=prompt),
                types.Part(
                    inline_data=types.Blob(
                        mime_type="image/png",
                        data=image_data
                    )
                )
            ],
        ),
    ]
    
    generate_content_config = types.GenerateContentConfig(
        response_modalities=["IMAGE", "TEXT"],
        response_mime_type="text/plain"
    )

    result = {
        "text_response": "",
        "image_path": None
    }

    file_index = 0
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if not (chunk.candidates and chunk.candidates[0].content and chunk.candidates[0].content.parts):
            continue
            
        if chunk.candidates[0].content.parts[0].inline_data and chunk.candidates[0].content.parts[0].inline_data.data:
            file_name = f"generated_image_{file_index}"
            file_index += 1
            inline_data = chunk.candidates[0].content.parts[0].inline_data
            data_buffer = inline_data.data
            file_extension = mimetypes.guess_extension(inline_data.mime_type)
            image_path = f"{file_name}{file_extension}"
            save_binary_file(image_path, data_buffer)
            result["image_path"] = image_path
        else:
            result["text_response"] += chunk.text

    return result

