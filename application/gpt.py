import openai
openai.api_key = "wprzlNppD6DwlmSTfw35yGnUyaQ8XwfqnFKAnxB6WAjOaRp641FrM91T_NY1E05F6DyW6iIMsmJVSjuyKU8NZsg"
openai.api_base = "https://api.openai.iniad.org/api/v1"



def ask_gpt(question):
    response = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{question}"}
        ]
    )
    return response['choices'][0]['message']['content']

# ユーザーからの質問を要求
user_question = input("質問を入力してください: ")

# ChatGPTに質問を投げ、返答を表示
print(ask_gpt(user_question))