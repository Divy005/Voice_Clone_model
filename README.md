# AI Voice Clone

🎤 **Bring any voice to life with text-to-speech.**

A powerful voice cloning system that can replicate any person's voice and generate speech from text input. Built with YourTTS model and FastAPI, packaged with Docker for easy deployment.

![Voice Clone Interface](screenshot.png)

## ✨ Features

- 🎯 **Voice Cloning**: Clone any voice with just a short audio sample
- 🔤 **Text-to-Speech**: Convert any text to speech in the cloned voice
- 🚀 **FastAPI Backend**: High-performance REST API
- 🐳 **Docker Ready**: Containerized for easy deployment
- 📱 **Web Interface**: Clean and intuitive user interface
- 🎵 **High Quality**: Generates clear .wav audio files

## 🛠️ Tech Stack

- **AI Model**: YourTTS (Your Text-To-Speech)
- **Backend**: FastAPI
- **Frontend**: HTML/CSS/JavaScript
- **Audio Processing**: PyTorch, Torchaudio, SciPy
- **Deployment**: Docker

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Docker (optional)

### Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Divy005/voice-cloning-api.git
   cd voice-cloning-api
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8080 --reload
   ```

4. **Open your browser**
   Navigate to `http://localhost:8080`

### Docker Installation

1. **Build the Docker image**
   ```bash
   docker build -t voice-clone-api .
   ```

2. **Run the container**
   ```bash
   docker run -p 8080:8080 voice-clone-api
   ```

## 📖 How to Use

1. **Enter Text**: Type the text you want to convert to speech
2. **Upload Voice Sample**: Upload a .wav file of the voice you want to clone
3. **Generate Audio**: Click "Generate Audio" to create the cloned voice
4. **Download**: Get your generated .wav file


## 🔌 API Endpoints

### `GET /`
Health check endpoint

### `POST /synthesize/`
Generate cloned voice audio
- **Parameters**:
  - `text` (string): Text to synthesize
  - `voice_file` (file): Voice sample (.wav format)
- **Returns**: Generated audio file (.wav)

## 🎯 Applications

- 🤖 **Virtual Assistants**: Custom voice personalities
- 📚 **Audiobooks**: Automated narration
- ♿ **Accessibility**: Tools for speech difficulties
- 🎬 **Entertainment**: Voice dubbing and content creation
- 🎓 **Education**: Personalized learning content

## ⚡ Performance

- **Processing Time**: ~5-15 seconds per request
- **Audio Quality**: High-fidelity .wav output
- **Supported Formats**: WAV input/output
- **Concurrent Users**: Supports multiple simultaneous requests

## 🔧 Configuration

### Environment Variables
```bash
PORT=8080                # Server port
MAX_FILE_SIZE=10MB       # Maximum upload size
MODEL_PATH=./models/     # Model directory
OUTPUT_PATH=./outputs/   # Output directory
```

### Audio Requirements
- **Format**: WAV
- **Sample Rate**: 22050 Hz recommended
- **Duration**: 5-30 seconds for best results
- **Quality**: Clear, noise-free recordings

## 🚧 Limitations

- Voice quality depends on input sample clarity
- Processing time varies with text length
- Requires good quality voice samples for best results
- Currently supports single-language processing

## 🔮 Future Enhancements

- [ ] Real-time voice streaming
- [ ] Multiple language support
- [ ] Voice emotion control
- [ ] Batch processing capabilities
- [ ] User account management
- [ ] Cloud storage integration

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Divy Dobariya**
- GitHub: [@Divy005](https://github.com/Divy005)
- LinkedIn: [Divy Dobariya](https://linkedin.com/in/divy-dobariya)
- Email: divydobariya11@gmail.com

## 🙏 Acknowledgments

- YourTTS team for the amazing voice cloning model
- FastAPI community for the excellent framework
- PyTorch team for the deep learning framework

---

⭐ **If you found this project helpful, please give it a star!** ⭐
