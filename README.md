## Project Work

Songs Analysis

The purpose of this project is to analyze a given song and extract relevant information from it. In the music industry, understanding the factors that contribute to a song's popularity is crucial for artists, producers, and record labels. 
This project aims to analyze the influence of lyrics and musical features on the popularity of songs. By combining information from the Spotify Dataset, and the Billboard Hot 100 Dataset, and trying the proposed methods as below:
Sentiment Analysis: Analyze song lyrics to determine sentiment and emotional content.
Correlation Analysis: Examine correlations between audio features (from Spotify data) and chart performance data (from Billboard data).


Further analysis is on report.ipynb or final-report.pdf
(https://htmlpreview.github.io/?https://github.com/nish-nm/made-template/blob/main/project/final-report.html)


To replicate project please create an account on data.world and kaggle, you would need api keys for downloading datasets, otherwise you are free to use repective data files in ''/data/'' folder
More instructions to setup data.world and kaggle api keys are at the respective urls: [data.world](https://developer.data.world/docs/dwapi-spec-stoplight/4ad490cb5668e-api-overview) and [kaggle](https://www.kaggle.com/docs/api)

Make sure to use setup Python v3.9.13 or above, use requirements.txt to install all dependencies alternatively you can also use pipenv to setup your Python enviournment.
```bash
project/
├── fetch_data.py       -- fetches data, removes null values and deletes unneccesary files
├── pipeline.sh         -- makes a fetch data pipeline
├── project-plan.md		-- project plan readme file
├── report.ipynb        -- contains analysis
├── test.sh	            -- implements test.py
└── tests.py            -- implements unit tests for fetch_data pipeline 
```

# Project Plan

## Title
<!-- Give your project a short title. -->
Analyzing the Influence of Lyrics and Musical Features on Song Popularity


## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. To what extent do song lyrics, specifically sentiment, and themes, influence a song's chart performance?
2. Are there specific musical features (e.g., tempo, danceability) that are correlated with a song's chart success on the Billboard Hot 100?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
In the music industry, understanding the factors that contribute to a song's popularity is crucial for artists, producers, and record labels. 
This project aims to analyze the influence of lyrics and musical features on the popularity of songs. By combining information from the Spotify Dataset, and the Billboard Hot 100 Dataset, and trying the proposed methods as below:
Sentiment Analysis: Analyze song lyrics to determine sentiment and emotional content.
Correlation Analysis: Examine correlations between audio features (from Spotify data) and chart performance data (from Billboard data).

## Datasources

<!-- Describe each data source you plan to use in a section. Use the prefix "DatasourceX" where X is the id of the data source. -->

### Datasource1: Billboard hot-100 with lyrics
* Metadata URL: [Billboard hot-100 with lyrics](https://data.world/tazwar2700/billboard-hot-100-with-lyrics-and-emotion-mined-scores)
* Data URL: https://data.world/tazwar2700/billboard-hot-100-with-lyrics-and-emotion-mined-scores/workspace/file?filename=Final+processed+dataset.xlsx
* Data Type: XLSX

Excel file provided on [data.world](https://data.world/), contains lyrics and songs in Billboard's top 100 from 1958 to 2020.

### Datasource2: Spotify Dataset 1921-2020
* Metadata URL: [Spotify Dataset 1921-2020](https://www.kaggle.com/datasets/yamaerenay/spotify-dataset-19212020-600k-tracks)
* Data URL1: https://www.kaggle.com/datasets/yamaerenay/spotify-dataset-19212020-600k-tracks/download?datasetVersionNumber=1
* Data Type1: CSV (artists.csv)
* Data Type2: CSV (tracks.csv)
* Data Type3: JSON (dict_artists.json)

The Excel file provided on [kaggle](https://www.kaggle.com/datasets), contains 600k+ songs on the popular streaming platform Spotify and contains information about artists, their tracks, and Musical Features.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Understand and explore dataset [#1][i1]
2. Explore data [#2][i2]
3. Explore results[#3][i2]
4. Add regression model and autoencoder models [#4][i2]
5. Add feature importance and drop the features [#5][i2]
6. Add test file and automate it using github actions [#6][i3]

[i1]: https://github.com/nish-nm/made-template/issues/1
[i2]: https://github.com/nish-nm/made-template/issues/2
[i3]: https://github.com/nish-nm/made-template/issues/3

