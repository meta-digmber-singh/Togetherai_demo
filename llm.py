from together import Together
from jinja2 import Template
from dotenv import load_dotenv

load_dotenv()

client = Together()


def generate_prompt(query: str, data: str | None):
  with open("templates/prompt.j2") as f:
    template = Template(f.read())

  return template.render(user_query = query, realtime_data = data)


def get_responce(query: str, data: str | None):
  
  prompt = generate_prompt(query, data)
  
  response = client.chat.completions.create(
      model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
      messages=[
        {
          "role": "user",
          "content": prompt
        }
      ]
  )
  return response
