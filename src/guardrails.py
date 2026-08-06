class InputValidator:
    """Validates user input before recommendations are generated."""

    @staticmethod
    def validate_request(request: str):
        if not request or not request.strip():
            raise ValueError("The music request cannot be empty.")

    @staticmethod
    def validate_energy(energy: float):
        if energy < 0 or energy > 1:
            raise ValueError(
                "Energy preference must be between 0 and 1."
            )

    @staticmethod
    def validate_preferences(user_prefs: dict):
        InputValidator.validate_request(
            user_prefs.get("genre", "")
        )

        InputValidator.validate_energy(
            float(user_prefs.get("energy", 0))
        )
    