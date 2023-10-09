<?php

$conn = mysqli_connect("localhost", "root", "", "db1");

$sql = "create table Emp(
    e_id int primary key AUTO_INCREMENT,
    name varchar(20),
    pass varchar(20)
)";

mysqli_query($conn, $sql);

echo "Table Created Successfully";

?>