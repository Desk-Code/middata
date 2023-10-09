<?php

$conn = mysqli_connect("localhost", "root", "", "db1");
if (isset($_GET['id'])) {
    $sql = "delete from emp where e_id =" . $_GET['id'];
    mysqli_query($conn, $sql);

    header("location:display.php");

}

?>