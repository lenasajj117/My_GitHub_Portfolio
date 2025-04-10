<?php
// Enable error reporting
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database credentials
$servername = "localhost";
$username = "root";
$password = ""; // Update if you set a password for MySQL
$dbname = "login";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} else {
    echo "Database connection successful!";
}
$conn->close();
?>
