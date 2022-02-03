var name_search = document.getElementById('name_form');
id_search.onsubmit = function(e) {
    e.preventDefault();
    var form = new FormData(id_search);
    fetch("http://localhost:5000/search/name", {method:'POST', body:form})
        .then(response => response.json())
        .then(data => console.log(data))
}