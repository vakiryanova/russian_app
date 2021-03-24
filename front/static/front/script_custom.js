function exercise_processing(model_name, data){
    //model_name - название модели (таблицы) для бэка
    //model_name - список словарей с данными

    var word_inputs = document.querySelectorAll(".word-input"); //все окошки ввода
    var word_checks = document.querySelectorAll(".word-check"); //все кнопочки для проверки
    var words_left = word_inputs.length; //счетчик заданий которые еще не решили

    //возвращает элемент с заданым id
    function get_answer(word_id){
        for (var i=0; i<data.length; i++){
            if (Number(data[i]['id']) == Number(word_id)){
                return data[i]}
            else
                console.log('-')
        }
    };

    // убираем выделение красным с окошка ввода
    word_inputs.forEach(function(elem) {
        elem.addEventListener("click", function() {
            elem.classList.remove('red-outline');
        })});

    // обработка нажатия кнопок проверки
    word_checks.forEach(function(elem) {
        elem.addEventListener("click", function() {
            var word_id = elem.id.split('-')[1] //парсим нажатую кнопку чтобы получить id задания (id как в базе)
            var answer = document.getElementById("word-"+word_id) //получаем окно ввода рядом с этой кнопкой
            if (answer.value==''){ //если окно пустое выделяем красным
                answer.classList.add('red-outline');
                return
            }
            else{
                var true_answer = get_answer(word_id) //правильный ответ
                if (answer.value == true_answer.answer){ //если все ок выделяем зеленым
                    answer.style.borderColor = 'green'
                    true_answer['correct'] = true //помечаем как правильное
                }
                else
                    answer.style.borderColor = 'red'
                answer.disabled = true //вырубаем кнопку и ввод
                elem.disabled = true
                words_left-=1
            }

            if (words_left == 0)
                document.getElementById("submit").disabled = false; //когда все задания прошли включаем кнопку Завершить
        });
    });

    // обработка нажатия кнопки Завершить 
    document.getElementById("submit").addEventListener('click', function(){
        const XHR = new XMLHttpRequest();

        XHR.open( 'POST', '/exercises/end/' );
        XHR.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

        XHR.send(JSON.stringify({'model_name': model_name, 'data': data})); //отправка данных на бэк
        window.location.href = "/exercises"; //переброс на страницу тестов
    });
}