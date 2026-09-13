https://202618015rachitzaverids605-tgrdbwpmrdwhyjvsecp8fr.streamlit.app/

Objective
The goal of this project is to build a complete, end-to-end machine learning workflow to estimate the nightly price of an Airbnb listing in New York City. The project moves from raw data cleaning to training a model, and finally deploying a user-friendly web application.

Task 1: Data Analysis and Preparation
To make the data readable for a machine learning model, we took a step-by-step approach using basic Pandas functions:

Handling Missing Values: Empty spaces in text columns (like names) were filled with the word "Unknown". Empty reviews per month were filled with 0.

Dropping Unnecessary Columns: We removed columns like id and host_id because a random ID number does not help predict a home's price.

Removing Outliers: The dataset contained extreme anomalies, like homes priced at $0 or $10,000 per night. We filtered the data to only include realistic prices between $1 and $1000 so the model wouldn't get confused by luxury outliers.

Feature Transformation: Models only understand math, not words. We used the simple pd.get_dummies() function to convert text categories (like "Manhattan" or "Private room") into simple 1s (yes) and 0s (no).

Task 2: Model Training and Evaluation
We tested two straightforward models to see which could learn the pricing patterns better:

Linear Regression: This model tried to draw a straight line through the data but struggled because housing prices do not follow a perfect straight line.

Decision Tree Regressor: This model acts like a flowchart of questions (e.g., "Is it an entire home?" -> "Is it in Brooklyn?"). This performed much better.

Overfitting Prevention: To stop the Decision Tree from just memorizing the training data, we set a max_depth of 10.

Final Performance: We evaluated the model using Mean Absolute Error (MAE), which tells us the average dollar amount the model's guess is off by. The Decision Tree was chosen as the final model and saved as a .pkl file.

Task 3: Application Results
The final model is deployed using a simple Streamlit web application. Users do not need to look at code; they can just use dropdown menus and number boxes to input details about an Airbnb listing. The app takes these inputs, translates them into the 1s and 0s the model needs, and instantly returns a realistic estimated nightly price.

Task 4: Limitations of the System
Ignoring Text Details: To keep the system simple and fast, we dropped the text descriptions. The model does not know the difference between a "Basic basement" and a "Luxury apartment with a view" if they share the same room type and neighborhood.

No Seasonality: The model assumes the price is exactly the same all year round. It cannot adjust for holidays, weekends, or tourist seasons.
