# 🎧 Model Card: Applied AI Music Recommender System

## 1. Model Name

**Applied AI Music Recommender System**

---

## 2. Intended Use

This system is designed to recommend music based on a user's preferences, including genre, mood, energy level, and acoustic preference. It assumes that the user provides reasonable preference values and that the songs in the local dataset represent the types of music they may enjoy.

This project was developed as part of a classroom assignment to demonstrate Applied AI concepts rather than to compete with commercial music recommendation systems. In addition to recommending songs, this version demonstrates Retrieval-Augmented Generation (RAG), guardrails, logging, and confidence scoring as part of a complete Applied AI workflow.

---

## 3. How the Model Works

The recommender compares each song's features with the user's preferences. It checks whether the genre and mood match and compares how closely the song's energy level matches the user's preferred energy. Songs that match more of the user's preferences receive higher scores.

Before recommendations are generated, the system retrieves relevant music knowledge from a local knowledge base using Retrieval-Augmented Generation (RAG). The system also validates user input before processing requests, records recommendation activity through logging, and calculates a confidence score for every recommendation.

Compared to the original Module 3 project, this Applied AI version adds Retrieval-Augmented Generation (RAG), input validation, logging, and confidence scoring to improve transparency and reliability.

---

## 4. Data

The dataset contains **15 songs** stored in `songs.csv`. The songs include genres such as pop, rock, lofi, jazz, EDM, ambient, folk, blues, hip hop, synthwave, and electronic. They also include different moods such as happy, chill, intense, relaxed, focused, energetic, melancholy, and euphoric.

The project also includes a local knowledge base (`music_knowledge.txt`) that provides additional music guidance for situations such as studying, working out, relaxing, sleeping, and driving.

Although additional songs were added to expand the catalog, the dataset is still relatively small and does not include features such as lyrics, listening history, artist popularity, or user ratings.

---

## 5. Strengths

The recommender performs well when a user's preferences closely match songs within the dataset.

For example:

- High-Energy Pop correctly recommends energetic pop songs.
- Study-focused users receive lofi recommendations along with retrieved study guidance.
- Workout requests retrieve exercise-related music knowledge before recommendations are generated.
- Every recommendation includes an explanation and confidence score to improve transparency.

The combination of recommendation explanations, retrieved knowledge, and confidence scoring makes the system easier to understand than the original project.

---

## 6. Limitations and Biases

Although the recommender performs well for this project, it has several limitations.

- The dataset is relatively small.
- The scoring algorithm relies heavily on genre, mood, and energy.
- The RAG component uses simple keyword matching instead of semantic search.
- Confidence scores are based on recommendation scores and should not be interpreted as prediction probabilities.
- The recommender does not learn from previous user behavior or listening history.
- Users with uncommon music preferences may receive less accurate recommendations because similar songs may not exist in the dataset.

---

## 7. Evaluation

The system was tested using several user profiles, including study, workout, and relaxation scenarios.

Testing focused on verifying that:

- Recommendations matched user preferences.
- Retrieval returned relevant music knowledge.
- Guardrails correctly rejected invalid inputs.
- Recommendation requests were successfully logged.
- Confidence scores were generated for every recommendation.

One interesting discovery was that an earlier version of the retrieval system incorrectly returned study guidance for workout requests. Updating the keyword mapping significantly improved retrieval accuracy and overall recommendation quality.

Overall, all reliability tests passed successfully.

---

## 8. Future Work

If I continued this project, I would:

- Expand the music catalog with hundreds or thousands of songs.
- Replace keyword retrieval with semantic search or vector embeddings.
- Learn user preferences from listening history.
- Include artist similarity, lyrics, and playlists.
- Improve recommendation diversity.
- Replace the rule-based scoring algorithm with a machine learning recommendation model.

---

## 9. Responsible AI Reflection

### Limitations and Biases

The recommender uses a relatively small dataset and a rule-based scoring system, so it cannot capture the full complexity of individual music preferences. It also relies on keyword-based retrieval instead of semantic search, which means some user requests may not retrieve the most relevant music knowledge.

### Potential Misuse

Users might incorrectly assume that the recommender is as personalized as commercial streaming platforms. To reduce this risk, the project clearly documents that recommendations come from a limited local dataset and that confidence scores represent recommendation quality rather than certainty.

### Reliability Testing

During testing, I was surprised by how much the retrieval component improved recommendation explanations. I also learned that even small changes to retrieval rules could significantly affect the quality of the generated recommendations. Logging and guardrails made it much easier to identify and fix unexpected behavior.

### Collaboration with AI

AI served as a development assistant throughout this project. It helped explain programming concepts, debug Python code, improve documentation, and suggest new Applied AI features.

One particularly helpful suggestion was implementing Retrieval-Augmented Generation (RAG) using a local music knowledge base. This significantly improved the explanations provided alongside each recommendation while satisfying the project requirements.

One suggestion that turned out to be flawed was an early implementation of the retrieval function that matched keywords too broadly. During testing, workout-related requests incorrectly returned study-related music guidance. After identifying this issue through testing, I replaced the retrieval logic with a more accurate keyword-to-topic mapping, which resolved the problem.

