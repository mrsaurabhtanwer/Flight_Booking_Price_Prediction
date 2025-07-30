# ✈️ Flight Booking Price Prediction

Predict airline ticket prices using machine learning based on historical booking data. This project demonstrates a typical end-to-end data science workflow from data cleaning and feature engineering to model development, evaluation, and price prediction.

## 📌 Project Overview

- **Goal:** Predict the price of airline tickets based on input features such as airline, route, timings, stops, duration, etc.
- **Why:** Helps travelers find the best time to book, informs airline pricing strategies, and serves as a valuable machine learning case study.
- **Use Cases:** Travel agencies, airline revenue teams, travel apps, ML learning modules.

## 📁 Dataset

- **File:** `Flight_Booking.csv`
- **Main Features:** Airline, Date_of_Journey, Source, Destination, Route, Duration, Total_Stops, Additional_Info, Price

## 🛠️ Workflow

1. **Data Preprocessing**
   - Handling missing values
   - Encoding categorical variables
   - Parsing and transforming columns (dates, times)
2. **Feature Engineering**
   - Extracting useful attributes (day, month, duration in minutes, etc.)
   - Dropping irrelevant columns
3. **Model Building**
   - Tested various regressors
   - **Best Model:** Random Forest Regressor
4. **Evaluation**
   - R² Score ~0.98 (very high)
   - Visualization of predictions vs. actuals
5. **Prediction**
   - Feed input features → Get price prediction

## 🔍 Algorithms Used

- **Random Forest Regressor** (best results)
- Benchmarked vs. Linear Regression, Decision Tree, etc.

## 📈 Results

- **Accuracy:** R² ≈ 0.98
- **Outcome:** Highly accurate prediction with minimal errors on test data
- **Feature Importance:** Explored which inputs have the most impact on price

| Feature Example | Value          |
|-----------------|---------------|
| Airline         | Indigo        |
| Date_of_Journey | 24/03/2019    |
| Source          | Delhi         |
| Destination     | Cochin        |
| ...             | ...           |
| **Predicted Price** | ₹ 6,745    |

## 🚀 How to Use

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/Flight_Booking_Price_Prediction.git
   cd Flight_Booking_Price_Prediction
   ```
2. **Place `Flight_Booking.csv`** in the repo folder.
3. **Run the notebook or script** for model training and predictions.
4. **Modify/extend** as needed for your dataset/application.

## 💡 Applications

- **Consumers:** Book tickets at optimal times
- **Travel Agencies:** Power fare prediction engines
- **Airlines:** Revenue optimization & market analysis
- **Students:** Practice regression with real-world data

## 📝 Conclusion

- Random Forest Regressor provides excellent accuracy for flight fare prediction.
- Feature engineering/cleaning is crucial for model performance.
- Ready for extension or integration in larger applications.

## 🤝 Contributing

Contributions and suggestions are welcome!  
Fork the repo, raise an issue, or submit a pull request.

## 📄 License

Add your license here (e.g., MIT, Apache 2.0, etc.).

## 🙏 Acknowledgements

- Public datasets from Kaggle and open sources
- Python libraries: Pandas, Scikit-learn, Matplotlib
