// Desbloquear el UI al finalizar la operacion AJAX
// --------------------------------------------------
$(document).ajaxStop($.unblockUI); 



// Esconder los botones de resultado de las pruebas al cargar la interfaz
// -----------------------------------------------------------------------
$(document).ready(function () {
    $("#pass-1").hide();
    $("#pass-2").hide();
});


// Al hacer click en el boton PROBAR 
// ---------------------------------------------------
$("#probar-1").on("click", function () {
    $.blockUI({ message: '<h1><img src="https://tamilnaducouncil.ac.in/wp-content/uploads/2018/10/loading-gif.gif" /> Ejecuntando Prueba..</h1>' });
    $.ajax({
        type: 'POST',
        url: './pruebas',
        data: '{"prueba_id":1}',
        success: function (data) {console.log(data.id)},
        contentType: "application/json",
        dataType: 'json'
    });
});

$("#probar-2").on("click", function () {
    $.blockUI({ message: '<h1><img src="https://tamilnaducouncil.ac.in/wp-content/uploads/2018/10/loading-gif.gif" /> Ejecuntando Prueba..</h1>' });
    $.ajax({
        type: 'POST',
        url: './pruebas',
        data: '{"prueba_id":2}',
        success: function (data) {console.log(data.id)},
        contentType: "application/json",
        dataType: 'json'
    });
});