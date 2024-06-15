import re

def parse_outcome(game_code):
    """
    Parse the given game code to predict the outcome of the game (small or big).
    """
    # Simulating the actual game behavior using regex patterns found in the code.
    small_pattern = re.compile(r'\bsmall\b', re.IGNORECASE)
    big_pattern = re.compile(r'\bbig\b', re.IGNORECASE)
    
    # Check for small outcome
    if small_pattern.search(game_code):
        return "small"
    # Check for big outcome
    elif big_pattern.search(game_code):
        return "big"
    else:
        return "unknown"

# Example usage with a string from the game code that should reflect the game's outcome
game_code_snippet = """
  async function playGame() {
    const outcome = getOutcome(); // Simulated outcome function
    if (outcome === 'small') {
      console.log('You got a small outcome!');
    } else if (outcome === 'big') {
      console.log('You got a big outcome!');
    } else {
      console.log('Outcome unknown');
    }
  }
"""

outcome = parse_outcome(game_code_snippet)
print(outcome)  # Output: small