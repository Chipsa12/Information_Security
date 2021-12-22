async function res(text, type) {
    const url = "http://localhost:9000/api/lab4";
    const output_text = document.querySelector('#output_text'); 
    try {
        const response = await fetch(url, {
            method: 'POST',
            body: `{"input_text": "${text}", "type_mode": "${type}"}`
        });
        response.json().then(data => {
            console.log(data);
            
            if (type == 'hash') {
                output_text.innerHTML =  data.answer.hash;
            } else {
                output_text.innerHTML = "Ошибка"
            }
        });  
    } catch (error) {
        output_text.innerHTML = "Ошибка"
    }
}

document.addEventListener('DOMContentLoaded', () => { 
    const hashBtn = document.querySelector('#hash_btn');
    

    hashBtn.addEventListener('click', () => {
        const text = document.querySelector('#hash_text').value;
        if (text != '') {
            res(text, 'hash');
        } else {
            alert('Введине сообщение');
        }
    });
})