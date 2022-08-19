from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView
from PyQt5 import uic

from model.inventario import Inventario as inv
from model.inventario_dao import InventarioDAO as invDAO

FILE_UI = 'view/main_window.ui'

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(FILE_UI, self)
        
        self.addBtn.clicked.connect(self.add)
        self.editBtn.clicked.connect(self.edit)
        self.delBtn.clicked.connect(self.delete)
        self.addBtn.clicked.connect(self.valores)
        self.editBtn.clicked.connect(self.valores)
        self.delBtn.clicked.connect(self.valores)    
        
        self.tabela.horizontalHeader().setStretchLastSection(True) 
        self.tabela.horizontalHeader().setSectionResizeMode( 
            QHeaderView.Stretch)
        
        self.loadData()
        self.valores()
        
        
    def loadData(self):
        items_lst = invDAO.selectALL()
        for i in items_lst:
            self.addTableItem(i)
        
    def valores(self):
        valorTotal = invDAO.valores()
        valorTratado = valorTotal[0]
        qtd = len(invDAO.selectALL())
        self.avisos(valorTratado[0],str(qtd))
        
    def add(self):
        nome = self.nome.text()
        sala = self.sala.text()
        descricao = self.descricao.text()
        marca = self.marca.text()
        data = self.data.text()
        valor = self.valor.text()
        serie = self.numSerie.text()
            
        newItem = inv(-1, nome, sala, descricao, marca, data, float(valor), int(serie))
        id = invDAO.add(newItem)
        newItem.id = id
            
        self.addTableItem(newItem)
        self.nome.clear()
        self.sala.clear()
        self.descricao.clear()
        self.marca.clear()
        self.valor.clear()
        self.numSerie.clear()
            
    def avisos(self, valor, quantidade):
        self.valorTotal.setText(f"R$ {valor}")
        self.qtd.setText(quantidade)
        
    """def fill_fields(self, line):
        nome = self.tabela.item(line, 1)
        sala = self.tabela.item(line, 2)
        descricao = self.tabela.item(line, 3) 
        marca = self.tabela.item(line, 4)
        data = self.tabela.item(line, 5)
        valor = self.tabela.item(line, 6)
        serie = self.tabela.item(line, 7)
        self.nome.setText(nome.text())"""
    
    def edit(self):
        lineSel = self.tabela.currentRow()
        lineItem = self.tabela.item(lineSel, 0)
        #self.fill_fields(lineSel)
        id = lineItem.text()
        nome = self.nome.text()
        sala = self.sala.text()
        descricao = self.descricao.text()
        marca = self.marca.text()
        data = self.data.text()
        valor = self.valor.text()
        serie = self.numSerie.text()

        edit = inv(id, nome, sala, descricao, marca, data, float(valor), int(serie))
        self.updateTable(edit)
        invDAO.edit(edit)

    def delete(self):
        lineSel = self.tabela.currentRow()
        lineItem = self.tabela.item(lineSel, 0)
        id = lineItem.text()
        self.tabela.removeRow(lineSel)
        invDAO.delete(int(id))
        
    def addTableItem(self, i: inv):
        line = self.tabela.rowCount()
        self.tabela.insertRow(line)
        id = QTableWidgetItem(str(i.id))
        nome = QTableWidgetItem(i.nome)
        sala = QTableWidgetItem(i.sala)
        descricao = QTableWidgetItem(i.descricao)
        marca = QTableWidgetItem(i.marca)
        data = QTableWidgetItem(i.data)
        valor = QTableWidgetItem(str(i.valor))
        serie = QTableWidgetItem(str(i.serie))
            
        self.tabela.setItem(line, 0, id)
        self.tabela.setItem(line, 1, nome)
        self.tabela.setItem(line, 2, sala)
        self.tabela.setItem(line, 3, descricao)
        self.tabela.setItem(line, 4, marca)
        self.tabela.setItem(line, 5, data)
        self.tabela.setItem(line, 6, valor)
        self.tabela.setItem(line, 7, serie)
            
    def updateTable(self, i: inv):
        lineSel = self.tabela.currentRow()
        nome = QTableWidgetItem(i.nome)
        sala = QTableWidgetItem(i.sala)
        descricao = QTableWidgetItem(i.descricao)
        marca = QTableWidgetItem(i.marca)
        data = QTableWidgetItem(i.data)
        valor = QTableWidgetItem(str(i.valor))
        serie = QTableWidgetItem(str(i.serie))
            
        self.tabela.setItem(lineSel, 1, nome)
        self.tabela.setItem(lineSel, 2, sala)
        self.tabela.setItem(lineSel, 3, descricao)
        self.tabela.setItem(lineSel, 4, marca)
        self.tabela.setItem(lineSel, 5, data)
        self.tabela.setItem(lineSel, 6, valor)
        self.tabela.setItem(lineSel, 7, serie)
            