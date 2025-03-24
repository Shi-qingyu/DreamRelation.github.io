import json
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load JSON files
with open('benchmark_single.json', 'r') as file:
    data_single = json.load(file)

with open('benchmark_multi.json', 'r') as file:
    data_multi = json.load(file)

# Extract verbs
verbs_single = [item['verb'].replace("_", " ") for item in data_single]
verbs_multi = [item['verb'].replace("_", " ") for item in data_multi]

# Combine the verbs
all_verbs = verbs_single + verbs_multi

# Create a counter for the verbs
verb_counter = Counter(all_verbs)

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color ='white').generate_from_frequencies(verb_counter)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

