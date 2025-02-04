"""CSC111 Project 1: Text Adventure Game - Game Entities

Instructions (READ THIS FIRST!)
===============================

This Python module contains the entity classes for Project 1, to be imported and used by
 the `adventure` module.
 Please consult the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2025 CSC111 Teaching Team
"""
from dataclasses import dataclass
from typing import Optional, Dict, List

@dataclass
class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - id: Unique identifier for the location
        - brief_description: Short description of the location
        - long_description: Detailed description of the location
        - available_commands: Dictionary of available movement commands
        - items: List of item names present at this location
        - puzzle: Optional puzzle configuration for the location
        - visited: Whether the player has visited this location

    Representation Invariants:
        - id >= 0
    """

    # This is just a suggested starter class for Location.
    # You may change/add parameters and the data available for each Location object as you see fit.
    #
    # The only thing you must NOT change is the name of this class: Location.
    # All locations in your game MUST be represented as an instance of this class.

    def __init__(self, location_id: int, brief_description: str, long_description: str, available_commands:Dict[str, int], items: List[str],puzzle: Optional[Dict] = None,
                 visited: bool = False) -> None:
        """Initialize a new location.

        # TODO Add more details here about the initialization if needed
        """

        self.id = location_id
        self.brief_description = brief_description
        self.long_description = long_description
        self.available_commands = available_commands
        self.items = items
        self.visited = visited
        self.puzzle = puzzle


@dataclass
class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - name: The unique name of the item (e.g., "flashlight", "convocation_key").
        - description: A detailed description of the item.
        - start_position: The initial location ID where the item is placed.
        - target_position: The target location ID where the item needs to be moved to score points.
        - target_points: The points awarded when the item is moved to its target position.
        - required_item: An optional item name required to interact with this item (for puzzles)

    Representation Invariants:
        - start_position >= -1
        - target_position >= -1
        - target_points >= 0
    """

    # NOTES:
    # This is just a suggested starter class for Item.
    # You may change these parameters and the data available for each Item object as you see fit.
    # (The current parameters correspond to the example in the handout).
    #
    # The only thing you must NOT change is the name of this class: Item.
    # All item objects in your game MUST be represented as an instance of this class.

    name: str
    start_position: int
    target_position: int
    target_points: int
    description: str
    required_item: Optional[str] = None

    def __init__(
            self,
            name: str,
            description: str,
            start_position: int,
            target_position: int,
            target_points: int,
            required_item: Optional[str] = None
    ):
        self.name = name
        self.description = description
        self.start_position = start_position
        self.target_position = target_position
        self.target_points = target_points
        self.required_item = required_item


# Note: Other entities you may want to add, depending on your game plan:
# - Puzzle class to represent special locations (could inherit from Location class if it seems suitable)
# - Player class
# etc.

if __name__ == "__main__":
    pass
    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    # import python_ta
    # python_ta.check_all(config={
    #     'max-line-length': 120,
    #     'disable': ['R1705', 'E9998', 'E9999']
    # })
