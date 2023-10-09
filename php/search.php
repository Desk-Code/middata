<html>

<body>
    <form>
        <table>
            <tr>
                <td>
                    Search by Id :
                </td>
                <td>
                    <input type="text" name="search">
                </td>
                <td>
                    <input type="submit" name="submit">
                </td>
            </tr>
        </table>
    </form>

</body>

</html>

<?php

$conn = mysqli_connect("localhost", "root", "", "db1");
if (isset($_GET['search'])) {

    echo "<table border='1'>";

    $sql = "select * from emp where e_id =" . $_GET['search'];
    $res = mysqli_query($conn, $sql);

    while ($row = mysqli_fetch_array($res)) {
        echo "<tr><td>" . $row[0] . "</td><td>" . $row[1] . "</td><td>" . $row[2] . "</td></tr>";
    }
}

echo "<a href='display.php'>Display Page</a></br>";

?>