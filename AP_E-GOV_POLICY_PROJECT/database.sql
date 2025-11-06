CREATE TABLE housing_scheme (
    id INT AUTO_INCREMENT PRIMARY KEY,
    applicant_name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    family_income DECIMAL(10,2) NOT NULL,
    aadhar_card VARCHAR(16) NOT NULL UNIQUE,
    ration_card VARCHAR(16) NOT NULL,
    occupation VARCHAR(255) NOT NULL,
    district VARCHAR(255) NOT NULL,
    state VARCHAR(255) NOT NULL,
    contact_number VARCHAR(15) NOT NULL,
    submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);