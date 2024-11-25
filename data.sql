DELETE FROM brand;
INSERT INTO brand (`id`, `name`)
VALUES
(1, 'Pepsi'),
(2, 'Monster'),
(3, 'Fanta'),
(4, 'Coca_Cola'),
(5, 'Tropicana'),
(6, 'Nestle');



DELETE FROM product;
INSERT INTO product (`id`, `name`, `price`, `brand_id`)
VALUES
(1, 'Pepsi Cola', 1.50, 1),
(2, 'Coca_Cola', 1.50, 4),
(3, 'Fanta Orange', 1.40, 3),
(4, 'Monster Energy', 2.00, 2),
(5, 'Tropicana Juice', 2.50, 5),
(6, 'Nestle Water', 1.20, 6);



DELETE FROM technician;
INSERT INTO technician (`id`, `name`, `contact_info`)
VALUES
(1, 'John Doe', 'john.doe@example.com'),
(2, 'Jane Smith', 'jane.smith@example.com'),
(3, 'Michael Johnson', 'michael.johnson@example.com'),
(4, 'Emily Davis', 'emily.davis@example.com'),
(5, 'David Wilson', 'david.wilson@example.com');


DELETE FROM vendingmachine;
INSERT INTO vendingmachine (`id`, `address`, `gps_coordinates`, `last_restock_date`, `technician_id`)
VALUES
(1, '123 Main St, City A', '40.7128,-74.0060', '2024-10-01', 1),
(2, '456 Elm St, City B', '34.0522,-118.2437', '2024-10-02', 2),
(3, '789 Oak St, City C', '41.8781,-87.6298', '2024-10-03', 1),
(4, '321 Maple St, City D', '51.5074,-0.1278', '2024-10-04', 3),
(5, '654 Pine St, City E', '48.8566,2.3522', '2024-10-05', 2),
(6, '987 Cedar St, City F', '35.6762,139.6503', '2024-10-06', 1);

SELECT id, gps_coordinates FROM vendingmachine;


DELETE FROM menu;
INSERT INTO menu (`id`, `availability`, `product_id`, `vendingmachine_id`)
VALUES
(1, 11, 1, 1),
(2, 10, 2, 1),
(3, 15, 3, 2),
(4, 17, 4, 2),
(5, 13, 5, 3),
(6, 0, 6, 3);

DELETE FROM coincollection;
INSERT INTO coincollection(`id`, `collection_date`, `amount_collected`, `vendingmachine_id`)
VALUES
(1, '2024-10-01', 150.00, 1),
(2, '2024-10-02', 200.00, 1),
(3, '2024-10-03', 250.00, 2),
(4, '2024-10-04', 300.00, 2),
(5, '2024-10-05', 350.00, 3);


DELETE FROM coinrestock;
INSERT INTO coinrestock (`id`, `restock_date`, `amount`, `vendingmachine_id`)
VALUES
(1, '2024-10-01', 100.00, 1),
(2, '2024-10-02', 150.00, 1),
(3, '2024-10-03', 200.00, 2),
(4, '2024-10-04', 250.00, 2),
(5, '2024-10-05', 300.00, 3);



DELETE FROM stock;
INSERT INTO stock (`id`, `machine_id`, `quantity`)
VALUES
(1, 1, 100),
(2, 1, 24),
(3, 2, 32),
(4, 3, 3),
(5, 4, 5);



DELETE FROM sales;
INSERT INTO sales (`id`, `quantity_sold`, `sale_date`, `product_id`, `vendingmachine_id`)
VALUES
(1, 10, '2024-10-01', 1, 1),
(2, 5, '2024-10-01', 1, 2),
(3, 7, '2024-10-02', 2, 3),
(4, 12, '2024-10-02', 2, 1),
(5, 15, '2024-10-03', 3, 4);



DELETE FROM transactionlog;
INSERT INTO transactionlog (`id`, `transaction_date`, `amount`, `vendingmachine_id`, `technician_id`)
VALUES
(1, '2024-10-01', 200.00, 1, 1),
(2, '2024-10-02', 250.00, 1, 2),
(3, '2024-10-03', 300.00, 2, 3),
(4, '2024-10-04', 150.00, 2, 4),
(5, '2024-10-05', 400.00, 3, 5);


DELETE FROM feedback;
INSERT INTO feedback (id, vendingmachine_id, feedback_date, rating, comment)
VALUES
(1, 2, '2024-10-04', 150, 'Good performance, but could use some improvements.'),
(2, 3, '2024-10-05', 400, 'Excellent machine, works flawlessly!'),
(3, 1, '2024-10-06', 200, 'Machine works well, but some options are missing in the menu.'),
(4, 2, '2024-10-07', 100, 'Had some technical issues, didn’t work properly.'),
(5, 3, '2024-10-08', 350, 'Very efficient and quick service, very happy with it!');
