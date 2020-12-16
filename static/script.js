login = () =>{
    let xhr = new XMLHttpRequest();
    xhr.open('POST','/login',true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    let data = {
        "user_id": document.getElementById('user_id'),
        "password": document.getElementById('password')
    }
    xhr.send(JSON.stringify(data));

}