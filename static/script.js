document.getElementById('insuranceForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const formData = {
        vehicleType: document.getElementById('vehicleType').value,
        ageGroup: document.getElementById('ageGroup').value,
        vehicleValue: document.getElementById('vehicleValue').value,
        drivingHistory: document.getElementById('drivingHistory').value,
        coverageType: document.getElementById('coverageType').value
    };

    console.log('Form submitted with data:', formData);

    try {
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        const data = await response.json();
        console.log('Response received:', data);
        
        document.getElementById('annualPremium').textContent = `$${data.annual_premium.toLocaleString()}`;
        document.getElementById('monthlyPremium').textContent = `$${data.monthly_premium.toLocaleString()}`;
        document.getElementById('result').style.display = 'block';

        // Smooth scroll to results
        document.getElementById('result').scrollIntoView({ behavior: 'smooth' });

    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while calculating the insurance premium. Please try again.');
    }
});
