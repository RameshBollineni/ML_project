from flask import Flask
import sys 
from creditcard.logger import logging
from creditcard.expection import CreditcardExpection

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])  

def index():
    try:
        raise Exception("We are testing custom expetcion")
    except Exception as e: 
        creditcard = CreditcardExpection(e,sys)
        logging.info(creditcard.error_message)
        logging.info('We are testing logging module')

    return "This is my first project in ML"


if __name__=='__main__':
    app.run(debug=True)

