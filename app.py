from flask import Flask, render_template, request

app = Flask(__name__)

def soma(num1, num2):
 return num1 + num2

def subtracao(num1, num2):
 return num1 - num2

def multiplicacao(num1, num2):
 return num1 * num2

def divisao(num1, num2):
 if num2 != 0:
  return num1 // num2
 return "Divisão por zero não pode :("

def potencia(num1, num2):
 return num1 ** num2

def raiz(num1, num2):
 if num1 > 0:
  return num1 ** (1 / num2)
 return "Não é possível calcular a raiz de um número negativo ou de zero :("

def calculadora(num1, operador, num2):
 if operador == '+':
  return soma(num1, num2)
 if operador == '-':
  return subtracao(num1, num2)
 if operador == '*':
  return multiplicacao(num1, num2)
 if operador == '/':
  return divisao(num1, num2)
 if operador == '**':
  return potencia(num1, num2)
 if operador == 'rad':
  return raiz(num1, num2)
 return "Operador inválido :("

@app.route('/', methods=['GET', 'POST'])
def index():
 resultado = None
 if request.method == 'POST':
  try:
   num1 = float(request.form['num1'])
   operador = request.form['operador']
   num2 = float(request.form['num2'])
   resultado = calculadora(num1, operador, num2)
  except:
   resultado = "Erro na entrada. Verifique os valores."
 return render_template("index.html", resultado=resultado)

if __name__ == '__main__':
 app.run(debug=True)
