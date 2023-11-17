document.addEventListener('DOMContentLoaded', function() {
    var regionSelect = document.getElementById('region');
    var comunaSelect = document.getElementById('comuna');
    var defaultComunaOption = '<option value="">Elija una comuna</option>';

    regionSelect.addEventListener('change', function() {
        var selectedRegion = regionSelect.value;
        fetch('/obtener_comunas/' + selectedRegion)
            .then(response => response.json())
            .then(data => {
                comunaSelect.innerHTML = '';
                comunaSelect.innerHTML = defaultComunaOption;
                data.forEach(comuna => {
                    var option = document.createElement('option');
                    option.text = comuna;
                    option.value = comuna;
                    comunaSelect.add(option);
                });
            })
            
    });

    // Restablecer la opción de comuna al cambiar la región a "Elija una región"
    regionSelect.addEventListener('click', function() {
        if (regionSelect.value === '') {
            comunaSelect.innerHTML = '';
            comunaSelect.innerHTML = defaultComunaOption;
        }
    });

    // Verificar si la opción 'Elija una región' ya existe antes de agregarla
    if (regionSelect.value === '') {
        comunaSelect.innerHTML = defaultComunaOption;
    }
});
