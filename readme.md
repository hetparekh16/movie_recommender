# Movie Recommender System v1.0

A Streamlit-powered movie and TV series recommendation system leveraging TMDB API for content discovery.

## 🎯 Features

- **Content Discovery**: Browse through curated movies and TV series
- **Smart Recommendations**: Get personalized content suggestions
- **Visual Interface**: Clean card-based UI with movie posters
- **Multi-Language Support**: Support for different language content
- **Content Filtering**: Filter by year

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/movie_recommender.git
cd movie_recommender

# Install dependencies
uv sync

# Set up environment variables
touch "API_KEY=your_tmdb_api_key_here" > .env

# Run python files
uv python run sry/recommender/data_prep/retriever.py
uv python run sry/recommender/data_prep/transform_load.py
uv python run sry/recommender/main.py

# Run the application
streamlit run src/recommender/st_app.py
```

## 📁 Project Structure

```
movie_recommender/
├── data/
│   ├── processed_data/
│   │   ├── movies.csv
│   │   └── series.csv
│   └── raw_data/
├── src/
│   └── recommender/
│       ├── __init__.py
│       ├── config.py
│       ├── main.py
│       ├── st_app.py
│       └── data_prep/
├── README.md
└── pyproject.toml
```


## 🎬 Usage Guide

1. **Browse Content**
   - Navigate using the radio buttons at the top
   - View movie/series cards with posters and titles
   - Scroll through paginated results

2. **Get Recommendations**
   - Select "Watch something similar"
   - Enter a movie/series title
   - View similar content recommendations

3. **Filter Content**
   - Use sidebar filters for year ranges
   - Toggle adult content visibility
   - Select specific genres

## 🛠️ Development

Built with:
- Python 3.12+
- Streamlit
- Pandas
- Sentence Transformers
- TMDB API


## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 🚀 Movie Recommender System v1.0 is Live! 🎉

We’re excited to launch the first version of our Movie Recommender System, powered by Streamlit and the TMDB API.

🔥 v1.0 Highlights:
✅ API Fetching: Seamless data retrieval from TMDB API.
✅ Streamlit UI: Clean, responsive, and easy-to-use interface.
✅ Recommendation Logic: Similarity-based content suggestions for personalized discovery.

## But we’re not stopping here! v2.0 is on the way! 🚀

🔮 Coming Soon in v2.0:
⚡ Parallel Batch Fetching: Faster and more efficient data retrieval.
🧠 ChromaDB Integration: Leveraging a vector database for better recommendations.
🔍 Enhanced Search & Retrieval: Smarter content discovery with real-time suggestions.

Stay tuned for a smarter, faster, and more scalable recommendation experience! 🎬✨