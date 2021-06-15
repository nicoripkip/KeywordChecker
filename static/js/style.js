let table_data = document.getElementById('result-table-tbody').children;
let filter = document.getElementById('filter-word');


filter.onchange = () => {
    data = filter_word(filter.value)

    t = table_data[0].parentNode;

    clear_table();

    for (let i = 0; i < data.length; i++) {
        t.appendChild(data[i]);
    }
}


function filter_word(word) {
    result = [];

    for (let i = 0; i < table_data.length; i++) {
        if (table_data[i].children[1].textContent.includes(word) && word != "") {
            console.log(table_data[i].children[1].textContent)
            
            result.push(table_data[i]);
        } else {
            result.push(    [i]);
        }
    }

    return result;
}


function clear_table() {
    let t = table_data[0].parentNode;

    while(t.firstChild) {
        t.removeChild(t.lastChild);
    }
}


$('#table_id').DataTable({
    "paging": true,
    "lengthChange": false,
    "pageLength": 100,
    "searching": false,
    "ordering": true,
    "info": true,
    "autoWidth": false,
    "responsive": true,
    "language": {
        "url": "//cdn.datatables.net/plug-ins/1.10.24/i18n/Dutch.json",
    },
});