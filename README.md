# 🎵 Applied AI Music Recommender System

## Project Summary

### Original Module 3 Project

This project is an extension of my **Module 3: Music Recommender Simulation** project.

The original system implemented a content-based music recommender that compared a user's music preferences with song features such as genre, mood, energy, tempo, valence, danceability, and acousticness. Songs were scored based on how closely they matched the user's taste profile, and the highest-scoring songs were recommended.

### Final Applied AI System

This project expands the original recommender into a more complete Applied AI system by integrating Retrieval-Augmented Generation (RAG), guardrails, logging, and confidence scoring.

Before generating recommendations, the system retrieves relevant music knowledge from a local knowledge base, validates user input, logs every recommendation request, and provides a confidence score for each recommendation. These additions improve the system's reliability, transparency, and explainability.

## How The System Works

My music recommender uses a content-based approach, meaning it recommends songs by comparing each song's features to a user's taste profile rather than comparing the user to other listeners. While platforms like Spotify and YouTube Music combine collaborative filtering with content-based filtering, my recommender focuses only on song features such as genre, mood, energy, tempo, valence, danceability, and acousticness.

Each `Song` stores information like its title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness.
 
The `UserProfile` stores the user's preferred genre, mood, and target values for the numerical features. The recommender computes a weighted score for every song by comparing the song's features with the user's preferences. Genre and mood matches receive the highest weight, while numerical features such as energy, danceability, valence, tempo, and acousticness contribute additional points based on how closely they match the user's preferred values. The songs are then ranked from highest to lowest score, and the top recommendations are returned.


## New AI Features

This Applied AI version extends the original recommender with several additional AI capabilities.

### Retrieval-Augmented Generation (RAG)

Before recommending songs, the system searches a local knowledge base (`music_knowledge.txt`) for relevant music guidance based on the user's request. The retrieved context is displayed alongside every recommendation so users understand why certain music may fit their situation.

### Guardrails

The system validates user requests before generating recommendations. Empty requests, missing preferences, and invalid values are detected before recommendation generation to improve reliability.

### Logging

Every recommendation request is automatically written to `logs/application.log`, including:

- User request
- User preferences
- Retrieved context

This provides traceability for debugging and evaluation.

### Confidence Scoring

Each recommendation includes a confidence percentage derived from its recommendation score. This provides users with an estimate of how strongly the system believes a recommendation matches their preferences.


### Algorithm Recipe

Each song is scored out of 100 points based on how well it matches the user's preferences.

- Genre match: **25 points**
- Mood match: **20 points**
- Energy similarity: **up to 15 points**
- Danceability similarity: **up to 15 points**
- Valence similarity: **up to 10 points**
- Tempo similarity: **up to 10 points**
- Acousticness similarity: **up to 5 points**

Genre and mood earn full points when they match. The numerical features earn more points the closer they are to the user's preferred values. Once every song is scored, the recommender ranks them from highest to lowest and recommends the top matches.

## Data Flow

Input

- User request
- User preferences
- Song database
- Local music knowledge base

Processing

1. Validate user input.
2. Retrieve relevant music knowledge (RAG).
3. Score every song using the recommendation algorithm.
4. Rank recommendations.
5. Calculate confidence scores.
6. Log the recommendation request.

Output

- Top recommended songs
- Recommendation explanations
- Retrieved music knowledge
- Confidence scores

### Potential Bias

This recommender puts the most weight on genre and mood, so it may recommend similar types of songs over and over. Because the dataset is small, it also has limited variety and may miss songs that fit the user's taste in other ways.

---

## Architecture Overview

The system is organized into several components:

- **User Input** – Collects the user's music request and preferences.
- **Guardrails** – Validates the request and preference values before processing.
- **Retriever (RAG)** – Searches a local music knowledge base for relevant guidance.
- **Recommendation Engine** – Scores every song based on similarity to the user's preferences.
- **Confidence Scoring** – Converts recommendation scores into confidence percentages.
- **Logger** – Records recommendation requests and retrieved context for evaluation.
- **Output** – Displays retrieved knowledge, ranked recommendations, explanations, and confidence scores.

The complete system architecture is shown in `diagrams/architecture.mmd`.

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
Loaded songs: 15

=== Study Session ===
User request: I need music for studying and concentration.
Preferences: {'genre': 'lofi', 'mood': 'focused', 'energy': 0.4, 'likes_acoustic': True}

Retrieved music knowledge:
Lofi music is commonly recommended for studying because it minimizes distractions and maintains a calm atmosphere. Classical music is often effective for reading, writing, and concentration.

Top recommendations:
1. Focus Flow by LoRoom
   Score: 6.28
   Confidence: 97%
   Because: genre match (+2.0), mood match (+1.5), energy similarity (+2.00), acoustic preference (+0.78)
   Retrieved context used: Lofi music is commonly recommended for studying because it minimizes distractions and maintains a calm atmosphere. Classical music is often effective for reading, writing, and concentration.

2. Library Rain by Paper Lanterns
   Score: 4.76
   Confidence: 73%
   Because: genre match (+2.0), energy similarity (+1.90), acoustic preference (+0.86)
   Retrieved context used: Lofi music is commonly recommended for studying because it minimizes distractions and maintains a calm atmosphere. Classical music is often effective for reading, writing, and concentration.

3. Midnight Coding by LoRoom
   Score: 4.67
   Confidence: 72%
   Because: genre match (+2.0), energy similarity (+1.96), acoustic preference (+0.71)
   Retrieved context used: Lofi music is commonly recommended for studying because it minimizes distractions and maintains a calm atmosphere. Classical music is often effective for reading, writing, and concentration.

4. Coffee Shop Stories by Slow Stereo
   Score: 2.83
   Confidence: 44%
   Because: energy similarity (+1.94), acoustic preference (+0.89)
   Retrieved context used: Lofi music is commonly recommended for studying because it minimizes distractions and maintains a calm atmosphere. Classical music is often effective for reading, writing, and concentration.

5. Grandma's Porch by Willow Creek
   Score: 2.74
   Confidence: 42%
   Because: energy similarity (+1.80), acoustic preference (+0.94)
   Retrieved context used: Lofi music is commonly recommended for studying because it minimizes distractions and maintains a calm atmosphere. Classical music is often effective for reading, writing, and concentration.

=== Workout Session ===
User request: I need energetic music for a workout.
Preferences: {'genre': 'pop', 'mood': 'intense', 'energy': 0.9, 'likes_acoustic': False}

Retrieved music knowledge:
High-energy pop music can improve motivation during exercise. Rock music with high energy is frequently used for strength training and running.

Top recommendations:
1. Gym Hero by Max Pulse
   Score: 5.44
   Confidence: 84%
   Because: genre match (+2.0), mood match (+1.5), energy similarity (+1.94)
   Retrieved context used: High-energy pop music can improve motivation during exercise. Rock music with high energy is frequently used for strength training and running.

2. Sunrise City by Neon Echo
   Score: 3.84
   Confidence: 59%
   Because: genre match (+2.0), energy similarity (+1.84)
   Retrieved context used: High-energy pop music can improve motivation during exercise. Rock music with high energy is frequently used for strength training and running.

3. Storm Runner by Voltline
   Score: 3.48
   Confidence: 54%
   Because: mood match (+1.5), energy similarity (+1.98)
   Retrieved context used: High-energy pop music can improve motivation during exercise. Rock music with high energy is frequently used for strength training and running.

4. Rooftop Lights by Indigo Parade
   Score: 2.72
   Confidence: 42%
   Because: related genre (+1.0), energy similarity (+1.72)
   Retrieved context used: High-energy pop music can improve motivation during exercise. Rock music with high energy is frequently used for strength training and running.

5. Desert Mirage by Sand Vega
   Score: 1.96
   Confidence: 30%
   Because: energy similarity (+1.96)
   Retrieved context used: High-energy pop music can improve motivation during exercise. Rock music with high energy is frequently used for strength training and running.

```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Reliability Testing

The system includes several reliability improvements.

| Test | Result |
|------|--------|
| Valid recommendation request | Pass |
| Empty request | Pass |
| Missing preferences | Pass |
| RAG retrieval | Pass |
| Logging | Pass |
| Confidence scoring | Pass |

- 6 of 6 reliability checks passed successfully.
- Guardrails correctly rejected invalid inputs.
- Retrieval successfully returned relevant music knowledge for each supported query.
- Confidence scores were generated for every recommendation.
- Recommendation requests and retrieved context were successfully logged.

## Design Decisions

Several design decisions were made while extending the original project.

- A local text knowledge base was used instead of an online API to ensure reproducibility.
- Rule-based retrieval was selected because it is simple, transparent, and easy to explain.
- Confidence scores improve explainability for users.
- Logging improves debugging and evaluation.
- Guardrails prevent invalid inputs before recommendation generation.

## Experiments You Tried

Several experiments were performed while improving the recommender.

- Added Retrieval-Augmented Generation (RAG) using a local music knowledge base. This allowed recommendations to include relevant music guidance based on the user's request.

- Added guardrails to reject empty requests and invalid user preferences before recommendations were generated.

- Added confidence scoring so users can better understand how strongly each recommendation matches their preferences.

- Tested different user profiles including study, workout, and relaxation scenarios. Each profile produced different recommendations and retrieved different music knowledge.

---

## Limitations and Risks

Although the recommender performs well for this project, it has several limitations.

- It only uses a small local music catalog.
- The RAG component relies on a simple keyword-based retrieval method rather than semantic search.
- Confidence scores are based on the recommendation algorithm and do not represent true prediction probabilities.
- The recommender does not learn from user feedback over time.
- The system may over-recommend songs with similar genres or moods because those features receive the highest weights.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

This project demonstrated how a simple AI recommender can be extended into a more complete Applied AI system. Adding retrieval, validation, logging, and confidence scoring made the recommender more transparent, reliable, and easier to evaluate. The project reinforced the importance of building AI systems that are not only accurate, but also explainable and reproducible. This project also showed me how retrieval, validation, logging, and confidence scoring can make AI systems more trustworthy and easier to debug.

## Portfolio Reflection

This project demonstrates my ability to build an AI application that goes beyond a basic recommendation algorithm. I extended a content-based music recommender by integrating Retrieval-Augmented Generation (RAG), input validation through guardrails, logging, confidence scoring, testing, and documentation. Throughout the project, I focused on making the system transparent, reliable, and easy to explain. It reflects my approach as an AI engineer: building practical AI systems that are accurate, reproducible, and designed with responsible AI principles in mind.

## GitHub Repository

https://github.com/anoshasharif/applied-ai-music-recommender


