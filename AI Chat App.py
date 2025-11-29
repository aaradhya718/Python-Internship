import google.generativeai as genai

# Define your API key
key = "Enter your API key here"
print(key)

# Configure the library with your API key
genai.configure(api_key=key)  # This line was missing - you need to configure the API key

# Create the model
model = genai.GenerativeModel("gemini-2.5-flash")

# conversation loop
while True:
    user = input("Enter what you want to search or type exit to close: ")
    if user.lower() == "exit":
        print("bye bye")
        break
    response = model.generate_content(user)
    print("BOT:", response.text)