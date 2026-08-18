CREATE DATABASE IF NOT EXISTS ai_it_operations;

USE ai_it_operations;
USE ai_it_operations;

SELECT COUNT(*) AS Total_Tickets
FROM tickets;
SELECT
    Department,
    COUNT(*) AS Total_Tickets,
    ROUND(AVG(Resolution_Hours), 2) AS Avg_Resolution_Hours,
    ROUND(AVG(CSAT), 2) AS Avg_CSAT
FROM tickets
GROUP BY Department
ORDER BY Total_Tickets DESC;
SELECT
    Department,
    COUNT(*) AS Total_Tickets,
    SUM(SLA_Breach) AS SLA_Breaches,
    ROUND(SUM(SLA_Breach) * 100.0 / COUNT(*), 2) AS SLA_Breach_Rate
FROM tickets
GROUP BY Department
ORDER BY SLA_Breach_Rate DESC;
SELECT
    AI_Predicted_Priority,
    COUNT(*) AS Predicted_Tickets,
    ROUND(AVG(AI_Priority_Score), 2) AS Avg_AI_Score,
    ROUND(AVG(AI_Confidence), 2) AS Avg_AI_Confidence
FROM tickets
GROUP BY AI_Predicted_Priority
ORDER BY Predicted_Tickets DESC;
SELECT
    Priority AS Actual_Priority,
    AI_Predicted_Priority,
    COUNT(*) AS Ticket_Count
FROM tickets
GROUP BY
    Priority,
    AI_Predicted_Priority
ORDER BY
    Priority,
    Ticket_Count DESC;
    SELECT
    COUNT(*) AS Total_Tickets,
    SUM(
        CASE
            WHEN Priority = AI_Predicted_Priority THEN 1
            ELSE 0
        END
    ) AS Correct_Predictions,
    ROUND(
        SUM(
            CASE
                WHEN Priority = AI_Predicted_Priority THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS AI_Alignment_Percentage
FROM tickets;
SELECT
    Department,
    COUNT(*) AS Total_Tickets,
    SUM(SLA_Breach) AS SLA_Breaches,
    ROUND(
        SUM(SLA_Breach) * 100.0 / COUNT(*),
        2
    ) AS SLA_Breach_Rate
FROM tickets
GROUP BY Department
ORDER BY SLA_Breach_Rate DESC;
SELECT
    Priority AS Actual_Priority,
    AI_Predicted_Priority,
    COUNT(*) AS Ticket_Count
FROM tickets
GROUP BY
    Priority,
    AI_Predicted_Priority
ORDER BY
    Priority,
    Ticket_Count DESC;