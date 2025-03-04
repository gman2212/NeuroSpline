import json
import requests
import re

def read_prompt_file(prompt_file):
    """Reads the prompt file and returns the content."""
    with open(prompt_file, 'r') as file:
        return file.read()

def read_input_json(input_file):
    """Reads the input JSON file and returns the parsed data."""
    with open(input_file, 'r') as file:
        return json.load(file)

def clean_response(response_text):
    """Extracts JSON from response text and removes extra formatting."""
    match = re.search(r"{.*}", response_text, re.DOTALL)  # Capture JSON inside curly brackets
    if match:
        json_str = match.group(0)
    else:
        json_str = response_text  # Assume raw JSON if no match

    try:
        return json.loads(json_str)  # Convert to proper JSON
    except json.JSONDecodeError as e:
        print("JSON Parsing Error:", e)
        return None  # Return None if parsing fails

def query_ollama(model, prompt, input_data):
    """Queries the Ollama API and extracts JSON output."""
    url = "http://localhost:11434/api/generate"  # Adjust if using a different Ollama setup
    payload = {
        "model": model,
        "prompt": prompt + "\nInput Data: " + json.dumps(input_data),
        "stream": False
    }
    
    response = requests.post(url, json=payload).json()
    
    # Debugging: Print the entire response
    print("Raw Response from Model:", response)

    # Try extracting response text
    response_text = response.get("response", "")
    
    # Debugging: Print raw text
    print("Extracted Response Text:", response_text)

    if not response_text:
        print("Error: Model did not return a valid response.")
        return {"error": "Model response was empty"}
    
    response_json = clean_response(response_text)

    if response_json:
        reasoning_split = response_text.split("And here is the reasoning")
        if len(reasoning_split) > 1:
            response_json["reasoning"] = reasoning_split[1].strip()
    
    return response_json if response_json else {}

def select_best_response(response1, response2):
    """Selects the best response based on reasoning."""
    reasoning1 = response1.get("reasoning", "")
    reasoning2 = response2.get("reasoning", "")
    
    # Example logic: prefer the response that emphasizes smoothness and shortest path
    if "smooth" in reasoning1.lower() and "shortest" in reasoning1.lower():
        return response1
    elif "smooth" in reasoning2.lower() and "shortest" in reasoning2.lower():
        return response2
    else:
        # Default to first response if no clear reasoning
        return response1

def main():
    input_file =  # Replace with input JSON path
    prompt_file =  # Replace with prompt file path
    
    input_data = read_input_json(input_file)
    prompt = read_prompt_file(prompt_file)
    
    # Query both models
    response_llama = query_ollama("llama3", prompt, input_data)
    response_deepseek = query_ollama("deepseek-r1", prompt, input_data)
    
    # Select the best response
    best_response = select_best_response(response_llama, response_deepseek)
    
    # Save the best output
    with open("output.json", "w") as file:
        json.dump(best_response, file, indent=4)
    
    print("Best response saved to output.json")

if __name__ == "__main__":
    main()
