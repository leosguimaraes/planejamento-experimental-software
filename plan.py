# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 23:56:38 2020

@author: Leonardo
"""
from PyQt5 import uic, QtWidgets
from doepy import build
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import QMessageBox,QMenuBar, QMenu, QAction, QFileDialog
import statsmodels.api as sm
from statsmodels.formula.api import ols


def mostra_form():
     form1.show()

def transforma_dict():
     form2.show() 
     a = form1.fator1.text()
     b = form1.fator2.text()
     c = form1.fator3.text()
     d = form1.nivel1_fator1.text()
     e = form1.nivel2_fator1.text()
     f = form1.nivel3_fator1.text()
     g = form1.nivel1_fator2.text()
     h = form1.nivel2_fator2.text()
     i = form1.nivel3_fator2.text()
     j = form1.nivel1_fator3.text()
     l = form1.nivel2_fator3.text()
     m = form1.nivel3_fator3.text()
     
     x = {a:[d, e, f], b:[g, h, i], c:[j, l, m] }
    
     
     box = build.box_behnken(x, center=3)
     form2.tabela_planejamento.setRowCount(len(box))
     form2.tabela_planejamento.setColumnCount(3)
     df = pd.DataFrame(box)
     tabela = np.array(df)
   
    
     for i in range(0, len(tabela)):
         for j in range (0, 3):
             form2.tabela_planejamento.setItem(i, j, QtWidgets.QTableWidgetItem(str(tabela[i][j])))
     
def salvar_planejamento():
     form2.show() 
     a = form1.fator1.text()
     b = form1.fator2.text()
     c = form1.fator3.text()
     d = form1.nivel1_fator1.text()
     e = form1.nivel2_fator1.text()
     f = form1.nivel3_fator1.text()
     g = form1.nivel1_fator2.text()
     h = form1.nivel2_fator2.text()
     i = form1.nivel3_fator2.text()
     j = form1.nivel1_fator3.text()
     l = form1.nivel2_fator3.text()
     m = form1.nivel3_fator3.text()
     
     x = {a:[d, e, f], b:[g, h, i], c:[j, l, m] }
     box = build.box_behnken(x, center=3)
     planejamento = box.to_excel('planejamento.xlsx')
     QMessageBox.about(form2, 'Alerta!', 'Planejamento salvo com sucesso!')
    
def chama_form_anova():
        form_anova.show()
        

        
def abrir_arquivo():
    x = form_anova.nome_arquivo.text()
    y = pd.read_excel(x)
    arquivo = pd.DataFrame(y)
    form_anova.tabela_anova.setRowCount(len(x))
    form_anova.tabela_anova.setColumnCount(4)   
    tabela = np.array(arquivo)
    for i in range(0, len(tabela)):
         for j in range (0, 4):
             form_anova.tabela_anova.setItem(i, j, QtWidgets.QTableWidgetItem(str(tabela[i][j])))
     
    
def anova():
    x = form_anova.nome_arquivo.text()
    y = pd.read_excel(x)
    arquivo = pd.DataFrame(y)
    
    x1 = arquivo.iloc[:, 0]
    x2 = arquivo.iloc[:, 1]
    x3 = arquivo.iloc[:, 2]
    y = arquivo.iloc[:, 3]
    funcao = 'y ~ x1*x2*x3'
    modelo = ols(funcao, arquivo).fit()
    anova = sm.stats.anova_lm(modelo)
    print(anova)
    
    
    
    

app = QtWidgets.QApplication([])
form_principal = uic.loadUi('form_principal.ui')
form1 = uic.loadUi('form1.ui')
form2 = uic.loadUi('form2.ui')
form_anova = uic.loadUi('form_anova.ui')
form1.btn_gerar_planejamento.clicked.connect(transforma_dict)
form2.btn_salvar_planejamento.clicked.connect(salvar_planejamento)
form_principal.actionGerar_Planejamento_2.triggered.connect(mostra_form)
form_principal.actionGerar_ANOVA.triggered.connect(chama_form_anova)
form_anova.btn_abrir.clicked.connect(abrir_arquivo)
form_anova.btn_gerar_anova.clicked.connect(anova)
form_principal.show()
app.exec()
