# Project 1
---
## PROBLEM STATEMENT
---
The College Board (SAT), in partnership with ACT Inc. wishes to explore if:
<ul> 
  <li>Household median annual income</li>
  <li>College enrollment rates </li>
  <li>State population </li>
  <li>Test participation rates </li>
  </ul>
have any relationship with each state's ACT and SAT performance. 
<br>
<br>
We are a team of analysts hired to analyse the provided data, use supporting data from other sources  and present our findings to the college boards.
<br>
<br>

---
## My task
---
* To find out if each state's SAT / ACT participation rates had a relationship with SAT / ACT performance respectively.
* Optional: To find trends within intended college major, test takers and test score
* Optional: To find out if household median annual income had a relationship with SAT / ACT performance. 
<br>
<br>

---
## Construct function for data munging
---
* Write a function that takes in a string that is a number and a percent symbol (ex. '50%', '30.5%', etc.) and converts this to a float that is the decimal approximation of the percent. For example, inputting '50%' in your function should return 0.5, '30.5%' should return 0.305, etc. 
<br>
<br>

---
## DATA USED
---
<br>

### Data provided by General Assembly
---
* [sat_2017.csv](./data/sat_2017.csv) 
* [sat_2018.csv](./data/sat_2018.csv) 
* [sat_2019.csv](./data/sat_2019.csv) 
* [sat_2019_by_intended_college_major.csv](./data/sat_2019_by_intended_college_major.csv)
* [sat_act_by_college.csv](./data/sat_act_by_college.csv)
<br>
<br>

### Data after cleaning and munging by me
---
<br>

|FEATURE|TYPE|DATASET|DESCRIPTION|
|---|---|---|---|
|**State**|*object*|SAT_processed|US states excluding Virgin Islands and Puerto Rico| 
|**Participation_19, _18, _17**|*float*|SAT_processed|Participation rate per year per state for SAT| 
|**EBRW_19, _18, _17**|*integer*|SAT_processed|Evidence-based reading and writing scores per year per state for SAT| 
|**Math_19, _18, _17**|*integer*|SAT_processed|Math scores for SAT per year per state| 
|**Total_19, _18, _17**|*integer*|SAT_processed|Total scores for SAT per year per state| 
|**Participation_mean**|*float*|SAT_processed|Participation rate mean across 2017-19 per state| 
|**EBRW_mean**|*float*|SAT_processed|Evidence-based reading and writing score mean across 2017-19 per state| 
|**Math_mean**|*float*|SAT_processed|Math score mean across 2017-19 per state| 
|**Total_mean**|*float*|SAT_processed|Total score mean across 2017-19 per state| 
|---|---|---|---|
|**IntendedCollegeMajor**|*object*|SAT_19_major|Name of major that test takers shortlisted on test application| 
|**TestTakers**|*integer*|SAT_19_major|Number of test takers who shortlisted that major| 
|**Percent**|*float*|SAT_19_major|Proportion of the total number of test takers who shortlisted that major,<br> if zero, means very small proportion, <br> does not mean no test taker shortlisted that major| 
|**EBRW**|*integer*|SAT_19_major|Evidence-based reading and writing score **average** of applicants who shortlisted this major| 
|**Math**|*integer*|SAT_19_major|Math score **average** of applicants who shortlisted this major| 
|**Total**|*integer*|SAT_19_major|Total score **average** of applicants who shortlisted this major| 
|---|---|---|---|
|**School**|*object*|SAT_21_college|Names of colleges that applicants applied to| 
|**Number of Applicants**|*integer*|SAT_21_college|Number of applicants per college for 2021| 
|**Accept Rate**|*float*|SAT_21_college|Proportion of applicants accepted by the college over <br>the total applicants for that college for 2021| 
|**SAT_25th percentile**|*float*|SAT_21_college|25th percentile SAT score for accepted applicants in this college for 2021| 
|**SAT_75th percentile**|*float*|SAT_21_college|75th percentile SAT score for accepted applicants in this college for 2021| 
|**ACT_25th percentile**|*float*|SAT_21_college|25th percentile ACT score for accepted applicants in this college for 2021| 
|**ACT_75th percentile**|*float*|SAT_21_college|75th percentile ACT score for accepted applicants in this college for 2021| 
<br>
<br>

---
### Data Dictionary of team mates' cleaned data used by me
---
<br>

* Combination of provided data by General Assembly and external data
    * Provided data
        * [act_2017.csv](./data/act_2017.csv)
        * [act_2018.csv](./data/act_2018.csv)
        * [act_2019.csv](./data/act_2019.csv)
    * External data
        * [ACT_2018_data.csv](./data/external/ACT_2018_data.csv) from [link](https://nces.ed.gov/programs/digest/d18/tables/dt18_226.60.asp)
        * [ACT_2019_data.csv](./data/external/ACT_2019_data.csv) from [link](https://nces.ed.gov/programs/digest/d19/tables/dt19_226.60.asp)
        * [Median Household Income by State (2017-2019).xlsx](./data/external/MedianHouseholdIncomebyState(2017-2019).xlsx) from [link](https://www.census.gov/data/tables/time-series/demo/income-poverty/historical-income-households.html)
---
<br>

|FEATURE|TYPE|DATASET|DESCRIPTION|WHO CLEANED|
|---|---|---|---|---|
|**State**|*object*|ACT_combined|Names of 51 US states and 'National' row|Bryan| 
|**Participation 2017/ 2018/ 2019**|*float*|ACT_combined|Participation rate per year per state for ACT|Bryan| 
|**English 2017/ 2018/ 2019**|*float*|ACT_combined|mean English scores per year per state for ACT|Bryan|
|**Math 2017/ 2018/ 2019**|*float*|ACT_combined|mean Math scores per year per state for ACT|Bryan|
|**Read 2017/ 2018/ 2019**|*float*|ACT_combined|mean Reading scores per year per state for ACT|Bryan|
|**Science 2017/ 2018/ 2019**|*float*|ACT_combined|mean Science scores per year per state for ACT|Bryan|
|**Composite 2017/ 2018/ 2019**|*float*|ACT_combined|Composite scores per year per state for ACT|Bryan|
|---|---|---|---|---|
|**State**|*object*|med_income_17_19|US states and a 'United States' row <br> representing national median household income|Anand|
|**income_2017**|*integer*|med_income_17_19|Median household income in 2017 by state|Anand|
|**income_2018**|*integer*|med_income_17_19|Median household income in 2018 by state|Anand|
|**income_2019**|*integer*|med_income_17_19|Median household income in 2019 by state|Anand|
|---|---|---|---|---|
<br>

---
## Method of analysis
---
<br>

### 1. Incorporate Bryan's cleaned data with my SAT_processed data
* Formated values in columns in Bryan's data to have consistency with my data
* Added new 'National' row for SAT data to match with ACT 'State' column keys
* pd.merged SAT and ACT data
* Changed column names for clarity and differentiation between ACT and SAT data
* Export to [SAT_ACT_combined.csv](data/processed/SAT_ACT_combined.csv) without new index
* Removed 'National' row prior to analysis but leave it in exported dataset
<br>

### 2. Incorporate Anand's cleaned data (median income) with SAT_ACT_combined data
* Renamed 'United States' row to 'National'
* Added 'Income_mean' column
* Removed 'National' row after merge
* Export to [SAT_ACT_income_no_national](data/processed/SAT_ACT_income_no_national.csv) without new index
<br>
<br>

### 3. Exploratory Data Analysis 
---
<br>

#### Summary Statistics
---
* `df.describe()`
* `df.isnull().sum()`
<br>
<br>

---
#### Dictionary comprehension to find standard deviation
---
* Self-constructed standard deviation function `std_dvn(col)`
* Assign variable to dictionary
* `{col.name:std_dvn(col) for col in [df[i] for i in df.columns if (df[i].dtype=='float64') or (df[i].dtype=='int64')]}`
<br>
<br>

---
#### Trends within SAT and ACT data
---

* Which states have the highest and lowest participation rates for the 2017, 2019, or 2019 SAT and ACT?
* Which states have the highest ad lowest mean participation rates for SAT and ACT?
* Which states have the highest and lowest mean scores for SAT and ACT?
* Which states have the highest and lowest mean total/composite scores for the 2017, 2019, or 2019 SAT and ACT?
* Do any states with 100% participation on a given test have a rate change year-to-year?
* Do any states show have >50% participation on both tests each year?
<br>
<br>

---
#### Inferential statistics - Hypothesis testing
---
* Can the following predict SAT performance for each SAT component?
    * SAT_Pptn_19 
    * SAT_Pptn_18 
    * SAT_Pptn_17 
    * SAT_Pptn_mean 
    * Income_19
    * Income_18
    * Income_17
    * Income_mean
* Can the following predict ACT performance for each ACT component?
    * ACT_Pptn_19 
    * ACT_Pptn_18 
    * ACT_Pptn_17 
    * ACT_Pptn_mean 
    * Income_19
    * Income_18
    * Income_17
    * Income_mean
<br>
<br>

---
## Data Visualisation
---
* Heatmaps
  * SAT mean scores and mean participation rate
  * ACT mean scores and mean participation rate
  * Acceptance rates, ACT percentiles, SAT percentiles, number of applicants
  * testtakers and total SAT score
  * SAT vs ACT
    * By participation rate per year
    * By SAT Total versus ACT Composite score per year
    * By SAT math score versus ACT math score per year
    * By SAT EBRW score versus ACT english and reading scores per year
* Pairplots
  * SAT mean scores and mean participation rate
  * ACT mean scores and mean participation rate
  * Acceptance rates, ACT percentiles, SAT percentiles, number of applicants
  * SAT vs ACT
    * By participation rate per year
    * By SAT Total versus ACT Composite score per year
    * By SAT math score versus ACT math score per year
    * By SAT EBRW score versus ACT english and reading scores per year
* Horizontal bar plot
  * Intended college major and test takers
  * Intended college major and total SAT score
* Scatterplots
  * To display the significant relationships found from the above visualisations in a clearer, concised manner
    * Negative correlation between ACT and SAT participation rates
    * Negative correlation between ACT performance and ACT participation rate
    * Negative correlation between SAT performance and SAT participation rate
    * Positive correlation between ACT performance and SAT participation rate
    * Positive correlation between SAT performance and ACT participation rate
      * By year
      * By mean
* Boxplots
  * To find trends across 3 years for both ACT and SAT scores and participation rates (2017-2019)
* Geographic mapping
  * Use `Plotly Express`, 
  * `import plotly.graph_objects as go`
  * Compare geographic distribution of SAT vs ACT mean participation rate 
* Histograms
  * Explore distributions of:
    * SAT and ACT mean participation rates
    * SAT mean component scores and Total score
    * ACT mean component scores and composite score
<br>
<br>

---    
### Optional Data visualisation
---
* Geographic mapping
  * Map each year median annual income geographic distribution (2017-2019)
  * Map mean of median annual income geographic distribution (2017-2019)
* Horizontal barcharts
  * Rank household median income per year (high to low)
  * Rank mean of household median income (2017-2019) (high to low)
* Boxplots
  * To find median income trend across 2017 to 2019
* Histograms
  * Explore distribution of:
    * Household median annual income per year
* Heatmaps
* Pairplots
  * Compare SAT data with median income by year
  * Compare ACT data with median income by year
<br>
<br>

---
## Summary of findings
---
<br>

---
### SAT scores association with participation rates
---
* Negative correlation between SAT participation rates and SAT scores
* Using hypothesis testing
  * Mean SAT participation rates have a consistent statistically significant relationship with predicting SAT performance scores
    * 3 out of 4 datapoints showed SAT participation rates have a statistically significant relationship in predicting SAT EBRW, Math, and Total scores respectively. 
* States that perform well in one component in SAT, tend to also perform well in other components in SAT
* 75th percentile SAT participation rate increasing from 2017 to 2019
<br>
<br>

---
### ACT scores association with participation rates
---
* Negative correlation between ACT participation rates and ACT scores
* Using hypothesis testing
  * Mean ACT participation rates have a consistent statistically significant relationship with predicting ACT performance scores 
    * 3 out of 4 datapoints showed ACT participation rates have a statistically significant relationship in predicting ACT English and Reading scores respectively 
* Candidates tend to perform better in reading component compared to english component for ACT (consistent for 2017-2019)
* 25th percentile ACT participation rate decreasing from 2017 to 2019
<br>
<br>

---
### SAT vs ACT
---
* Negative correlation between SAT and ACT participation rates
* Positive correlation between ACT scores and SAT participation rate
* Positive correlation between SAT math/total scores and ACT participation rate
<br>
<br>

---
### SAT/ ACT performance association with income
---
* ACT math performance has a weak positive correlation to median income
* Household median income generally follow normal distribution
* Household median Income shows a statistically significant relationship with ACT scores but not with SAT scores
<br>
<br>

---
### College acceptance rates association with ACT/SAT percentile scores
---
* Negative correlation between ACT/SAT percentile scores and university acceptance rates
* Health profession is the most popular major shortlisted by SAT candidates in 2019. However, candidates who shortlisted this major were not best performers
<br>
<br>

---
## Recommendations to college boards
---
* More data is required from other years e.g 2011 to 2021 for a better certainty on trends and association
* More research is recommended to find out what barriers candidates from low income households in US face to performing well in ACT
* More research is recommended to find out why states that perform well in SAT and ACT tend to have lower participation rates
* More research is required to find out why household median income does not seem to affect SAT performance as much as it affects ACT performance, and how to replicate that effect for ACT.
