# DataExplore Project

This project aims to practice creating a Python package for exploratory data analysis using the `DataExplorer` class. The primary goal is to gain hands-on experience in creating and distributing a Python package on the Python Package Index (PyPI). The package offers functionalities for quick and easy data exploration and visualization, helping users understand their datasets and make informed decisions.

## Package Structure

- [`dataExplore/`](dataExplore/): The package folder containing the `DataExplorer` class and related functionality.

## Usage

For detailed information on how to use the `DataExplorer` class and its methods, please refer to the main package's [README.md](~/dataExplore/REAMDE.md) file.

## Installation

Here are the required dependencies.

```bash
pip install pandas matplotlib seaborn numpy
```

## Example

Here's a simple example of how to use the `DataExplorer` class:

```python
from datainspect import DataExplorer

# Instantiate the DataExplorer class with your dataset
explorer = DataExplorer('data.csv')

# Get a summary of the dataset
summary = explorer.summary()
print(summary)

# Generate histograms
explorer.histogram()

# Visualize correlation using a heatmap
explorer.heat_map()

# Display missing data information
missing_info = explorer.missing_data_info()
print(missing_info)
```

## Contributing

Contributions to this project are welcome! If you have suggestions, enhancements, or bug fixes, please submit pull requests or open issues.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
