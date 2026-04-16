<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST');
header('Access-Control-Allow-Headers: Content-Type');

$dataDir = __DIR__ . '/users/';
if (!file_exists($dataDir)) mkdir($dataDir, 0777, true);

$user = $_GET['user'] ?? $_POST['user'] ?? '';
if (!$user) die(json_encode(['error' => 'No user']));

$file = $dataDir . md5($user) . '.dat';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = file_get_contents('php://input');
    file_put_contents($file, $data);
    echo json_encode(['ok' => true]);
} else {
    if (file_exists($file)) {
        echo file_get_contents($file);
    } else {
        echo json_encode(['data' => null]);
    }
}
?>
