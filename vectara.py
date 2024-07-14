import requests
import json
import streamlit as st

customerID = "566695243"
corpusID = "15"
api_key = st.secrets["VECTARA_API_KEY"]


# Step 1 Reset Corpus
def ResetCorpus():
    url = "https://api.vectara.io/v1/reset-corpus"

    payload = json.dumps({"corpusId": corpusID})
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "x-api-key": api_key,
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


# Step 2 Add Transcription Txt to Corpus
def AddFile():
    url = f"https://api.vectara.io/v1/upload?c={customerID}&o={corpusID}"

    payload = {}
    files = [
        ("file", ("course_slides", open("video_transcription.txt", "rb"), "application/txt"))
    ]
    headers = {
        "customer-id": f"{customerID}",
        "Accept": "application/json",
        "x-api-key": api_key,
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)


# Step 3 Ask Question
def askQuestion(prompt):
    url = "https://api.vectara.io/v1/query"

    payload = json.dumps(
        {
            "query": [
                {
                    "query": prompt,
                    "start": 0,
                    "numResults": 3,
                    "contextConfig": {
                        "sentences_before": 3,
                        "sentences_after": 3,
                        "start_tag": "<b>",
                        "end_tag": "</b>",
                    },
                    "corpusKey": [{"corpus_id": corpusID}],
                    "summary": [{"max_summarized_results": 10, "response_lang": "en"}],
                }
            ]
        }
    )
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "customer-id": customerID,
        "x-api-key": api_key,
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    response_data = response.json()
    result = response_data["responseSet"][0]["summary"][0]
    RawAnswer = result["text"]

    return RawAnswer
