from flask import Flask,render_template,request
import google.generativeai as genai

genai.configure(api_key='AIzaSyBheBRUilFd5KOXtNnqnXw-9zBlp6XaD-I')


mymodel = genai.GenerativeModel('gemini-1.5-flash')
chat = mymodel.start_chat()

app = Flask(__name__)

conv = ''

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit',methods=['POST'])
def contact():
    global conv
    user_input = request.form.get('name')
    print(user_input)
    response = chat.send_message(user_input)
    print('GEMINI:', response.text)
    conv = conv + '\n' + response.text
    return render_template('home.html', output = conv)

app.run()




