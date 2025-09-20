# News Attention Measurement Dashboard

A Streamlit-based interactive dashboard for visualizing and analyzing news articles related to attention measurement in advertising across different countries and time periods.

## Features

- **Interactive Date Range Selection**: Filter news articles by custom date ranges
- **Geographical Visualization**: Interactive world map showing news distribution by country
- **Statistical Charts**: Pie charts displaying percentage breakdown of news by country
- **Country-Specific Filtering**: Dropdown selection to view news from specific countries
- **Paginated Article View**: Browse through articles with embedded links and AI-generated abstracts
- **Real-time Data Validation**: Built-in warnings for invalid date ranges or missing data

## Screenshots

The dashboard includes:
- A geographical heatmap showing news distribution globally
- Pie chart visualization of news percentages by country
- Detailed article listings with clickable links and AI-generated summaries

## Installation

### Prerequisites

Make sure you have Python 3.7+ installed on your system.

### Required Dependencies

Install the required packages using pip:

```bash
pip install streamlit pandas geopandas plotly folium streamlit-folium numpy
```

Or install from requirements file:

```bash
pip install -r requirements.txt
```

### Requirements.txt
```
streamlit
pandas
geopandas
plotly
folium
streamlit-folium
numpy
```

## Data Requirements

The application expects a CSV file named `attention_OpenAI_yes.csv` with the following columns:

- `URL`: Link to the news article
- `Date`: Publication date of the article
- `Country`: Country of origin (supports: unitedstates, unitedkingdom, australia, canada, singapore, japan, mexico, hongkong)
- `Title`: Article headline
- `Text`: Full article text
- `Decision`: Classification decision ("Yes"/"No")
- `Justification`: AI-generated abstract/summary of the article

### Sample Data Format
```csv
URL,Date,Country,Title,Text,Decision,Justification
https://example.com/article1,2023-10-13,unitedstates,Sample Title,Article content...,Yes,This article discusses attention measurement...
```

## Usage

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/news-attention-dashboard.git
cd news-attention-dashboard
```

2. **Place your data file**:
   - Ensure `attention_OpenAI_yes.csv` is in the same directory as the main script

3. **Run the application**:
```bash
streamlit run app.py
```

4. **Access the dashboard**:
   - Open your browser and navigate to `http://localhost:8501`

### Using the Dashboard

1. **Set Date Range**: Use the sidebar to select start and end dates for filtering
2. **View Geographic Distribution**: Explore the interactive world map to see news distribution
3. **Analyze Statistics**: Review the pie chart for percentage breakdowns
4. **Select Country**: Choose a specific country from the dropdown to view detailed articles
5. **Browse Articles**: Use pagination to navigate through articles with embedded links

## Configuration

### Date Range Settings
- **Default Date Range**: January 1, 2020 to October 23, 2023
- **Default End Date**: October 13, 2023
- Dates can be customized in the sidebar

### Display Settings
- **Articles per page**: 10 (configurable in the `rows_per_page` variable)
- **Map zoom level**: Global view (zoom_start=1)
- **Page layout**: Wide layout for better visualization

## Data Processing

The application automatically:
- Converts country codes to full country names
- Filters articles based on decision criteria ("Yes" only)
- Validates date ranges and data availability
- Processes URLs into clickable HTML links
- Handles pagination for large datasets

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/new-feature`)
6. Create a Pull Request

## Troubleshooting

### Common Issues

1. **"Data not available" warning**: Check that your CSV file contains data within the selected date range
2. **Map not loading**: Ensure geopandas and folium are properly installed
3. **Country not appearing**: Verify country names match the supported format in the code
4. **Date range errors**: Ensure end date is not earlier than start date

### Error Messages
- **Date validation**: "The End date should not be earlier than the Start date"
- **Data availability**: "Data not available for the specified date range"

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Geographic data from [Natural Earth](https://www.naturalearthdata.com/)
- Visualization powered by [Plotly](https://plotly.com/) and [Folium](https://folium.readthedocs.io/)

## Support

For questions or issues, please open an issue on GitHub or contact [your-email@domain.com].

---

**Note**: This dashboard is designed for analyzing news articles related to attention measurement in advertising. Ensure your data follows the expected format for optimal performance.
