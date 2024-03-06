<?php
// Get the search query from the URL parameter
if(isset($_GET['q'])) {
    $query = urlencode($_GET['q']);

    // Redirect to Google search with the query
    header("Location: https://www.google.com/search?q=$query");
    exit;
} else {
    // If no query is provided, redirect to homepage
    header("Location: index.html");
    exit;
}
?>
