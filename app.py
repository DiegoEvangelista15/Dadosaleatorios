from PyQt5 import uic, QtWidgets
import sqlite3


def fechar():
    formulario.close()


def fechar2():
    formulario2.close()


def fechar3():
    formulario3.close()


def fechar4():
    formulario4.close()


def aleatorio():
    formulario4.show()

    conn = sqlite3.connect('dadosjuliana.db')
    cursor = conn.cursor()
    cursor.execute('update dados set quantidade = null where quantidade =""')
    cursor.execute('SELECT quantidade FROM dados WHERE quantidade IS NOT NULL ORDER BY RANDOM() ')
    a = cursor.fetchone()
    for a1 in a:
        formulario4.lineEdit.setText(a1)
    cursor.execute('update dados set sujeito = null where sujeito =""')
    cursor.execute('SELECT sujeito FROM dados WHERE sujeito IS NOT NULL ORDER BY RANDOM() ')
    b = cursor.fetchone()
    for b1 in b:
        formulario4.lineEdit_2.setText(b1)
    cursor.execute('update dados set acessorio = null where acessorio =""')
    cursor.execute('SELECT acessorio FROM dados WHERE acessorio IS NOT NULL ORDER BY RANDOM() ')
    c = cursor.fetchone()
    for c1 in c:
        formulario4.lineEdit_3.setText(c1)
    cursor.execute('update dados set acao = null where acao =""')
    cursor.execute('SELECT acao FROM dados WHERE acao IS NOT NULL ORDER BY RANDOM() ')
    d = cursor.fetchone()
    for d1 in d:
        formulario4.lineEdit_4.setText(d1)
    cursor.execute('update dados set com = null where com =""')
    cursor.execute('SELECT com FROM dados WHERE com IS NOT NULL ORDER BY RANDOM() ')
    e = cursor.fetchone()
    for e1 in e:
        formulario4.lineEdit_5.setText(e1)
    conn.commit()
    conn.close()


def salvar_dados():
    linha1 = formulario2.lineEdit.text()
    linha2 = formulario2.lineEdit_2.text()
    linha3 = formulario2.lineEdit_3.text()
    linha4 = formulario2.lineEdit_4.text()

    conn = sqlite3.connect('dadosjuliana.db')

    cursor = conn.cursor()

    cursor.execute("INSERT INTO dados (sujeito,acessorio ,acao,com) VALUES (?,?,?,?)", (linha1, linha2, linha3, linha4))

    conn.commit()

    conn.close()
    formulario3.show()
    formulario3.pushButton_3.clicked.connect(fechar3)

    formulario2.lineEdit.setText('')
    formulario2.lineEdit_2.setText('')
    formulario2.lineEdit_3.setText('')
    formulario2.lineEdit_4.setText('')


def gerar_novamente():
    formulario4.close()
    aleatorio()


def segunda_tela():
    formulario2.show()

    formulario2.pushButton.clicked.connect(salvar_dados)
    formulario2.pushButton_2.clicked.connect(fechar2)


app = QtWidgets.QApplication([])
formulario = uic.loadUi('inicial.ui')
formulario2 = uic.loadUi('page2.ui')
formulario3 = uic.loadUi('page3.ui')
formulario4 = uic.loadUi('page4.ui')

formulario.pushButton.clicked.connect(aleatorio)
formulario.pushButton_2.clicked.connect(segunda_tela)
formulario.pushButton_3.clicked.connect(fechar)
formulario4.pushButton.clicked.connect(fechar4)
formulario4.pushButton_2.clicked.connect(gerar_novamente)

formulario.show()
app.exec()
