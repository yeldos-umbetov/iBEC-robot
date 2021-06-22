import pickle

from flask import Flask, request, jsonify
from model_files.slogan_model import generate, load_tokenizer_and_model

app = Flask('ibec_robot')

@app.route("/")
def hello():
    return "Hello World!"

# generate
@app.route("/bot", methods=['POST'])
def hellobot():
    company = request.args.get('company')
    industry = request.args.get('industry')
    # product = request.args.get('product')

    result_text = "Компания: " + company + ". Индустрия: " + industry + ". Слоган: "

    tok, model = load_tokenizer_and_model("sberbank-ai/rugpt3small_based_on_gpt2")
    generated = generate(model, tok, result_text, num_beams=10)
    generated_text = generated[0]

    return generated_text


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
