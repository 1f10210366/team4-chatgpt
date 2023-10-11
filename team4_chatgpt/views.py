from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from .forms import ChatForm
import openai


def index(request):
  

  # 応答結果
  chat_result = ""

  if request.method == "POST":
    #chatgptボタンが押された場合

    form = ChatForm(request.POST)
    if form.is_valid():
      sentence = form.cleaned_data['sentence']

      openai.api_key = "wprzlNppD6DwlmSTfw35yGnUyaQ8XwfqnFKAnxB6WAjOaRp641FrM91T_NY1E05F6DyW6iIMsmJVSjuyKU8NZsg"
      openai.api_base = "https://api.openai.iniad.org/api/v1"

      response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{sentence}"}
        ]
    )
    
    chat_results = response["choices"][0]["message"]["content"]

  
  else:
    form = ChatForm()
    
  template = loader.get_template('team4_chatgpt/index.html')
  context = {
    'form':form,
    'chat_results':chat_results
  }

    

  return HttpResponse(template.render(context,request))


