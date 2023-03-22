const searchParams = new URLSearchParams(window.location.search);
const id = searchParams.get('id');
if(id == null){

}
else{
    axios.post('http://13.231.225.7:8000/api/submition_list/',{username:"rohsai",text_id:id})
    .then(response =>{
        const obj = response.data
        const d = JSON.parse(obj)
        data = d[0]
        console.log(data)
        const text_id = data['text_id']
        const submition_id = data['submition_id']
        const text_name=data['text_name']
        const level=data['level']
        const correct_answer = data['correct_answer']
        const accuracy = data['accuracy']
        const answer_status = data['answer_status']
        const user_answer = data['submit_answer']
        const suggestion = data['suggestions']

        document.getElementById("text_id").innerHTML = text_id + ". "
        document.getElementById("text_name").innerHTML = text_name
        document.getElementById("user_answer").innerHTML = user_answer
        document.getElementById("admin_answer").innerHTML = correct_answer
        document.getElementById("level_value").innerHTML = level
        document.getElementById("accuracy_value").innerHTML = accuracy
        document.getElementById("status_value").innerHTML = answer_status
        document.getElementById("suggestion_value").innerHTML = suggestion


    })
    .catch((err) =>{
        console.log(err);
    })
}