from yoyo import step

__depends__ = {}

UP_QUERY = """
CREATE TABLE `category_grup` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nm_grup` varchar(100) NOT NULL,
  `is_no_use` tinyint(1) NOT NULL DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8
"""

DOWN_QUERY = """
DROP TABLE category_grup
"""

steps = [
    step(UP_QUERY, DOWN_QUERY),
]