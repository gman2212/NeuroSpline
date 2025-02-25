# NeuroSpline
SplineGen is a Python-based tool for generating and visualizing optimal spline paths using AI models like LLAMA and DeepSeek via the Ollama API(You can use any Model that is compatible with Ollama). It reads environment data, processes JSON outputs, and provides visualization options in Matplotlib and Unreal Engine.

## Features
- **Generates and evaluates optimal paths** based on obstacle avoidance and smoothness.
- **Uses Ollama API** to query models for optimal path generation.
- **Evaluates paths** based on:
  -  **Consistency** (Does it reliably avoid obstacles?)
  -  **Accuracy** (Does it follow constraints from the input JSON?)
  -  **Output Structure** (Is the JSON valid?)
  -  **Processing Time** (How fast does it generate a response?)
  -  **Z-axis Handling** (Is Z-axis used correctly?)

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
5. Run Evaluation
    ```commandline
    python metrics.py
    ```
    This script evaluates the generated path and outputs `evaluation_results.json`

6. Visualize the Path
   Matplotlib (2D Visualization)
   ```commandline
   python matplot.py
   ```
   ![Plotfig](https://github.com/user-attachments/assets/03837d76-c74d-41b5-9696-5c024b853d97)


   The Matplot visualization will look like this.


## License
This project is open-source under the MIT License.
