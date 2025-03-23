# Voting Rules Implementation
This project is a personal initiative to implement and explore different voting rules in Python. It simulates various voting scenarios where agents (voters) rank candidates, and a winner is selected based on different rules. The goal of this project is to deepen my understanding of Python and its applications while learning how to implement algorithmic voting systems.

## Overview
The project contains several voting rules, each with its own method for selecting a winner from a set of candidates based on agents' preferences. The following voting rules are implemented:

- Dictatorship Rule: The winner is the alternative ranked first by a specified agent.

- Scoring Rule: The winner is the alternative with the highest score, calculated based on a scoring vector. Tie-breaking is determined by a specified agent.

- Plurality Rule: The winner is the alternative that appears most frequently in the first position of agents' preference rankings.

- Veto Rule: Alternatives ranked last by any agent receive zero points, and the winner is the alternative with the highest total score.

- Borda Rule: Each agent assigns points to alternatives based on their ranking. The alternative with the highest total score wins.

- Single Transferable Vote (STV): The winner is determined through rounds of elimination, where alternatives with the least first-place votes are removed until only one remains. Tie-breaking is done by a specified agent's preference.

The project demonstrates how different voting mechanisms can be implemented in Python, offering insights into decision-making processes that are used in elections and other scenarios.


## Usage
- Each function takes a preferences object, which is an instance of the Preference class. This object provides methods for retrieving candidates, voters, and their respective rankings.

- The tie_break parameter is used in several rules to handle tie situations. The specified agent's ranking is used to determine the winner among tied candidates.
