<?php
if (isset($_POST['file'])) {
  $file = 'uploads/' . basename($_POST['file']);

  if (file_exists($file)) {
    unlink($file);
    echo json_encode(['success' => true]);
  } else {
    echo json_encode(['success' => false]);
  }
} else {
  echo json_encode(['success' => false]);
}
?>