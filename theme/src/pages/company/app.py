# app.py

#from flask import Flask, request, jsonify
#from transformers import GPT2LMHeadModel, GPT2Tokenizer

#app = Flask(__name__)

# Load the GPT-2 model and tokenizer
#model = GPT2LMHeadModel.from_pretrained("gpt2")
#tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

#@app.route("/api/chatbot", methods=["POST"])
#def chatbot():
 #   data = request.get_json()
  #  user_message = data["message"]
#
 #   # Tokenize the user's message and generate chatbot response
  #  input_ids = tokenizer.encode(user_message, return_tensors="pt")
   # output = model.generate(input_ids, max_length=100, num_return_sequences=1)
    #chatbot_response = tokenizer.decode(output[0], skip_special_tokens=True)

    #return jsonify({"message": chatbot_response})

#if __name__ == "__main__":
 #   app.run(debug=True)