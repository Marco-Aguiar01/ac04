import os
  2 from flask import Flask, jsonify, request
  3 from math import sqrt
  4 
  5 app = Flask(__name__)
  6 
  7 @app.route('/')
  8 def nao_entre_em_panico():
  9     proximo = 1
 10     anterior = 0
 11     limite = 50
 12     found = 0
 13     resposta = "0,"
 14     while (found < limite):
 15         tmp = proximo
 16         proximo = proximo + anterior
 17         anterior = tmp
 18         found = found+1reposta+= str(proximo) + ","
 20 
 21 
 22     return resposta
 23 
 24 if __name__ =="__main__":
 25     port = int(os.environ.get("PORT", 5000))
 26     app.run(host='0.0.0.0', port=port)
 27 
                                                        
