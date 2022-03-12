from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        #data is a dictionary
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    #READ
    @classmethod
    def muestra_usuarios(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('esquema_usuarios1').query_db(query)
        users = []
 
        for user in results:
            users.append(cls(user))
    
        return users
    
    #CREATE
    @classmethod
    def guardar(cls, formulario):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        result = connectToMySQL('esquema_usuarios1').query_db(query, formulario)
        return result

    #DELETE
    @classmethod
    def borrar(cls, formulario):
        #formulario = {"id": "1"}
        query = "DELETE FROM users WHERE id = %(id)s"
        result = connectToMySQL('esquema_usuarios1').query_db(query, formulario)
        return result


    #GET USER BY ID
    @classmethod
    def obtener_user_by_id(cls, formulario):
        #formulario = {"id": "1"}
        print(formulario)
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('esquema_usuarios1').query_db(query, formulario)
        # [  {'3','Juana','Herrera','juana@codingdojo.com','2022-03-09 14:50:58','2022-03-09 14:50:58'} ]
        print(result)
        user = result[0]
        user = cls(user)
        return user

    #UPDATE
    @classmethod
    def actualizar(cls, formulario):
        #formulario = {"id": "1", "first_name": "Miriam", "last_name": "Acuña", "email": "macuna@gmail.com"}
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s"
        result = connectToMySQL('esquema_usuarios1').query_db(query, formulario)
        return result
