// Desbloquear el UI al finalizar la operacion AJAX
// --------------------------------------------------
$(document).ajaxStop($.unblockUI); 



// Esconder los botones de resultado de las pruebas al cargar la interfaz
// -----------------------------------------------------------------------
$(document).ready(function () {
    $("#pass-1").hide();
    $("#fail-1").hide();
    $("#pass-2").hide();
    $("#fail-2").hide();
    $("#pass-3").hide();
    $("#fail-3").hide();
    $("#pass-4").hide();
    $("#fail-4").hide();
    $("#pass-5").hide();
    $("#fail-5").hide();
    $("#pass-6").hide();
    $("#fail-6").hide();
    $("#pass-7").hide();
    $("#fail-7").hide();
});


// Al hacer click en el boton PROBAR 
// ---------------------------------------------------
$("#probar-1").on("click", function () {
    $.blockUI({ message: '<h1><img src="https://tamilnaducouncil.ac.in/wp-content/uploads/2018/10/loading-gif.gif" /> Ejecuntando Prueba..</h1>' });
    $.ajax({
        type: 'POST',
        url: './pruebas',
        data: '{"prueba_id":1}',
        success: function (data) {
            if (data.prueba == 'pass') {
                $("#pass-1").show();
            } else {
                $("#fail-1").show();
            }
        },
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
        success: function (data) {
            if (data.prueba == 'pass') {
                $("#pass-2").show();
            } else {
                $("#fail-2").show();
            }
        },
        contentType: "application/json",
        dataType: 'json'
    });
});

$("#probar-3").on("click", function () {
    $.blockUI({ message: '<h1><img src="https://tamilnaducouncil.ac.in/wp-content/uploads/2018/10/loading-gif.gif" /> Ejecuntando Prueba..</h1>' });
    $.ajax({
        type: 'POST',
        url: './pruebas',
        data: '{"prueba_id":3}',
        success: function (data) {
            if (data.prueba == 'pass') {
                $("#pass-3").show();
            } else {
                $("#fail-3").show();
            }
        },
        contentType: "application/json",
        dataType: 'json'
    });
});

$("#probar-4").on("click", function () {
    $.blockUI({ message: '<h1><img src="https://tamilnaducouncil.ac.in/wp-content/uploads/2018/10/loading-gif.gif" /> Ejecuntando Prueba..</h1>' });
    $.ajax({
        type: 'POST',
        url: './pruebas',
        data: '{"prueba_id":4}',
        success: function (data) {
            if (data.prueba == 'pass') {
                $("#pass-4").show();
            } else {
                $("#fail-4").show();
            }
        },
        contentType: "application/json",
        dataType: 'json'
    });
});

$("#probar-5").on("click", function () {
    $.blockUI({ message: '<h1><img src="https://tamilnaducouncil.ac.in/wp-content/uploads/2018/10/loading-gif.gif" /> Ejecuntando Prueba..</h1>' });
    $.ajax({
        type: 'POST',
        url: './pruebas',
        data: '{"prueba_id":5}',
        success: function (data) {
            if (data.prueba == 'pass') {
                $("#pass-5").show();
            } else {
                $("#fail-5").show();
            }
        },
        contentType: "application/json",
        dataType: 'json'
    });
});

$("#probar-6").on("click", function () {
    $.blockUI({ message: '<h1><img src="https://tamilnaducouncil.ac.in/wp-content/uploads/2018/10/loading-gif.gif" /> Ejecuntando Prueba..</h1>' });
    $.ajax({
        type: 'POST',
        url: './pruebas',
        data: '{"prueba_id":6}',
        success: function (data) {
            if (data.prueba == 'pass') {
                $("#pass-6").show();
            } else {
                $("#fail-6").show();
            }
        },
        contentType: "application/json",
        dataType: 'json'
    });
});

$("#probar-7").on("click", function () {
    $.blockUI({ message: '<h1><img src="https://tamilnaducouncil.ac.in/wp-content/uploads/2018/10/loading-gif.gif" /> Ejecuntando Prueba..</h1>' });
    $.ajax({
        type: 'POST',
        url: './pruebas',
        data: '{"prueba_id":7}',
        success: function (data) {
            if (data.prueba == 'pass') {
                $("#pass-7").show();
            } else {
                $("#fail-7").show();
            }
        },
        contentType: "application/json",
        dataType: 'json'
    });
});