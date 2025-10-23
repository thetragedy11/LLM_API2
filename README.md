#LLM API PROJECT

This program reads text from a file, calls a LLM API, saves generated responses to an output JSON file

##Features:
1.Reading text from a text file(text.txt)
2.Calling Groq LLM API(`llama-3.1-8b-instant` model)
3.Saving respones to a structured JSON file
4.Handling some API errors(Failed responses, invalid API key, etc.)

##Setup:
1.Cloning repository:
  git clone <url>
  cd <folder>
2.Install dependencies:
  cmd<< pip install -r requirements.txt
3.Setup API key:
  use Groq, and make ur own API<< Copy the API KEY
  use the following commands in cmd, to store the Key temporarily as environmental variable
    -export GROQ_API_KEY="your_api_key_here"   # Linux / macOS
    -setx GROQ_API_KEY="your_api_key_here"      # Windows

##How to run:
1.Add prompts to data/text.txt, ensuring a single prompt on each line
2.Run the script, cd src
                  python llm_api_client.py
3.Responses are saved in data/responses.json