// Fetch data from Django API
// You need to implement this part

// Populate year filter
const yearFilter = document.getElementById('year-filter');

// Example data (replace with actual data fetched from API)
const availableYears = [2019, 2020, 2021, 2022];

// Populate year filter options
availableYears.forEach(year => {
  const option = document.createElement('option');
  option.value = year;
  option.text = year;
  yearFilter.appendChild(option);
});

// Event listener for year filter change
yearFilter.addEventListener('change', () => {
  const selectedYear = yearFilter.value;
  
  // Fetch data for selected year and update dashboard content
  // You need to implement this part
});
