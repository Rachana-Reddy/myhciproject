document.getElementById('submit').addEventListener("click",(e)=>{
    let text=document.getElementById('inputText').value;
    fetch("https://api.openai.com/v1/completions", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer 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"
        },
        body: JSON.stringify({
            "model": "text-davinci-003",
            "prompt": text,
            "temperature": 0.7,
            "max_tokens": 256,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0
        })
      })
      .then(response => response.json())
      .then(response => {
        // Display the API's response in the div
        document.getElementById("outputBox").innerHTML = response.choices[0].text;
        console.log(response.choices[0].text);
        document.getElementById('inputText').value=''
      });
})