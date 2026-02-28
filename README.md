# 🎬 Bollywood AI Movie Recommender

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3%2B-orange)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

## ✨ Features

- **🎭 Genre-Based Filtering**: Browse movies by your favorite genres
- **🤖 AI-Powered Recommendations**: Get personalized suggestions using TF-IDF and cosine similarity
- **🎨 Beautiful UI**: Modern, responsive interface with movie posters
- **⭐ Trending Movies**: Discover top-rated movies in each genre
- **🔍 Smart Search**: Find movies instantly with intelligent filtering
- **📱 Mobile-Friendly**: Works seamlessly on all devices

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Machine Learning**: Scikit-learn (TF-IDF Vectorizer, Cosine Similarity)
- **Data Processing**: Pandas
- **API**: TMDB (The Movie Database) for movie posters
- **Model Persistence**: Joblib

## 📁 Project Structure

```
Recommendation System/
├── app.py                 # Main Streamlit application
├── train_model.py         # Model training script
├── requirements.txt       # Python dependencies
├── data/
│   └── bollywood_movies.csv # Bollywood movies dataset
├── model/
│   └── bollywood_model.pkl # Trained recommendation model
└── README.md             # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/bollywood-ai-recommender.git
   cd bollywood-ai-recommender
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the model**
   ```bash
   python train_model.py
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:8501`

## 📊 How It Works

### 1. Data Processing
- Loads Bollywood movies dataset with genres, directors, and cast information
- Cleans and preprocesses text data
- Combines features for better similarity matching

### 2. Feature Engineering
- Uses **TF-IDF Vectorizer** to convert text features into numerical vectors
- Creates a combined feature matrix from genre, director, and cast information

### 3. Similarity Calculation
- Computes **cosine similarity** between movies
- Generates a similarity matrix for all movie pairs

### 4. Recommendation Engine
- Given a selected movie, finds the most similar movies
- Ranks recommendations by similarity score
- Filters by genre for more relevant results

### 5. User Interface
- Interactive Streamlit app with genre filtering
- Displays movie posters from TMDB API
- Shows similarity percentages for transparency

## 🎯 Usage

1. **Select a Genre**: Choose your preferred movie genre from the dropdown
2. **Browse Trending**: View top-rated movies in the selected genre
3. **Pick a Movie**: Select a movie you enjoyed from the filtered list
4. **Get Recommendations**: Click "Recommend" to discover similar movies
5. **Adjust Quantity**: Use the slider to control the number of recommendations

## 📈 Performance

- **Model Training Time**: ~30 seconds for 1000+ movies
- **Response Time**: <1 second for recommendations
- **Accuracy**: Based on content similarity (genre, director, cast)
- **Scalability**: Can handle thousands of movies efficiently

## 🔧 Configuration

### TMDB API Key

The app uses TMDB API to fetch movie posters. To use your own API key:

1. Sign up at [TMDB](https://www.themoviedb.org/)
2. Get your API key
3. Replace the API key in `app.py` (line 54):

```python
TMDB_API_KEY = "your_api_key_here"
```

### Custom Dataset

To use your own dataset:

1. Place your CSV file in the `data/` directory
2. Ensure it has columns: `Movie Name`, `Genre`, `Director`, `Cast`
3. Update the filename in `train_model.py` (line 9)
4. Retrain the model

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 for Python code style
- Add comments for complex logic
- Test your changes thoroughly
- Update documentation as needed

## 🐛 Troubleshooting

### Common Issues

**Model not found error**
```bash
# Solution: Train the model first
python train_model.py
```

**API key issues**
- Ensure your TMDB API key is valid
- Check your internet connection
- Verify API rate limits

**Streamlit not running**
```bash
# Solution: Install/update streamlit
pip install --upgrade streamlit
```

**Memory issues with large datasets**
- Reduce dataset size for testing
- Use streaming for very large datasets
- Consider using more efficient data structures

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [TMDB](https://www.themoviedb.org/) for movie poster API
- [Streamlit](https://streamlit.io/) for the amazing web app framework
- [Scikit-learn](https://scikit-learn.org/) for machine learning tools
- The Bollywood movie community for the dataset

## 📞 Contact

- **Author**: Boomi Rao
- **Email**: boomirao0720@gmail.com.com
- **LinkedIn**: https://www.linkedin.com/in/boomirao20/
---

<div align="center">

**⭐ If you like this project, please give it a star!**

Made with ❤️ by Boomi Rao | AI/ML Project

</div>
