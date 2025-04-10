<?php
session_start();
error_reporting(E_ALL);
ini_set('display_errors', 1);

if (!isset($_SESSION['user_id'])) {
    header("Location: login.html"); // Redirect to login if not logged in
    exit();
}

echo "Welcome to the dashboard!";
?>

<a href="logout.php">Logout</a>
