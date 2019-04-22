CREATE VIEW `zentao`.`dev_user` AS SELECT
	id,
	realname as name
FROM
	zt_user 
WHERE
	deleted = '0' 
	AND dept =3 
ORDER BY account ;