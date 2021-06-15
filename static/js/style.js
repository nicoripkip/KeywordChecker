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


let download_excel = document.getElementById('download-excel');
let download_csv = document.getElementById('download-csv');
let download_txt = document.getElementById('download-txt');

download_excel.onclick = () => {
    $("#table_id").table2excel({
        name: 'dataset',
        filename: 'dataset',
        fileext: 'xlsx'
    })
}

download_csv.onclick = () => {
    let csv = export_table_to_csv();

    file = new Blob([csv], { 
        type: "text/csv",
    });

    download_csv.href = window.URL.createObjectURL(file);

    download_csv.click();
}

download_txt.onclick = () => {
    let txt = export_table_to_csv();

    file = new Blob([csv], {
        type: 'text/txt',
    });

    download_txt.href = window.URL.createObjectURL(file);

    download_txt.click();
}


function export_table_to_csv() {
    let csv = [];
    let head = document.querySelector("table thead tr");
    let body = document.querySelector("table tbody tr");

    console.log(head);

    for (let i = 0; i < head.parentNode.children.length; i++) {
        let row = [];
        let cols = head.parentNode.children[i].querySelectorAll("td");
        
        console.log(i);

        for (let j = 0; j < cols.length; j++) {
            row.push(cols[j].innerText);
        }
        csv.push(row.join(", "))
    }

    for (let i = 0; i < body.parentNode.children.length; i++) {
        let row = [];
        let cols = body.parentNode.children[i].querySelectorAll("td");
        
        for (let j = 0; j < cols.length; j++) {
            row.push(cols[j].innerText);
        }
        csv.push(row.join(", "))
    }

    return csv;
}