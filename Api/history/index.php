<?php
// include database and object files
include_once '../config/database.php';
include_once '../objects/user.php';
include_once '../objects/history.php';

// get database connection
$database = new Database();
$db = $database->getConnection();

// prepare user object
$user = new User($db);
$history = new History($db);
// set ID property of user to be edited
$user->username = isset($_POST['username']) ? $_POST['username'] : die();
$user->password = md5(isset($_POST['password']) ? $_POST['password'] : die());
// read the details of user to be edited
$stmt = $user->login();
if ($stmt->rowCount() > 0) {
    // get retrieved row
    $history = $history->list();
    if (!$history->rowCount()) {
        $finalResult = array(
            "status" => false,
            "message" => "Data is Empty!",
        );
    } else {
        $rows = $history->fetchAll(PDO::FETCH_ASSOC);

        // create array
        $finalResult = [];
        foreach ($rows as $row) {
            $finalResult[] = [
                'id' => $row['id'],
                'data' => $row['data'],
                'waktu' => $row['waktu'],
            ];
        }
    }
} else {
    $finalResult = array(
        "status" => false,
        "message" => "Invalid Username or Password!",
    );
}
// make it json format
print_r(json_encode($finalResult));
