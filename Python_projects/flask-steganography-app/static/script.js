document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("hideForm").addEventListener("submit", function(event) {
        event.preventDefault();
        alert("Text hidden in image! (Backend processing required)");
    });

    document.getElementById("extractForm").addEventListener("submit", function(event) {
        event.preventDefault();
        alert("Extracting hidden text... (Backend processing required)");
    });
});
