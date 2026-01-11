-- CREATE USER 'analytics_user'@'localhost' IDENTIFIED BY 'analytics123';
GRANT ALL PRIVILEGES ON financial_fraud.* TO 'analytics_user'@'localhost';
FLUSH PRIVILEGES;
USE financial_fraud;
SELECT COUNT(*) FROM fraud_transactions;
SELECT * 
FROM fraud_transactions
LIMIT 10;
SELECT * FROM fraud_transactions;
