# ⏰ TimeKeeper (Flask + Google Sheet + Vercel)

A simple time logging app using Flask + Bootstrap as UI, and Google Sheets as the database.

## 🚀 Deploy Steps

1. Create a Google Cloud Service Account → enable Google Sheets API.
2. Download the service account JSON.
3. Go to Vercel → Project Settings → Environment Variables:
   - Key: `GOOGLE_CREDS_JSON`
   - Value: (paste entire JSON content)
4. Create a Google Sheet named `TimeKeeper` with headers:
   - `Timestamp | Task | Note`
5. Share the sheet with your service account email.
6. Push this repo to GitHub and import into Vercel.
7. Open your Vercel project → you now have a working TimeKeeper GUI.
