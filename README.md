# Shubham Sarraf — Developer Portfolio

A responsive personal portfolio built with HTML, CSS, JavaScript, Python, and Flask.

## Features

- Responsive layout with mobile navigation
- About, skills, projects, and contact sections
- Flask route serving the website
- Demo JSON contact endpoint with basic validation
- No database or paid API required

## Run on Windows with PowerShell

1. Extract the ZIP and open PowerShell in the extracted `shubham_portfolio` folder.
2. Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, you can use the environment's Python directly instead:

   ```powershell
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   .\.venv\Scripts\python.exe app.py
   ```

   Or, after activation, install the dependency:

   ```powershell
   python -m pip install -r requirements.txt
   ```

3. Start Flask:

   ```powershell
   python app.py
   ```

4. Open http://127.0.0.1:5000 in your browser.

Stop the development server with `Ctrl+C`.

## Personalize it

Open `app.py` and edit the `PROFILE`, `PROJECTS`, and `SKILLS` values. Replace the placeholder email address with an address you want to publish. Remove or update any project description that doesn't accurately represent your work.

## Important notes

- Flask's debug server is for local development only. Do not expose it directly to the public internet or use it as a production server.
- The contact form is a demo: the endpoint validates input and logs the sender name/email, but it does not send email or save the message.
- The page loads Google Fonts from the internet. If offline support is important, remove the font imports and use the fallback fonts.
- Review all public links and contact details before deploying.
