$(document).ready(function() {

    // Wijets
    $.wijets().make();

	var oTable = $('#tabletools').dataTable({
        "language": {
            "lengthMenu": "_MENU_",
            "sProcessing":     "Procesando...",
            "sZeroRecords":    "No se encontraron resultados",
            "sEmptyTable":     "Ningún dato disponible en esta tabla",
            "sInfo":           "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
            "sInfoEmpty":      "Mostrando registros del 0 al 0 de un total de 0 registros",
            "sInfoFiltered":   "(filtrado de un total de _MAX_ registros)",
            "sInfoPostFix":    "",
            "sUrl":            "",
            "sInfoThousands":  ",",
            "sLoadingRecords": "Cargando...",
            "oPaginate": {
                "sFirst":    "Primero",
                "sLast":     "Último",
                "sNext":     "Siguiente",
                "sPrevious": "Anterior"
            },
            "oAria": {
                "sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
                "sSortDescending": ": Activar para ordenar la columna de manera descendente"
            }
        }
    });

	var tableTools = new $.fn.dataTable.TableTools( oTable, {
        "buttons": [
            "copy",
            "csv",
            "xls",
            "pdf",
            { "type": "print", "buttonText": "Print me!" }
        ],
        "sSwfPath" : "TableTools/swf/copy_csv_xls_pdf.swf"
    });



    //DOM Manipulation to move datatable elements integrate to panel

    $('#panel-tabletools .panel-ctrls').append("<i class='separator pull-right '></i>");

    $('#panel-tabletools .panel-ctrls').append($('.dataTables_length').addClass("pull-right"));
    $('#panel-tabletools .panel-ctrls .dataTables_length label').addClass("mb0");


    $('#panel-tabletools .panel-footer').append($(".dataTable+.row"));
    $('.dataTables_paginate>ul.pagination').addClass("pull-right");

});