from openai import OpenAI
import requests

openai_client = OpenAI()


def speech_to_text(audio_binary):
    return None


def text_to_speech(text, voice=""):
    # Set up Watson Text to Speech HTTP Api url
    base_url = "https://sn-watson-stt.labs.skills.network"
    api_url = base_url + '/text-to-speech/api/v1/synthesize?output=output_text.wav'

    # Adding voice parameter in api_url if the user has selected a preferred voice
    if voice != "" and voice != "default":
        api_url += "&voice=" + voice

    # Set the headers for our HTTP request
    headers = {
        'Accept': 'audio/wav',
        'Content-Type': 'application/json',
    }

    # Set the body of our HTTP request
    json_data = {
        'text': text,
    }

    # Send a HTTP Post reqeust to Watson Text to Speech Service
    response = requests.post(api_url, headers=headers, json=json_data)
    print('text to speech response:', response)
    return response.content

def openai_process_message(user_message):
    # Set the prompt for OpenAI Api
    instruction = "Act like a personal assistant. You can respond to questions, translate sentences, summarize news, and give recommendations. "
    messages = [{"role": "system", "content": instruction},
             {"role": "user", "content": user_message}]
    # Call the OpenAI Api to process our prompt
    openai_response = openai_client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    print("openai response:", openai_response)
    # Parse the response to get the response text for our prompt
    response_text = openai_response.choices[0].message.content
    return response_text