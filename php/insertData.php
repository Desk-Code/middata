<?php

$conn = mysqli_connect("localhost", "root", "", "db1");
$name = $pass = "";
if (isset($_GET['submit'])) {
    $name = $_GET['name'];
    $pass = $_GET['pass'];

    $sql = "Insert into Emp(name,pass) values('$name','$pass')";
    mysqli_query($conn, $sql);
    echo "Data inserted Successfully";
    header('location:display.php');
}

?>