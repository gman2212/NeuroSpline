# NeuroSpline
SplineGen is a Python-based tool for generating and visualizing optimal spline paths using AI models like LLAMA and DeepSeek via the Ollama API(You can use any Model that is compatible with Ollama). It reads environment data, processes JSON outputs, and provides visualization options in Matplotlib and Unreal Engine.


1. Clone the repository
   ```commandline
   git clone https://github.com/YOUR_USERNAME/SplineGen.git
   cd SplineGen
   ```
2. Install Dependencies
   ```commandline
   pip install ollama
   pip install requests
   pip install ollama
   ```
3. Start Ollama Server
   ```commandline
   ollama serve
   ```
   If the models aren't installed, pull them:
   ```commandline
   ollama pull llama3
   ollama pull deepseek
   ```
4. Run the AI Path Generator
   ```commandline
   python pathfinder.py
   ```
