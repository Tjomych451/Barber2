document.getElementById('id_master').addEventListener('change', function() {
    const masterId = this.value;
    fetch(`/get-services/${masterId}/`)
        .then(response => response.json())
        .then(data => {
            const serviceSelect = document.getElementById('id_service');
            serviceSelect.innerHTML = '';
            data.services.forEach(service => {
                const option = new Option(
                    `${service.name} ($${service.price})`,
                    service.id
                );
                serviceSelect.add(option);
            });
        });
});
