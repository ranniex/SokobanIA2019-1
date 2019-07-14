var mapaInicial=['primer elemento'];

const input = 
    document.querySelector('input[type="file"]')
    input.addEventListener('change',function (e) {
        console.log(input.files)
        const reader = new FileReader()
        reader.onload = function () {
            const lines = reader.result.split('\n').map(function(line){
                document.write(line);
                mapaInicial.push[line
