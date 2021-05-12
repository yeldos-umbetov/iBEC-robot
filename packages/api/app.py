from flask import Flask, request
from ml_model.slogan_model import generate 
# import model

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# generate  
@app.route("/bot", methods=['POST'])
def hellobot():
    company = request.args.get('company')
    industry = request.args.get('industry')
    #product = request.args.get('product')
    
    result_text = "Компания: " + company + ". Индустрия: " + industry + ". Слоган: " 
    
    tok, model = load_tokenizer_and_model("sberbank-ai/rugpt3small_based_on_gpt2")
    generated = generate(model, tok, result_text, num_beams=10)
    generated_text = generated[0]
    
    return generated_text

if __name__ == '__main__':
    app.run()