<?php

$conn = mysqli_connect("localhost", "root", "", "db1");
if (isset($_GET['id'])) {
    $sql = "select * from emp where e_id =" . $_GET['id'];
    $res = mysqli_query($conn, $sql);
    $row = mysqli_fetch_array($res);
}

?>

<html>

<body>
    <form>
        <table>
            <input type="hidden" name="hdn" value="<?php echo "$row[0]" ?>">
            <tr>
                <td>
                    Name :
                </td>
                <td>
                    <input type="text" name="name" value="<?php echo "$row[1]" ?>">
                </td>
            </tr>
            <tr>
                <td>

                    Pass :
                </td>
                <td>
                    <input type="text" name="pass" value="<?php echo "$row[2]" ?>">
                </td>

            </tr>
            <tr>
                <td colspan="2" align="center">
                    <input type="submit" name="submit">
                </td>
            </tr>
        </table>
    </form>
</body>

</html>

<?php

$conn = mysqli_connect("localhost", "root", "", "db1");
$id = $name = $pass = "";
if (isset($_GET['submit'])) {
    $id = $_GET['hdn'];
    $name = $_GET['name'];
    $pass = $_GET['pass'];
    $sql = "update emp set name = '" . $name . "', pass = '" . $pass . "' where e_id =" . $id;
    mysqli_query($conn, $sql);
    header("location:display.php");
}

?>