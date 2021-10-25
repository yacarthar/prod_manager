-- insert sample records

insert into "user" (username) values ('Tony'), ('Adam'), ('Maldini'), ('Sully');
insert into category (name) values ('food'), ('vehicle'), ('electronic'), ('clothes');
insert into product (name, price, category_id) values
	('coconut', 200, 1),
	('orange', 300, 1),
	('apple', 400, 1),
	('lemon', 250, 1),
	('mercedes', 4000, 2),
	('audi', 5000, 2),
	('toyota', 300, 2),
	('samsung phone', 2000, 3),
	('huawei phone', 2500, 3),
	('macbook', 5000, 3),
	('adidas', 800, 4)
;
insert into "order" (user_id) values (1), (1), (2), (2), (3), (3), (4), (4);

insert into order_detail (amount, product_id, order_id) values
	(1, 1, 1),
	(2, 2, 2),
	(3, 3, 3),
	(4, 4, 4),
	(5, 5, 5),
	(6, 6, 6),
	(7, 7, 7),
	(8, 8, 8)
;