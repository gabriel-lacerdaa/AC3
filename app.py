from flask import Flask, jsonify, request, json
import mysql.connector
app = Flask(__name__)
conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='admin'
)
cursor = conn.cursor()
cursor.execute('USE Produtos;')


@app.route('/produtos')
def TodosProdutos():
    cursor.execute(f'SELECT * FROM Produtos;')
    produtos = cursor.fetchall()
    print(produtos)
    return produtos


@app.route('/produtos/cadastrar', methods=["POST"])
def cadastrarProduto():
    nome = request.args.get("nome")
    preco = request.args.get("preco")
    sql = '''
    INSERT INTO Produtos(nome, preco)
    values (%s, %s)
    '''
    try:
        cursor.execute(sql, (nome,preco))
        conn.commit()
        return "produto inserido com sucesso", 201
    except:
        return "Erro ao inserir", 400



@app.route("/produtos/deletar", methods=["DELETE"])
def deletarProduto():
    id = request.args.get("id")
    sql = f'DELETE FROM Produtos WHERE id = {id}'
    cursor.execute(sql)
    conn.commit()
    return f"produto com id {id} foi deletado", 200


if __name__ == "__main__":
    app.run(host="localhost",debug=True)
