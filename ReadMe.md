# Table of Contents
1. [Motivation](#motivation)
2. [Feature Engineering](#feature_engineering)
3. [Data Preprocesing](#data_preprocessing)
4. [Results](#results)
5. [Conclusions](#conclusions)
6. [Dataset](#dataset)

## Motivation <a name="motivation"></a>
The dataset contains measurements of air chemicals through sensors. A sparser set of ground truth
values for the chemicals are provided as well along with information on humidity, temperature, and time.
My goal in the project is to predict the presence of chemicals in the air and gain some useful information on
which parameters affect them most.
  
## Feature Engineering <a name="feature_engineering"></a>
We can get some useful features from the datetime column by extracting time of day (morning, afternoon, evening, 
night, sleep-time), day of the week, and month. I furthermore decided to sum up the amount of chemicals to obtain
a danger meter. This step has the added benefit of reducing the dimension of the target variable space.  

## Data Preprocessing <a name="data_preprocessing"></a>
The first priority is to fill up missing values of the ground truth values for the chemicals. In other words, 
we are going to use the sensor data to fill up the missing true chemical values throughout the given timeline.
For this step I have used Scitkit-Learn's iterative imputer to build a relationship between the chemicals (
sensor and real) only. Similarly missing values for temperature and humidity are imputed with the iterative imputer
given the inherent relationship between these variables.

## Results <a name="results"></a>
## Conclusions <a name="conclusions"></a>

## Dateset <a name="dataset"></a>
You can find the data [here](https://archive.ics.uci.edu/ml/datasets/Air+Quality).