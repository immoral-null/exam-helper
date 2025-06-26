# Exam Helper

This tool uses AI to answer screenshot-based exam questions automatically.
Just run the container, drop screenshots into a folder, and get answers.

---

## ▶️ Setup

1. **Install Docker**  
   Make sure Docker is installed and running. You can get it from [https://docker.com](https://docker.com).

2. **Copy `docker-compose.yml`** from this repo to your PC  
   [📥 Download docker-compose.yml](https://raw.githubusercontent.com/immoral-null/exam-helper/main/docker-compose.yml)

3. **Create a `.env` file**  
   In the same folder, create a file named `.env` with the following content:
   ```
   GEMINI_API_KEY=your-google-api-key
   ```

   > 💡 You can get your Gemini API key from: https://aistudio.google.com/app/apikey

---

## ▶️ Usage (During Exam)

1. **Run the app**  
   In the folder containing `docker-compose.yml`, run:
   ```
   docker compose up
   ```

2. **Add exam screenshots**  
   Save screenshots of exam questions to `data/screenshots/`.

3. **Get answers**  
   AI-generated answers will be:
   - written to output
   - collected in `data/summary/summary.txt`.

> ✅ That’s it. Good luck with your exam!