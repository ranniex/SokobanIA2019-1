var mapaInicial=[];
var jugador=[];
var caja1 = [], caja2 = [], caja3 = [];
var meta1 = [], meta2 = [], meta3 = [];
var lineaActual=0;
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
                }else{
                    if(line.includes('X')){
                        if (meta1[0]==undefined){
                            meta1[0]=lineaActual;
                            meta1[1]=line.indexOf('X');

                            if (meta2[0] == undefined && (-1!=line.indexOf('X',meta1[1]+1))) {
                                meta2[0] = lineaActual;
                                meta2[1] = line.indexOf('X',meta1[1]+1);

                                if (meta3[0] == undefined && (-1 != line.indexOf('X', meta2[1] + 1))) {
                                    meta3[0] = lineaActual;
                                    meta3[1] = line.indexOf('X',meta2[1]+1);
                                    document.write("ENTROOOOOOOOOOOOOO");

                                }

                            }
                        }else if(meta2[0] == undefined){
                                meta2[0] = lineaActual;
                                meta2[1] = line.indexOf('X');

                            if (meta3[0] == undefined && (-1 != line.indexOf('X', meta2[1] + 1))) {
                                    meta3[0] = lineaActual;
                                    meta3[1] = line.indexOf('X',meta2[1]+1);
                                }
                        }else if(meta3[0] == undefined){
                            meta3[0] = lineaActual;
                            meta3[1] = line.indexOf('X');
                        }
                    }else{}
                }
                lineaActual+=1;
            })
            document.write("La meta 1 esta en " + meta1[0] + "," + meta1[1] + '\n');
            document.write("La meta 2 esta en " + meta2[0] + "," + meta2[1] + '\n');
            document.write("La meta 3 esta en " + meta3[0] + "," + meta3[1] + '\n');
        }
        reader.readAsText(input.files[0]);
    },false)

