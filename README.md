# Vocal Range Identifier

A Python application that records a user's voice, detects the sung pitch, and estimates their vocal range.

## Features

- 🎤 Record audio from a microphone
- 🎵 Detect pitch in real time
- 📊 Estimate the user's vocal range

## Technologies

- Python 
- streamlit
- numpy
- parselmouth
- soundfile

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/maryannliu/vocalRangeIdentifier.git
cd vocalRange
```

### 2. Create a virtual environment

macOS / Linux

```bash
python3 -m venv .venv
```

Windows

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

macOS / Linux

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Project

Make sure your virtual environment is activated and all dependencies are installed.

Start the application with:

```bash
streamlit run app.py
```

Once the server starts, Streamlit will display a local URL similar to:

```
Local URL: http://localhost:8501
```

Open the URL in your web browser to use the application.

## Project Structure

```
vocalRange/
│
├── app.py
├── functions.py
├── requirements.txt
├── vocalRanges.py
├── README.md
├── .gitignore
└── .venv/      (not committed)
```


## Future Improvements
## Future Improvements

- **Web Deployment:** Deploy the application so it can be accessed through the internet without requiring users to clone the repository or install dependencies locally.
- **Improved User Interface:** Enhance the application's design with a more intuitive and visually appealing interface to provide a better user experience.
- **Browser-Based Audio Recording:** Replace local microphone recording with browser-based audio capture, allowing users to record their voice directly from the website.
- **Enhanced Pitch Detection:** Improve the accuracy and robustness of pitch detection, particularly in noisy environments.
- **Expanded Vocal Analysis:** Provide additional insights such as vocal range history, voice type estimation, and visualizations of detected notes.

## License

This project is licensed under the MIT License.
