import tkinter as tk
import bs4, requests, os


window = tk.Tk()
window.title('Global Finance Info')
window.geometry('1000x1000')
window.configure(background='gold')

def usinfo():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }

    url = 'https://www.cnyes.com/futures/indexftr2.aspx'                     # 這個伺服器會擋住網頁
    html = requests.get(url, headers=headers)

    objSoup = bs4.BeautifulSoup(html.text, 'lxml')

    stock = objSoup.find('div',class_='tab')

    a = stock.find_all('td')
    data = []
    for d in a:
        data.append(d.text)
    # print(data)

    # for i in range(0,29):
    #     result = ''
    #     for h in range(i*9,(i+1)*9):
    #         result = result +''+ a[h].text+' '
    #     resultusinfo_label.insert('end', result)
    for i in range(0,28):
        qaz = ''
        wsx = ''
        edc = ''
        if i ==0:
            for h in range(0,8):
                qaz = qaz + ' ' +a[h].text + ' '
        elif i == 1:
            for h in range(11,19):
                edc = edc + ' ' +a[h].text + ' '
        else:
            for h in range(i*11,(i+1)*11-2):
                wsx = wsx + ' ' + a[h].text+' '
        result = qaz + wsx + edc
        resultusinfo_label.insert('end', result)
def urinfo():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }

    url = 'https://www.cnyes.com/futures/indexftr2.aspx'                     # 這個伺服器會擋住網頁
    html = requests.get(url, headers=headers)

    objSoup = bs4.BeautifulSoup(html.text, 'lxml')

    stock = objSoup.select('.tab')

    euro = stock[2].find_all('td')

    data = []
    for d in euro:
        data.append(d.text)

    for i in range(0,28):
        qaz = ''
        wsx = ''
        edc = ''
        if i ==0:
            for h in range(0,8):
                qaz = qaz + ' ' +euro[h].text + ' '
        elif i == 1:
            for h in range(11,19):
                edc = edc + ' ' +euro[h].text + ' '
        else:
            for h in range(i*11,(i+1)*11-2):
                wsx = wsx + ' ' + euro[h].text+' '
        result = qaz + wsx + edc
        resulturinfo_label.insert('end', result)

def chinfo():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }

    url = 'https://www.cnyes.com/futures/indexftr2.aspx'                     # 這個伺服器會擋住網頁
    html = requests.get(url, headers=headers)

    objSoup = bs4.BeautifulSoup(html.text, 'lxml')

    stock = objSoup.select('.tab')

    asia = stock[1].find_all('td')

    data = []
    for d in asia:
        data.append(d.text)

    for i in range(0,28):
        qaz = ''
        wsx = ''
        edc = ''
        if i ==0:
            for h in range(0,8):
                qaz = qaz + ' ' +asia[h].text + ' '
        elif i == 1:
            for h in range(11,19):
                edc = edc + ' ' +asia[h].text + ' '
        else:
            for h in range(i*11,(i+1)*11-2):
                wsx = wsx + ' ' + asia[h].text+' '
        result = qaz + wsx + edc
        resultchinfo_label.insert('end', result)
def gdinfo():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)\
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
                Safari/537.36', }

    url = 'https://www.cnyes.com/futures/heavymetal.aspx'                     # 這個伺服器會擋住網頁
    html = requests.get(url, headers=headers)

    objSoup = bs4.BeautifulSoup(html.text, 'html.parser')
    datas = []
    price = (objSoup.find_all('td'))
    for data in price:
        datas.append(data.text)
    
    # result = ''
    for i in range(0,9):
        result = ''
        for h in range(i*12,(i+1)*12):
            result = result +' '+ price[h].text+' '
        resultgdinfo_label.insert('end', result)

        # result = result + price[i].text
        # print(datas[i], end='   ')
    #     if (i > 0 and i %12 == 11 ):
    #         result = result + price[i].text+'\n'
    #     else:
    #         result = result + price[i].text
    #         # result = price[i].text
    # resultgdinfo_label.insert('end', result)

def clear():
    resultgdinfo_label.delete(0,'end')
    resultusinfo_label.delete(0,'end')
    resultchinfo_label.delete(0,'end')
    resulturinfo_label.delete(0,'end')


header_label = tk.Label(window, text='Financial Commodity Inquiry', font=('verdana', 30,'bold','italic'), bg='lightblue')
clear_btn = tk.Button(window, text='Clear', command=clear, font=('verdana', 30), width=5)
checkusinfo_btn = tk.Button(window, text='查詢美股指數', command=usinfo, font=('Arial', 15))
resultusinfo_label = tk.Listbox(window, font=('Arial', 10), width=90, height=12)
checkurinfo_btn = tk.Button(window, text='查詢歐股指數', command=urinfo, font=('Arial', 15))
resulturinfo_label = tk.Listbox(window, font=('Arial', 10), width=90, height=12)
checkchinfo_btn = tk.Button(window, text='查詢亞股指數', command=chinfo, font=('Arial', 15))
resultchinfo_label = tk.Listbox(window, font=('Arial', 10), width=90, height=12)
checkgdinfo_btn = tk.Button(window, text='查詢貴金屬\n的期貨價格', command=gdinfo, font=('Arial', 15))
resultgdinfo_label = tk.Listbox(window, font=('Arial', 10), width=90, height=12)
listbox = tk.Listbox(window, width = 100, height = 30)

# 版面配置
header_label.grid(row=0, column=0, columnspan=3)
clear_btn.grid(row=0, column=3)
checkusinfo_btn.grid(row=1, column=0)
resultusinfo_label.grid(row=1, column=1)
checkurinfo_btn.grid(row=2, column=0)
resulturinfo_label.grid(row=2, column=1)
checkchinfo_btn.grid(row=3, column=0)
resultchinfo_label.grid(row=3, column=1)
checkgdinfo_btn.grid(row=4, column=0)
resultgdinfo_label.grid(row=4, column=1)


window.mainloop()