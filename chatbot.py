from langchain_ollama import ollamaLLM
from langchain_core.prompts import chatPromptTemplate

template = """
Answer the question below.
here is the conversation history: {context}

question: {question}

Answer:
"""

model = ollamaLLM(model = "llama3.1")
prompt = chatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    content = ""
    print("Welcome to my space! Type 'exit' or 'quit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:

            print("Ending the conversation. Goodbye!")
            break

        result = chain.run(context=content, question=user_input)

        print(f"Chatbot: {result}")

        content += f"You: {user_input}\nChatbot: {result}\n"

handle_conversation()
