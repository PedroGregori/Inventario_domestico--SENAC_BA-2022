from .db import connect
from .inventario import Inventario as inv

class InventarioDAO():
    def add(i: inv):
        conn = connect()
        cursor = conn.cursor()
        SQL = 'INSERT INTO inventario(nome, sala, descricao, marca, data, valor, serie) VALUES (?,?,?,?,?,?,?);'
        dados = [i.nome, i.sala, i.descricao, i.marca, i.data, i.valor, i.serie]
        cursor.execute(SQL, dados)
        id_return = cursor.execute("SELECT last_insert_rowid();")
        id = id_return.fetchall()[0] [0]
        conn.commit()
        conn.close()
        
        return id
    
    def edit(i: inv):
        conn = connect()
        cursor = conn.cursor()
        SQL = 'UPDATE inventario SET nome=?, sala=?, descricao=?, marca=?, data=?, valor=?, serie=? WHERE id=?'
        dados = [i.nome, i.sala, i.descricao, i.marca, i.data, i.valor, i.serie, i.id]
        cursor.execute(SQL, dados)
        conn.commit()
        conn.close()
    
    def delete(id: int):
        conn = connect()
        cursor = conn.cursor()
        SQL = "DELETE FROM inventario WHERE id=?;"
        cursor.execute(SQL, [id])
        conn.commit()
        conn.close()
    
    def selectALL():
        items_lst = []
        conn = connect()
        cursor = conn.cursor()
        SQL = 'SELECT * FROM inventario'
        cursor.execute(SQL)
        return_lst = cursor.fetchall()
        for i in return_lst:
            novo_item = inv(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
            items_lst.append(novo_item)
        conn.close()
        
        return items_lst