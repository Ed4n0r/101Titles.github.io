<?php
if (isset($_GET['search'])) {
  $search = $_GET['search'];
  
  $files = array_diff(scandir('uploads'), array('.', '..'));
  $filteredFiles = array_filter($files, function($file) use ($search) {
    return stripos($file, $search) !== false;
  });

  echo json_encode(['files' => $filteredFiles]);
} else {
  echo json_encode(['files' => []]);
}
?>