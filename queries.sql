-- 1. Database and Table Setup
CREATE DATABASE JapanTourismDB;
USE JapanTourismDB;

CREATE TABLE tourism_data (
    Year INT,
    Country VARCHAR(50),
    Tourists_Count INT,
    Avg_Spend_JPY INT,
    Primary_Purpose VARCHAR(50),
    Total_Revenue_JPY BIGINT
);

-- 2. Advanced SQL Analysis Queries

-- Query A: Calculate Total Revenue and Average Spend per Year
SELECT 
    Year, 
    SUM(Tourists_Count) AS Total_Tourists,
    SUM(Total_Revenue_JPY) AS Total_Revenue_Generated_JPY
FROM tourism_data
GROUP BY Year
ORDER BY Year DESC;

-- Query B: Calculate Year-over-Year (YoY) Growth Percentage using Window Functions
SELECT 
    Year,
    Tourists_Count,
    LAG(Tourists_Count, 1) OVER (ORDER BY Year) AS Previous_Year_Tourists,
    ROUND(((Tourists_Count - LAG(Tourists_Count, 1) OVER (ORDER BY Year)) / LAG(Tourists_Count, 1) OVER (ORDER BY Year)) * 100, 2) AS YoY_Growth_Percent
FROM tourism_data;
