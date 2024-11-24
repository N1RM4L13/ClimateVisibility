# Prediction Workflow  

## Prediction Data Description  
- The client provides data in multiple file batches, each containing climate indicators across 10 columns.  
- A **schema file** is also required from the client, which includes:  
  - File name format.  
  - Length of the date value in the file name.  
  - Length of the time value in the file name.  
  - Number of columns.  
  - Names of the columns.  
  - Data types of each column.  

---

## Data Validation  

Validation is performed on the prediction files to ensure data integrity and consistency:  

1. **Name Validation**  
   - File names are validated against the schema using a regex pattern.  
   - The lengths of the date and time values in the file names are checked.  
   - Valid files are moved to the **"Good_Data_Folder"**, while invalid files are moved to the **"Bad_Data_Folder"**.  

2. **Number of Columns**  
   - Files with a column count different from the schema specification are moved to the **"Bad_Data_Folder"**.  

3. **Name of Columns**  
   - Validate column names against the schema.  
   - Files with mismatched column names are moved to the **"Bad_Data_Folder"**.  

4. **Datatype of Columns**  
   - Column data types are validated against the schema during database insertion.  
   - Files with incorrect data types are moved to the **"Bad_Data_Folder"**.  

5. **Null Values in Columns**  
   - Files with columns where all values are NULL or missing are moved to the **"Bad_Data_Folder"**.  

---

## Data Insertion in Database  

1. **Database Creation and Connection**  
   - Create a database with the specified name or connect to an existing one.  

2. **Table Creation**  
   - Create a table named **"Good_Data"** for storing validated files, with column names and data types from the schema.  
   - If the table already exists, insert new files into the existing table.  

3. **File Insertion**  
   - Files from the **"Good_Data_Folder"** are inserted into the database.  
   - Files with invalid data types are not inserted and are moved to the **"Bad_Data_Folder"**.  

---

## Prediction  

1. **Data Export from Database**  
   - Export the stored data as a CSV file for prediction.  

2. **Data Preprocessing**  
   - **Drop irrelevant columns**: Remove columns identified as non-contributory during EDA.  
   - **Handle invalid values**: Replace invalid values with `numpy.nan` for imputation.  
   - **Impute null values**: Use the **KNN imputer** to fill missing values.  
   - **Scale the data**: Scale the data for consistency.  

3. **Clustering**  
   - Load the **KMeans model** trained during the model training phase.  
   - Predict clusters for the preprocessed prediction data.  

4. **Prediction**  
   - Based on the predicted cluster, load the corresponding trained model.  
   - Generate predictions for the data in that cluster.  

5. **Output Results**  
   - Combine predictions across all clusters.  
   - Save the predictions along with the original labels (before encoding) in a CSV file at a specified location.  
   - Return the file location to the client.  
