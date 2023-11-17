btnArtesano = document.getElementById('btnGraficoArtesanos');
btnDeporte = document.getElementById('btnGraficoDeportes');
btnVolver = document.getElementById('btnVolver');
btnActualizar = document.getElementById('btnActualizar');

// Configuración del gráfico de barras verticales para los artesanos
     
function cargarTipos (){
  Highcharts.chart('stats-artesanos', {
    chart: {
      type: 'column'
    },
    title: {
      text: 'Cantidad de artesanos por tipo'
    },
    xAxis: {
        categories: ['mármol', 'madera', 'cerámica', 'mimbre', 'metal', 'cuero', 'joyas', 'telas', 'otro']
    },
    yAxis: {
      title: {
        text: 'Valores'
      }
    },
    series: [{
      name: 'Tipos de Artesanias',
      data: [],
      dataLabels: {

        enabled: true,
        inside: true,
        format: '{y}'
      }
    }]
  });
    // cargar los tipos de artesanias
    fetch('/get-stats-artesanos')
    .then(response => response.json())
    .then(data => {
        // Mapear los datos a un formato adecuado para Highcharts
        const ordenLlaves =  ['mármol', 'madera', 'cerámica', 'mimbre', 'metal', 'cuero', 'joyas', 'telas', 'otro']
  
        let parsedData =ordenLlaves.map(llave => ({ name: llave, y: data[llave] || 0}));
        // Obtener el gráfico por ID
        let chart = Highcharts.charts.find(chart => chart && chart.renderTo.id === 'stats-artesanos');
  
        // Actualizar el gráfico con los nuevos datos
        chart.update({
            series: [
                {
                    data: parsedData,
                },
            ],
            plotOptions: {
              series: {
                  animation: {
                    dutarion: 1000
                  }
              }
          }
        });
    })
    .catch(error => {
        console.error('Error al obtener los datos:', error);
    });
}

function cargarDeportes (){
  Highcharts.chart('stats-hinchas', {
    chart: {
      type: 'column'
    },
    title: {
      text: 'Cantidad de hinchas por deporte'
    },
    xAxis: {
        categories: []
    },
    yAxis: {
      title: {
        text: 'Valores'
      }
    },
    series: [{
      name: 'Hinchas por deporte',
      data: [],
      dataLabels: {

        enabled: true,
        inside: true,
        format: '{y}'
      }
    }]
  });
    fetch('/get-stats-hinchas')
    .then(response => response.json())
    .then(data => {
        let parsedData =Object.entries(data).map(([tipo,cantidad]) => ({ name: tipo, y:cantidad || 0}));
        // Obtener el gráfico por ID
        let chart = Highcharts.charts.find(chart => chart && chart.renderTo.id === 'stats-hinchas');
  
        // Actualizar el gráfico con los nuevos datos
        chart.update({
              xAxis: [{
                  categories: Object.keys(data)
              }],
            series: [
                {
                    data: parsedData,
                },
            ],
            plotOptions: {
                series: {
                    animation: {
                      dutarion: 1000
                    }
                }
            }
        });
    })
    .catch(error => {
        console.error('Error al obtener los datos:', error);
    });
}



function mostrarGrafico(grafico) {
    // Mostrar el gráfico
    btnArtesano.style.display = 'none';
    btnDeporte.style.display = 'none';
    btnVolver.style.display = 'inline-block';
    btnActualizar.style.display = 'inline-block';
    document.getElementById(grafico).style.display = 'inline-block';
    cargarTipos();
    cargarDeportes();
    

}

function volver() {
    // volver al inicio de stats
    btnArtesano.style.display = 'inline-block';
    btnDeporte.style.display = 'inline-block';
    btnVolver.style.display = 'none';
    btnActualizar.style.display = 'none';
    document.getElementById('stats-artesanos').style.display = 'none';
    document.getElementById('stats-hinchas').style.display = 'none';
    chart.destroy();
}

function actualizar() {
    cargarTipos();
    cargarDeportes(); 
    // puede que cargar los dos no sea lo mas eficiente, pero es lo mas facil xd
    // si me queda tiempo puedo crear 2 botones de actualizar
    // y usando if mostrar el que se necesite
}

