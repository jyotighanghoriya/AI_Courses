from smolagents import Tool
from typing import Any, Optional

class SimpleTool(Tool):
    name = "suggest_menu"
    description = "Return a predefined menu for an occasion."
    inputs = {'occasion': {'type': 'string', 'description': "One of 'casual', 'formal', or 'superhero'. Use 'formal' for formal parties and elegant events. Use 'casual' for informal gatherings. Use 'superhero' for superhero-themed parties."}}
    output_type = "string"

    def forward(self, occasion: str) -> str:
        """
        Return a predefined menu for an occasion.

        Args:
            occasion: One of 'casual', 'formal', or 'superhero'.
                Use 'formal' for formal parties and elegant events.
                Use 'casual' for informal gatherings.
                Use 'superhero' for superhero-themed parties.

        Returns:
            The predefined menu for the occasion.
        """
        if occasion == "casual":
            return "Casual menu: Pizza, Sandwiches, Salad"
        elif occasion == "formal":
            return "Formal menu: Champagne, Canapés, Roast Chicken, Salad"
        elif occasion == "superhero":
            return "Superhero menu: Chips, Salsa, Burgers, Hot Dogs"
        else:
            return "Menu not available for this occasion."