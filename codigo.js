var mapaInicial=[]

const input = 
    document.querySelector('input[type="file"]')
    input.addEventListener('change',function (e) {
        console.log(input.files)
        const reader = new FileReader()
        reader.onload = function () {
            const lines = reader.result.split('\n').map(function(line){
                document.write(line.split('\n'))
                mapaInicial.push[line.split('\n')]
                document.write(mapaInicial[0])
            })
            document.write(mapaInicial.length)
        }
        reader.readAsText(input.files[0])
    },false)

