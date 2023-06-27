# euro-diffusion

# Coin Sharing Algorithm

This project implements a coin sharing algorithm that distributes coins among cities based on certain rules. The algorithm is used to solve a specific problem outlined in the input file.

## Project Structure

The project consists of the following files:

- `settings.py`: Contains configuration settings for the algorithm.
- `utility_classes.py`: Defines utility classes required for the algorithm, including `City` and `Country`.
- `main.py`: The main entry point of the program that reads input, runs the algorithm, and writes the output.
- `algorithm.py`: Contains the implementation of the `Algorithm` class used for solving the coin sharing problem.

## Usage

To use this project, follow the steps below:

1. Ensure that you have the input file (`input.txt`) ready with the required input data.
2. Run the `main.py` file using the Python interpreter.
3. The program will read the input file, execute the algorithm for each case, and generate an output file (`output.txt`) with the results.

Please make sure to replace the content of the `input.txt` file with your own input data before running the program.

## Configuration

The algorithm can be customized using the configuration settings in `settings.py`. The available settings are as follows:

- `INITIAL_COIN_COUNT`: The initial number of coins each city starts with.
- `REPRESENTATIVE_PORTION`: The number of coins required to trigger a sharing event with neighboring cities.
- `MAX_XY_VALUE`: The maximum value for the X and Y coordinates of a city.

## Customization

You can extend the functionality of this project by modifying or adding new classes and methods as per your requirements. The existing code provides a foundation for solving the coin sharing problem, but you can adapt it to different scenarios or expand it to handle additional features.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as needed.