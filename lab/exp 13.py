# Program to find word frequency in customer reviews

from collections import Counter

# Sample customer reviews
reviews = [
    "This product is very good",
    "Good quality and good price",
    "Very useful product and good design",
    "Quality of the product is good"
]

# Convert reviews into a single string
text = " ".join(reviews)

# Convert text to lowercase
text = text.lower()

# Split text into words
words = text.split()

# Calculate word frequency
word_frequency = Counter(words)

# Display frequency distribution
print("Word Frequency Distribution:")
for word, count in word_frequency.items():
    print(word, ":", count)
