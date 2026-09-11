from flask import Blueprint, send_from_directory, request
from base import BASE_DIR
from email.message import EmailMessage
import smtplib, os

portfolio = Blueprint('portfolio', __name__)
PORTFOLIO_DIR = BASE_DIR / 'frontend/portfolio/dist/portfolio/browser'
DOC_DIR = BASE_DIR / 'backend/docs/_build/html'

@portfolio.route('/')
def portfolio_index():
    return send_from_directory(PORTFOLIO_DIR, 'index.html')

@portfolio.route('/<path:path>')
def portfolio_data(path):
    return send_from_directory(PORTFOLIO_DIR, path)

@portfolio.route('/docs/')
def portfolio_doc_index():
    return send_from_directory(DOC_DIR, 'index.html')

@portfolio.route('/docs/<path:path>')
def portfolio_doc_files(path):
    return send_from_directory(DOC_DIR, path)

@portfolio.route('/contact', methods=['POST'])
def getContactData():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    question = data.get('question')
    if (name and email and question):
        notify_me(name, email, question)
        send_confirm(name, email)
        return '', 200
    else: return '', 400

def notify_me(name:str, email:str, question:str):
    password = os.environ['MAIL_PASSWORD']
    msg = EmailMessage()
    msg['Subject'] = f'Portfolioanfrage von {name}'
    msg['From'] = 'marco.elste@web.de'
    msg['To'] = 'marco.elste@web.de'
    msg['Reply-To'] = email

    msg.set_content(f"""
    Neue Protfolioanfrage:

    Name: {name}
    E-Mail: {email}
    question: {question}
    """)

    with smtplib.SMTP('smtp.web.de', 587) as smtp:
        smtp.starttls()
        smtp.login('marco.elste@web.de', password)
        smtp.send_message(msg)

def send_confirm(name:str, email:str):
    password = os.environ['MAIL_PASSWORD']
    msg = EmailMessage()
    msg['Subject'] = f'Ihre Portfolioanfrage'
    msg['From'] = 'marco.elste@web.de'
    msg['To'] = email
    msg['Reply-To'] = 'marco.elste@web.de'

    msg.set_content(f"""
    Hallo {name},

    ich habe Ihre Anfrage erhalten und werde diese so schnell wie möglich beantworten.

    Vielen Dank!

    Freundliche Grüße

    Marco Elste
    """)

    with smtplib.SMTP('smtp.web.de', 587) as smtp:
        smtp.starttls()
        smtp.login('marco.elste@web.de', 'Elma#280489')
        smtp.send_message(msg)