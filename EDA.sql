--TOTAL COUNT
SELECT COUNT(*) FROM housing_data;

--CHECKING FOR DULPICATE ENTRIES
SELECT id,COUNT(*) FROM housing_data GROUP BY ID HAVING COUNT(*) > 1;

--AVERAGE PRICE AND AVERAGE PRICE PER SQUARE FOOT BY STATE
SELECT 
    AVG(price_in_lakhs) AS avg_price, 
    AVG(price_per_sqft) AS avg_sqft_price, 
    state 
FROM housing_data AS h
GROUP BY state
ORDER BY avg_price DESC;

--AVERAGE PRICE AND AVERAGE PRICE PER SQUARE FOOT BY CITY
SELECT 
    city,
    AVG(price_in_lakhs) AS "avg_price_(lakhs)",
    AVG(price_per_sqft) AS "avg_sqft_price"
FROM housing_data AS h
GROUP BY city
ORDER BY "avg_price_(lakhs)" DESC;

--DISTRIBUTION OF PRICE PER SQUARE FOOT BY PROPERTY TYPE
SELECT 
    property_type,
    AVG(price_per_sqft) AS avg_sqft_price,
    MAX(price_per_sqft) AS max_sqft_price
FROM housing_data AS h
GROUP BY property_type
ORDER BY avg_sqft_price DESC;

--MEDIAN AGE OF PROPERTIES
SELECT 
    locality,
    AVG(age_of_property) AS median_age
FROM housing_data AS h
GROUP BY locality
ORDER BY median_age DESC;

--DISTRIBUTION OF BHK ACROSS CITIES
SELECT
    city,
    COUNT(*) AS total_properties,
    SUM(CASE WHEN bhk = 1 THEN 1 ELSE 0 END) AS bhk_1_count,
    SUM(CASE WHEN bhk = 2 THEN 1 ELSE 0 END) AS bhk_2_count,
    SUM(CASE WHEN bhk = 3 THEN 1 ELSE 0 END) AS bhk_3_count,
    SUM(CASE WHEN bhk >= 4 THEN 1 ELSE 0 END) AS bhk_4_plus_count
FROM housing_data AS h
GROUP BY city
ORDER BY total_properties DESC;

--RELATIONSHIP BETWEEN NEARBY SCHOOLS AND PRICE
SELECT
    nearby_schools,
    AVG(price_in_lakhs) AS avg_price
FROM housing_data AS h
GROUP BY nearby_schools
ORDER BY avg_price DESC;    

--RELATIONSHIP BETWEEN NEARBY HOSPITALS AND PRICE
SELECT
    nearby_hospitals,
    AVG(price_in_lakhs) AS avg_price
FROM housing_data AS h
GROUP BY nearby_hospitals
ORDER BY avg_price DESC;  

--PRICE DISTRIBUTION BASED ON FURNISHED STATUS
SELECT
   furnished_status,
   AVG(price_in_lakhs) AS avg_price
FROM housing_data AS h
GROUP BY furnished_status
ORDER BY avg_price DESC;  

--PRICE DISTRIBUTION BASED ON FACING
SELECT
   facing,
   AVG(price_in_lakhs) AS avg_price
FROM housing_data AS h
GROUP BY facing
ORDER BY avg_price DESC;   

--PROPERTY DISTRIBUTION BY OWNER TYPE
SELECT 
   owner_type,
   COUNT(*) AS total_properties,
   AVG(price_in_lakhs) AS avg_price
FROM housing_data AS h
GROUP BY owner_type
ORDER BY total_properties DESC;

--PROPERTY DISTRIBUTION BASED ON AVAILABILITY STATUS
SELECT
   availability_status,
   COUNT(*) AS total_properties
FROM housing_data AS h
GROUP BY availability_status
ORDER BY total_properties DESC;

--RELATIONSHIP BETWEEN PROPERTY SIZE AND PARKING LOT
SELECT
    AVG(size_in_sqft) AS avg_size_in_sqft,
    parking_space
FROM housing_data AS h
GROUP BY parking_space 
ORDER BY avg_size_in_sqft DESC;  

--RELATIONSHIP BETWEEN PRICE AND AMENITIES
SELECT
    amenities,
    AVG(price_in_lakhs) AS avg_price
FROM housing_data AS h
GROUP BY amenities
ORDER BY avg_price DESC;    


