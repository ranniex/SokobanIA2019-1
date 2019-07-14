var mapaInicial=[];
var jugador=[];
var caja1 = [], caja2 = [], caja3 = [];

const input = 
    document.querySelector('input[type="file"]')
    input.addEventListener('change',function (e) {
        console.log(input.files)
        const reader = new FileReader()
        reader.onload = function () {
            const lines = reader.result.split('\n').map(function(line){
                mapaInicial.push(line);
                if (line[1] == ','){
                    if (jugador[0]==undefined){
                        jugador[0]=line[0];
                        jugador[1]=line[2];
                        document.write("El jugador esta en: "+jugador[0]+","+jugador[1]+'\n');
                    }else if (caja1[0] == undefined){
                            caja1[0] = line[0];
                            caja1[1] = line[2];
                            document.write("la caja1 esta en: " + caja1[0] + "," + caja1[1] + '\n');
                    }else if (caja2[0] == undefined){
                            caja2[0] = line[0];
                            caja2[1] = line[2];
                            document.write("la caja2 esta en: " + caja2[0] + "," + caja2[1] + '\n');
                    }else if (caja3[0] == undefined){
                            caja3[0] = line[0];
                            caja3[1] = line[2];
                            document.write("la caja3 esta en: " + caja3[0] + "," + caja3[1] + '\n');
                    }
                }else{}
            })
        }
        reader.readAsText(input.files[0]);
    },false)

