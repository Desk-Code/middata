<?php

$conn = mysqli_connect("localhost", "root", "");
$sql = "create database db1";
mysqli_query($conn, $sql);
echo "Database Created";

?>