// console.log(document.getElementById('username').value)
document.getElementById('username200').innerHTML = getCookie("username")
function textsubmit(){
    console.log("clicked");
    text = document.querySelector("#final").innerHTML;
    if(id == null){
        q_id = 3;
    }
    else{
        q_id = id;
    }
    axios.post('http://13.231.225.7:8000/api/submit_answer/',{username:"rohsai",text_id:q_id,"answer":text})
    .then(response=>{
        alert("success");
        window.location.href = "submitionPage.html?id="+q_id;
        }
    )
    .catch((e)=>{
        document.getElementById("errormsg").innerHTML = e;
        setTimeout(()=>{
            document.getElementById("errormsg").innerHTML = "";
        },5000)
    })
}
function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) {
                c_end = document.cookie.length;
            }
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return "";
}
const searchParams = new URLSearchParams(window.location.search);
const id = searchParams.get('id');
if(id == null)
{
    axios.post('http://13.231.225.7:8000/api/get_demo_text/',{})
.then(response=>{
    const obj = response.data
    const d = JSON.parse(obj)
    data = d[0]
    const text = data['name']
    document.getElementById("titleid").innerHTML = text
    const textn = hexToString(data['hindiText'])
    const hint = data['hintString']
    const hintn = hexToString(hint)
    document.querySelector("#final2").innerHTML = textn
    document.querySelector("#final3").innerHTML = hintn
    }
)
.catch((e)=>{
    document.getElementById("errormsg").innerHTML = e;
    setTimeout(()=>{
        document.getElementById("errormsg").innerHTML = "";
    },5000)
})
}
else{
    axios.post('http://13.231.225.7:8000/api/text/',{"id":id})
    .then(response=>{
        const obj = response.data
        const data = JSON.parse(obj)
        const text = data['name']
        document.getElementById("titleid").innerHTML = text
        const textn = hexToString(data['hindiText'])
        const hint = data['hintString']
        const hintn = hexToString(hint)
        document.querySelector("#final2").innerHTML = textn
        document.querySelector("#final3").innerHTML = hintn
        }
    )
    .catch((e)=>{
        document.getElementById("errormsg").innerHTML = e;
        setTimeout(()=>{
            document.getElementById("errormsg").innerHTML = "";
        },5000)
    })
}
function hexToString(hexRepresentation) {
    let byteArray = new Uint8Array(hexRepresentation.match(/[\da-f]{2}/gi).map(function (h) {
        return parseInt(h, 16)
    }))
    return new TextDecoder().decode(byteArray)
}


