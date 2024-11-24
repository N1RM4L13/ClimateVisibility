# Climate Visibility Prediction

## Problem Statement
Poor visibility caused by adverse climatic conditions—such as fog, rain, or snow—poses significant challenges in disaster management, including increased risks of transportation accidents, delays in rescue operations, and reduced efficiency in emergency response. Predicting visibility distances under varying weather conditions remains a critical need to ensure public safety and effective disaster mitigation.

## Sections
1. [Dataset Description](dataset/README.md)
2. [Training Workflow](training/README.md)
3. [Prediction Workflow](prediction/README.md)

## Application Flow
<img src="assets\appDiagram.png" alt="Climate Visibility Overview" width="500" height="500">

## Run Locally

1. Clone the project
```bash
  git https://github.com/N1RM4L13/ClimateVisibility.git

2. Install dependencies
```bash
  pip install -r requirements.txt
```

3. Start the Service

```bash
  python main.py
```

4. The API will start running on http://127.0.0.1:5000 by default (or any specified port in your configuration).

5. You can test the API using tools like Postman or cURL.

To test the API, use the following cURL command with JSON input:
```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{"filepath":"Prediction_Batch_Files"}'
```
Alternatively, if you prefer to use localhost instead of the IP address, you can replace http://127.0.0.1:5000 with http://localhost:5000 in the cURL command.

## Use Case
A regression model is developed to predict visibility distances based on climatic indicators such as temperature, humidity, precipitation, wind speed, and air pressure. This tool can be used by disaster management agencies to:

- **Enhance Transportation Safety:** Provide early warnings to reduce accidents on roads, railways, and air routes.
- **Optimize Rescue Operations:** Plan and execute rescue missions effectively by understanding visibility constraints in real-time.
- **Improve Emergency Planning:** Enable proactive responses by integrating visibility forecasts into disaster preparedness strategies, such as deploying resources or issuing alerts in affected regions.
