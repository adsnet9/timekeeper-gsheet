from flask import Flask, render_template, request, redirect
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import os
import json

app = Flask(__name__)

# Setup Google Sheet via Service Account JSON di Environment Variables
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

creds_dict = json.loads(os.environ.get("GOOGLE_CREDS_JSON"))
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

sheet = client.open("TimeKeeper").sheet1

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        note = request.form.get("note")
        sheet.append_row([datetime.datetime.now().isoformat(), task, note])
        return redirect("/")
    
    data = sheet.get_all_records()
    return render_template("index.html", entries=data)

# handler untuk Vercel
handler = app
