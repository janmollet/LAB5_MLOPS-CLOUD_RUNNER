☁️ Cloud Run Intermediate Lab 

For this lab, I used Google Cloud Run and Docker to build and deploy a basic web application. The website includes personal information, hobbies, and integrates Google Cloud services.

🛠️ Setup in Google Cloud
1. Created a new Google Cloud project
2.Enabled required APIs:
  - BigQuery
  - Cloud Storage
  - Cloud Run
3. Created a Cloud Storage bucket
4. Configured and deployed a Cloud Run service

🧾 Application Development (app.py)
- Built the application using Flask
- Embedded HTML directly inside the Python file
- Improved the UI with:
    - Styled layouts (CSS)
    - Buttons for navigation
    - Emojis and visual elements
    -     - Better overall presentation
    - 
🌐 Endpoints
The application includes three main routes:
/query --> Retrieves and displays data using BigQuery
/music --> Redirects to my YouTube music channel
/about_me --> Displays information about me and my interests

🚀 Summary

This project demonstrates:

- Containerizing an application with Docker
- Deploying to Cloud Run
- Integrating Google Cloud services
- Building a simple multi-page Flask web app

🔝 ACCESS THE WEBSITE: https://cloud-run-intermediate-service-362452253630.us-central1.run.app
