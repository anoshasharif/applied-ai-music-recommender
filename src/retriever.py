from pathlib import Path


class MusicKnowledgeRetriever:
    """Retrieves relevant music guidance from a local knowledge base."""

    def __init__(self, knowledge_file: str = "data/music_knowledge.txt"):
        self.knowledge_file = Path(knowledge_file)

        if not self.knowledge_file.exists():
            raise FileNotFoundError(
                f"Knowledge file not found: {self.knowledge_file}"
            )

        self.sections = self._load_sections()

    def _load_sections(self) -> dict[str, str]:
        """Loads headings and their related knowledge from the text file."""

        sections: dict[str, list[str]] = {}
        current_heading = "General"

        for line in self.knowledge_file.read_text(
            encoding="utf-8"
        ).splitlines():
            line = line.strip()

            if not line:
                continue

            if line.startswith("#"):
                current_heading = line.lstrip("#").strip()
                sections[current_heading] = []
            else:
                sections.setdefault(current_heading, []).append(line)

        return {
            heading: " ".join(content)
            for heading, content in sections.items()
        }

    def retrieve(self, query: str) -> str:
        """Returns the most relevant knowledge section for a query."""

        if not query or not query.strip():
            return "No additional music knowledge was found."

        query = query.lower()

        keyword_map = {
            "study": "Study",
            "studying": "Study",
            "concentration": "Study",
            "workout": "Workout",
            "exercise": "Workout",
            "gym": "Workout",
            "relax": "Relaxation",
            "relaxing": "Relaxation",
            "stress": "Relaxation",
            "happy": "Happy Mood",
            "sad": "Sad Mood",
            "driving": "Driving",
            "drive": "Driving",
            "sleep": "Sleep",
        }

        for keyword, heading in keyword_map.items():
            if keyword in query:
                return self.sections.get(
                    heading,
                    "No additional music knowledge was found."
                )

        return "No additional music knowledge was found."