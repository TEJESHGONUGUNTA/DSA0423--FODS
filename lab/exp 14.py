import pandas as pd
import matplotlib.pyplot as plt
import string
from collections import Counter

# Customer feedback dataset
feedback = [
    "This product is very good",
    "Good quality and nice design",
    "Price is affordable and good",
    "Service is excellent",
    "Quality product and fast delivery"
]

# Convert list to DataFrame
data = pd.DataFrame(feedback, columns=["feedback"])

# Combine all feedback text
text = " ".join(data["feedback"])

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans("", "", string.punctuation))

# Stop words
stop_words = ["the","and","is","in","to","of","a","for","on","with","this","that","it"]

# Split words
words = text.split()

# Remove stop words
filtered_words = [word for word in words if word not in stop_words]

# Frequency distribution
word_freq = Counter(filtered_words)

# Top N words (input given directly)
N = 5

top_words = word_freq.most_common(N)

print("Top", N, "Frequent Words:")
for word, freq in top_words:
    print(word, ":", freq)

# Prepare data for graph
words = [w[0] for w in top_words]
freqs = [w[1] for w in top_words]

# Plot bar graph
plt.bar(words, freqs)
plt.title("Top Frequent Words in Customer Feedback")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.show()
