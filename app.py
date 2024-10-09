import google.generativeai as ai

API_KEY = "AIzaSyCCppM4Pkxkpc-m96KFF743dxDxr2VOgds"

#configure the API
ai.configure(api_key=API_KEY)

#create new model
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

#start a conversation
while True:
    message = input("You: ")
    if message.lower()=='bye':
        print('ChatBot: Goodbye!!')
        break
    response = chat.send_message(message)
    print("ChatBot: ", response.text)