document.addEventListener("DOMContentLoaded", function(event) {
    document.querySelector('.answer').onclick = myClick;

    function myClick(){
        let a = document.querySelector('.form-control').value;
        if (a != ''){
            if (a == document.querySelector('.otvet').innerHTML) {
                alert( 'Да вы знаток!' );
            } else {
            alert( 'А вот и неправильно!' );}
        document.querySelector('.form-control').value = '';
        }else{
        alert('Введите ответ!');}
    }
});