from flask import Flask, render_template, request, jsonify, send_from_directory
import json

app = Flask(__name__)

# Insurance calculation factors
BASE_RATES = {
    'sedan': 1000,
    'suv': 1200,
    'truck': 1400,
    'luxury': 1600
}

AGE_FACTORS = {
    '18-25': 1.5,
    '26-35': 1.2,
    '36-50': 1.0,
    '51-65': 1.1,
    '65+': 1.3
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_insurance():
    data = request.get_json()
    
    vehicle_type = data.get('vehicleType', 'sedan')
    age_group = data.get('ageGroup', '36-50')
    vehicle_value = float(data.get('vehicleValue', 20000))
    driving_history = data.get('drivingHistory', 'clean')
    coverage_type = data.get('coverageType', 'basic')
    
    # Base calculation
    base_premium = BASE_RATES.get(vehicle_type, 1000)
    age_factor = AGE_FACTORS.get(age_group, 1.0)
    
    # Value factor (0.5% of vehicle value)
    value_factor = vehicle_value * 0.005
    
    # Driving history factor
    history_factor = 1.0
    if driving_history == 'accidents':
        history_factor = 1.5
    elif driving_history == 'violations':
        history_factor = 1.3
    
    # Coverage factor
    coverage_factor = 1.0
    if coverage_type == 'comprehensive':
        coverage_factor = 1.5
    elif coverage_type == 'collision':
        coverage_factor = 1.3
    
    # Calculate final premium
    total_premium = (base_premium + value_factor) * age_factor * history_factor * coverage_factor
    
    return jsonify({
        'annual_premium': round(total_premium, 2),
        'monthly_premium': round(total_premium / 12, 2)
    })

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy-policy.html')

@app.route('/terms-conditions')
def terms_conditions():
    return render_template('terms-conditions.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog/understanding-car-insurance-coverage-types')
def blog_post_coverage_types():
    return render_template('blog-post.html')

@app.route('/blog/top-tips-lower-insurance-premium')
def blog_post_lower_premium():
    return render_template('blog-post-lower-premium.html')

@app.route('/blog/liability-insurance-guide')
def blog_post_liability():
    return render_template('blog-post-liability.html')

@app.route('/blog/comprehensive-coverage-guide')
def blog_post_comprehensive():
    return render_template('blog-post-comprehensive.html')

@app.route('/blog/what-affects-insurance-rates')
def blog_post_insurance_rates():
    return render_template('blog-post-insurance-rates.html')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('static', 'sitemap.xml', mimetype='application/xml')

@app.route('/api/contact', methods=['POST'])
def submit_contact():
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'subject', 'message']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'success': False, 'message': f'Missing required field: {field}'}), 400
        
        # Here you would typically:
        # 1. Send an email
        # 2. Store in database
        # 3. Forward to a CRM system
        # For now, we'll just return success
        
        return jsonify({
            'success': True,
            'message': 'Thank you for your message! We will get back to you soon.'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'An error occurred while processing your request.'
        }), 500

if __name__ == '__main__':
    app.run(debug=false)
