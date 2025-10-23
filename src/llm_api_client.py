import os
import json
import requests

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

INPUT_FILE = "data/text.txt"
OUTPUT_FILE = "data/responses.json"
    
def reading_input(file_path):
    with open( file_path, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]
    return lines

def calling_gpt(prompt):
    headers= {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}",
    }
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": prompt}],
    }

    response = requests.post(GROQ_API_URL, headers= headers, json = payload)

    try:
        data = response.json()
    except Exception as e:
        print("Couldnt make response", e)
        print(response.text)
        return "Error"
    
    if response.status_code !=200:
        print(f"ERROR {response.status_code}:{data}")
        return f"Error: API returns {response.status_code}"
    if "choices" not in data:
        print("wrong response format:",data)
        return "Error"

    return data["choices"][0]["message"]["content"].strip()

    # data = response.json()
    # return data["choices"][0]["message"]["content"].strip()

def making_json_file(prompts,responses, output_path):
    result = [{"prompt":p, "response":r} for p, r in zip(prompts,responses)]
    with open(output_path,"w",encoding="utf-8") as json_file:
        json.dump(result, json_file, indent = 4, ensure_ascii=False)
    print(f"responded to {output_path}")

def main():
    if not GROQ_API_KEY:
        raise ValueError("No API key found.")

    prompts = reading_input(INPUT_FILE)       
    print(f"extracted {len(prompts)} prompts from given text file.")

    responses = []
    for i, prompt in enumerate(prompts, start=1):
        print(f"\n Processing prompt {i} of {len(prompts)}:{prompt}")
        reply= calling_gpt(prompt) 
        responses.append(reply)
    making_json_file(prompts, responses, OUTPUT_FILE)

if __name__ == "__main__":
    main()