import pandas as pd 

# load data
items = pd.read_csv('../data/jester_items.csv')
ratings = pd.read_csv('../data/jester_ratings.csv')
ratings = ratings.drop(columns=['userId'])

# create average ratings
average_ratings = ratings.groupby('jokeId').mean()

# clean joke text
def clean_text(text):
    insert_space = [
    '!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '.', '/', ':', ';',
    '<', '>', '?', '@', '[', '\\', ']', '^', '_', '{', '|', '}', '~', "\n", '\t', '-'
    ]

    insert_none = [
        "'" 
    ]

    text = text.strip()
    text = text.lower()
    for item in insert_none:
        text = text.replace(item, "")
        
    for item in insert_space:
        text = text.replace(item, " ")

    return text

cleaned_jokes = items
cleaned_jokes['jokeText'] = cleaned_jokes['jokeText'].apply(lambda text : clean_text(text))

# combine average ratings and cleaned joke text
combined = pd.merge(average_ratings, cleaned_jokes, on='jokeId')

# Normalize the rating column to the 0-10 scale
min_value = combined['rating'].min()
max_value = combined['rating'].max()
combined['rank'] = 10 * (combined['rating'] - min_value) / (max_value - min_value)

# drop uneeded columns
combined = combined.drop(columns=['rating', 'jokeId'])

print(combined)
combined.to_csv('../data/jester_combined.csv')