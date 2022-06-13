CREATE TABLE IF NOT EXISTS json_tables
(
    id INT NOT NULL AUTO_INCREMENT,
    title varchar(100) NOT NULL,
    json_datas JSON DEFAULT NULL,
    PRIMARY KEY (id)
);