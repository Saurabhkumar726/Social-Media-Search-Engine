# Social Media Integrated Search Engine

A unified web-based application that allows users to perform keyword-based searches across multiple platforms and view the aggregated results in one place. This tool is designed using Python (Flask) for backend processing and Beautiful Soup for web scraping, with a responsive user interface built using HTML and CSS.

## 🔍 Features

- 🔎 **Search Functionality**: Allows users to input keywords and search across supported platforms.
- 🌐 **Web Scraping**: Uses Beautiful Soup to fetch live data from external websites based on the user's query.
- 🖥️ **Responsive UI**: Clean and user-friendly design with HTML, CSS, and multimedia content (images, videos).
- ⚙️ **Flask Backend**: Lightweight and scalable server-side processing using Python's Flask framework.

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: Python (Flask)
- **Scraping**: Beautiful Soup
- **Others**: Requests, Bootstrap (optional)

## 📸 Screenshots

> Add screenshots of your UI here if available. Example:
> ![Homepage](screenshots/homepage.png)
> ![Search Results](screenshots/results.png)

## 🚀 Getting Started

### Prerequisites

Make sure you have Python installed. Install required packages using:

```bash
pip install flask beautifulsoup4 requests

📁 Project Structure
├── app.py               # Main Flask app
├── templates/
│   └── index.html       # UI for search and results
├── static/
│   └── style.css        # Styling for the UI
├── images/              # Optional: images used in the app
└── README.md            # Project documentation

Run the Project
1.Clone the repository:git clone https://github.com/yourusername/social-media-search-engine.git
  cd social-media-search-engine
2.Run the Flask application: python app.py
3.Open your browser and go to: http://localhost:5000

