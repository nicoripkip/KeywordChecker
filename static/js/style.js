//let table_data = document.getElementById('result-table-tbody').children;
let filter = document.getElementById('filter-word');
let filter_min = document.getElementById('min_volume');
let filter_max = document.getElementById('max_volume');
let header_filter = document.getElementById('header-filter');
let header_download = document.getElementById('header-download');


if (window.location.pathname == "/") {
    window.location.reload()
}


filter.onkeyup = () => {
    let table_data = document.getElementById('result-table-tbody').children;
    console.log(table_data)
    
    data = filter_word(filter.value, table_data)

    t = table_data[0].parentNode;
}

function filter_word(word, table_data) {
    result = [];

    for (let i = 0; i < table_data.length; i++) {
        if (table_data[i].children[1].textContent.replace(" ", "").includes(word)) {
            console.log(table_data[i].children[1].textContent)
            table_data[i].style = "";
        } else {
            table_data[i].style = "display: none !important";
        }
    }

    return result;
}


filter_min.onkeyup = () => {
    let table_data = document.getElementById('result-table-tbody').children;

    for (let i = 0; i < table_data.length; i++) {
        if (parseFloat(table_data[i].children[2].textContent) < parseFloat(filter_min.value) ) {
            table_data[i].style = "";
        } else {
            console.log("iets")
            table_data[i].style = "display: none !important";
        }
    }
}


filter_max.onkeyup = () => {
    let table_data = document.getElementById('result-table-tbody').children;
 
    for (let i = 0; i < table_data.length; i++) {
        if (parseFloat(table_data[i].children[2].textContent) < filter_max.value && table_data[i].style.includes('display: none') != true) {
            table_data[i].style = "";
        } else {
            table_data[i].style = "display: none !important";
        }
    }
}

header_filter.onclick = () => {
    if (header_filter.parentNode.style.height == '450px') {
        header_filter.parentNode.style.height = '100px';
    } else {
        header_filter.parentNode.style.height = '450px';
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

    file = new Blob([txt], {
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