-- Query 1: Get all the shipping data
SELECT * FROM shipping_data;

-- Query 2: Get the total quantity of each product
SELECT product, SUM(product_quantity) AS total_quantity
FROM shipping_data
GROUP BY product;

-- Query 3: Get the count of shipments for each origin warehouse
SELECT origin_warehouse, COUNT(*) AS shipment_count
FROM shipping_data
GROUP BY origin_warehouse;

-- Query 4: Get the count of shipments for each destination store
SELECT destination_store, COUNT(*) AS shipment_count
FROM shipping_data
GROUP BY destination_store;

-- Query 5: Get the count of on-time shipments
SELECT COUNT(*) AS on_time_shipments
FROM shipping_data
WHERE on_time = 'Yes';



