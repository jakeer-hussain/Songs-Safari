function addReview() {
    var name = document.getElementById("name").value;
    var rating = document.querySelector('input[name="rating"]:checked').value;
    var review = document.getElementById("review").value;

    // Create a new table row and cells
    var table = document.getElementById("reviewsTable");
    var row = table.insertRow();
    var nameCell = row.insertCell(0);
    var ratingCell = row.insertCell(1);
    var reviewCell = row.insertCell(2);

    // Set the values of the cells
    nameCell.innerHTML = name;
    ratingCell.innerHTML = rating;
    reviewCell.innerHTML = review;

    // Reset the form
    document.getElementById("name").value = "";
    document.querySelector('input[name="rating"]:checked').checked = false;
    document.getElementById("review").value = "";
  }