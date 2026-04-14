\# DAB111 Group Project



\## Description

This project collects Netflix Movies and TV Shows data, stores it in a SQLite database, and displays it through a Flask web application. Users can view, search, and add records dynamically.



\## Project Structure

\- data\_collection: Contains raw dataset (CSV file)

\- data\_processing: Data cleaning scripts

\- database: SQLite database creation and data storage

\- website: Flask application and HTML templates



\## Features

\- View all data from the database

\- Search records by title

\- Add new records to the database

\- About page with dataset explanation



\## Tools Used

\- Python

\- SQLite (sqlite3)

\- Flask

\- Pandas



\## Data Source

Netflix Movies and TV Shows Dataset from Kaggle:

https://www.kaggle.com/datasets/muqaddasejaz/netflix-movies-and-tv-shows-dataset



\## Variables

\- Title: Name of the movie or TV show

\- Type: Movie or TV Show

\- Country: Country of production

\- Release Year: Year of release

\- Rating: Age rating (e.g., PG, TV-MA)

\- Duration: Length of movie or number of seasons



\## How to Run



1\. Install required packages:

pip install -r requirements.txt



2\. Run the Flask application:



cd website in cmd

python app.py





3\. Open your browser:



http://127.0.0.1:5000/





\## Notes

\- Ensure the database file `netflix.db` is located in the `database/` folder.

\- Templates (`data.html`, `about.html`, `add.html`) must be inside the `website/templates/` folder.



