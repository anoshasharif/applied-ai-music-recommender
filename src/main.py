"""
Command-line runner for the Applied AI Music Recommender.
"""

from .recommender import (calculate_confidence, load_songs, recommend_songs,)
from .retriever import MusicKnowledgeRetriever
from .guardrails import InputValidator
from .logger import log_recommendation


def print_recommendations(
    profile_name,
    user_request,
    user_prefs,
    songs,
    retriever,
):
    """Prints retrieved guidance and top recommendations."""

    # Validate user input before generating recommendations
    InputValidator.validate_request(user_request)
    InputValidator.validate_preferences(user_prefs)

    retrieved_context = retriever.retrieve(user_request)

    log_recommendation(user_request,user_prefs,retrieved_context,)

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print(f"\n=== {profile_name} ===")
    print(f"User request: {user_request}")
    print(f"Preferences: {user_prefs}")

    print("\nRetrieved music knowledge:")
    print(retrieved_context)

    print("\nTop recommendations:")

    for position, (song, score, explanation) in enumerate(
        recommendations,
        start=1,
    ):
        confidence = calculate_confidence(score)

        print(f"{position}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f}")
        print(f"   Confidence: {confidence}%")
        print(f"   Because: {explanation}")
        print(f"   Retrieved context used: {retrieved_context}")
        print()
        


def main() -> None:
    songs = load_songs("data/songs.csv")
    retriever = MusicKnowledgeRetriever("data/music_knowledge.txt")

    print(f"Loaded songs: {len(songs)}")

    profiles = {
        "Study Session": {
            "request": "I need music for studying and concentration.",
            "preferences": {
                "genre": "lofi",
                "mood": "focused",
                "energy": 0.4,
                "likes_acoustic": True,
            },
        },
        "Workout Session": {
            "request": "I need energetic music for a workout.",
            "preferences": {
                "genre": "pop",
                "mood": "intense",
                "energy": 0.9,
                "likes_acoustic": False,
            },
        },
        "Relaxing Evening": {
            "request": "I want relaxing music after work.",
            "preferences": {
                "genre": "jazz",
                "mood": "relaxed",
                "energy": 0.35,
                "likes_acoustic": True,
            },
        },
    }

    for profile_name, profile_data in profiles.items():
        print_recommendations(
            profile_name=profile_name,
            user_request=profile_data["request"],
            user_prefs=profile_data["preferences"],
            songs=songs,
            retriever=retriever,
        )


if __name__ == "__main__":
    main()
