from flask import Flask, render_template, request
from fifo import *
from lru import *
from flaskwebgui import FlaskUI
import random

app = Flask(__name__)
ui = FlaskUI(app, width="1200", height="700")

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/FIFO')
def FIFO():
    return render_template('FIFO.html')

@app.route('/LRU')
def LRU():
    return render_template('LRU.html')

@app.route('/randomLru')
def randomLru():
    data_lru = []
    n = random.randint(4,10)
    for i in range(n):
        data_lru.append(random.randint(0,9))
    addPage_lru = addPageLru(data_lru,3)
    page_lru =  addPage_lru[0]
    page_fault_lru = "Page fault is "+str(addPage_lru[1])

    for pg in page_lru:
        print(pg)

    return render_template('LRU.html', page_lru = page_lru, page_fault_lru=page_fault_lru, data_lru = data_lru)

@app.route('/randomFifo')
def randomFifo():
    data = []
    n = random.randint(4,10)
    for i in range(n):
        data.append(random.randint(0,9))
    addPage = addPageFifo(data,3)
    page =  addPage[0]
    page_fault = "Page fault is "+str(addPage[1])

    for pg in page:
        print(pg)

    return render_template('Fifo.html', page = page, page_fault=page_fault, data = data)    

@app.route('/fifop/', methods=['POST','GET'])
def showPagefifo():
    data = request.form['data']
    addPage = addPageFifo(data,3)
    page =  addPage[0]
    page_fault = "Page fault is "+str(addPage[1])

    for pg in page:
        print(pg)

    return render_template('Fifo.html', page = page, page_fault=page_fault, data = data)

@app.route('/lrup/', methods=['POST','GET'])
def showPagelru():
    data_lru = request.form['data_lru']
    addPage_lru = addPageLru(data_lru,3)
    page_lru =  addPage_lru[0]
    page_fault_lru = "Page fault is "+str(addPage_lru[1])

    for pg in page_lru:
        print(pg)

    return render_template('LRU.html', page_lru = page_lru, page_fault_lru=page_fault_lru, data_lru = data_lru)

@app.route('/back')
def back():
    return render_template('index.html')

# if __name__ == '__main__':
#    app.run(debug=True)

ui.run()
   
