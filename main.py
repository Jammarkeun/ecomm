from website import create_app
from flask import Flask, render_template, redirect, url_for

app = create_app()

@app.route('/account_page')
def account_page():
    return render_template('account.html')

if __name__ == "__main__":
    app.run(debug=True)
  

