# aancha.14.2025_EMATM0048
# Software Development: Programming and Algorithms (SDPA) Coursework

**Name: Aanchala Bhongade**
**Student no.: 2830709**

## Part 1: Flower Shop Simulation

### Description
A text-based simulation, based on object oriented programming techniques. The user here is the owner who manages florists, inventory (roses, daisies, greenery) and monthly sales of bouquets to avoid going bankrupt.

### Overview
1. **main.py:** This is the entry point for the simulation. It also handles input and output validation and simulation loop.
2. **Flower_Shop.py:** This the main controller of the simulation. This is responsible for cash flow, inventory management and employee management.
3. **Florist.py:** It defines *florists* and *specialisedflorist* (subclass of florist class). It used inheritance and polymorphism for calculation of time needed to make bouquets.
4. **Vendor.py:** Class for Vendor, which defines details about them and pricing.

### Designing
1. **Extension**: I implemented a *specialisedflorist* subclass.
**Polymorphism**: Used polymorphism to override the get.speed() method, as usual time taken by a florist is 1.0 and florist with specialisation takes 0.5 for their specific bouquet type.
**Logic Used:** The sales_plan here prioritises the specialised florists before assigning the work.
2. **Data Structures:** Dictionaries are used for inventory and bouquet types.
3.**Error Handling:** Custom check points ensure that inputs are correct not invalid.
4. **Dependencies:** Standard python libraries: math (used for ceil function in calculation of depreciation cost). No external packages are required.

### How to run the code
1. Open Terminal. Ensure you have python 3 installed in terminal.
2. Navigate to the directory containing main.py.
3. Run the command: python main.py
4. Follow the screen prompts and run the simulation.


## Part 2: Data Analysis

## Analysis of Blockchain Security: Market Volatility vs. Crime Severity

### Description: 
An analysis of blockchain data to learn about patterns in financial crimes. I investigate the relationship between cryptocurrency market conditions and security breaches. Specifically, does the 'hype' of Bull Market lead to more frequent or more severe financial crimes compared to a Bear Market? It includes exploratory data analysis (EDA).

### Files:
1. **Notebook.ipynb:** The Jupyter Notebook contains the full analysis and pipeline.
2. **blockchain_security_dataset:** The dataset collected form DefiLlama and Blockchain Public Api and then merged together and then cleaned and handled missing values. It contains the Date, Amount lost, etc price, blockchain and target.
### Dataset:
* **Columns:** 'timestamp_s', 'target', 'amount_usd', 'category', 'blockchain', 'timestamp_ms' and 'eth_price'.
* **Collection:** extracted the data from the *DefiLlama Hacks API* and *Binance Public API*.

### Librabries:
To run the notebook, the following python libraries are required:
1. pandas: Data manipulation
2. matplotlib and seaborn: Data visualisation
3. requests: To crawl data from external APIs (DefiLlama & Binance)
4. scipy.stats: Used for statistical analysis like hypothesis testing (T-Test)

No additional scripts were used.

#### How to use:
1. Save dataset and notebook in same folder.
2. Open Notebook.ipynb in Jupyter Notebook.


