from flask import Flask, render_template, request, send_file
import pandas
from geopy.geocoders import Nominatim
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success-table', methods=['GET', 'POST'])
def success_table():
    # print(request.files) # FileStorage:
    try:
        df = pandas.read_csv(request.files['file'])
        # print(df)
        gc = Nominatim()
        print('geocode start')

        def geocode(address):
            return gc.geocode(address, timeout=10)

        df['Coodinates'] = df['Address'].apply(geocode)
        print('geocode end')
        df['Latitude'] = df['Coodinates'].apply(lambda x: x.latitude if x != None else None)
        df['Longitude'] = df['Coodinates'].apply(lambda x: x.longitude if x != None else None)
        df.drop('Coodinates', 1)
        global filename
        filename = datetime.datetime.now().strftime("uploads/%Y-%m-%d-%H-%M-%S-%f"+".csv")
        df.to_csv(filename, index=None)
        return render_template("index.html", text=df.to_html(), btn='download.html')
    except Exception as ex:
        print(ex)
        return render_template("index.html", text="Please make sure you have an address column in your CSV file!")


@app.route("/download-file/")
def download():
    return send_file(filename, attachment_filename='yourfile.csv', as_attachment=True)

if __name__ == '__main__':
    app.debug = True
    app.run()

