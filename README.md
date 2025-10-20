# WikiPath Finder 

A simple yet powerful Python web crawler to find the shortest path (in clicks) between two Wikipedia pages.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)

---

## 🎯 Project Goal

The goal of **WikiPath Finder** is to demonstrate the "six degrees of separation" concept as it applies to Wikipedia's vast network. The script starts from a chosen page and navigates through its internal links to find a target page, ultimately displaying the most efficient path to connect the two topics.

This project is an excellent practical exercise for understanding:
* **Web Scraping**: Extracting data from web pages using `requests` and `BeautifulSoup`.
* **Graph Algorithms**: Implementing a Breadth-First Search (BFS) algorithm to explore the page network.
* **Data Management**: Using data structures like queues (`deque`) and sets to manage the exploration efficiently.

---

## 🔧 Setup

To run this script on your local machine, follow these steps.

### Prerequisites
* **Python 3.7** or higher.
* **pip** (Python's package installer).

### Installation Steps
1.  **Clone the repository**
    ```bash
    git clone [https://github.com/your-username/your-repository.git](https://github.com/your-username/your-repository.git)
    cd your-repository
    ```

2.  **Create a `requirements.txt` file**
    Create a file named `requirements.txt` in the project's root folder and add the following dependencies:
    ```
    requests
    beautifulsoup4
    ```

3.  **Install the dependencies**
    Run this command in your terminal to install the necessary libraries:
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 Usage

Once the installation is complete, you can run the script from your terminal.

1.  **Run the Python script**
    ```bash
    python main.py
    ```
    *(Replace `main.py` with the name of your script file)*

2.  **Enter the required input**
    The script will prompt you for two pieces of information:
    * **Starting URL**: The full web address of the Wikipedia page where the search begins.
        * *Example: `https://en.wikipedia.org/wiki/Cat`*
    * **Target Page Title**: The **exact** title of the page you want to reach, as it appears at the top of the article (not the name in the URL slug).
        * *Example: `Ancient Egypt` (and not `Ancient_Egypt`)*

### Example Output
```bash
Enter the starting Wikipedia URL: [https://en.wikipedia.org/wiki/Cat](https://en.wikipedia.org/wiki/Cat)
Enter the target page title: Ancient Egypt
----------------------------------------
🏁 Starting search from: [https://en.wikipedia.org/wiki/Cat](https://en.wikipedia.org/wiki/Cat)
🎯 Target to find: 'Ancient Egypt'

[1/500] Visiting: [https://en.wikipedia.org/wiki/Cat](https://en.wikipedia.org/wiki/Cat)
...
...
[25/500] Visiting: [https://en.wikipedia.org/wiki/Ancient_Egypt](https://en.wikipedia.org/wiki/Ancient_Egypt)

🎉🎉🎉 Target found! 🎉🎉🎉

Path found through the following links:
Cat -> Felis -> Domestication -> Near_East -> Ancient_Egypt

Total steps: 4
----------------------------------------
