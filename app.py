from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
  return "Hello World"


@app.route("/product/<int:product_id>")
def product_page(product_id):
  # return f'welcome to {product_id}\'s page!'
  return render_template('product-page.html', id=product_id)

if __name__ == '__main__':
  app.run(port=5000)
