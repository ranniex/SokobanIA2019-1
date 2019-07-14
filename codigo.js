var mapaInicial=[];
var probando_comit = "test";
const input = 
    document.querySelector('input[type="file"]')
    input.addEventListener('change',function (e) {
        console.log(input.files)
        const reader = new FileReader()
        reader.onload = function () {
            const lines = reader.result.split('\n').map(function(line){
                mapaInicial.push(line);
                if (line[1] == ','){
                    document.write("Es posicion"+ "  "+ line[0]+ "\n");
                }else{
                    document.write("Es mapa" + "  " + line[0] + "\n");
                }
                
            })
        }
        reader.readAsText(input.files[0]);
    },false)
