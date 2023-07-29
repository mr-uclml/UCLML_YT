from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# First, you need to set up your API key
openai.api_key = "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"
model_engine = "gpt-3.5-turbo"

@app.route('/gpt', methods=['GET'])
def get_response():
    msg = request.args.get('txt', '')
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[{"role": "user", "content": msg}]
    )
    output_text = response['choices'][0]['message']['content']
    return jsonify({'gpt': output_text})

if __name__ == '__main__':
    app.run()