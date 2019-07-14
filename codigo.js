var mapaInicial=[];
var jugador=[];
var caja1 = [], caja2 = [], caja3 = [];
var meta1 = [], meta2 = [], meta3 = [];
var lineaActual=0;

const input = 
    document.querySelector('input[type="file"]')
    input.addEventListener('change',function (e) {
        const reader = new FileReader()
        reader.onload = function () {
            const lines = reader.result.split('\n').map(function(line){
                mapaInicial.push(line);
                if (line[1] == ','){
                    if (jugador[0]==undefined){
                        jugador[0]=line[0];
                        jugador[1]=line[2];
                        document.write("ya se asigno el jugador\n" + jugador[0] + "," + jugador[1]);

                    }else if (caja1[0] == undefined){
                            caja1[0] = line[0];
                            caja1[1] = line[2];
                    }else if (caja2[0] == undefined){
                            caja2[0] = line[0];
                            caja2[1] = line[2];
                    }else if (caja3[0] == undefined){
                            caja3[0] = line[0];
                            caja3[1] = line[2];
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
        }
        reader.readAsText(input.files[0]);

    },false)


var moverUp = function () {
    var lin = jugador[0];
    var col = jugador[1];
    //document.write("El jugador esta en " + lin + "," + col + "bueno?\n");
    var renglon = mapaInicial[lin];
    if (((renglon.jugador[0] - 1) == '0') || ((renglon.jugador[0] - 1) == 'X')) {
        if (((caja1[0] == (jugador[0] - 1)) && (caja1[1] == jugador[1]))) {
            if (((renglon.jugador[0] - 2) == '0') || ((renglon.jugador[0] - 2) == 'X')) {
                if ((caja2[0] == (jugador[0] - 2) && caja2[1] == jugador[1]) || (caja3[0] == (jugador[0] - 2)) && (caja3[1] == jugador[1])) {
                } else {
                    caja1[0] = jugador[0] - 2;
                    jugador[0] = jugador[0] - 1;
                }
            }
        } else if (((caja2[0] == (jugador[0] - 1)) && (caja2[1] == jugador[1]))) {
            if (((renglon.jugador[0] - 2) == '0') || ((renglon.jugador[0] - 2) == 'X')) {
                if ((caja1[0] == (jugador[0] - 2) && caja1[1] == jugador[1]) || (caja3[0] == (jugador[0] - 2)) && (caja3[1] == jugador[1])) {
                } else {
                    caja2[0] = jugador[0] - 2;
                    jugador[0] = jugador[0] - 1;
                }
            }
        } else if (((caja3[0] == (jugador[0] - 1)) && (caja3[1] == jugador[1]))) {
            if (((renglon.jugador[0] - 2) == '0') || ((renglon.jugador[0] - 2) == 'X')) {
                if ((caja2[0] == (jugador[0] - 2) && caja2[1] == jugador[1]) || (caja1[0] == (jugador[0] - 2)) && (caja1[1] == jugador[1])) {
                } else {
                    caja3[0] = jugador[0] - 2;
                    jugador[0] = jugador[0] - 1;
                }
            }
        }
    }
}
  

