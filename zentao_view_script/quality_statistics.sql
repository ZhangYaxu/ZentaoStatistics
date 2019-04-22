CREATE  VIEW `zentao`.`quality_statistics` AS SELECT
  b.id as bug_id,
	p.name as product_name,
	u.realname as name,
	concat(p.name,u.realname) as id,
  u.deleted as user_delete, 
	u.dept as user_dept,
	b.confirmed,
	b.closedDate,
	b.severity,
	b.activatedCount
FROM
	zt_bug AS b
	LEFT JOIN zt_user AS u ON b.resolvedBy = u.account
	LEFT JOIN zt_product as p on b.product = p.id
WHERE u.deleted = '0'
AND b.confirmed = 1
AND u.dept = '3' 
ORDER BY id ;