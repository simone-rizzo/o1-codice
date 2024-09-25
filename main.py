from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

# print(api_key)

client = OpenAI(api_key=api_key)

query = "Se lancio una moneta da 2 euro dal balcone del 6sto piano di un palazzo, qual'è la velocità finale della moneta nel colpire il suolo?"
response = client.chat.completions.create(
  model="o1-preview",
  messages=[
      {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Sei un professore di Fisica che è in grado di rispondere a qualsiasi problema utilizzando la Fisica. Se nel problema ci sono dati mancanti fai delle assunzioni e risolvilo."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": f"<problema>{query}</problema>"
        }
      ]
    }
  ]
)
print(response.choices[0].message.content)