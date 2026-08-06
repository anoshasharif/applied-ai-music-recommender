import csv
from dataclasses import asdict, dataclass
from typing import Dict, List, Tuple


@dataclass
class Song:
    """Represents a song and its musical attributes."""

    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """Represents a user's music preferences."""

    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """Provides object-oriented song recommendations."""

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Returns the top matching songs for a user."""

        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }

        ranked_songs = sorted(
            self.songs,
            key=lambda song: score_song(user_prefs, asdict(song))[0],
            reverse=True,
        )

        return ranked_songs[:k]

    def explain_recommendation(
        self, user: UserProfile, song: Song
    ) -> str:
        """Explains why a song matches the user's preferences."""

        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }

        _, reasons = score_song(user_prefs, asdict(song))
        return ", ".join(reasons)


def load_songs(csv_path: str) -> List[Dict]:
    """Loads song records from a CSV file."""

    songs = []

    with open(csv_path, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])

            songs.append(row)

    return songs


def score_song(
    user_prefs: Dict, song: Dict
) -> Tuple[float, List[str]]:
    """Scores one song and returns its recommendation reasons."""

    score = 0.0
    reasons = []

    preferred_genre = user_prefs["genre"].strip().lower()
    song_genre = song["genre"].strip().lower()

    if preferred_genre == song_genre:
        score += 2.0
        reasons.append("genre match (+2.0)")
    elif preferred_genre in song_genre:
        score += 1.0
        reasons.append("related genre (+1.0)")

    preferred_mood = user_prefs["mood"].strip().lower()
    song_mood = song["mood"].strip().lower()

    if preferred_mood == song_mood:
        score += 1.5
        reasons.append("mood match (+1.5)")

    target_energy = float(user_prefs["energy"])
    song_energy = float(song["energy"])

    energy_difference = abs(target_energy - song_energy)
    energy_score = max(0.0, 1.0 - energy_difference) * 2.0

    score += energy_score
    reasons.append(f"energy similarity (+{energy_score:.2f})")

    if user_prefs.get("likes_acoustic") is True:
        acoustic_score = float(song["acousticness"])
        score += acoustic_score
        reasons.append(f"acoustic preference (+{acoustic_score:.2f})")

    return round(score, 2), reasons

def calculate_confidence(score: float, max_score: float = 6.5) -> int:
    """
    Converts a recommendation score into a confidence percentage.

    The current scoring system has an approximate maximum score of 6.5.
    The result is capped between 0 and 100.
    """

    if max_score <= 0:
        return 0

    confidence = round((score / max_score) * 100)

    return max(0, min(confidence, 100))


def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5,
) -> List[Tuple[Dict, float, str]]:
    """Scores all songs and returns the top-ranked recommendations."""

    ranked_results = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        ranked_results.append((song, score, explanation))

    return sorted(
        ranked_results,
        key=lambda result: result[1],
        reverse=True,
    )[:k]
