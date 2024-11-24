# Training Workflow

## Data Validation  
This step involves various checks to ensure the integrity and consistency of the training files.  

1. **Name Validation**  
   - Validate file names based on the schema file using a regex pattern.  
   - Check the length of the date and time values in the file names.  
   - Files meeting the requirements are moved to the **"Good_Data_Folder"**, while non-compliant files are moved to the **"Bad_Data_Folder"**.  

2. **Number of Columns**  
   - Validate the number of columns in each file.  
   - Files with mismatched column counts are moved to the **"Bad_Data_Folder"**.  

3. **Name of Columns**  
   - Validate column names against those specified in the schema file.  
   - Files with incorrect column names are moved to the **"Bad_Data_Folder"**.  

4. **Datatype of Columns**  
   - Validate column data types as per the schema file during database insertion.  
   - Files with incorrect data types are moved to the **"Bad_Data_Folder"**.  

5. **Null Values in Columns**  
   - If all values in a column are NULL or missing, the file is discarded and moved to the **"Bad_Data_Folder"**.  

---

## Data Insertion in Database  

1. **Database Creation and Connection**  
   - Create a database with the specified name, or connect to an existing database.  

2. **Table Creation**  
   - Create a table named **"Good_Data"** in the database with column names and datatypes as per the schema file.  
   - If the table already exists, insert new files into it to accommodate both new and old training data.  

3. **File Insertion**  
   - Insert all files from the **"Good_Data_Folder"** into the database.  
   - Files with invalid data types are not inserted and are moved to the **"Bad_Data_Folder"**.  

---

## Model Training  

1. **Data Export from Database**  
   - Export data from the database as a CSV file for model training.  

2. **Data Preprocessing**  
   - **Drop irrelevant columns**: Identify and drop columns that are not useful for training during EDA.  
   - **Handle invalid values**: Replace invalid values with `numpy.nan` for imputation.  
   - **Impute null values**: Use the **KNN imputer** to fill missing values.  
   - **Scale data**: Scale training and testing data separately.  

3. **Clustering**  
   - Use the **KMeans algorithm** to create clusters in the preprocessed data.  
   - Determine the optimal number of clusters using the **elbow plot** and **KneeLocator** function.  
   - Train the KMeans model and save it for future predictions.  

4. **Model Selection**  
   - Train two models, **Decision Tree Regressor** and **XGBoost Regressor**, for each cluster using the best parameters from **GridSearch**.  
   - Calculate the **R-squared scores** for both models and select the best-performing model for each cluster.  
   - Save the selected models for each cluster for use in prediction.  