$(function () {
    $('#datetimepicker').datetimepicker({
        format: 'DD/MM/YYYY HH:mm',  // Formato de data e hora
        defaultDate: moment(),       // Define a data e hora atuais como padrão
        locale: 'pt-br'              // Define o idioma como português brasileiro
    });
});
