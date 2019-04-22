CREATE  VIEW `zentao`.`product` AS SELECT
	id,
NAME as p_name 
FROM
	zt_product 
WHERE
	deleted = '0'
	ORDER BY name ;