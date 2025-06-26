from together import Together
from dotenv import load_dotenv

load_dotenv()

client = Together()


def get_responce(query):
  response = client.chat.completions.create(
      model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
      messages=[
        {
          "role": "user",
          "content": f"{query}, please give the answer in markdown format"
        }
      ]
  )
  return response
