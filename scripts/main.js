let table = new DataTable('#myTable', {
    responsive: true,

    // set column priorities
    columnDefs: [
      { responsivePriority: 1, targets: 1 }, // title
      { responsivePriority: 2, targets: 2 }, // author
      { responsivePriority: 3, targets: 0 }, // row number column
    ],

    // add column controls
    columnControl: ['order', ['orderAsc', 'orderDesc', 'search']],
});
