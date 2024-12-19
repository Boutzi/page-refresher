# Selenium Page Refresher

This script uses Selenium to continuously refresh a webpage as fast as possible, with performance optimizations like disabling images and using headless mode.

---

## Prerequisites

Ensure you have the following installed:

- Python 3.7 or higher
- `pip` (Python package manager)

---

## Setup Instructions

### 1. Clone the Repository

```bash
# Replace with your repository URL if applicable
git clone https://github.com/Boutzi/page-refresher.git
cd page-refresher
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python libraries using the `requirements.txt` file:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### `requirements.txt` content:

```txt
selenium==4.27.1
webdriver-manager==4.0.2
```

---

## Usage

1. **Edit the Script:**
   Open the `main.py` file and replace `https://your-website` with the URL of the webpage you want to refresh.

2. **Run the Script:**

   ```bash
   python main.py
   ```

3. **Output:**
   The script will print how long each page refresh takes, for example:

   ```
   Page refreshed in 0.53 seconds
   Page refreshed in 0.50 seconds
   ```

4. **Stop the Script:**

   Press `ESCAPE` or `CTRL + C`

## Optional Configurations

### Disable Image Loading

To further optimize performance, uncomment the following lines in the script:

```python
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
```

### Adjust Refresh Speed

The script refreshes the page as quickly as possible. If you want to add a delay between refreshes, modify the loop in `main()`:

```python
while True:
    start_time = time.time()
    refreshPage(driver)
    end_time = time.time()
    print(f"Page refreshed in {end_time - start_time:.2f} seconds")
    time.sleep(1)  # Add a 1-second delay
```

---

## Troubleshooting

### Common Issues

#### 1. WebDriver not found

Ensure you have the correct version of Chrome installed and that `webdriver-manager` is up to date:

```bash
pip install --upgrade webdriver-manager
```

#### 2. Virtual Environment Not Activated

If you see missing dependencies, ensure the virtual environment is active:

```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
