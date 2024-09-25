# Last Digit Mode Finder

This Python script analyzes a list of floating-point numbers, extracts the last digit from each number, and calculates the most frequent last digits (modes). It finds the first, second, and third most frequent last digits along with their counts.

## Features

- Extracts the last digit from a list of floating-point numbers.
- Calculates the mode (most frequent digit).
- Displays the second and third most frequent digits, along with how many times they appeared.

## How It Works

1. The program takes a multiline string of numbers as input.
2. Each number is processed to extract its last digit.
3. Using Python's `collections.Counter`, it counts the occurrences of each last digit.
4. The script then identifies the first, second, and third most frequent last digits.

## Requirements

- Python 3.x
- Standard libraries used:
  - `statistics`
  - `collections`

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/emmyliano/entry-spot_analysis
    ```
2. Navigate to the project directory:
    ```bash
    cd last-digit-mode-finder
    ```
3. Run the script:
    ```bash
    python3 main.py
    ```

## Example Output

The program will output the top 3 most frequent last digits from the input dataset:

```text
1 mode: Last digit 3 appeared 15 times
2 mode: Last digit 5 appeared 12 times
3 mode: Last digit 7 appeared 10 times