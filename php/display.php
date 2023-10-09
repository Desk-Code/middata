<?php

$conn = mysqli_connect("localhost", "root", "", "db1");

echo "<table border='1'>";

$sql = "select * from emp";
$res = mysqli_query($conn, $sql);

while ($row = mysqli_fetch_array($res)) {
    echo "<tr><td>" . $row[0] . "</td><td>" . $row[1] . "</td><td>" . $row[2] . "</td>";
    echo "<td><a href='update.php?id=$row[0]'>Update</a></td>";
    echo "<td><a href='delete.php?id=$row[0]'>Delete</a></td>";
}

echo "<a href='form.php'>Insert New Data</a></br>";
echo "<a href='search.php'>Search</a></br>";


?>