$(document).ready(function() {
    $('#accordeon .item1').on('click', acc);
});

function acc(){
//скрываем все кроме того, что должны открыть
  $('#accordeon .item2').not($(this).next()).slideUp(500);
// открываем или скрываем блок под заголовоком, по которому кликнули
    $(this).next().slideToggle(500);
}
