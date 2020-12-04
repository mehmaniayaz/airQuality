# Table of Contents
1. [Motivation](#motivation)
2. [Feature Engineering](#feature_engineering)
3. [Data Preprocesing](#data_preprocessing)
4. [Results](#results)
5. [Conclusions](#conclusions)
6. [Dataset](#dataset)

## Motivation <a name="motivation"></a>
The dataset contains measurements of air chemicals through sensors. A sparser set of ground truth
values for the chemicals are provided along with information on humidity, temperature, and datetime.
My goal in the project is to predict the presence of chemicals in the air and gain some useful information on
which parameters affect them most.
  
## Feature Engineering <a name="feature_engineering"></a>
We can get some useful features from the datetime column by extracting time of day (morning, afternoon, evening, 
night, sleep-time), day of the week, and month. I furthermore decided to sum up the amount of chemicals to obtain
a single target variable. This step has the benefit of reducing the dimension of the target variable space.  

## Data Preprocessing <a name="data_preprocessing"></a>
An immediate observation is that NMHC ground truth, with an above 90% missing sample, is an unreliable feature and should therefore be dropped.
A pairplot visualization of data suggests that the chemical values should be normalized as their magnitudes relative to each other is not important.
This step will furthermore help us in summing up the chemicals as part of feature engineering.
The first priority is to fill up missing ground truth values for the chemicals. In other words, 
we are going to use the sensor data to fill up the missing true chemical values throughout the given timeline.
For this step I have used scitkit-learn's iterative imputer to build a relationship between the chemicals (sensor and real) only. Similarly, missing
values for temperature and humidity are imputed with the iterative imputer given the inherent relationship between these variables that we 
would like to retain. Compared to univariate imputer, the iterative imputer attempts to keep the relationship between features 
as close as possible.

## Results <a name="results"></a>
I have used Random Forest Regressor to build a machine learning model. They accuracy of the r2 score of train and test
sets are about 94% and 57%. This discrepancy indicates a high amount of overfitting which is likely due to the
the increased number of dummy variables which increases the dimension of the feature space. However, despite the overfitting consequence,
I decided to keep the detailed categorical features to obtain usefule information on when air pollution is highest. 


<img src="./plots/residual_analysis.png " width="80%"/>

Figure 1: We observe that our model does not predict all values  equally, indicating higher errors in predicting chemical
concentrations at intermediate chemical concentrations.
 
## Conclusions <a name="conclusions"></a>
We find that hours between 12AM to 6Am (sleep_time) and 4PM to 8PM (evening) have the highest impacts on air pollution.
The influence follows whether a day is a Sunday. Weather conditions (temperature and humidity) have a considerable
impact as well, though their influence is not as clear-cut as the time of day and day of the week.  Month of November
has an important effect amongst all months on air pollution, likely due to the increased travel and decreased 
temperature. Interestingly, although pollution increases on Sundays, Saturdays do not have a particular impact.

<img src="./plots/shap.png " width="80%"/>

Figure 2: SHAP values. Time of day and day of week have the highest impact on air pollution. 

## Dateset <a name="dataset"></a>
You can find the data [here](https://archive.ics.uci.edu/ml/datasets/Air+Quality).