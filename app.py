import pickle
import pandas as pd
import streamlit as st


data = pickle.load(open('movies_dict.pkl', mode='rb'))
data = pd.DataFrame(data)

similarity = pickle.load(open('similarity.pkl', mode='rb'))


def recommend(movie):
    recommended_movies = []
    movie_index = data[data['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    for i in movie_list:
        recommended_movies.append(data.iloc[i[0]].title)

    return recommended_movies

st.markdown(
    """
    <style>
        .stApp {
            background-image: url('https://analyticsindiamag.com/wp-content/uploads/2019/05/apps.55787.9007199266246365.687a10a8-4c4a-4a47-8ec5-a95f70d8852d.jpg');
            background-size: cover;
            background-position: center;
            height: 100vh;
        }
        .recommendation-title {
            color: white;
            font-size: 2em; /* Increase font size */
            font-weight: bold;
            margin-bottom: 10px; /* Add space between title and list */
        }
        .recommendation-movie {
            font-size: 1.2em;
            color: white; /* White text for movie names */
            margin-top: 5px;
        }
    </style>
    """, unsafe_allow_html=True
)

st.image("https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg", width=200, use_container_width=True)

st.title(':red[Movie Recommendation System]:pushpin:')

selected_movies = st.selectbox('Choose your movie:', data['title'].values)

bt = st.button('Recommend')

if bt:
    top_5_movies = recommend(selected_movies)
    st.markdown('<div class="recommendation-box">', unsafe_allow_html=True)
    st.markdown('<div class="recommendation-title">Top 5 Recommendations:</div>', unsafe_allow_html=True)
    for movie in top_5_movies:
        st.markdown(f'<div class="recommendation-movie">{movie}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True) 
