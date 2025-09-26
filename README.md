# https-classroom.github.com-a-Y7y-s1VG
cis2368

 Shopping List Application - Homework 1

Database Setup

Step 1: AWS RDS Configuration
- Created an AWS RDS MySQL instance with the following details:
  - Engine: MySQL
  - Instance Type: Free Tier
  - Public Accessibility: Enabled
  - Security Group: Configured to allow connections on port 3306 from my IP address.

Step 2: Database credentials
- Endpoint: `database1.cm5ge0qyc76x.us-east-1.rds.amazonaws.com`
- Username: `admin` (or the username you configured)
- Password: Jazib!23

Step 3: Database schema
- Created a database named `shopping_list_db`:
  ```sql
  CREATE DATABASE shopping_list_db;
  USE shopping_list_db;

#Created table
CREATE TABLE shopping_list (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    added_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

#Inserted at least 15 records
INSERT INTO shopping_list (item_name, quantity) VALUES ('Apples', 5);
INSERT INTO shopping_list (item_name, quantity) VALUES ('Bananas', 10);
INSERT INTO shopping_list (item_name, quantity) VALUES ('Oranges', 7);
INSERT INTO shopping_list (item_name, quantity) VALUES ('Milk', 2);
INSERT INTO shopping_list (item_name, quantity) VALUES ('Bread', 1);
INSERT INTO shopping_list (item_name, quantity) VALUES ('Eggs', 12);
INSERT INTO shopping_list (item_name, quantity) VALUES ('Cheese', 3);
INSERT INTO shopping_list (item_name, quantity) VALUES ('Butter', 1);
INSERT INTO shopping_list (item_name, quantity) VALUES ('Rice', 4);
INSERT INTO shopping_list (item_name, quantity) VALUES ('Pasta', 3);
INSERT INTO shopping_list (item_name, quantity) VALUES ('Tomatoes', 6);
INSERT INTO shopping_list (item_name, quantity) VALUES ('Potatoes', 8);
INSERT INTO shopping_list (item_name, quantity) VALUES ('Onions', 4);
INSERT INTO shopping_list (item_name, quantity) VALUES ('Chicken', 2);
INSERT INTO shopping_list (item_name, quantity) VALUES ('Beef', 3);

#Verified the database connection

mysql -h database1.cm5ge0qyc76x.us-east-1.rds.amazonaws.com -u admin -p

#Ran test queries for functionality
SELECT * FROM shopping_list;