from flet import *
from conn_serv import *

def main(page:Page):
    page.window_height = 600
    page.window_width = 500
    
    clavetxt = TextField(label="Precio")
    nametxt = TextField(label="nombre")
    
    edit_clavetxt = TextField(label="Precio")
    edit_nametxt = TextField(label="Nombre")
    edit_id = Text()
    
    mydt = DataTable(
        columns=[
            DataColumn(Text("id")),
            DataColumn(Text("Precio")),
            DataColumn(Text("Nombre")),
            DataColumn(Text("Actions")),
        ],
        rows=[]
        )
    
    def deletebtn(e):
        try:
            sql = "DELETE FROM SERVICIO WHERE SERV_ID = %s"
            val = (e.control.data['SERV_ID'],)
            cursor.execute(sql, val)
            conexion.commit()
            
            mydt.rows.clear()
            load_data()
                
            page.snack_bar = SnackBar(
                Text("Eliminado con exito", size = 30),
                    bgcolor='red'
            )
            page.snack_bar.open = True
            page.update()
        except Exception as e:
            print(e)
            print("error delete")
    
    
    def savedata(e):
        try:
            sql = "UPDATE SERVICIO SET SERV_PRECIO = %s , SERV_NOMBRE = %s WHERE SERV_ID = %s"
            val = (edit_clavetxt.value, edit_nametxt.value, edit_id.value)
            
            cursor.execute(sql, val)
            conexion.commit()
            
            print("guardado")
            dialog.open = False
            page.update()
            
            edit_clavetxt.value = ""
            edit_nametxt.value = ""
            edit_id.value = ""
            
            mydt.rows.clear()
            load_data()
            
            page.snack_bar = SnackBar(
                Text("editado con exito", size = 30),
                bgcolor='green'
            )
            page.snack_bar.open = True
            page.update()
        except Exception as e:
            print(e)
            print("Error editar")
    
    dialog = AlertDialog(
        title=Text("Editar"),
        content=Column([
            edit_clavetxt,
            edit_nametxt
        ]),
        actions=[
            TextButton("Guardar",
                       on_click=savedata)
        ]
    )
    
    def editbtn(e):
        edit_clavetxt.value = e.control.data['SERV_PRECIO']
        edit_nametxt.value = e.control.data['SERV_NOMBRE']
        edit_id.value = e.control.data['SERV_ID']
        
        page.dialog = dialog
        dialog.open = True
        page.update()
    
    def load_data():
        cursor.execute("SELECT * FROM SERVICIO")
        result = cursor.fetchall()
        
        columns = [column[0] for column in cursor.description]
        rows = [dict(zip(columns, row)) for row in result]
        
        
        for row in rows:
            mydt.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(row['SERV_ID'])),
                        DataCell(Text(row['SERV_PRECIO'])),
                        DataCell(Text(row['SERV_NOMBRE'])),
                        DataCell(
                            Row([
                                IconButton('delete', icon_color='red',
                                           data=row,
                                           on_click=deletebtn
                                           ),
                                IconButton('create', icon_color='blue',
                                           data=row,
                                           on_click=editbtn
                                           ),
                            ])
                            
                            )
                    ]
                )   
            )
            
        page.update()
        
    load_data()
    
    def addto(e):
        try:
            sql = "INSERT INTO SERVICIO (SERV_PRECIO, SERV_NOMBRE) VALUES(%s, %s)"
            val = (clavetxt.value, nametxt.value)
            cursor.execute(sql, val)
            conexion.commit()
            
            mydt.rows.clear()
            load_data()
            
            page.snack_bar = SnackBar(
                Text("Agregado con exito", size = 30),
                bgcolor='green'
            )
            page.snack_bar.open = True
            page.update()
            
        except Exception as e:
            print(e)
            print("Error add")
        
        clavetxt.value = ""
        nametxt.value = ""
        
        page.update()
    
    
    page.add(
        Column([
            clavetxt,
            nametxt,
            ElevatedButton("Agregar", on_click=addto),
            mydt
        ])
    )


app(target=main)