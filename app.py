from flask import Flask, render_template, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)


@app.route('/')
def display_data():
    sheet = client.open('Indian Millet Information').worksheet('Cost_of_Cultivation')
    data = sheet.get_all_records()
    print(data)
    return render_template('data.html', data=data)


@app.route('/add', methods=['POST'])
def add_data():
    sheet = client.open('Indian Millet Information').sheet1
    new_row = [request.form.get('name'), request.form.get('email')]
    sheet.append_row(new_row)
    return 'Data added successfully!'


if __name__ == '__main__':
    app.run()
