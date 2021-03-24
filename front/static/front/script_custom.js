function exercise_processing(model_name, data){
    var word_inputs = document.querySelectorAll(".word-input");
    var word_checks = document.querySelectorAll(".word-check");
    var words_left = word_inputs.length;


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
            var word_id = elem.id.split('-')[1]
            var answer = document.getElementById("word-"+word_id)
            if (answer.value==''){
                answer.classList.add('red-outline');
                return
            }
            else{
                var true_answer = get_answer(word_id)
                if (answer.value == true_answer.answer){
                    answer.style.borderColor = 'green'
                    true_answer['correct'] = true
                }
                else
                    answer.style.borderColor = 'red'
                answer.disabled = true
                elem.disabled = true
                words_left-=1
            }

            if (words_left == 0)
                document.getElementById("submit").disabled = false;
        });
    });

    // обработка нажатия кнопки
    document.getElementById("submit").addEventListener('click', function(){
        const XHR = new XMLHttpRequest();

        XHR.open( 'POST', '/exercises/end/' );
        XHR.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

        XHR.send(JSON.stringify({'model_name': model_name, 'data': data}));
        window.location.href = "/exercises";
    });
}