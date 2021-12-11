async function res(text, type) {
    const url = "http://localhost:9000/api/lab3";
    const output_text = document.querySelector('#decipher_output_text'); 
    try {
        const response = await fetch(url, {
            method: 'POST',
            body: `{"input_text": "${text}", "type_mode": "${type}"}`
        });
        response.json().then(data => {
            console.log(data);
            
            if (type == '-s') {
                str = '';
                for(let i=0; i < data.answer.result.length; i++) {
                    str += data.answer.result[i] + ' '
                }
                output_text.innerHTML = str;
            } else if (type == '-d') {
                output_text.innerHTML = data.answer.result;
            } else {
                output_text.innerHTML = "Ошибка"
            }
        });  
    } catch (error) {
        output_text.innerHTML = "Ошибка"
    }
}

document.addEventListener('DOMContentLoaded', () => { 
    const encryptionBtn = document.querySelector('#encryption_btn');
    const decipherBtn = document.querySelector('#decipher_btn');
    

    encryptionBtn.addEventListener('click', () => {
        const text = document.querySelector('#encryption_text').value;
        if (text != '') {
            res(text, '-s');
        } else {
            alert('Введине сообщение');
        }
    });

    decipherBtn.addEventListener('click', () => {
        const text = document.querySelector('#encryption_text').value;
        if (text != '') {
            res(text, '-d');
        } else {
            alert('Введине сообщение');
        }
    });
})





