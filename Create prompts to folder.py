import os
import requests
import json
import openai
import datetime

# Replace with your OpenAI API Key
api_key = "ENter API KEy HEre"

# The base URL for the OpenAI API
api_url = "https://api.openai.com/v1/chat/completions"


# The number of API calls for each prompt
num_calls = 10  # Change this to the number you want


def call_api(prompt):
    """
    Function to call OpenAI API and return the response
    """
    openai.api_key = api_key
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }
    response = openai.ChatCompletion.create(**data)

    return response['choices'][0]['message']['content'].strip()

def create_prompt_folder(i):
    """
    Function to create a unique folder for a prompt
    """
    # Create folder name with the current time and number of prompts
    folder_name = datetime.datetime.now().strftime('%Y%m%d_%H%M') + f"_prompt_{i+1}"

    # Ensure the folder does not already exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        
    return folder_name

def write_prompt_to_file(prompt, folder_name):
    """
    Function to write the prompt to a text file
    """
    with open(os.path.join(folder_name, "PROMPT.txt"), "w") as file:
        file.write(prompt)

def write_responses_to_files(prompt, i):
    """
    Function to write API responses to text files
    """
    # Create a unique folder for the prompt
    folder_name = create_prompt_folder(i)
    
    # Write the prompt to a text file
    write_prompt_to_file(prompt, folder_name)
    
    # Make API calls and write responses to files
    for j in range(num_calls):
        response = call_api(prompt)
        with open(os.path.join(folder_name, f"{j+1}.txt"), "w") as file:
            file.write(response)

# Replace with your prompts
prompts = [
    "Write a ONE PARAGRAPH story based on the following sentence: he was a **s m a r t** and handsome man", 
    "Write a ONE PARAGRAPH story based on the following sentence: he was a smart and h a n d s o m e man"
]

for i, prompt in enumerate(prompts):
    write_responses_to_files(prompt, i)
