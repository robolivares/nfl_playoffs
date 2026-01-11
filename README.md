# 🏈 NFL Playoff Challenge 2026

A dynamic, real-time playoff bracket and sweepstakes application built with Firebase. This pool features automated reseeding logic and a Fibonacci-based scoring system.

## 🚀 Features
* **Interactive Bracket Picker:** Automated NFL reseeding logic for the Divisional round.
* **Fibonacci Scoring:** Points awarded per round: **3, 5, 8, 13**.
* **Live Leaderboard:** Real-time standings updated via a Python-based Cloud Function.
* **Admin Control Panel:** Secured interface to update official game results and revert errors.
* **Transparency Mode:** View any participant's full bracket selection once the games begin.

---

## 🛠 Tech Stack
* **Frontend:** HTML5, Tailwind CSS, JavaScript (ES6 Modules).
* **Database:** Google Firestore.
* **Hosting:** Firebase Hosting.
* **Backend Logic:** Python (Cloud Functions) for leaderboard calculations.

---

## 💻 Local Setup

### 1. Prerequisites
* [Node.js](https://nodejs.org/) installed.
* Firebase CLI: `npm install -g firebase-tools`.
* A Firebase Project created in the [Firebase Console](https://console.firebase.google.com/).

### 2. Configuration
Create a `public/app-config.js` file with your Firebase credentials. **Note:** This file is ignored by Git for security.

```javascript
export const appConfig = {
    TOURNAMENT_ID: "nfl_playoffs_2026",
    TOURNAMENT_NAME: "NFL Playoff Sweepstakes",
    VIEWER_MODE_ENABLED: false // Set to true once games start
};

export const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT.firebaseapp.com",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_PROJECT.appspot.com",
    messagingSenderId: "YOUR_ID",
    appId: "YOUR_APP_ID"
};
```
## 📦 Deployment to Firebase
Follow these steps to push your local changes to the live production site:


### 1. Login & Initialize

```bash
# Log in to your Google account
firebase login

# Initialize the project (required only for the first setup)
firebase init
```

* Select Hosting.
* Choose Use an existing project.
* Set the public directory to public.
* Configure as a single-page app: No.

### 2. Deploying Changes

Run these commands every time you update the code or the tournament_data.json file:

```bash
# Deploy only the website frontend
firebase deploy --only hosting

# Deploy everything (including Cloud Functions)
firebase deploy
```

